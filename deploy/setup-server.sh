#!/usr/bin/env bash
# Einmaliges Server-Setup fuer oscal.neoprehn.de (als root auf dem VPS ausfuehren).
# Voraussetzung: Subdomain oscal.neoprehn.de ist in Plesk angelegt (inkl. Let's-Encrypt-Zertifikat).
#
#   curl -fsSL https://raw.githubusercontent.com/neoprehn/neo-oscal/main/deploy/setup-server.sh | sudo bash
#
# Variablen (optional): SUBDOMAIN_DIR, APP_USER
set -euo pipefail

SUBDOMAIN_DIR="${SUBDOMAIN_DIR:-/var/www/vhosts/neoprehn.de/oscal.neoprehn.de}"
APP_DIR="$SUBDOMAIN_DIR/app"
WEB_DIR="$SUBDOMAIN_DIR/httpdocs"
REPO="https://github.com/neoprehn/neo-oscal.git"

# Plesk legt den Systembenutzer der Subdomain als Besitzer des Verzeichnisses an.
APP_USER="${APP_USER:-$(stat -c %U "$SUBDOMAIN_DIR")}"
APP_GROUP="$(id -gn "$APP_USER")"
echo "Benutzer: $APP_USER:$APP_GROUP  App: $APP_DIR  Web: $WEB_DIR"

[ -d "$SUBDOMAIN_DIR" ] || { echo "Fehler: $SUBDOMAIN_DIR existiert nicht (Subdomain in Plesk angelegt?)"; exit 1; }

# Repo klonen bzw. aktualisieren
if [ -d "$APP_DIR/.git" ]; then
  git -C "$APP_DIR" fetch origin main && git -C "$APP_DIR" reset --hard origin/main
else
  git clone "$REPO" "$APP_DIR"
fi

# Python-Umgebung + NIST-Inhalte
python3 -m venv "$APP_DIR/venv"
"$APP_DIR/venv/bin/pip" install -q --upgrade pip
"$APP_DIR/venv/bin/pip" install -q -e "$APP_DIR/backend"
"$APP_DIR/venv/bin/python" "$APP_DIR/scripts/fetch_content.py"

chown -R "$APP_USER:$APP_GROUP" "$APP_DIR" "$WEB_DIR"

# systemd-Dienst
sed -e "s#__APP_USER__#$APP_USER#g" -e "s#__APP_GROUP__#$APP_GROUP#g" -e "s#__APP_DIR__#$APP_DIR#g" \
  "$APP_DIR/deploy/oscal.service" > /etc/systemd/system/oscal.service
systemctl daemon-reload
systemctl enable --now oscal
sleep 2
curl -fsS http://127.0.0.1:8731/api/health && echo

cat <<MSG

Serverseitig fertig. Noch in Plesk (Domains -> oscal.neoprehn.de -> Apache & nginx-Einstellungen ->
"Zusaetzliche nginx-Anweisungen") eintragen, siehe $APP_DIR/deploy/plesk-nginx.conf :

    location /api/ {
        proxy_pass http://127.0.0.1:8731;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }

Danach: Deploy-Public-Key in ~$APP_USER/.ssh/authorized_keys eintragen (oder fuer root, wie bei fair-web).
MSG
