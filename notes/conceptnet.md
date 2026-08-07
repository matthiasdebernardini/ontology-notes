# ConceptNet

**What it is**
ConceptNet is a freely available, open multilingual semantic network intended to help computers understand word meanings. It combines knowledge originating in Open Mind Common Sense with other crowdsourced, expert-created, dictionary, encyclopedia, ontology, and game-derived sources.

**Key concepts**
ConceptNet exposes relational assertions as Linked Open Data through a JSON-LD API, including relation, start and end concepts, source attribution, surface text, and weight. `ExternalURL` links connect terms to resources such as WordNet, DBpedia, and OpenCyc; ConceptNet also provides multilingual, cross-language-aligned word embeddings designed to avoid harmful stereotypes.

**How you'd use it**
Browse concepts or query the REST/JSON-LD API for general relational knowledge, follow external vocabulary links for additional information, or use its published embeddings for word similarity and analogy tasks.

**LLM angle**
none stated

**Pitfalls & lessons**
The graph aggregates heterogeneous sources, so retain the assertion-level source metadata when provenance matters. Follow the site’s attribution guidance and review the CC BY-SA 4.0 licensing details before redistributing data.

**Verdict**
A practical multilingual source of general word- and concept-level relationships with an accessible linked-data API.

## Sources consulted
- http://conceptnet.io/
- `sources/conceptnet.txt`
