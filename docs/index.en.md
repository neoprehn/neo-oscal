# neo-oscal Documentation

*Controls automation based on NIST OSCAL.*

**neo-oscal** is a personal tool for managing security controls in machine-readable form:
browse catalogs (e.g. NIST SP 800-53 Rev5), build profiles and baselines, document the
implementation and export it as [OSCAL](https://pages.nist.gov/OSCAL/). It is inspired by
[myctrl.tools](https://myctrl.tools/).

Live app: <https://oscal.neoprehn.de>

## Contents

- **[OSCAL Fundamentals](oscal-grundlagen.md)** – the layers of the OSCAL model and how
  neo-oscal maps them.
- **[Development](entwicklung.md)** – local setup, tests, project layout.
- **[Operations & CI/CD](betrieb.md)** – pipeline and deployment to oscal.neoprehn.de.
- **[Roadmap](roadmap.md)** – planned stages.

## Tech

- **Backend:** FastAPI + Pydantic
- **Frontend:** Vite + React + TypeScript
- **Content source:** [usnistgov/oscal-content](https://github.com/usnistgov/oscal-content)
