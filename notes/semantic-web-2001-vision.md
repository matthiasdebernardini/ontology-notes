# The Semantic Web Vision (Berners-Lee, Hendler, Lassila 2001)

**What it is**
The Scientific American article that moved ontologies from an AI research topic to a web-scale programme. Tim Berners-Lee, James Hendler, and Ora Lassila argued that the web should carry not only documents but data with machine-readable meaning, so that software agents could act on it. The article opens with a scenario in which Pete and Lucy's agents negotiate their mother's physical-therapy appointments against provider ratings, insurance coverage, and both siblings' calendars, with no service having been built to talk to any other. Berners-Lee later rebranded the programme Web 3.0.

**Key concepts**
Machine-readable meaning as an extension of the existing web rather than a replacement; agents that compose services they were never wired to; RDF triples as the grammar; ontologies supplying the shared terms; the URI as the identifier that lets independent parties talk about the same thing; decentralisation as the point.

**How you'd use it**
Read the 2001 article as the design brief that produced RDF, RDFS, OWL, and SPARQL. The standards make sense as answers to its requirements: RDF because agents need a data model that merges without coordination, URIs because merging needs global identity, OWL because agents need to infer what publishers did not state, SPARQL because someone eventually has to query the result. The article also explains a persistent cultural trait of the field, which is that the standards were built for an open world of anonymous publishers rather than for a single enterprise.

**LLM angle**
The 2001 agent scenario is close to what current tool-using language-model agents attempt, with one inversion. The Semantic Web plan was to make the data structured enough for a simple agent. The current plan is to make the agent capable enough for unstructured data. The scenario is the same, the layer doing the work moved.

**Pitfalls & lessons**
The vision assumed voluntary, accurate, widespread annotation by publishers with no direct incentive to provide it. That assumption is the single point on which most later criticism turns.

## Sources consulted
- https://www.scientificamerican.com/article/the-semantic-web/
- https://twobithistory.org/2018/05/27/semantic-web.html
- `research/firecrawl/semweb-sciam-2001.md`
