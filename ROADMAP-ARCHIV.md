# Roadmap-Archiv — neo-oscal

Erledigte Arbeit. Aktive Punkte stehen in [`ROADMAP.md`](ROADMAP.md).

## Phase 0 — Fundament (2026-10-22)

- [x] Repo `neoprehn/neo-oscal` angelegt und nach `D:\Entwicklung\oscal` geklont (eigenes Repo, getrennt vom Parent `Entwicklung`)
- [x] Backend: FastAPI + Pydantic, verlustfreie OSCAL-Catalog-Modelle, Loader, API zum Auflisten/Suchen, pytest
- [x] Frontend: Vite + React + TypeScript, Katalogauswahl und Suche, Dev-Proxy `/api`
- [x] `scripts/fetch_content.py`: NIST SP 800-53 Rev5 Katalog und Baselines aus `usnistgov/oscal-content`
- [x] Doku im Stil von fair-web: MkDocs (readthedocs-Theme, DE/EN per Suffix), `.readthedocs.yaml`, `.readthedocs-en.yaml`
- [x] CI (`ci.yml`): pytest, ruff, Frontend-Build, Doku-Build strict (DE + EN)
- [x] CD (`deploy.yml`): Frontend per rsync, Backend per SSH, Dienst-Neustart; schaltbar über `DEPLOY_ENABLED`
- [x] Server: Plesk-Subdomain `oscal.neoprehn.de`, systemd-Dienst `oscal` (uvicorn, `127.0.0.1:8731`),
      nginx-Proxy `/api/`, Setup-Skript `deploy/setup-server.sh`
- [x] Ende-zu-Ende geprüft: `/api/catalogs` liefert den Katalog (1196 Controls), automatischer Deploy nach grüner CI

Erkenntnisse: Port 8010 war auf dem Server durch ein Gunicorn belegt (jetzt 8731). Plesk definiert `location /`
selbst — in den zusätzlichen nginx-Anweisungen nur `location /api/`. Git auf dem Server braucht `safe.directory`,
weil das Repo dem Plesk-Benutzer gehört.
