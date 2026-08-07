# Alignment API

**What it is**
The Alignment API is a Java API and implementation for expressing and sharing ontology alignments. It uses an extensible RDF alignment format to represent sets of correspondences between entities in ontologies that need reconciliation.

**Key concepts**
Its five main interfaces are `OntologyNetworks`, `Alignment`, `Cell`, `Relation`, and `Evaluator`. Services include storing and finding alignments, piping alignment algorithms, thresholding and hardening results, generating transformations or axioms, and comparing alignments with measures such as precision and recall; the package also includes the `ontowrap` wrapper for several ontology APIs.

**How you'd use it**
Use the Java API, command line, web interface, or Alignment Server to represent, manipulate, evaluate, generate, store, and share alignments. The server exposes documented REST and SOAP messaging, while EDOAL is available for expressive, declarative alignments.

**LLM angle**
none stated

**Pitfalls & lessons**
The project emphatically states that the API is not itself an ontology matcher. Its bundled trivial matchers are examples, not serious baselines for matcher comparisons, so evaluations should name and compare actual matching systems rather than claim comparison with “the Alignment API.”

**Verdict**
A reusable alignment representation and processing infrastructure, not a substitute for a competitive matching algorithm.

## Sources consulted
- http://alignapi.gforge.inria.fr/
- `sources/alignment-api.txt`
