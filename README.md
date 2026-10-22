# neo-oscal

Controls-Automatisierung nach [NIST OSCAL](https://pages.nist.gov/OSCAL/) – ein persönliches
Werkzeug in Anlehnung an [myctrl.tools](https://myctrl.tools/).

## Roadmap (OSCAL-Schichten)
1. **Catalog** – Kataloge laden, durchsuchen, anzeigen (NIST SP 800-53 Rev5) ← *Gerüst steht*
2. **Profile** – Baselines (Low/Moderate/High) auflösen, eigene Profile mit Parametern
3. **Component Definition** – Technologie-/Systemkomponenten mit Control-Umsetzung
4. **SSP** – System Security Plan
5. **Assessment Plan/Results, POA&M**
6. Crosswalk zwischen Frameworks, OSCAL-Export (JSON/YAML/XML)

## Entwicklung
```
python scripts/fetch_content.py
cd backend && python -m venv .venv && .venv/Scripts/pip install -e ".[dev]"
.venv/Scripts/uvicorn app.main:app --reload     # :8000
cd ../frontend && npm install && npm run dev    # :5173
```
