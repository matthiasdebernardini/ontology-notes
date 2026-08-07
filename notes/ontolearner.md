# OntoLearner

- **What it is** — OntoLearner is a modular, extensible Python framework for semi-automatic ontology construction and enrichment. It joins reusable ontology loading and modularization with datasets, learner models, and evaluation for a full `fit → predict → evaluate` workflow.

- **Key concepts** —
  - Its core learning objects are **terms/entities**, which populate an ontology, and **types/classes**, which provide its abstract categories.
  - The LLMs4OL task model comprises **term typing** (map a lexical term to a class), **taxonomy discovery** (find hierarchical `is-a`/subclass relations), and **non-taxonomic relation extraction** (find relations such as `part-of`, `causes`, or `used-for`). **Text2Onto** separately extracts terms and types from raw text.
  - `OntologyData` carries term-to-type mappings, parent–child taxonomic relations, and head–relation–tail non-taxonomic relations. Earlier task outputs can feed later tasks, though tasks may also run in parallel.
  - An **Ontologizer** turns an ontology into a Python object, retaining provenance metadata and extracting ML-ready datasets; the documented analyzer distinguishes graph-topology metrics from extracted-dataset metrics.

- **How you'd use it** — Install with `pip install -U ontolearner` (the docs recommend Python 3.10+, plus PyTorch and Transformers). Instantiate a built-in Ontologizer or use `AutoOntology`, load from Hugging Face or a local OWL/RDF/XML/TTL file, call `.extract()`, split the resulting `OntologyData`, and run an LLM-only, retriever-only, or RAG learner directly or through `LearnerPipeline`. The tooling also supports custom Ontologizers and extraction hooks, generated JSON task datasets, ontology metrics, synthetic Text2Onto corpora, and Dublin Core metadata exported as RDF/XML.

- **LLM angle** — LLM-only learners use a model's inherent knowledge; retriever-only learners index training examples as embeddings; RAG retrieves similar ontology examples and supplies them as domain-specific few-shot context to the LLM. Text2Onto uses a direct Hugging Face `transformers` backend to generate synthetic documents, enriching prompts with term-typing, taxonomy, and non-taxonomic graph context so passages stay closer to the source ontology.

- **Pitfalls & lessons** —
  - The authors recommend pure LLMs mainly for general or well-known domains, RAG for specialized domains, and LLM/symbolic or multi-model ensembles for higher-stakes reliability.
  - Clear prompts and structured output reduce hallucination and inconsistency; relationships and labels should be validated, and evaluation should use representative held-out data, multiple metrics, domain-specific criteria, and classical baselines.
  - Large retrieval contexts can cause memory problems; `AutoRetrieverLearner(batch_size=...)` computes similarities in smaller batches.
  - Text2Onto works best with instruction-tuned models and ontology context that fits the model window. The docs identify stricter structured-output validation, repair retries for missing labels, richer graph-context retrieval, and candidate reranking as possible improvements.
  - New ontologies may need custom extraction logic when they do not use standard RDF/OWL constructs, plus ontology-specific blank-node filtering; format/path mismatches can cause parsing or missing-file failures.

- **Verdict** — A focused experimentation and benchmarking toolkit for converting curated ontologies or raw text into standardized ontology-learning datasets and comparing retrieval, LLM, and RAG approaches across the documented ontology tasks.

## Sources consulted

- `README.md`
- `docs/source/index.rst`
- `docs/source/installation.rst`
- `docs/source/quickstart.rst`
- `docs/source/learning_tasks/learning_tasks.rst`
- `docs/source/learning_tasks/llms4ol.rst`
- `docs/source/learning_tasks/text2onto.rst`
- `docs/source/learners/llm.rst`
- `docs/source/learners/retrieval.rst`
- `docs/source/learners/rag.rst`
- `docs/source/ontologizer/ontology_modularization.rst`
- `docs/source/ontologizer/ontology_hosting.rst`
- `docs/source/ontologizer/new_ontologies.rst`
- `docs/source/ontologizer/metadata.rst`
- `docs/source/ontologizer/metrics.rst`
