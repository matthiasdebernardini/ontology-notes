# obonet

- **What it is** — `obonet` is a lightweight Python package for reading OBO-serialized ontologies into a NetworkX `MultiDiGraph`. Its parser targets OBO format specifications 1.2 and 1.4, and the project describes itself as specializing in OBO-to-NetworkX loading rather than general ontology processing.

- **Key concepts** — Ontology terms become graph nodes, while typed relationships become directed edges; multiple relationships between the same nodes are retained by the `MultiDiGraph`. Traditional ontology edges such as `is_a` run from subterm to superterm, so in this representation NetworkX `descendants` returns superterms and `ancestors` returns subterms. The tutorial demonstrates node properties, ID/name mappings, parent and child relationships, all paths to a root, ontology-level metadata, and obsolete-term replacement via `replaced_by`.

- **How you'd use it** — Call `obonet.read_obo()` with a local path, URL, or open file handle; compression is inferred from the path extension. Analyze the returned graph with NetworkX—for example, count nodes and edges, check whether it is a DAG, traverse superterms/subterms, inspect properties, or enumerate paths to a root. Pass `include_clauses=True` to preserve parsed OBO comments and trailing modifiers, pass `ignore_obsolete=False` when building obsolete-to-replacement mappings, or use the CLI to convert OBO to NetworkX node-link JSON.

- **LLM angle** — none stated

- **Pitfalls & lessons** — Only reading OBO files is supported. Some ontology nodes may have an ID but no name, so mappings should access `name` defensively. The documented edge direction can be confusing because it makes NetworkX ancestor/descendant terminology opposite the ontology's general/specific hierarchy. Compared with the more general `nxontology`/`pronto` route, format coverage and retained metadata differ; conversion to a plain `DiGraph` requires choosing relationship types, reversing edges, and collapsing parallel edges.

- **Verdict** — A focused choice when the job is to load OBO 1.2/1.4 data into a metadata-rich NetworkX multigraph and analyze it with standard graph operations.

## Sources consulted

- `README.md`
- `examples/go-obonet.ipynb`
