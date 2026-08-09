# The Knowledge Graph Turn (2012 onwards)

**What it is**
The rebranding and repositioning that let ontology technology survive the Semantic Web's disappointment. Google launched the Knowledge Graph in May 2012 and announced it under the title of Amit Singhal's post "Introducing the Knowledge Graph: Things, Not Strings." It was built largely on Freebase: "Google's Knowledge Graph derives from Freebase, a proprietary graph database acquired by Google in 2010 when it bought Metaweb." Ars Technica records the jump in scale — "when Google purchased Metaweb, Freebase's database had 12 million entities; Knowledge Graph now tracks 500 million entities." Microsoft shipped Satori for Bing in the same period: "as of June 1, Satori had mapped over 400 million entities and Knowledge Graph had reached half a billion." The phrase "knowledge graph" then spread past any single definition; as one survey puts it, "the definition of a 'knowledge graph' remains contentious, where a number of (sometimes conflicting) definitions have emerged, varying from specific technical proposals to more inclusive general proposals." Google's own graph is not built on the W3C stack; Satori, by contrast, "uses the Resource Description Framework and the SPARQL query language."

**Key concepts**
Things not strings; heterogeneity of entities, schemas, and values as the integration problem the VLDB survey foregrounds; the shift from open-web publishing to proprietary curated graphs; schema.org as the surviving open vocabulary, "started by Google, Bing, and Yahoo with the express purpose of delivering better search results"; the VLDB account of three generations — entity-based, text-rich, and dual neural knowledge graphs — "and the business impact"; Wikidata, which the two-decades-on survey lists among the field's success stories.

**How you'd use it**
Use the distinction to avoid a common category error. A knowledge graph is a data-shaped commitment: entities and relations rather than rows and joins. An ontology is a semantic commitment: a formal vocabulary with axioms whose consequences a reasoner can derive. Many production knowledge graphs have no ontology in the formal sense, and this corpus documents a concrete case: [scigraph.md](scigraph.md) records an OWL-to-Neo4j mapping that "is explicitly lossy and does not round-trip ontologies."

**LLM angle**
The knowledge-graph framing is the one current retrieval work inherits. The VLDB survey's position is that "at the current moment, LLMs clearly have not replaced knowledge graphs," the stated reason being hallucination. How often the graph is justified as model grounding rather than as an agent substrate is my impression, not a measured claim any source here makes.

**Pitfalls & lessons**
The turn traded openness for viability. The 2001 plan was that anyone could publish data and any agent could use it. What shipped is a small number of large private graphs that a provider must feed to be visible. Berners-Lee's decentralisation requirement was the casualty, and it was the point of the original design: "today we are stuck with giant, centralized repositories of information," and "no precedent exists in the Semantic Web setting for the type of decentralised infrastructure envisaged by Berners-Lee."

**Verdict**
Worth studying, mostly as a corrective. It explains why the word "ontology" and the word "knowledge graph" are not interchangeable, and why most things sold as knowledge graphs carry no formal semantics at all.

## Sources consulted
- https://arstechnica.com/information-technology/2012/06/inside-the-architecture-of-googles-knowledge-graph-and-microsofts-satori/
- https://www.vldb.org/pvldb/vol16/p4130-dong.pdf
- https://www.technologyreview.com/2012/06/14/19504/googles-new-brain-could-have-a-big-impact/
- `research/firecrawl/kg-arstechnica-2012.md`
- `research/firecrawl/kg-generations-vldb.md`
- `research/firecrawl/semweb-twobithistory.md`
- `research/firecrawl/semweb-two-decades-on.md`
- `research/exa/kg-revival.json` (launch month; definitional contention)
