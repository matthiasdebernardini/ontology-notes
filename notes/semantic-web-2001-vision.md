# The Semantic Web Vision (Berners-Lee, Hendler, Lassila 2001)

**What it is**
The Scientific American article that moved ontologies from an AI research topic to a web-scale programme. Tim Berners-Lee, James Hendler, and Ora Lassila argued that the web should carry not only documents but data with machine-readable meaning, so that software agents could act on it. The article opens with a scenario in which Pete and Lucy's agents negotiate their mother's physical-therapy appointments against provider ratings, insurance coverage, and both siblings' calendars, with no service having been built to talk to any other. Berners-Lee, Sinclair Target records, later "began referring to the Semantic Web as Web 3.0."

**Key concepts**
Machine-readable meaning as an extension of the existing web rather than a replacement; agents that compose services they were never wired to, so that "programs could exchange data across the Semantic Web without having to be explicitly engineered to talk to each other"; RDF triples as the grammar; ontologies supplying the shared terms; decentralisation as the point.

**How you'd use it**
Read the 2001 article as the design brief that produced RDF, RDFS, and OWL. Target's account connects those three to it directly: RDF as "the grammar in which Semantic webpages expressed information," and "RDF Schema and another standard called OWL" as the way to "make inferences about omitted information." Reading the rest of the stack, SPARQL included, as answers to the same brief is my own reconstruction and not a claim any source here makes; SPARQL postdates the article by five years. The article does explain a persistent cultural trait of the field, which is that the standards were built for an open world. Horrocks, Patel-Schneider and van Harmelen state the reason plainly: OWL "adopts the standard logical model of an open world assumption: a statement cannot be assumed true on the basis of a failure to prove it. Clearly, on the huge and only partially knowably World Wide Web this is the correct assumption."

**LLM angle**
The 2001 agent scenario is close to what current tool-using language-model agents attempt, with one inversion. The Semantic Web plan was to make the data structured enough for a simple agent. The current plan is to make the agent capable enough for unstructured data. The scenario is the same, the layer doing the work moved.

**Pitfalls & lessons**
The vision assumed voluntary, accurate, widespread annotation by publishers with no direct incentive to provide it. Target's summary of the objection is that "most web users were likely to provide either no metadata at all or else lots of misleading metadata meant to draw clicks." That assumption is the single point on which most later criticism turns.

**Verdict**
Worth reading in full, and it is six pages. Every later argument in this corpus — the standards, the criticism, the knowledge-graph turn, the agent pitch — is either executing this brief or objecting to it.

## Sources consulted
- https://www.scientificamerican.com/article/the-semantic-web/
- https://www-sop.inria.fr/acacia/cours/essi2006/Scientific%20American_%20Feature%20Article_%20The%20Semantic%20Web_%20May%202001.pdf (archived full text)
- https://twobithistory.org/2018/05/27/semantic-web.html
- https://www.cs.ox.ac.uk/people/ian.horrocks/Publications/download/2003/HoPH03a.pdf
- `research/firecrawl/semweb-sciam-2001.md` (paywall stub: masthead only, no article body)
- `research/firecrawl/semweb-sciam-2001-fulltext.md` (archived PDF of the full article)
- `research/firecrawl/semweb-twobithistory.md`
- `research/firecrawl/semweb-two-decades-on.md`
- `research/firecrawl/semweb-making-of-owl.md`
