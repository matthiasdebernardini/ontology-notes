# The Knowledge Graph Turn (2012 onwards)

**What it is**
The rebranding and repositioning that let ontology technology survive the Semantic Web's disappointment. Google launched the Knowledge Graph in May 2012, built largely on the Freebase data it acquired with Metaweb, and marketed it as "things, not strings." Microsoft shipped Satori for Bing in the same period. The phrase "knowledge graph" spread to describe any large, entity-centric, linked data store, whether or not it used RDF or OWL at all.

**Key concepts**
Things not strings; entity resolution as the hard problem rather than logic; the shift from open-web publishing to proprietary curated graphs; schema.org as the surviving open vocabulary, driven by search-engine incentives rather than by agents; the VLDB account of successive generations of knowledge graphs and their business impact; Wikidata as the open community-curated survivor; graph databases with no formal semantics adopting the vocabulary of the field.

**How you'd use it**
Use the distinction to avoid a common category error. A knowledge graph is a data-shaped commitment: entities and relations rather than rows and joins. An ontology is a semantic commitment: a formal vocabulary with axioms whose consequences a reasoner can derive. Many production knowledge graphs have no ontology in the formal sense, and this corpus documents a concrete example where a lossy graph mapping cannot round-trip its source ontology.

**LLM angle**
The knowledge-graph framing is the one current retrieval work inherits, and the graph is now most often justified as grounding for language models rather than as a substrate for agents.

**Pitfalls & lessons**
The turn traded openness for viability. The 2001 plan was that anyone could publish data and any agent could use it. What shipped is a small number of large private graphs that a provider must feed to be visible. Berners-Lee's decentralisation requirement was the casualty, and it was the point of the original design.

## Sources consulted
- https://arstechnica.com/information-technology/2012/06/inside-the-architecture-of-googles-knowledge-graph-and-microsofts-satori/
- https://www.vldb.org/pvldb/vol16/p4130-dong.pdf
- https://www.technologyreview.com/2012/06/14/19504/googles-new-brain-could-have-a-big-impact/
- `research/firecrawl/kg-arstechnica-2012.md`
- `research/firecrawl/kg-generations-vldb.md`
