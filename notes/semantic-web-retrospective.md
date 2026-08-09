# What Happened to the Semantic Web

**What it is**
The retrospective account of why the 2001 programme did not arrive as described. Sinclair Target's Two-Bit History account of 27 May 2018 sets out a periodisation in four phases. The first, "from 2001 to 2005, was the golden age of Semantic Web activity," in which "the W3C issued the first version of the RDF standard in 2004." The second shifted "from setting standards and building toy examples to creating and popularizing large RDF datasets" — linked open data. The third "involved adapting the W3C's standards to fit the actual practices and preferences of web developers," which produced JSON-LD and schema.org. The fourth is the W3C's retrenchment "under the heading of 'Data Activity'." The move to enterprise and scientific deployment is a separate thread, argued by Ontotext rather than by Target. Aaron Swartz, in an unfinished book published after his death, argued that Doctorow was attacking a straw man and located the failure elsewhere: the "formalizing mindset of mathematics and the institutional structure of academics" produced years of standards debate before there were applications to standardise, and the standards that emerged were too abstract to adopt.

**Key concepts**
Standards before applications; RDF's origins in Ramanathan Guha's metadata work at Apple; XML's associated machinery as a cost JSON undercut — "whereas XML came packaged with a bunch of associated technologies of indeterminate purpose … JSON was just JSON. It was less verbose and more readable"; the shift from annotate-the-open-web to publish-a-dataset (linked open data) to model-an-enterprise; centralisation of the agent layer into Google, Yelp, Siri, so that a provider advertises to the platform rather than from its own site; the survival of the machinery in biomedicine, cultural heritage, and finance.

**How you'd use it**
Use the periodisation to date any claim you read. Criticism written in the early 2000s — Doctorow's *Metacrap* is dated 26 August 2001 — is aimed at annotating the open web by hand, and mostly landed. The successes the retrospectives themselves name are schema.org, knowledge graphs, Wikidata, DBpedia and biomedical ontologies: governed, funded, bounded domains where somebody has an incentive to curate. This corpus documents further cases in the same shape — see [gene-ontology-go.md](gene-ontology-go.md), [cidoc-crm-conceptual-reference-model.md](cidoc-crm-conceptual-reference-model.md) and [fibo.md](fibo.md) — though no retrospective in this corpus names them. When evaluating a new ontology proposal, ask which of these two situations it resembles.

**LLM angle**
Ontotext argues the machinery found its market as the substrate for enterprise knowledge graphs rather than as an open-web annotation layer: "enterprise knowledge graphs came as a second wave to serve a different purpose." That post says nothing about language models. The retrieval leg comes from elsewhere: the VLDB survey of knowledge-graph generations notes that "at the current moment, LLMs clearly have not replaced knowledge graphs," citing hallucination — see [knowledge-graph-turn.md](knowledge-graph-turn.md).

**Pitfalls & lessons**
The strongest lesson in the retrospective is about sequencing rather than semantics. A committee that specifies before anyone ships produces artifacts nobody adopts. Schema.org succeeded partly because search engines gave publishers a direct reason to comply: it "was started by Google, Bing, and Yahoo with the express purpose of delivering better search results," and its team "are careful to state on their website that they are not attempting to create a 'universal ontology'."

**Verdict**
Worth reading before any argument about whether ontologies work. It supplies the dates that decide which criticism is aimed at what, and the sequencing lesson — applications before standards — is the one most reusable outside this field.

## Sources consulted
- https://twobithistory.org/2018/05/27/semantic-web.html
- https://twobithistory.org/about.html (byline)
- https://semantic-web-journal.net/system/files/swj2303.pdf
- https://www.ontotext.com/blog/the-semantic-web-20-years-later/
- https://www.cs.ox.ac.uk/people/ian.horrocks/Publications/download/2003/HoPH03a.pdf
- `research/firecrawl/semweb-twobithistory.md`
- `research/firecrawl/semweb-two-decades-on.md`
- `research/firecrawl/semweb-ontotext-20yr.md`
- `research/firecrawl/semweb-making-of-owl.md`
- `research/firecrawl/semweb-twobithistory-about.md`
- `research/firecrawl/crit-doctorow-metacrap.md`
- `research/firecrawl/kg-generations-vldb.md`
