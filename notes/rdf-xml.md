# RDF/XML

**What it is**
RDF/XML is a W3C-defined syntax for serializing an RDF graph as an XML document. Its media type is `application/rdf+xml`, and the fetched source identifies RDF/XML 1.1 as released on 24 February 2014.

**Key concepts**
It is an XML-derived container for RDF data and was historically the first official W3C RDF serialization format. It is also the primary exchange syntax for OWL 2 and must be supported by all OWL 2 tools.

**How you'd use it**
Use RDF/XML when an RDF graph must be exchanged as XML, particularly with OWL 2 tooling that is required to support it.

**LLM angle**
none stated

**Pitfalls & lessons**
RDF/XML is sometimes misidentified as RDF itself; it is only one syntax for expressing the RDF graph model.

**Verdict**
A standardized XML exchange syntax with mandatory OWL 2 tool support, but it should not be conflated with RDF as a whole.

## Sources consulted
- https://en.wikipedia.org/wiki/RDF/XML
- `sources/rdf-xml.txt`
