# Betrieb & CI/CD

Die App läuft unter <https://oscal.neoprehn.de> auf dem IONOS-VPS (wie fair-web).

## Pipeline

| Workflow | Auslöser | Aufgabe |
|---|---|---|
| `ci.yml` | Push / Pull Request | Backend-Tests (pytest, ruff), Frontend-Typecheck und Build, Doku-Build (`mkdocs build --strict`) |
| `deploy.yml` | Push auf `main` (nach grünem CI), manuell | Frontend bauen, per rsync hochladen, Backend aktualisieren, Dienst neu starten |

Das Deployment ist standardmäßig **aus**. Es wird erst aktiv, wenn in GitHub unter
*Settings → Secrets and variables → Actions* die Variable `DEPLOY_ENABLED=true` gesetzt ist.

### Benötigte Secrets

| Secret | Inhalt |
|---|---|
| `VPS_HOST` | Hostname/IP des Servers |
| `VPS_USER` | SSH-Benutzer |
| `VPS_SSH_KEY` | privater Deploy-Key (nur für dieses Deployment) |

## Einmaliges Server-Setup

1. DNS: `A`-Record `oscal.neoprehn.de` auf den VPS, TLS-Zertifikat (Let's Encrypt).
2. Verzeichnis `/var/www/vhosts/neoprehn.de/oscal` anlegen und das Repo klonen.
3. Backend: `python -m venv venv && venv/bin/pip install -e backend` und
   `venv/bin/python scripts/fetch_content.py`.
4. systemd-Dienst `oscal` (uvicorn auf `127.0.0.1:8000`).
5. Webserver: Statische Dateien aus `frontend-dist/` ausliefern, `/api/` an
   `127.0.0.1:8000` weiterreichen.

```ini
# /etc/systemd/system/oscal.service
[Unit]
Description=neo-oscal API
After=network.target

[Service]
WorkingDirectory=/var/www/vhosts/neoprehn.de/oscal/backend
ExecStart=/var/www/vhosts/neoprehn.de/oscal/venv/bin/uvicorn app.main:app --host 127.0.0.1 --port 8000
Restart=on-failure
User=www-data

[Install]
WantedBy=multi-user.target
```

## Dokumentation (Read the Docs)

Zwei RTD-Projekte nach dem Muster von fair-web:

- **neo-oscal** – zweisprachig (Deutsch an der Wurzel, Englisch unter `/en/`),
  Konfiguration `.readthedocs.yaml` → `mkdocs.yml`.
- **neo-oscal-en** – optional, nur Englisch. Im RTD-Admin unter *Settings →
  Configuration file* auf `.readthedocs-en.yaml` setzen (→ `mkdocs.en.yml`).
