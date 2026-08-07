# LODE

**What it is**
LODE 2.0 is an open-source service that extracts entities and textual definitions from semantic artifacts and renders browsable, linked HTML documentation. It can produce live documentation for browsing or a ZIP containing a static site, RDF serializations, and stylesheets for deployment.

**Key concepts**
`/extract` returns HTML or Turtle, RDF/XML, or N3, optionally scoped to one resource; `/build` creates one HTML page per resource plus serializations and stylesheets. Options cover annotation language, structural warnings, direct imports or their transitive closure, URL caching, file upload, and content negotiation between human-readable pages and raw ontology files.

**How you'd use it**
Submit an ontology URL or supported local RDF file to generate documentation, enable warnings or imported axioms as needed, and use `/build` for a one-off static bundle. For CI/CD or GitHub Actions, install LODE locally and run `lode build` instead of automating the web `/build` endpoint.

**LLM angle**
none stated

**Pitfalls & lessons**
Despite the service’s broader semantic-artifact description, the implementation-status section says only `read_as=owl` is currently enabled; RDF/RDFS and SKOS modes return errors. URL results may come from a four-hour cache unless `cache=false`, and specifying both `imported` and `closure` gives precedence to `imported`.

**Verdict**
A useful publishing utility for turning OWL artifacts into navigable live or static documentation, with clear current limits outside OWL.

## Sources consulted
- https://essepuntato.it/lode/
- `sources/lode.txt`
