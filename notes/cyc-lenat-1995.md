# Cyc as a Knowledge-Engineering Programme (Lenat 1995)

**What it is**
Doug Lenat's 1995 CACM article describing the Cyc project, begun with Mary Shepherd in 1984, as an attempt to hand-codify common sense. Lenat's premise was that machine learning and natural-language understanding both stall without a large base of background knowledge, so somebody had to enter that knowledge by hand until the system reached critical mass and could take over its own learning. The paper reports a universal schema of general concepts, roughly a million hand-crafted commonsense axioms, and millions more inferred and cached. Lenat states plainly that he and Shepherd knew they had little chance of success and saw no alternative but to try.

**Key concepts**
Common sense as an engineering target; the critical-mass hypothesis; causality, time, space, substances, intention, contradiction, uncertainty, belief, and emotion as things that must be represented; microtheories for locally consistent contexts; the examples the paper uses — you cannot remember events that have not happened yet; half a lump of peanut butter is a lump of peanut butter, half a table is not a table.

**How you'd use it**
Treat Cyc as the reference experiment for the cost side of ontology engineering. It is the largest sustained attempt to answer the question every ontology project eventually faces: how much of the world do we have to write down before the model earns its keep? Cyc's answer, decades of specialist labour, is the number every "we will just model our domain properly" plan is implicitly betting against.

**LLM angle**
Cyc's motivating claim — that statistical systems fail without codified background knowledge — is the claim large language models most directly contest, since they absorb an enormous amount of that background from text without anyone hand-writing axioms. The counter-claim is that what they absorb is not inspectable, not consistent, and cannot be audited, which is what a Cyc-style axiom gives you.

**Pitfalls & lessons**
Lenat's own framing concedes the risk up front: the project's payoff was always deferred to a critical mass that had not yet arrived. A knowledge base whose value depends on reaching a threshold, rather than on being useful at every stage, is a bet on the threshold. Compare the layered approach the rest of this corpus recommends, where a small ontology answers real competency questions early.

## Sources consulted
- https://faculty.cc.gatech.edu/~isbell/classes/reading/papers/lenat95cyc.pdf
- `research/firecrawl/ai-lenat-cyc95.md`
- See also [notes/cyc.md](notes/cyc.md) for the current commercial positioning.
