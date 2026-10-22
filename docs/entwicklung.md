# Entwicklung

## Setup

```bash
python scripts/fetch_content.py
cd backend && python -m venv .venv && .venv/Scripts/pip install -e ".[dev]"
.venv/Scripts/uvicorn app.main:app --reload     # :8000
cd ../frontend && npm install && npm run dev    # :5173
```

Der Vite-Dev-Server leitet `/api` an das Backend auf Port 8000 weiter.

## Tests

```bash
cd backend && .venv/Scripts/python -m pytest
cd frontend && npx tsc -b
```

## Struktur

| Pfad | Inhalt |
|---|---|
| `backend/app/oscal.py` | OSCAL-Modelle (verlustfrei) und Loader |
| `backend/app/main.py` | FastAPI-Anwendung |
| `frontend/` | Vite + React + TypeScript |
| `scripts/fetch_content.py` | NIST-Inhalte laden |
| `docs/` | Diese Doku (MkDocs, DE/EN) |

## Doku lokal bauen

```bash
pip install -r docs/requirements.txt
mkdocs serve
```

Deutsche Seiten liegen als `name.md`, englische als `name.en.md` im selben Ordner.
