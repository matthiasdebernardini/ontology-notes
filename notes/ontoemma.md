# OntoEMMA

- **What it is** — OntoEMMA is an ontology matcher for generating alignments between knowledgebases. It provides training and alignment workflows with either a logistic-regression model or an AllenNLP neural-network model.

- **Key concepts** —
  - Alignment is staged as candidate selection followed by pairwise prediction. Candidate entities are ranked using word and character n-gram token maps and summed token IDF scores.
  - Pair features use entity aliases plus the canonical names of parents and children; canonical-name tokens are also stemmed and lemmatized.
  - Candidate quality can be evaluated against gold mappings with candidate yield and precision/recall at selected top-*k* values; final predicted alignments can likewise be evaluated when a gold file is supplied.
  - UMLS-derived supervision treats identifiers mapped under the same concept ID as positive pairs. Training data adds hard negatives selected from nonmatching candidates and easy negatives sampled randomly from the rest of the knowledgebase.

- **How you'd use it** — Run `./setup.sh` to create the `ontoemma` Conda environment. Train with `train_ontoemma.py`, choosing `lr` or `nn`, a model path, and a JSON configuration; then align a source and target with `run_ontoemma.py`, optionally supplying an input alignment, output TSV, and CUDA device. OntoEMMA documents support for its KnowledgeBase JSON and pickle files and, “to the best of its ability,” OBO, OWL, TTL, RDF, and ontology web URIs. Its UMLS extractor writes knowledgebases as JSON and pairwise mappings/training examples as TSV.

- **LLM angle** — No LLM or RAG integration is stated. The documented learned matchers are logistic regression and an AllenNLP neural network; the knowledge-graph-related scope is ontology/knowledgebase alignment.

- **Pitfalls & lessons** — The README explicitly says the library is no longer maintained. Format handling for OBO, OWL, TTL, and RDF is qualified as working only “to the best of its ability.” Reproducing UMLS training also requires obtaining the UMLS Metathesaurus and updating local path variables, while the documented defaults point to AllenAI-internal NFS locations.

- **Verdict** — A documented, classical ML pipeline for candidate-based ontology alignment and UMLS-derived training data, useful as a reference but constrained by discontinued maintenance and environment-specific data setup.

## Sources consulted

- `README.md`
- `docs/ontoemma.md`
