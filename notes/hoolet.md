# Hoolet

**What it is**

Hoolet is a prototype OWL-DL reasoner that translates an ontology into first-order axioms and sends them to a first-order prover for consistency checking. Its implementation uses the WonderWeb OWL API for parsing, Vampire for reasoning, and TPTP as the communication format; it was also extended to translate SWRL rules.

**Key concepts**
- OWL-to-first-order axiom translation.
- Consistency checking through Vampire, with TPTP allowing other compatible theorem provers in principle.
- Optional RDF-encoded SWRL rule sets activated alongside an ontology.

**How you'd use it**

On Linux, unpack the prototype, run `hooletGUI`, load an OWL ontology URL and optionally a rules URL, activate selected rules, and issue queries from the Query panel. Inputs are expected as OWL RDF/XML and rules as RDF using the proposed SWRL schema.

**LLM angle**

none stated

**Pitfalls & lessons**

The authors explicitly call the translation naive, say it is highly unlikely to scale, and position Hoolet for small illustrative examples rather than effective reasoning. The bundled prototype is Linux-only, loading an ontology clears current rules, rule class atoms must be named classes, and Hoolet's performance should not be treated as evidence about Vampire's general performance.

**Verdict**

Useful as a small-scale demonstrator of OWL/SWRL translation into first-order theorem proving, not as a scalable production reasoner.

## Sources consulted
- http://owl.man.ac.uk/hoolet/
- `sources/hoolet.txt`
