# OnToology

- **What it is** — OnToology automates part of collaborative ontology development for a GitHub repository containing OWL files. When a tracked ontology changes, it generates documentation, diagrams, an evaluation report, and a JSON-LD context, then proposes the generated files in a pull request; it can also publish ontologies through GitHub Pages with a `w3id.org` permanent identifier.
- **Key concepts** — Ontology engineering artifacts can be regenerated from the ontology on every repository change and reviewed before merging. The documented artifact set includes HTML documentation, class and taxonomy diagrams, an OOPS! evaluation based on common pitfalls, and a JSON-LD context. Publication assigns a unique reserved identifier such as `https://w3id.org/def/alojamiento`, while the syntax checker tests whether RDFLib can parse a supplied ontology URL in the selected serialization.
- **How you'd use it** — Put OWL files in a GitHub user repository, register `user/reponame`, authorize OnToology, and review the pull request it creates after processing. Generated resources live under a top-level `OnToology` directory that mirrors the repository structure; each ontology gets documentation, diagrams, evaluation, and an `OnToology.cfg`. Per-ontology `widoco`, `ar2dtool`, and `oops` sections enable or disable documentation, diagrams, and evaluation. You can also validate an ontology URL and format, download a publication bundle, or reserve a w3id and publish through the `gh-pages` branch.
- **LLM angle** — none stated
- **Pitfalls & lessons** — OWL functional-style syntax, GitHub organization repositories, and private repositories are not supported. Folder and file names are limited to English letters, underscores, dashes, and dots. Evaluation depends on the OOPS! web service, whose outages can prevent successful reports; publication can stall if authorization, the `OnToologyUser` collaborator, or `gh-pages` setup is missing. Generated documentation may not work when opened locally because Chrome and Firefox disable AJAX for local HTML, and large ontologies may time out in the syntax checker.
- **Verdict** — A GitHub-centered automation service for keeping documentation, diagrams, evaluation, JSON-LD context, and permanent publication in step with changing OWL ontologies.

## Sources consulted

- `README.md`
- `templates/stepbystep.html`
- `templates/faqs.html`
- `templates/syntax.html`
