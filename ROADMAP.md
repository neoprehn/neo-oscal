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
| Astro + React + Tailwind CSS (statisches JSON) | Vite + React + FastAPI; Tailwind übernehmen, Astro offen (Entscheidung 3) |

Abweichung: neo-oscal arbeitet **OSCAL-nativ** (verlustfreier Import/Export), myctrl.tools nutzt ein
eigenes Datenmodell.

---

## Phase 1a — Graph-Datenbank-Fundament *(aktiv, zuerst)*

Entscheidung 2026-10-23: **Neo4j Community (Docker) auf dem VPS** als zentrale Datenbank, **FastAPI bleibt**,
**Frontend bleibt Vite + React + Tailwind** (kein Astro). Das Original-OSCAL-JSON bleibt je Dokument erhalten
(verlustfreier Export); der Graph ist der Index über Controls und ihre Beziehungen.

- [ ] Graph-Schema entwerfen (Catalog, Group, Control, Param, Part; Beziehungen `HAS_GROUP`, `HAS_CONTROL`,
      `ENHANCES`, `RELATED_TO`, später `IMPORTS`, `MAPS_TO`, `IMPLEMENTS`) — als Doku + Constraints/Indizes
- [ ] Lokale Entwicklung: `docker-compose.yml` mit Neo4j, Zugangsdaten über `.env` (nicht im Repo)
- [ ] Server: Neo4j-Container auf dem VPS (Ports nur an `127.0.0.1`, Volume, Speicherlimit), Backup-Konzept.
      VPS-Stand 2026-10-23: 7,7 GiB RAM gesamt, ~2,3 GiB belegt, ~5,4 GiB verfügbar, **kein Swap**.
      Vorgabe: Container-Limit 2 GiB, Heap 512 MiB–1 GiB, Page-Cache 512 MiB (kein Swap → bei zu hohen Werten droht OOM-Kill
      auch für FAIR/IAM). `docker ps` auf dem Server prüfen, ob Docker schon läuft.
- [ ] Backend: Neo4j-Treiber, Konfiguration, Health-Check; Tests mit Testcontainer bzw. Compose-Dienst in der CI
- [ ] Import-Pipeline: OSCAL-Katalog (JSON) → Graph (idempotent, versioniert), Original-JSON als Quelle ablegen
- [ ] API liest aus dem Graph statt aus dem Speicher (löst auch das `--workers 2`-Thema)
- [ ] Doku (DE/EN): Datenmodell, Betrieb, Backup

## Phase 1 — Katalog-Browser

- [~] OSCAL-Catalog-Modelle und Loader (verlustfrei) — Gerüst vorhanden
- [ ] Control-Detailansicht: Statement, Guidance, Parameter, Teile (`parts`), Links, Enhancements
- [ ] Navigation nach Gruppen/Families, Breadcrumbs
- [ ] Volltextsuche über ID, Titel, Prosa
- [ ] Weitere Kataloge laden: NIST SP 800-171 Rev3, CSF 2.0 (aus `usnistgov/oscal-content`)
- [ ] Versionierte API `/api/v1/*` (frameworks, controls, search) mit Paginierung
- [ ] Frontend: Tailwind CSS einführen (wie myctrl.tools), Routing, Layout, Suchergebnisse verlinkt, Responsive
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

- [ ] Nutzerdaten (SSP) im Graph vom Katalog trennen (eigene Labels/Namespaces), Berechtigungen klären
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

## Architekturregeln Frontend (halten Astro als spätere Option offen)

- [ ] **Komponenten ohne Router-Kopplung:** Darstellung (Control-Karte, Tabellen, Suche) in eigenen React-Komponenten,
      Daten nur als Props; nur dünne „Seiten“-Dateien kennen Routing und Datenabruf.
- [ ] **Daten nur über einen API-Client** (ein Modul, keine verstreuten `fetch`-Aufrufe), damit ein Astro-Build
      dieselbe API nutzen kann.
- [ ] **Sprechende, stabile URLs** von Anfang an, z. B. `/frameworks/800-53/ac-2` statt `/?id=ac-2`.
- Astro (Vorab-Renderung nur für öffentliche Katalogseiten, SPA bleibt für SSP/Assessments) wird neu bewertet,
  falls die Seite öffentlich auffindbar sein soll. Beim Umstieg bleiben Backend, Neo4j und API unverändert; die CI
  bräuchte dann eine erreichbare Datenquelle für den Build.

## Querschnitt

- [ ] `workers 2` vs. Speicher: Katalog je Worker geladen — entfällt mit Phase 1a (Graph als gemeinsame Quelle)
- [ ] Authentifizierung, sobald Nutzerdaten (SSP/Assessments) serverseitig liegen
- [ ] Backups der Nutzerdaten
- [ ] Node-20-Deprecation der GitHub Actions (`checkout@v4`, `setup-node@v4`) beobachten

---

## Offene Entscheidungen

1. ~~Persistenz der Nutzerdaten~~ — **entschieden (2026-10-23): Neo4j Community in Docker, serverseitig**, weil die
   Beziehungen zwischen den Katalogen (Crosswalks, Profile, Umsetzungen) im Mittelpunkt stehen; FastAPI bleibt.
   Der VPS hat laut Nutzer ausreichend freie Ressourcen (genaue Werte per `free -h` vor der Installation notieren).
2. **Crosswalk-Quelle:** eigene Pflege, OSCAL-Mapping-Modell oder externes Datenset (z. B. Secure Controls Framework)?
3. ~~Frontend-Technik~~ — **entschieden (2026-10-23): Vite + React + Tailwind CSS, kein Astro.** myctrl.tools ist laut
   [About-Seite](https://myctrl.tools/about/) mit Astro, React und Tailwind gebaut (statisches JSON, Nutzerdaten im
   Browser). Vorgerenderte Seiten (Astro) lohnen sich nur für öffentlich auffindbare Katalogseiten; für ein
   persönliches Werkzeug nicht. Neu bewerten, falls die Seite öffentlich werden soll.
4. **Frontend-Zustandsverwaltung/Router:** React Router + TanStack Query als Standard.
