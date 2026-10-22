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

Voraussetzung: Die Subdomain `oscal.neoprehn.de` ist in Plesk angelegt (mit Let's-Encrypt-Zertifikat).

1. Auf dem VPS als root: `deploy/setup-server.sh` ausführen. Es klont das Repo nach
   `/var/www/vhosts/neoprehn.de/oscal.neoprehn.de/app`, legt die venv an, lädt die NIST-Inhalte
   und installiert den systemd-Dienst `oscal` (uvicorn auf `127.0.0.1:8010`).
2. In Plesk unter *Apache & nginx-Einstellungen → Zusätzliche nginx-Anweisungen* den Inhalt von
   `deploy/plesk-nginx.conf` eintragen: `/api/` geht an den Dienst, alles andere liefert nginx
   statisch aus `httpdocs/` aus (SPA-Fallback).
3. Deploy-Key: öffentlichen Schlüssel beim SSH-Benutzer hinterlegen, den privaten als Secret
   `VPS_SSH_KEY` in GitHub speichern.
4. `DEPLOY_ENABLED=true` setzen – ab dann deployt jeder Push auf `main` nach grüner CI.

| Pfad | Inhalt |
|---|---|
| `…/oscal.neoprehn.de/app` | Repo-Checkout, `venv/`, `data/content/` |
| `…/oscal.neoprehn.de/httpdocs` | gebautes Frontend (vom Deploy per rsync befüllt) |

## Dokumentation (Read the Docs)

Zwei RTD-Projekte nach dem Muster von fair-web:

- **neo-oscal** – zweisprachig (Deutsch an der Wurzel, Englisch unter `/en/`),
  Konfiguration `.readthedocs.yaml` → `mkdocs.yml`.
- **neo-oscal-en** – optional, nur Englisch. Im RTD-Admin unter *Settings →
  Configuration file* auf `.readthedocs-en.yaml` setzen (→ `mkdocs.en.yml`).
