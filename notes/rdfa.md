# RDFa

**What it is**
RDFa, or Resource Description Framework in Attributes, is a W3C Recommendation that adds attributes to HTML, XHTML, and XML-based documents so they can carry rich metadata. Its RDF mapping embeds subject-predicate-object expressions in markup and lets compliant user agents extract RDF triples.

**Key concepts**
- `about` identifies the resource being described; `rel` and `rev` express relationships.
- `src`, `href`, and `resource` identify a partner resource, while `property` names a property.
- `content`, `datatype`, and `typeof` control values, datatypes, and RDF types.
- RDFa Lite narrows the model to five attributes: `vocab`, `typeof`, `property`, `resource`, and `prefix`.
- RDFa 1.1 works with HTML 4/5 as well as XML because it no longer depends on XML namespaces.

**How you'd use it**
Annotate visible web content with vocabulary terms—for example, Dublin Core title, creator, and date properties—so the page remains readable while software can extract triples. For ordinary markup needs, the source presents RDFa Lite as a smaller, upward-compatible subset.

**LLM angle**
none stated

**Pitfalls & lessons**
Version and host-language distinctions matter: RDFa 1.0 is associated with older XHTML, whereas RDFa 1.1 is generic across HTML and XML. The usage figures in the fetched page are historical (2013 and 2017), including an explicit update marker, so they should not be treated as current adoption data.

**Verdict**
A practical bridge between human-facing web markup and extractable RDF, with RDFa Lite offering the clearest entry point described by the source.

## Sources consulted
- https://en.wikipedia.org/wiki/RDFa
- `sources/rdfa.txt`
