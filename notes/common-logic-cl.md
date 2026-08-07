# Common Logic (CL)

**What it is**
Common Logic is an ISO-published framework for a family of first-order-logic-based languages intended to exchange and transmit knowledge between computer systems. Concrete syntaxes are dialects that inherit CL semantics by demonstrating conformance to its abstract, model-theoretic semantics.

**Key concepts**
The standard specifies CLIF, CGIF, and XML-based XCL. Conformant dialects are comparable through translation to a common language, but they may differ in expressiveness; the page also names COLORE, Hets, and partially supporting `cltools` as implementations or supporting resources.

**How you'd use it**
Define or select a dialect whose concrete syntax maps precisely to the CL abstract syntax, then use that mapping to exchange logical knowledge across dialects. A less expressive CL subset can generally translate into a more expressive one.

**LLM angle**
none stated

**Pitfalls & lessons**
Reverse translation from a more expressive language is only defined for a subset of that language, so interchange is not automatically lossless in both directions. The article is also marked as needing more citations.

**Verdict**
A semantics-first interchange framework for heterogeneous logical syntaxes, strongest when conformance and expressiveness boundaries are made explicit.

## Sources consulted
- https://en.wikipedia.org/wiki/Common_Logic
- `sources/common-logic-cl.txt`
