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
