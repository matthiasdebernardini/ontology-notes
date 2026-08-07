# OntoAligner

- **What it is** — OntoAligner is a modular Python toolkit for matching entities across two ontologies or knowledge graphs. It exposes a consistent parse → encode → align → postprocess workflow across lexical/fuzzy, retrieval, LLM, RAG, knowledge-graph-embedding, property, graph, and ensemble methods, with evaluation and export support.
- **Key concepts** —
  - An ontology-matching dataset contains a source ontology, a target ontology, and optionally reference correspondences; parsed concepts can carry IRIs, labels, parents, children, synonyms, and comments.
  - Encoders turn those concepts into method-specific representations: lightweight natural-language strings, LLM prompts, RAG inputs, or graph triples. Aligners propose source–target correspondences, while optional reranking and postprocessing reorder, filter, normalize, or impose cardinality constraints.
  - Evaluation treats alignments as source–target pairs and reports precision, recall, F-score, and intersection; ranked candidate outputs can also be measured with Hit@K and MRR.
  - Ensemble alignment normalizes heterogeneous matcher outputs and fuses them through weighted voting, reciprocal-rank fusion, Borda, Condorcet, or score averaging before top-k, threshold, or bijective selection.
- **How you'd use it** — Install with `pip install -U OntoAligner` (the docs recommend Python 3.10+, PyTorch 1.4.0+, and Transformers 4.41.0+). Load OWL/RDF source and target files with `GenericOMDataset` or a track-specific dataset, choose compatible parser/encoder/aligner/postprocessor components, then run either the one-step `OntoAlignerPipeline` or the lower-level `AlignerPipeline`; optional reference alignments support evaluation, and results can be exported as OAEI-compatible XML or JSON. Custom parsers can redirect nonstandard label, synonym, definition, or hierarchy properties, or support non-RDF sources by extending the base parser.
- **LLM angle** — Standalone Hugging Face LLM aligners turn concept pairs and optional parent/child context into yes/no prompts, then map generated text back to match labels. The documented LLMs4OM RAG flow uses each source concept as a query over target concepts, retrieves candidates, and asks an LLM to verify each pair; it supports concept, concept-parent, and concept-children representations, plus few-shot and in-context-vector variants. The toolkit also includes KGE aligners that learn low-dimensional entity/relation vectors from graph triples, and ensembles can combine lexical, structural, retrieval, KGE, LLM, and RAG signals.
- **Pitfalls & lessons** —
  - Direct LLM matching has quadratic complexity and is documented as suitable for small ontologies (about 200 concepts or fewer); RAG narrows the candidate set and uses single-forward-pass logit scoring to reduce GPU use.
  - An LLM encoder and its dataset class must represent the same context (for example, children with children); mismatches can omit required fields and break the pipeline.
  - The generic parser assumes common RDF/OWL predicates such as `rdfs:label`, `skos:altLabel`, `rdfs:comment`, and `rdfs:subClassOf`; ontologies that store these semantics differently need targeted parser overrides.
  - Matching thresholds are dataset- and use-case-specific, and reranking is useful only when each source still has multiple target candidates—not after a single-target matcher has made its final selection.
- **Verdict** — A broad experimentation and integration toolkit for ontology alignment, strongest when you need one modular interface for comparing classical, retrieval, graph, LLM/RAG, and ensemble pipelines rather than a single fixed matcher.

## Sources consulted

- `README.md`
- `docs/source/gettingstarted/overview.rst`
- `docs/source/gettingstarted/installation.rst`
- `docs/source/gettingstarted/quickstart.rst`
- `docs/source/developerguide/pipeline.rst`
- `docs/source/developerguide/parsers.rst`
- `docs/source/developerguide/metrics.rst`
- `docs/source/developerguide/reranking.rst`
- `docs/source/aligner/lightweight.rst`
- `docs/source/aligner/retriever.rst`
- `docs/source/aligner/llm.rst`
- `docs/source/aligner/rag.rst`
- `docs/source/aligner/kge.rst`
- `docs/source/aligner/propmatch.rst`
- `docs/source/aligner/flora.rst`
- `docs/source/aligner/olala.rst`
- `docs/source/aligner/ensemble_learning.rst`
