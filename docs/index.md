# neo-oscal Dokumentation

*Controls-Automatisierung auf Basis von NIST OSCAL.*

**neo-oscal** ist ein persönliches Werkzeug, um Security-Controls maschinenlesbar zu
verwalten: Kataloge (z. B. NIST SP 800-53 Rev5) durchsuchen, Profile und Baselines
bilden, die Umsetzung dokumentieren und als
[OSCAL](https://pages.nist.gov/OSCAL/) exportieren. Inspiriert ist es von
[myctrl.tools](https://myctrl.tools/).

Live-App: <https://oscal.neoprehn.de>

## Inhalt

- **[OSCAL-Grundlagen](oscal-grundlagen.md)** – die Schichten des OSCAL-Modells und
  wie neo-oscal sie abbildet.
- **[Entwicklung](entwicklung.md)** – lokales Setup, Tests, Projektstruktur.
- **[Betrieb & CI/CD](betrieb.md)** – Pipeline und Deployment auf oscal.neoprehn.de.
- **[Roadmap](roadmap.md)** – geplante Ausbaustufen.

## Technik

- **Backend:** FastAPI + Pydantic
- **Frontend:** Vite + React + TypeScript
- **Quelle der Inhalte:** [usnistgov/oscal-content](https://github.com/usnistgov/oscal-content)
