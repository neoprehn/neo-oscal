# OSCAL Fundamentals

OSCAL (Open Security Controls Assessment Language) by NIST describes controls and their
assessment in JSON, YAML and XML. The model has layers that build on each other:

| Layer | Model | Purpose |
|---|---|---|
| Control | **Catalog** | Collection of controls (e.g. NIST SP 800-53) |
| Control | **Profile** | Selection and tailoring of controls (baseline) |
| Implementation | **Component Definition** | How a component implements controls |
| Implementation | **SSP** | System Security Plan |
| Assessment | **Assessment Plan** | Planning the assessment |
| Assessment | **Assessment Results** | Assessment findings |
| Assessment | **POA&M** | Plan of action for deviations |

neo-oscal reads the models **losslessly** (unknown fields are preserved) so an export does
not drop data. Currently the *Catalog* layer is implemented.

!!! note
    Content (catalog, baselines) comes from
    [usnistgov/oscal-content](https://github.com/usnistgov/oscal-content) and is fetched with
    `scripts/fetch_content.py`; it is not versioned in the repo.
