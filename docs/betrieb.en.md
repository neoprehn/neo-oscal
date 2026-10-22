# Operations & CI/CD

The app runs at <https://oscal.neoprehn.de> on the IONOS VPS (like fair-web).

## Pipeline

| Workflow | Trigger | Job |
|---|---|---|
| `ci.yml` | push / pull request | Backend tests (pytest, ruff), frontend typecheck and build, docs build (`mkdocs build --strict`) |
| `deploy.yml` | push to `main` (after green CI), manual | Build frontend, upload via rsync, update backend, restart service |

Deployment is **off** by default. It only becomes active once the GitHub variable
`DEPLOY_ENABLED=true` is set under *Settings → Secrets and variables → Actions*.

### Required secrets

| Secret | Content |
|---|---|
| `VPS_HOST` | Server hostname/IP |
| `VPS_USER` | SSH user |
| `VPS_SSH_KEY` | private deploy key (for this deployment only) |

## One-time server setup

1. DNS: `A` record `oscal.neoprehn.de` to the VPS, TLS certificate (Let's Encrypt).
2. Create `/var/www/vhosts/neoprehn.de/oscal` and clone the repo there.
3. Backend: `python -m venv venv && venv/bin/pip install -e backend` and
   `venv/bin/python scripts/fetch_content.py`.
4. systemd service `oscal` (uvicorn on `127.0.0.1:8000`).
5. Web server: serve static files from `frontend-dist/`, proxy `/api/` to
   `127.0.0.1:8000`.

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

## Documentation (Read the Docs)

Two RTD projects, following the fair-web pattern:

- **neo-oscal** – bilingual (German at the root, English under `/en/`),
  config `.readthedocs.yaml` → `mkdocs.yml`.
- **neo-oscal-en** – optional, English only. In the RTD admin under *Settings →
  Configuration file* set `.readthedocs-en.yaml` (→ `mkdocs.en.yml`).
