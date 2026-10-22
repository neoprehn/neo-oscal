# Entwicklung

```bash
python scripts/fetch_content.py
cd backend && python -m venv .venv && .venv/Scripts/pip install -e ".[dev]"
.venv/Scripts/uvicorn app.main:app --reload     # :8000
cd ../frontend && npm install && npm run dev    # :5173
```

Tests: `cd backend && .venv/Scripts/python -m pytest`
