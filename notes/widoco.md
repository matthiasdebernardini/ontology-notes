# WIDOCO

- **What it is** — WIDOCO (WIzard for DOCumenting Ontologies) generates enriched, customizable, human-readable ontology documentation through a GUI wizard or command line. It extends LODE for term documentation and integrates WebVOWL visualization, OOPS! evaluation, Licensius license metadata, PROV-O provenance, and Bubastis-based version changelogs.
- **Key concepts** —
  - Keep publication metadata with the ontology as annotations when possible; the docs recommend this over a separate `.properties` file because embedded metadata is easier to maintain across releases.
  - Describe the vocabulary itself with stable namespace and prefix, name/title/description, creators and contributors, license, version IRI and version information, creation date, and a link to the previous version. WIDOCO uses the previous-version relation to generate changelogs and emits a W3C PROV-O-compliant provenance page.
  - Describe classes and properties with labels and definitions; optional term annotations cover examples, original source, rationale, deprecation, and status. Supported term statuses include `unstable`, `testing`, `stable`, and `archaic`.
  - Treat publication as more than an HTML page: WIDOCO supports content negotiation, multiple ontology serializations, JSON-LD snippets in generated HTML, imported-ontology handling, evaluation reports, and diagrams.
- **How you'd use it** — Download the release JAR and run the GUI, or invoke `java -jar widoco-VERSION-jar-with-dependencies.jar` with a local ontology (`-ontFile`) or ontology URI (`-ontURI`) and an output folder. Docker and Maven/JitPack dependency workflows are also documented. Customize output through ontology annotations or `config.properties`; useful switches include multilingual generation, WebVOWL, OOPS!, imported terms, Apache publication bundles, section replacement, and serialization display controls. Inputs shown in the docs include Turtle/OWL ontology data, while generated publication support includes HTML plus Turtle, RDF/XML, N-Triples, and JSON-LD serialization links.
- **LLM angle** — none stated
- **Pitfalls & lessons** — A separate `.properties` file must be maintained independently, so ontology annotations are recommended. Entity-valued creator/contributor/publisher metadata is resolved only inside the ontology; external URI resolution is not supported. Generated split-section HTML may appear incomplete when opened directly from the local filesystem because browsers block local section loading; use `-uniteSections` or serve the files, noting that the LODE visualization is unavailable in the local united-file case. The JAR requires Java 8 or newer.
- **Verdict** — A focused ontology publication utility for turning annotated ontologies into customizable, standards-aware documentation, provenance, visualization, evaluation, and version-change artifacts.

## Sources consulted

- `README.md`
- `doc/metadataGuide/guide.md`
- `doc/bestPractices/sections/introduction-en.html`
- `doc/bestPractices/sections/checklist-en.html`
