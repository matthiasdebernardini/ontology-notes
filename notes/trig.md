# TriG

**What it is**
TriG is a plain-text serialization format for RDF graphs, named graphs, and RDF datasets. It extends Turtle, uses the `.trig` extension and `application/trig` media type, and is a W3C Recommendation.

**Key concepts**
A TriG document can declare prefixes and group RDF statements inside graph blocks identified by names. The source’s example uses three interlinked named graphs, including statements about who asserted or quoted other graphs.

**How you'd use it**
Write Turtle-like triples inside named graph blocks when one text document needs to preserve multiple related RDF graphs and their identities.

**LLM angle**
none stated

**Pitfalls & lessons**
The linked Yacker validator is explicitly described as not handling sub-graphs and not validating the page’s example, so validator capability should not be assumed from TriG support alone.

**Verdict**
A compact, readable RDF dataset syntax when named-graph structure matters.

## Sources consulted
- https://en.wikipedia.org/wiki/TriG_(syntax)
- `sources/trig.txt`
