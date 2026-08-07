# Uberon

**What it is**
Uberon is an integrated cross-species ontology of anatomical structures in animals. It bridges multiple species-specific ontologies and is scoped to anatomy and development across Metazoa.

**Key concepts**
- The distribution includes a core ontology, a base ontology of axioms defined within Uberon, a basic OBO edition with external ontologies and most relations excluded, and collected or composite metazoan and vertebrate editions.
- Its identifier space is `uberon`, its published PURL is `http://purl.obolibrary.org/obo/uberon.owl`, and the listed license is CC BY 3.0.
- The OBO Foundry page lists dependencies including BFO, CL, GO, NCBITaxon, PATO, RO, and others.
- Documented users apply it to sample and assay annotation, cross-species gene-expression comparison, and expression or phenotype queries.

**How you'd use it**
Annotate animal tissues or anatomical structures with shared Uberon terms so data can be compared or queried across species. Select the product matching the integration need: core/base for Uberon axioms, basic for fewer external imports and relations, or a collected/composite edition for broader multi-ontology coverage.

**LLM angle**
none stated

**Pitfalls & lessons**
Uberon is published in several editions with different inclusion and redundancy choices, so consumers must choose deliberately rather than treat every downloadable product as equivalent. The full ecosystem also has numerous ontology dependencies that an integration may need to resolve.

**Verdict**
A practical cross-species anatomy bridge with demonstrated use in biological annotation and comparative querying, but distribution choice and dependencies deserve attention.

## Sources consulted
- http://obofoundry.org/ontology/uberon
- `sources/uberon.txt`
