# SWRL (Semantic Web Rule Language)

**What it is**

SWRL is a 2004 W3C Member Submission proposing a rule language that combines OWL DL/OWL Lite with Unary/Binary Datalog RuleML. It extends OWL axioms with Horn-like rules and defines abstract, XML, and RDF syntaxes plus a model-theoretic semantics.

**Key concepts**

A rule is an implication whose antecedent and consequent are conjunctions of atoms; variables are universally quantified within a rule and variables in the consequent must also occur in the antecedent. Atoms can test class or data-range membership, properties, equality or difference, and built-in relations; the proposal includes built-ins for comparisons, math, booleans, strings, dates/times, URIs, and lists.

**How you'd use it**

Add implications that derive knowledge not conveniently expressed by OWL alone—for example, infer `hasUncle(?x,?z)` from `hasParent(?x,?y)` and `hasBrother(?y,?z)`. Prefer native OWL constructs when they already express the same fact, such as a subclass axiom instead of a rule saying every student is a person.

**LLM angle**

none stated

**Pitfalls & lessons**

The unrestricted extension makes OWL DL undecidable. The submission therefore advises restricting rule form or expressiveness to improve interoperability, reuse, implementation ease, scalability, and tractability; it also explicitly notes that W3C publication does not endorse the submission.

**Verdict**

A formally specified bridge between OWL knowledge bases and Horn-like rules, useful for explicit derivations but requiring disciplined restrictions and careful implementation expectations.

## Sources consulted

- https://www.w3.org/Submission/SWRL/
- `sources/swrl-semantic-web-rule-language.txt`
