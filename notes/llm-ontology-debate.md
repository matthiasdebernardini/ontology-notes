# Do Language Models Replace Ontologies?

**What it is**
The live argument about whether large language models make hand-built ontologies unnecessary, obsolete the labour of building them, or increase their value. The corpus already documents the tooling side of this in OntoLearner, OntoAligner, and ELOT. This note records the argument itself.

**Key concepts**
- **The replacement case**, reconstructed here rather than quoted, since no source in this corpus argues it directly. A model trained on a large corpus encodes much of the taxonomic and relational knowledge an ontology would state, and answers questions without anyone writing an axiom. Sun and colleagues confirm the debate exists — "sparking a growing debate about whether traditional knowledge graphs will be replaced by LLMs in real applications" — and that models "demonstrate an impressive ability to internalize knowledge and answer natural language questions." It is the strongest challenge to Lenat's premise; see [cyc-lenat-1995.md](cyc-lenat-1995.md).
- **The measured rebuttal.** Sun and colleagues ask "Are Large Language Models a Good Replacement of Taxonomies?" in *PVLDB* 17(11), 2024, and test it empirically. The result splits on two axes at once: "LLMs perform miserably poorly in handling specialized taxonomies and leaf-level entities. Specifically, the QA accuracy of the best LLM drops by up to 30% as we go from common to specialized domains and from root to leaf levels of taxonomies." They concede the other half plainly — for common domains, "the manually constructed and maintained taxonomies in these domains may not be needed shortly" — while recommending "that industrial practitioners continue with the current tree-structure taxonomies in specialized domains to ensure reliability."
- **Keet's objection.** Keet argues that generating an ontology from a model is harder than it looks. Her lead point is that models are not knowledge bases: "the LLMs do not store the (structured) facts, (axiomatised) sentences, and rules to make the inferences, and so nor does an LLM offer the reliability that it would return the same answer to a query when it's posed more than once," so "two different runs then may lead to two different ontologies." Her second is logical: "if a majority is ignorant of the fact that, say, whales are mammals and wrote about their misconception, an LLM may propose them to be fish, but that would make the ontology inconsistent if the rest of animal classification was represented properly. Inconsistent ontologies are bad computationally." Her third is about consensus: an ontology is supposed to record agreement, and "this doesn't entail that the humans in the project have reached consensus just because an LLM said so."
- **The grounding case.** Ontology-grounded retrieval work argues the relationship is complementary. The OG-RAG paper states the gap — "existing retrieval-augmented models, such as RAG, offer improvements but fail to account for structured domain knowledge… ontologies, which conceptually organize domain knowledge by defining entities and their interrelationships, offer a structured representation to address this gap" — and reports "30% faster attribution of responses to context" alongside a 27% gain in fact-based reasoning accuracy. On the other side, "LLMs also enable ontology extraction from both structured and unstructured data."
- **A division of labour, which is my summary rather than any source's.** Models are good at proposing candidates from text; reasoners and constraint languages are good at rejecting the proposals that do not hold. Note that Sun and colleagues propose a different split — the entities near the roots move into the model's weights, while the entities near the leaves stay in the tree.

**How you'd use it**
Separate the three questions people conflate. Can a model *replace* an ontology as a store of knowledge? Can it *build* one? Can it *use* one? My reading of the evidence in this corpus, not a finding any source states: it is weakest on the first, mixed and improving on the second, and strongest on the third. A team that needs auditable and consistent answers still needs the explicit artifact, whoever or whatever drafted it; if it also needs permission-governed answers, [palantir-ontology.md](palantir-ontology.md) shows what that costs.

**LLM angle**
The whole note is the LLM angle.

**Pitfalls & lessons**
The corpus's existing pitfalls apply directly. Clear prompts and structured output reduce hallucination and inconsistency but do not remove the need to validate relationships and labels. Direct all-pairs matching is quadratic and documented as suitable only for small ontologies, around two hundred concepts or fewer. Large retrieval contexts cause memory problems. Automatic validation checks lint and parsing, not semantic consistency, so syntactic validity is not semantic correctness. ELOT's guarded design — file writes project-scoped, disabled by default, confirmation-gated, revalidated with rollback, and with a separate consistency check still required — is the concrete pattern to copy.

**Verdict**
Worth studying, and the note to read before betting either way. The corpus's evidence says models do not replace ontologies outside common, well-represented domains, help build them only under guarded validation, and are most clearly useful when an ontology grounds them.

## Sources consulted
- https://www.vldb.org/pvldb/vol17/p2919-sun.pdf
- https://keet.wordpress.com/2025/03/26/is-developing-an-ontology-from-an-llm-really-feasible/
- https://aclanthology.org/2025.emnlp-main.1674/
- https://arxiv.org/abs/2511.05991v1
- `research/firecrawl/llm-taxonomies-vldb.md`
- `research/firecrawl/llm-keet-ontology.md`
- `research/exa/llm-ont.json` (the only local capture for the ACL Anthology and arXiv entries above)
- See also [ontolearner.md](ontolearner.md), [ontoaligner.md](ontoaligner.md), [elot.md](elot.md).
