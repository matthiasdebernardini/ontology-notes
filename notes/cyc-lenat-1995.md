# Cyc as a Knowledge-Engineering Programme (Lenat 1995)

**What it is**
Douglas Lenat's article "CYC: A Large-Scale Investment in Knowledge Infrastructure" describes the Cyc project, begun with Mary Shepherd in 1984, as an attempt to hand-codify common sense. It appeared in *Communications of the ACM* 38(11) in 1995, per its DBLP record. Lenat's premise was that machine learning and natural-language understanding both stall without a large base of background knowledge, so somebody had to enter that knowledge by hand until the system reached critical mass and could take over its own learning. The paper reports "a universal schema of roughly 10⁵ general concepts spanning human reality," about a million commonsense axioms "handcrafted for and entered into CYC's knowledge base, and millions more … inferred and cached by CYC," and "a person-century of effort" since 1984. Lenat states plainly: "Mary Shepherd and I embarked on that task in 1984, knowing we had little chance of success, but seeing no alternative but to try."

**Key concepts**
Common sense as an engineering target; the critical-mass hypothesis; causality, time, space, substances, intention, contradiction, uncertainty, belief, and emotion as things that must be represented; micro-theories, each of which "inhabits its own context" and is "relatively small, solid, and flat"; the examples the paper uses — "You cannot remember events that have not happened yet"; "if you cut a lump of peanut butter in half, each half is also a lump of peanut butter; but if you cut a table in half, neither half is a table."

**How you'd use it**
Treat Cyc as the reference experiment for the cost side of ontology engineering. It is the largest sustained attempt to answer the question every ontology project eventually faces: how much of the world do we have to write down before the model earns its keep? Cyc's answer — "a person-century of effort" by 1995 — is the number every "we will just model our domain properly" plan is implicitly betting against.

**LLM angle**
Cyc's motivating claim is that statistics alone will not resolve commonsense questions: "statistics, colocation, and frequency do not resolve such questions. But the task goes from impossible to trivial if one already knows a few things about boxes and pens." That is the claim large language models most directly contest, since they absorb an enormous amount of that background from text without anyone hand-writing axioms. The paper is from 1995 and says nothing about them; the counter-claim that what a model absorbs is not inspectable, not consistent, and cannot be audited is mine, and it is argued out in [llm-ontology-debate.md](llm-ontology-debate.md).

**Pitfalls & lessons**
Lenat's own framing concedes the risk up front: the project's payoff was always deferred to a critical mass that had not yet arrived. A knowledge base whose value depends on reaching a threshold, rather than on being useful at every stage, is a bet on the threshold. Compare the layered approach the rest of this corpus recommends, where a small ontology answers real competency questions early.

**Verdict**
Worth reading in full, and short. It is the only document in this corpus that states the price of hand-codified knowledge as a number, and every later argument about whether models can replace ontologies is arguing with it.

## Sources consulted
- https://faculty.cc.gatech.edu/~isbell/classes/reading/papers/lenat95cyc.pdf
- `research/firecrawl/ai-lenat-cyc95.md`
- https://dblp.org/rec/journals/cacm/Lenat95 (venue, volume, and year)
- `research/dblp/lenat-cyc-1995.json`
- See also [cyc.md](cyc.md) for the current commercial positioning.
