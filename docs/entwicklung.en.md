# Development

## Setup

```bash
python scripts/fetch_content.py
cd backend && python -m venv .venv && .venv/Scripts/pip install -e ".[dev]"
.venv/Scripts/uvicorn app.main:app --reload     # :8000
cd ../frontend && npm install && npm run dev    # :5173
```

The Vite dev server proxies `/api` to the backend on port 8000.

## Tests

```bash
cd backend && .venv/Scripts/python -m pytest
cd frontend && npx tsc -b
```

## Layout

| Path | Content |
|---|---|
| `backend/app/oscal.py` | OSCAL models (lossless) and loader |
| `backend/app/main.py` | FastAPI application |
| `frontend/` | Vite + React + TypeScript |
| `scripts/fetch_content.py` | Fetch NIST content |
| `docs/` | This documentation (MkDocs, DE/EN) |

## Build the docs locally

```bash
pip install -r docs/requirements.txt
mkdocs serve
```

German pages live as `name.md`, English ones as `name.en.md` in the same folder.
