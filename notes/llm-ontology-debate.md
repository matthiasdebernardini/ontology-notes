# Do Language Models Replace Ontologies?

**What it is**
The live argument about whether large language models make hand-built ontologies unnecessary, obsolete the labour of building them, or increase their value. The corpus already documents the tooling side of this in OntoLearner, OntoAligner, and ELOT. This note records the argument itself.

**Key concepts**
- **The replacement case.** A model trained on a large corpus already encodes most of the taxonomic and relational knowledge an ontology would state, and answers questions without anyone writing an axiom. This is the strongest challenge to Lenat's premise that common sense must be hand-codified.
- **The measured rebuttal.** Sun and colleagues, in a VLDB paper asking whether language models are a good replacement for taxonomies, test the claim empirically rather than rhetorically and find the substitution does not hold uniformly, particularly outside common, well-represented domains.
- **Keet's objection.** Maria Keet argues that generating an ontology from a model is harder than it looks, because the output must satisfy logical constraints and domain commitments a fluent generator has no way to guarantee.
- **The grounding case.** Ontology-grounded retrieval work argues the relationship is complementary: the ontology supplies auditable structure, identifiers, and constraints, and the model supplies language coverage and extraction from text.
- **The division of labour that keeps recurring.** Models are good at proposing candidates from text. Reasoners and constraint languages are good at rejecting the proposals that do not hold.

**How you'd use it**
Separate the three questions people conflate. Can a model *replace* an ontology as a store of knowledge? Can it *build* one? Can it *use* one? The evidence in this corpus is weakest on the first, mixed and improving on the second, and strongest on the third. A team that needs auditable, consistent, permission-governed answers still needs the explicit artifact, whoever or whatever drafted it.

**LLM angle**
The whole note is the LLM angle.

**Pitfalls & lessons**
The corpus's existing pitfalls apply directly: hallucination and inconsistency survive good prompting, all-pairs matching is quadratic and only viable for small ontologies, retrieval contexts cause memory problems, and syntactic validity is not semantic correctness. ELOT's guarded design — writes disabled by default, confirmation-gated, linted, parsed, rolled back on failed revalidation, with a separate consistency run still required — is the concrete pattern to copy.

## Sources consulted
- https://www.vldb.org/pvldb/vol17/p2919-sun.pdf
- https://keet.wordpress.com/2025/03/26/is-developing-an-ontology-from-an-llm-really-feasible/
- https://aclanthology.org/2025.emnlp-main.1674/
- https://arxiv.org/abs/2511.05991v1
- `research/firecrawl/llm-taxonomies-vldb.md`
- `research/firecrawl/llm-keet-ontology.md`
- See also [notes/ontolearner.md](notes/ontolearner.md), [notes/ontoaligner.md](notes/ontoaligner.md), [notes/elot.md](notes/elot.md).
