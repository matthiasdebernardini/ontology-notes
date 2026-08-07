# KBpedia

**What it is**
KBpedia is an open-source knowledge graph that integrates seven public knowledge bases into one computable structure for data interoperability and knowledge-based AI. Its distribution includes the KBpedia Knowledge Ontology (KKO), the full graph, mappings, and about 70 largely disjoint typologies.

**Key concepts**
- The seven core sources are Wikipedia, Wikidata, schema.org, DBpedia, GeoNames, OpenCyc, and UNSPSC products and services.
- The site reports more than 58,000 reference concepts, mappings to about 40 million entities, and 5,000 relations and properties.
- KKO is the upper structure; modular typologies can be substituted or expanded, and candidate additions are subjected to logic and consistency tests.
- KBpedia primarily uses OWL 2 and also names RDF, RDFS, SPARQL, SKOS, and SWRL among its open standards.

**How you'd use it**
Browse or query the graph through its SPARQL endpoint, download its resources, map an existing vocabulary or instance data into its scaffolding, and extend it with domain concepts. The source proposes uses including concept and entity tagging, disambiguation, semantic search, data integration, fact extraction, and creating machine-learning training sets or embedding corpora.

**LLM angle**
none stated

**Pitfalls & lessons**
The coverage, scale, speed, and accuracy figures on the fetched page are project claims rather than evaluation results presented in the source. Integrating another vocabulary still requires explicit mapping, which the site itself describes as essential.

**Verdict**
An ambitious cross-domain integration layer with broad public-KB mappings and concrete semantic-search and machine-learning workflows, best assessed by testing its downloadable graph against the target domain.

## Sources consulted
- http://kbpedia.org/
- `sources/kbpedia.txt`
