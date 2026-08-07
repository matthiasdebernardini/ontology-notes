# Common Core Ontologies (CCO)

- **What it is** — CCO is a suite of eleven ontologies containing logically defined generic terms and relations intended to cover entities across domains. It is a mid-level ontology extending the ISO-standard top-level Basic Formal Ontology (BFO), adding broadly reusable classes such as person, facility, date, employment, nickname, and measurement.

- **Key concepts**
  - CCO occupies the mid-level between BFO’s most generic categories and domain-specific ontologies; its authors explicitly encourage users to publish their own domain extensions rather than expanding CCO indefinitely with domain content.
  - Its eleven modules cover geospatial entities, information entities, events, time, agents, qualities, measurement units, currencies, facilities, artifacts, and extended relations.
  - Documented design patterns are motivated by use cases and competency questions, and include a Mermaid graph, a visualization, and a SPARQL query.

- **How you'd use it** — Clone the repository and import `AllCoreOntology.ttl` into Protégé to assemble the eleven modules, or use the pre-merged files under `src/cco-merged/` to avoid managing imports. Releases are also viewable through the Industrial Ontology Portal; documented patterns can be reused for RDF data mapping and SPARQL querying.

- **LLM angle** — The documentation explicitly recommends reusing CCO design patterns in knowledge graphs to speed data mapping and querying and improve consistency and interoperability. No LLM- or RAG-specific use is stated.

- **Pitfalls & lessons**
  - CCO is not intended to absorb content specific to individual domains; that content belongs in domain extensions.
  - The repository is undergoing modernization through planned 3.0 and 4.0 structural changes. The Governance Board recommends waiting until after 4.0 to update, while users needing current changes should pull from `develop`.
  - Different OWL API and Protégé versions can generate spurious formatting diffs; contributors are told to make a token change and inspect the diff before substantive edits, then verify that the result loads correctly in Protégé.
  - Version 2.0 changed the IRI namespace and adopted opaque local identifiers; the release summary says there were no other ontology changes from v1.7 to v2.0.

- **Verdict** — A documented cross-domain mid-level foundation for shared classes, relations, and reusable knowledge-graph patterns, intended to sit beneath separately maintained domain extensions.

## Sources consulted

- `README.md`
- `documentation/README.md`
- `documentation/user-guides/design-patterns/README.md`
- `documentation/contributing/README.md`
- `documentation/contributing/contributing.md`
- `documentation/contributing/registering IRIs.md`
- `documentation/diff-reports-previous-version/README.md`
- `documentation/diff-reports-previous-version/v1.7-release-summary.md`
