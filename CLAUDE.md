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

## Roadmap, Chat-Neustart, Knowledgegraph
- `ROADMAP.md` (aktiv, `[ ]/[~]/[x]`), `ROADMAP-ARCHIV.md` (erledigt), `new_chat_rule.md` (Einstiegstext für neue Chats).
- Doku-DoD: Ein Punkt ist erst fertig, wenn `docs/` + `docs/*.en.md` aktualisiert, CI grün und gepusht ist.
- **Code-Exploration zuerst über den Knowledgegraph (codebase-memory-mcp)**: `search_graph`, `trace_path`,
  `get_code_snippet`, `query_graph`, `get_architecture`, `search_code`. Projekt-Key: **`D-Entwicklung-oscal`**
  (Repo-Root `D:\Entwicklung\oscal`, nicht der Parent `D:\Entwicklung`). Nach größeren Änderungen
  `index_repository` erneut ausführen; Architektur-Entscheidungen stehen als ADR im Graph (`manage_adr`).
- Das Repo ist öffentlich: nie Schlüssel/Zugangsdaten/`.env` committen.

## Frontend-Architekturregeln (Astro bleibt als spätere Option offen)
- React-Komponenten für Darstellung kennen keinen Router und holen keine Daten selbst — Daten kommen als Props.
- Nur dünne Seiten-Dateien kennen Routing und Datenabruf. Alle API-Zugriffe laufen über **einen** API-Client (ein Modul).
- URLs sind sprechend und stabil (`/frameworks/800-53/ac-2`), kein Zustand nur im Speicher.
- Stack-Entscheidungen (Neo4j, FastAPI, Vite + React + Tailwind) stehen in `ROADMAP.md` unter „Offene Entscheidungen“.
