# DL Query (class expression)

**What it is**
The DL Query tab is a Protégé Desktop feature for searching a classified ontology with class expressions based on Manchester OWL syntax. It ships with Protégé Desktop 4, 5, and later as both a tab and a view widget.

**Key concepts**
Queries can retrieve individuals or classes according to inferred relationships, including subclasses and superclasses of an expression. The examples combine classes, properties, values, datatypes, cardinality restrictions, existential or universal restrictions, and negation.

**How you'd use it**
Start FaCT++ or HermiT to classify the active ontology, confirm that the inferred class hierarchy is populated, enter a Manchester-syntax expression, and select the result types you want. A useful query can be added to the ontology as a newly named defined OWL class.

**LLM angle**
none stated

**Pitfalls & lessons**
Queries only run on a classified ontology, and individual matches are not shown unless the “Individuals” result option is checked. If the inferred hierarchy contains only `Thing`, the ontology may not have been classified successfully.

**Verdict**
A practical Protégé interface for testing class definitions and exploring reasoner-derived matches before committing a definition to the ontology.

## Sources consulted
- https://protegewiki.stanford.edu/wiki/DLQueryTab
- `sources/dl-query-class-expression.txt`
