Lies bitte:

    Als allererstes: git pull (bzw. mind. git fetch + Abgleich mit origin/main) — der lokale Stand kann
    hinter dem sein, was zuletzt gepusht wurde (u. a. vom automatischen Deploy-Stand oder einem anderen
    Gerät). Dieses Verzeichnis ist ein eigenes Repo (neoprehn/neo-oscal), Git-Kommandos also immer
    mit `-C oscal`, wenn Claude im Parent `Entwicklung` gestartet wurde. Erst danach die folgenden
    Dateien lesen, sonst ggf. veralteter Stand:
    ROADMAP.md — „Stand" + offene Punkte mit [ ]/[~]/[x] sowie „Offene Entscheidungen"
      (das ist der eigentliche Übergabepunkt),
    ROADMAP-ARCHIV.md — was erledigt ist (inkl. Erkenntnisse zu Server/Deploy),
    CLAUDE.md — Projektregeln (Stack, Befehle, Doku, CI/CD, Vertrauensgrenze),
    docs/betrieb.md — Pipeline und Server-Setup (Plesk, systemd, Port 8731),
    Git-Historie — jeder Commit beschreibt einen Schritt,
    das persistente Memory (MEMORY.md + memory/*.md) — wird in jede neue Session geladen.

Arbeitsweise:

    - Code-Exploration zuerst über den Knowledgegraph (codebase-memory-mcp), Projekt-Key per
      `list_projects` prüfen (Repo-Root `D:\Entwicklung\oscal`, nicht der Parent `D:\Entwicklung`).
      Vor längerer Arbeit `index_status`, nach größeren Änderungen `index_repository`.
    - Doku-DoD: jede Änderung in `docs/` UND `docs/*.en.md`, CI grün, committen und pushen. Ein Push
      auf `main` deployt nach grüner CI automatisch nach https://oscal.neoprehn.de.
    - Das Repo ist öffentlich: nie Schlüssel, Zugangsdaten oder `.env` committen (SSH-Schlüssel liegen
      unter `~/.ssh/`, GitHub-Secrets: VPS_HOST, VPS_USER, VPS_SSH_KEY).
    - Commit-Sprache Deutsch; am Ende einer Arbeitssitzung routinemäßig committen und pushen.
    - Server-Eingriffe (VPS) macht der Nutzer selbst bzw. nur nach ausdrücklicher Freigabe.

Was steht als nächstes an? (Derzeit: Phase 1 — Katalog-Browser, siehe ROADMAP.md.)
