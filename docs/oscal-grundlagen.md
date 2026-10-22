# OSCAL-Grundlagen

OSCAL (Open Security Controls Assessment Language) des NIST beschreibt Controls und deren
Bewertung in JSON, YAML und XML. Das Modell hat aufeinander aufbauende Schichten:

| Schicht | Modell | Zweck |
|---|---|---|
| Control | **Catalog** | Sammlung von Controls (z. B. NIST SP 800-53) |
| Control | **Profile** | Auswahl und Anpassung von Controls (Baseline) |
| Implementation | **Component Definition** | Wie eine Komponente Controls umsetzt |
| Implementation | **SSP** | System Security Plan |
| Assessment | **Assessment Plan** | Planung der Prüfung |
| Assessment | **Assessment Results** | Ergebnisse der Prüfung |
| Assessment | **POA&M** | Maßnahmenplan für Abweichungen |

neo-oscal liest die Modelle **verlustfrei** ein (unbekannte Felder bleiben erhalten), damit
ein Export keine Daten verliert. Aktuell ist die Schicht *Catalog* umgesetzt.

!!! note
    Die Inhalte (Katalog, Baselines) stammen aus
    [usnistgov/oscal-content](https://github.com/usnistgov/oscal-content) und werden mit
    `scripts/fetch_content.py` geladen, nicht im Repo versioniert.
