# Wine Ontology

**What it is**
The Wine Ontology is an example OWL ontology derived from the DAML Wine ontology, with substantial changes to its region relations. It imports the OWL Guide food ontology and models wines, grapes, wineries, regions, vintages, and sensory descriptors.

**Key concepts**
`Wine` is constrained by maker, grape, sugar, flavor, body, color, and location properties. The file demonstrates OWL constructs including cardinality and value restrictions, intersections, unions, enumerated descriptor values, inverse properties, a transitive `locatedIn`, a symmetric `adjacentRegion`, and functional descriptor properties.

**How you'd use it**
Use it as a concrete OWL/RDF example for exploring class definitions and reasoning over wine categories—for example, `WhiteWine` combines `Wine` with a white-color value, while `FrenchWine` combines `Wine` with location in `FrenchRegion`.

**LLM angle**
none stated

**Pitfalls & lessons**
The ontology depends on an imported food ontology, and its own comment warns that its region-based relations were substantially changed from the DAML source. Its exact cardinality constraints are part of the model, not merely documentation.

**Verdict**
A compact, feature-rich teaching ontology that makes many OWL modeling patterns inspectable in one domain.

## Sources consulted
- https://www.w3.org/TR/owl-guide/wine.rdf
- `sources/wine-ontology.txt`
