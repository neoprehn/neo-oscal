# neo-oscal

Persönliches Tool zur Controls-Automatisierung auf Basis von NIST OSCAL
(https://pages.nist.gov/OSCAL/), inspiriert von https://myctrl.tools/.
Ziel: Control-Kataloge durchsuchen, Profile/Baselines bilden, Umsetzung
dokumentieren (SSP, Assessment) und als OSCAL exportieren. Domain: oscal.neoprehn.de

## Stack
- `backend/` – FastAPI + Pydantic (Python ≥3.12), Tests mit pytest
- `frontend/` – Vite + React + TypeScript, Dev-Proxy `/api` → :8000
- `scripts/fetch_content.py` – lädt NIST-800-53-Rev5-Inhalte nach `data/content/` (gitignored)

## Befehle
- Backend: `cd backend && .venv/Scripts/python -m pytest` bzw. `.venv/Scripts/uvicorn app.main:app --reload`
- Frontend: `cd frontend && npm run dev`
- Inhalte: `python scripts/fetch_content.py`

## Regeln
- Dieses Verzeichnis ist ein **eigenes Repo** (`neoprehn/neo-oscal`), liegt aber im
  Parent-Ordner `Entwicklung` (anderes Repo). Git-Kommandos immer mit `-C oscal`.
- Commit-Sprache: Deutsch.
- OSCAL-Modelle in `backend/app/oscal.py` bleiben verlustfrei (`extra="allow"`).

## Doku & CI/CD
- Doku: MkDocs (`mkdocs.yml`, DE an der Wurzel, EN per Suffix `.en.md`), Stil wie fair-web;
  RTD-Projekte `neo-oscal` (zweisprachig) und optional `neo-oscal-en` (`.readthedocs-en.yaml`).
  Bei Nav-Änderungen `mkdocs.yml` und `mkdocs.en.yml` synchron halten.
- `.github/workflows/ci.yml`: pytest/ruff, Frontend-Build, Doku-Build (strict).
- `.github/workflows/deploy.yml`: SSH/rsync-Deploy auf den VPS, nur aktiv bei Repo-Variable
  `DEPLOY_ENABLED=true` und gesetzten `VPS_*`-Secrets. Server-Setup: `docs/betrieb.md`.
