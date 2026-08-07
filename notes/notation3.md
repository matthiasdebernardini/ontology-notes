# Notation3

**What it is**
Notation3 (N3) is a compact, non-XML serialization for RDF models designed for human readability. It also goes beyond RDF serialization by supporting RDF-based rules, while Turtle is described as its simplified RDF-only subset.

**Key concepts**
- N3 uses prefixes, compact subject/predicate repetition, QNames, blank-node shorthand, lists, and RDF paths.
- It adds quantification directives such as `@forAll` and `@forSome`, statement lists, and implication or equivalence operators that the page says Turtle and N-Triples lack.
- The documented filename extension is `.n3`, and the media type is `text/n3;charset=utf-8`.

**How you'd use it**
Write RDF graphs in a more concise form than RDF/XML, using prefixes and punctuation to reduce repetition. Choose N3 rather than its Turtle subset when the model needs the additional rule, quantification, path, or statement-list features shown on the page.

**LLM angle**
none stated

**Pitfalls & lessons**
The page's feature comparison is explicitly marked incomplete. N3 should not be treated as interchangeable with Turtle: the example is valid in both, but several N3 constructs listed on the page are not Turtle syntax.

**Verdict**
A readable RDF notation with meaningful logic and rule extensions, useful when Turtle's RDF-only scope is too narrow.

## Sources consulted
- https://en.wikipedia.org/wiki/Notation3
- `sources/notation3.txt`
