# Product Types Ontology

**What it is** The Product Types Ontology provides GoodRelations-compatible class definitions for product or service types that have entries in English Wikipedia. It is intended for Semantic Web e-commerce and imports the GoodRelations vocabulary.

**Key concepts** Wikipedia-based product identifiers; GoodRelations compatibility; RDF/XML and OWL; per-class representations; a requested-class dump; CC BY-SA 3.0 licensing.

**How you'd use it** Use Product Ontology classes alongside GoodRelations when describing the type of a commercial product or service, and retrieve the dump or follow `rdfs:seeAlso` links when class data beyond the ontology header is needed.

**LLM angle** none stated

**Pitfalls & lessons** The root ontology document contains only the header. The dump includes only repeatedly requested, non-disambiguation classes and omits comments and non-English labels, which must be fetched through linked class representations.

**Verdict** A focused bridge from Wikipedia product/service types into GoodRelations-based e-commerce data, but consumers must account for its distributed and selective class data.

## Sources consulted

- http://www.productontology.org/
- `sources/product-types-ontology.txt`
