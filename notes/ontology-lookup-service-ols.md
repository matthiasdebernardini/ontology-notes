# Ontology Lookup Service (OLS)

- **What it is** — The rendered Ontology Lookup Service page is a browsable catalog of ontologies, prominently including OBO Foundry resources and many scientific and biomedical domains. Its catalog rows identify an ontology, ID, description, and actions for searching classes, properties, and individuals.

- **Key concepts** — Ontology catalogs, controlled-vocabulary and OWL ontology discovery, domain tags, ontology identifiers, class/property/individual browsing, and cross-domain coverage spanning anatomy, chemistry, disease, phenotype, organisms, simulation, and upper ontologies.

- **How you'd use it** — Filter the catalog by tags or text, select an ontology from the paginated results, and follow its actions to search classes, properties, or individuals. The rendered navigation also exposes API documentation, downloads, an MCP server, and informational pages.

- **LLM angle** — none stated

- **Pitfalls & lessons** — The unrendered page is only a JavaScript application shell, so automated consumers must use the service's rendered interface or documented machine interfaces rather than assume the initial HTML contains the catalog. Individual catalog descriptions vary in detail and should not be treated as a substitute for each ontology's own documentation.

- **Verdict** — Worth deeper study as a practical discovery and lookup front end for a large, domain-tagged collection of scientific ontologies.

## Sources consulted

- [https://www.ebi.ac.uk/ols4/ontologies](https://www.ebi.ac.uk/ols4/ontologies)
- `sources/ontology-lookup-service-ols.txt`
