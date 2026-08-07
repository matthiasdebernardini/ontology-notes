# DCMI Metadata Terms

**What it is**
DCMI Metadata Terms is the authoritative specification of metadata terms maintained by the Dublin Core Metadata Initiative. It includes the original fifteen Dublin Core elements plus several dozen properties, classes, datatypes, and vocabulary encoding schemes, expressed as RDF vocabularies for Linked Data.

**Key concepts**
- Four namespaces cover the original elements (`/elements/1.1/`), broader terms (`/terms/`), the DCMI Type Vocabulary (`/dcmitype/`), and vocabulary-description terms (`/dcam/`).
- Each term has a URI, label, definition, and type; applicable terms may also declare domain, range, hierarchy, membership, or equivalence information.
- The specification encourages `/terms/` for new use while promising indefinite support for `/elements/1.1/`.

**How you'd use it**
Choose stable DCMI URIs to describe resources and combine them with compatible vocabularies in an application profile. In non-RDF systems such as XML, JSON, UML, or relational databases, the document says you can treat RDF relations as usage suggestions and rely on the natural-language definitions, notes, and examples.

**LLM angle**
none stated

**Pitfalls & lessons**
The original fifteen properties exist in parallel in `/elements/1.1/` and `/terms/`; the source says most users can treat them as equivalent, but their formal ranges differ and matter to RDF applications.

**Verdict**
A strong primary reference for selecting and interpreting Dublin Core terms, especially when URI stability and formal RDF semantics matter.

## Sources consulted
- http://dublincore.org/documents/dcmi-terms/
- `sources/dcmi-metadata-terms.txt`
