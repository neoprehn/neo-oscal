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

Prerequisite: the subdomain `oscal.neoprehn.de` exists in Plesk (with a Let's Encrypt certificate).

1. On the VPS as root: run `deploy/setup-server.sh`. It clones the repo to
   `/var/www/vhosts/neoprehn.de/oscal.neoprehn.de/app`, creates the venv, fetches the NIST content
   and installs the systemd service `oscal` (uvicorn on `127.0.0.1:8731`).
2. In Plesk under *Apache & nginx Settings → Additional nginx directives* paste the content of
   `deploy/plesk-nginx.conf`: `/api/` goes to the service, everything else is served statically
   from `httpdocs/` by nginx. Do not add your own `location /` – Plesk defines it itself.
3. Deploy key: add the public key for the SSH user, store the private one as the GitHub secret
   `VPS_SSH_KEY`.
4. Set `DEPLOY_ENABLED=true` – from then on every push to `main` deploys after green CI.

| Path | Content |
|---|---|
| `…/oscal.neoprehn.de/app` | repo checkout, `venv/`, `data/content/` |
| `…/oscal.neoprehn.de/httpdocs` | built frontend (filled by the deploy via rsync) |

## Documentation (Read the Docs)

Two RTD projects, following the fair-web pattern:

- **neo-oscal** – bilingual (German at the root, English under `/en/`),
  config `.readthedocs.yaml` → `mkdocs.yml`.
- **neo-oscal-en** – optional, English only. In the RTD admin under *Settings →
  Configuration file* set `.readthedocs-en.yaml` (→ `mkdocs.en.yml`).
