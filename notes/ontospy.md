# Ontospy

**What it is**

Ontospy is a lightweight Python library and command-line tool for inspecting vocabularies encoded in RDF-family languages. It can scan RDFS, OWL, SKOS, and SHACL material, expose ontology information through Python objects, and generate documentation.

**Key concepts**

- It works as a Python package, direct command-line scanner, or optional interactive shell/REPL.
- Models can be loaded from files or graph URIs, then interrogated for classes, properties, SKOS concepts, SHACL shapes, and entity relationships.
- A local repository can cache ontologies for later inspection.
- Documentation output includes simple HTML, Markdown, and interactive D3.js-based visualizations; version 2 moved this facility from Django to Jinja and added SHACL support.

**How you'd use it**

Run `ontospy scan` against a graph URI for a quick terminal inventory, instantiate `Ontospy` in Python when an application needs schema information, or use `ontospy gendocs` to produce browsable ontology documentation. Cache frequently inspected vocabularies locally when repeated loading would be inconvenient.

**LLM angle**

none stated

**Pitfalls & lessons**

Ontospy explicitly does not edit ontologies. The interactive shell requires the optional `readline` dependency, and the version 2 internal changes may break custom extensions built around the older documentation generator.

**Verdict**

A focused inspection and documentation utility for people who want RDF schema visibility without opening a full ontology editor; use another tool when authoring or editing is required.

## Sources consulted

- http://lambdamusic.github.io/Ontospy/
- `sources/ontospy.txt`
