# Roadmap — neo-oscal

**Projekt:** Persönliches Werkzeug zur Controls-Automatisierung nach [NIST OSCAL](https://pages.nist.gov/OSCAL/),
in Anlehnung an [myctrl.tools](https://myctrl.tools/).
**Repository:** `neoprehn/neo-oscal` · **Live:** <https://oscal.neoprehn.de> · **Doku:** Read the Docs (`neo-oscal`)

Lebendes Dokument: `[ ]` offen, `[~]` teilweise, `[x]` erledigt. Abgeschlossene Phasen wandern nach
[`ROADMAP-ARCHIV.md`](ROADMAP-ARCHIV.md). Neue Chats starten mit [`new_chat_rule.md`](new_chat_rule.md).

**Leitprinzip — Dokumentations-DoD (gilt für jede Phase und jedes Feature).** Ein Punkt gilt erst als
fertig, wenn er in `docs/` **und** `docs/*.en.md` dokumentiert, getestet (CI grün) und **nach GitHub
gepusht** ist. Read the Docs baut nur aus dem Push; das Deployment läuft nach grüner CI automatisch.

## Stand

Fundament steht (siehe Archiv, Phase 0): FastAPI-Backend mit OSCAL-Katalog-Loader, React-Frontend mit
Katalogsuche, CI/CD nach oscal.neoprehn.de, zweisprachige Doku. Aktuell geladen: NIST SP 800-53 Rev5
(1196 Controls inkl. Enhancements) sowie die Low/Moderate/High-Baselines (noch nicht aufgelöst).

## Vorbild myctrl.tools — was wir übernehmen

| myctrl.tools | neo-oscal |
|---|---|
| Framework-Katalog (Controls, Families, Baselines) | Catalog + Profile (Phasen 1–2) |
| Crosswalk zwischen Frameworks | Phase 3 |
| Technology Guidance (Konfig-Beispiele, Verifikationsbefehle) | Component Definition (Phase 4) |
| Suche, Vergleich, Favoriten, Notizen | Phase 1 + 7 |
| Assessments, Whiteboards (lokal im Browser) | SSP/Assessment (Phasen 5–6) |
| Öffentliche REST-API `/api/v1/*` (nur lesend) | Phase 1 (versionierte API) |
| llms.txt / KI-Fragen je Control | Phase 8 (optional) |

Abweichung: neo-oscal arbeitet **OSCAL-nativ** (verlustfreier Import/Export), myctrl.tools nutzt ein
eigenes Datenmodell.

---

## Phase 1 — Katalog-Browser *(aktiv)*

- [~] OSCAL-Catalog-Modelle und Loader (verlustfrei) — Gerüst vorhanden
- [ ] Control-Detailansicht: Statement, Guidance, Parameter, Teile (`parts`), Links, Enhancements
- [ ] Navigation nach Gruppen/Families, Breadcrumbs
- [ ] Volltextsuche über ID, Titel, Prosa
- [ ] Weitere Kataloge laden: NIST SP 800-171 Rev3, CSF 2.0 (aus `usnistgov/oscal-content`)
- [ ] Versionierte API `/api/v1/*` (frameworks, controls, search) mit Paginierung
- [ ] Frontend: Routing, Layout, Suchergebnisse verlinkt, Responsive
- [ ] Tests für API-Verträge, Doku (DE/EN)

## Phase 2 — Profile & Baselines

- [ ] Profile-Modell (imports, include/exclude, `set-parameters`, `modify`)
- [ ] Profile-Auflösung (Profile Resolution) zu einem aufgelösten Katalog
- [ ] NIST-Baselines Low/Moderate/High anzeigen und vergleichen
- [ ] Eigene Profile anlegen/bearbeiten (Auswahl, Parameterwerte)
- [ ] Abgleich gegen die NIST-Referenzauflösung (Testdaten)

## Phase 3 — Crosswalk

- [ ] Mapping-Datenmodell (OSCAL-Mapping bzw. eigenes Format) und Quelle klären (siehe Offene Entscheidungen)
- [ ] Control-zu-Control-Zuordnung zwischen Frameworks (z. B. 800-53 ↔ ISO 27001/CSF)
- [ ] Anzeige im Control-Detail, Vergleichsansicht zweier Frameworks

## Phase 4 — Komponenten & Technology Guidance

- [ ] Component-Definition-Modell
- [ ] Komponenten (z. B. AWS, Kubernetes) mit Control-Umsetzung und Verifikationsbefehlen
- [ ] Guidance-Seiten je Technologie

## Phase 5 — System Security Plan (SSP)

- [ ] Persistenz festlegen (siehe Offene Entscheidungen), Nutzerdaten vom Katalog trennen
- [ ] SSP-Modell: System, Inventar, Control-Implementation je Control
- [ ] Bearbeitungs-UI (Status, Verantwortliche, Beschreibung)

## Phase 6 — Assessment

- [ ] Assessment Plan, Assessment Results, POA&M
- [ ] Findings/Observations je Control, Verknüpfung mit dem SSP

## Phase 7 — Export, Validierung, Komfort

- [ ] Export als OSCAL JSON/YAML/XML (verlustfrei)
- [ ] Validierung gegen die offiziellen OSCAL-JSON-Schemas
- [ ] Favoriten, Notizen, Vergleich (wie myctrl.tools)

## Phase 8 — Optional

- [ ] KI-Unterstützung je Control (Erklären, Umsetzungsvorschläge)
- [ ] `llms.txt`/Markdown-Exporte
- [ ] Mehrsprachige Controls (DE) — Quellenlage prüfen

## Querschnitt

- [ ] `workers 2` vs. Speicher: Katalog je Worker geladen; bei vielen Katalogen auf gemeinsames Laden/Cache umstellen
- [ ] Authentifizierung, sobald Nutzerdaten (SSP/Assessments) serverseitig liegen
- [ ] Backups der Nutzerdaten
- [ ] Node-20-Deprecation der GitHub Actions (`checkout@v4`, `setup-node@v4`) beobachten

---

## Offene Entscheidungen

1. **Persistenz der Nutzerdaten:** serverseitig (SQLite + SQLModel, passt zu FastAPI) oder wie myctrl.tools lokal
   im Browser (IndexedDB)? Empfehlung: SQLite, weil das Tool für eine Person auf eigenem Server läuft und Export
   als OSCAL ohnehin serverseitig sinnvoll ist.
2. **Crosswalk-Quelle:** eigene Pflege, OSCAL-Mapping-Modell oder externes Datenset (z. B. Secure Controls Framework)?
3. **Referenzprojekte von myctrl.tools:** welche Repos sind gemeint und was wird davon genutzt? (zu klären)
4. **Frontend-Zustandsverwaltung/Router:** React Router + TanStack Query als Standard?
