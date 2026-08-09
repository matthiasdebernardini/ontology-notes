# Quine and Ontological Commitment

**What it is**
Quine's 1948 paper "On What There Is" gives the criterion that makes ontology tractable for engineers. Quine's problem was that arguments about what exists get stuck: to deny that something exists, you seem to have to refer to it first. His move was to stop asking what exists and start asking what a *theory* says exists. A theory's ontological commitments are whatever must be in the range of its quantified variables for its statements to come out true. His slogan, in his own words, is "To be is to be the value of a variable" — the familiar "bound variable" version of it is Boolos's later title, not Quine's sentence. Quine's own statement of the criterion is that "a theory is committed to those and only those entities to which the bound variables of the theory must be capable of referring in order that the affirmations made in the theory be true."

**Key concepts**
Ontological commitment; "To be is to be the value of a variable"; regimenting a theory into first-order logic to read off its commitments; ontology as a property of a language rather than of the world; the criterion says nothing about which theory is correct.

**How you'd use it**
Use Quine's criterion as a debugging tool on any schema, database, or ontology. Ask what the model quantifies over. If your system has an `Employee` table with a `manager_id`, the schema is committed to employees and to a managing relation, but not to teams, contracts, or roles. If a competency question requires teams and nothing in the model quantifies over teams, no amount of querying will produce an answer. Guarino, Oberle and Staab give a construction of the same shape without citing Quine: an ontological commitment is a total function mapping each vocabulary symbol either to an element of the domain or to an intensional relation, which in turn fixes the set of intended models. Their paper never mentions Quine, so read the resemblance as structural rather than as a lineage anyone has traced.

**LLM angle**
none stated

**Pitfalls & lessons**
The criterion is deliberately neutral about truth. Quine says so directly: asked "how are we to adjudicate among rival ontologies? Certainly the answer is not provided by the semantical formula 'To be is to be the value of a variable'." It tells you what a theory is committed to, not whether the theory is any good. Quine also observes that "disagreement in ontology involves basic disagreement in conceptual schemes" while the schemes still converge in practice. My own reading of that, not his: two teams can model the same domain with different commitments and neither be at fault, which makes ontology alignment a standing engineering problem rather than a sign that somebody blundered.

**Verdict**
Worth studying, and short. Quine's criterion is the one philosophical idea in this corpus that transfers directly to a schema review, because it turns "what exists" into the answerable question "what does this model quantify over."

## Sources consulted
- https://rintintin.colorado.edu/~vancecd/phil375/Quine.pdf
- https://plato.stanford.edu/entries/ontological-commitment/
- https://iaoa.org/isc2012/docs/Guarino2009_What_is_an_Ontology.pdf
- `research/firecrawl/quine-onwhatthereis.md`
- `research/firecrawl/quine-sep-commitment.md`
- `research/firecrawl/guarino-what-is-ontology.md`
