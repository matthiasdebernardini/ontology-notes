# Description Logics (DLs)

**What it is**
Description logics are a family of formal knowledge-representation languages, generally more expressive than propositional logic and less expressive than first-order logic. They model concepts, roles, individuals, and axioms while balancing expressive power against reasoning complexity; many core reasoning problems are decidable.

**Key concepts**
- Concepts correspond to classes or unary predicates, roles to properties or binary predicates, and individuals to constants.
- A TBox states concept hierarchies; an ABox states facts about individuals.
- DL semantics interpret concepts as sets of individuals and roles as sets of ordered pairs.
- Common inference tasks include instance checking, relation checking, subsumption, and concept-consistency checking.
- DL does not generally assume unique names or a closed world.

**How you'd use it**
Use a DL to encode domain concepts and relationships, then ask a reasoner about membership, relations, subsumption, or consistency. The source identifies DLs as the logical foundation for OWL and its profiles and notes applications in ontologies, the Semantic Web, biomedical informatics, defense, climate modeling, and industrial knowledge graphs.

**LLM angle**
none stated

**Pitfalls & lessons**
Adding operators and making the TBox more complicated usually increases the computational complexity of inference. The open-world stance also means that lack of a fact does not imply its negation, and different names need not denote different things.

**Verdict**
A compact conceptual map of the logic beneath OWL, with the expressivity-versus-reasoning-cost tradeoff as the central design lesson.

## Sources consulted
- https://en.wikipedia.org/wiki/Description_logic
- `sources/description-logics-dls.txt`
