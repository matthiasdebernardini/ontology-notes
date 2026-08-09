# Quine and Ontological Commitment

**What it is**
W.V.O. Quine's 1948 paper "On What There Is" gives the criterion that makes ontology tractable for engineers. Quine's problem was that arguments about what exists get stuck: to deny that something exists, you seem to have to refer to it first. His move was to stop asking what exists and start asking what a *theory* says exists. A theory's ontological commitments are whatever must be in the range of its quantified variables for its statements to come out true. His slogan: to be is to be the value of a bound variable.

**Key concepts**
Ontological commitment; "to be is to be the value of a bound variable"; regimenting a theory into first-order logic to read off its commitments; ontology as a property of a language rather than of the world; the criterion says nothing about which theory is correct.

**How you'd use it**
Use Quine's criterion as a debugging tool on any schema, database, or ontology. Ask what the model quantifies over. If your system has an `Employee` table with a `manager_id`, the schema is committed to employees and to a managing relation, but not to teams, contracts, or roles. If a competency question requires teams and nothing in the model quantifies over teams, no amount of querying will produce an answer. Guarino's formal treatment of "ontological commitment" as a mapping from a vocabulary to an intended set of models is the direct descendant of this idea and is what OWL's model-theoretic semantics implements.

**LLM angle**
none stated

**Pitfalls & lessons**
The criterion is deliberately neutral about truth. It tells you what a theory is committed to, not whether the theory is any good. Two teams can build correct models of the same domain with completely different commitments, which is why ontology alignment is a permanent engineering problem rather than a sign that somebody made a mistake.

## Sources consulted
- https://rintintin.colorado.edu/~vancecd/phil375/Quine.pdf
- https://plato.stanford.edu/entries/ontological-commitment/
- https://iaoa.org/isc2012/docs/Guarino2009_What_is_an_Ontology.pdf
- `research/firecrawl/quine-onwhatthereis.md`
- `research/firecrawl/quine-sep-commitment.md`
