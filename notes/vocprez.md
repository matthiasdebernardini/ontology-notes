# VocPrez

- **What it is** — VocPrez is an archived, read-only web delivery system for RDF vocabularies formulated in SKOS. It presents vocabulary data over HTTP as human-readable pages and machine-readable representations, and the project says its functionality is now incorporated into Prez.

- **Key concepts** —
  - VocPrez treats a SKOS `ConceptScheme` as synonymous with a vocabulary and ships presentation support for SKOS `ConceptScheme`, `Collection`, and `Concept`, plus registers/containers of those resources.
  - It distinguishes an information-model view, defined by a formal *profile*, from the media format used to serialize that view; multiple profiles and multiple media types per profile are supported.
  - Its pyLDAPI foundation turns RDF data into Linked Data, exposing the same vocabulary material in human- and machine-readable forms.

- **How you'd use it** — Configure one or more vocabulary sources and instance details, then serve the Python/Flask WSGI application (the root README gives `gunicorn wsgi:application` for local use). Documented back ends include RDF databases/triplestores through SPARQL, local RDF files, Research Vocabularies Australia, VocBench3, vocabulary APIs, and GitHub; adapters populate a cached vocabulary index. Jinja2 templates produce HTML for SKOS objects, while mapping code provides RDF or other machine-readable formats, and deployments can override templates for institutional branding.

- **LLM angle** — none stated

- **Pitfalls & lessons** —
  - The repository is archived and directs users to Prez, where VocPrez has been incorporated.
  - VocPrez is a publisher, not a SKOS editor; it expects an existing configured data source.
  - It is ready for SKOS-only vocabularies; SKOS-plus-extra features require a fork or enhancement.
  - Release 2.4 changed configuration incompatibly by replacing `CACHE_DIR` with a required `CACHE_FILE`, and the 1.0 release is explicitly unsupported.

- **Verdict** — A focused SKOS-to-Linked-Data publishing interface with profile-aware HTML/RDF delivery, useful as documented precedent but superseded by Prez.

## Sources consulted

- `README.md`
- `docs/README.md`
- `docs/_coverpage.md`
- `docs/_media/README.md`
- `docs/_navbar.md`
- `docs/_sidebar.md`
- `docs/contacts.md`
- `docs/other/changelog.md`
- `docs/other/faq.md`
- `RELEASE_NOTES.md`
