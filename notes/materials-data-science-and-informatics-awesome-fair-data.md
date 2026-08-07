# Materials-Data-Science-and-Informatics/awesome-fair-data

- **What it is** — A curated “Awesome FAIR” list from the Helmholtz Metadata Collaboration’s Hub Information & FAIR Data Commons at FZJ. It collects resources around making scientific data findable, accessible, interoperable, and reusable, spanning principles, assessment, metadata and ontology standards, discovery, provenance, software publication, and repository infrastructure.

- **Key concepts** —
  - FAIR means findable, accessible, interoperable, and reusable; the README explicitly cautions that FAIR is not the same as open, although they overlap.
  - Interoperability is supported through shared metadata and semantic models such as DCAT, Dublin Core, RDF, Schema.org, SKOS, PROV-O, and the Helmholtz Digitization Ontology.
  - Persistent identification is part of the metadata layer: ORCID identifies people, ROR identifies organizations, and PIDA generates ontology IRIs through a maintained PURL service.
  - FAIR Digital Objects are presented through linked-data/RDF infrastructure work and pragmatic packaging such as RO-Crate, which combines existing technologies and ontologies to annotate scientific datasets.
  - Provenance is treated as a first-class concern for simulation, data, ML, and research workflows, with PROV-O and combinations of RO-Crate, PROV, and BagIt listed as standards-based mechanisms.

- **How you'd use it** — Use the README as a categorized directory: learn the FAIR principles, assess an identified dataset with FAIR Evaluator or F-UJI, choose metadata/semantic standards, find ontology lookup services, discover datasets or software, select provenance tooling, or identify repository software such as Dataverse, Invenio, and InvenioRDM. Documented practical formats include JSON-LD, JSON Schema, RDF, CITATION.cff, CodeMeta in JSON/XML, RO-Crate, PROV, and BagIt; several catalog and graph entries also expose search interfaces or APIs.

- **LLM angle** — No LLM or RAG use is stated. Knowledge-graph-adjacent material includes Microsoft Academy’s PID graph, OpenAIRE/Scholex scholarly-data links, Crossref’s queryable graph of related entities, RDF/linked data, ontologies, and SOMEF’s use of ML and other techniques to extract software-publication metadata from READMEs and other documentation.

- **Pitfalls & lessons** — FAIR should not be conflated with open data. The provenance section warns that general workflow-tool lists overlap with provenance tooling but not every pipeline or workflow manager provides good provenance tracking. The README marks Microsoft Academy as shut down at the end of 2021; contribution guidance also requires checking for duplicates and placing an item in exactly one category even when it fits several.

- **Verdict** — A useful, broad FAIR-data reference index with a strong metadata, ontology, identifier, and provenance layer, but it is a curated directory rather than an ontology specification or implementation guide.

## Sources consulted

- `README.md`
- `CONTRIBUTING.md`
