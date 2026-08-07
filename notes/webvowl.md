# WebVOWL

- **What it is** — WebVOWL is a browser UI for presenting ontology visualizations, with OWL2VOWL providing the conversion backend. The documented full-stack deployment combines both under one Tomcat origin, while a frontend-only deployment omits file and IRI conversion.

- **Key concepts** —
  - OWL2VOWL converts ontology files into VOWL-specific JSON for presentation by WebVOWL.
  - The legacy documentation names OWL, RDF, and TTL as watched ontology inputs; current operator docs demonstrate posting an RDF ontology to `/convert`.
  - The UI and converter are expected on the same origin because WebVOWL uses relative `/convert` and `/serverTimeStamp` endpoints.

- **How you'd use it** — Run the full stack with `docker compose build && docker compose up -d --wait`, then open `http://localhost:8080`; the image clones and builds OWL2VOWL and exposes `/convert`. A frontend-only Compose setup is available when conversion is unnecessary. For development, install Node dependencies, build with the npm/Grunt tasks, and serve `deploy/`; visualizations can be exported as SVG, provided the CSS-inlining code is kept synchronized with `vowl.css`.

- **LLM angle** — none stated

- **Pitfalls & lessons** —
  - The old `visualdataweb.org` URL is no longer owned by VisualDataWeb, and the legacy WAR download host is broken or compromised; the accepted Docker design builds OWL2VOWL from source instead.
  - Separating the UI and converter across two unproxied origins breaks the relative `/convert` integration.
  - Docker builds require network access to clone OWL2VOWL; pin `OWL2VOWL_GIT_REF` for reproducible releases.
  - The documented build toolchain retains end-of-life Node 12 and Java 8.
  - SVG export requires CSS rules to be inlined; changing `vowl.css` without regenerating the inlining code makes the exported image differ from the displayed graph.
  - The repository was migrated from internal SVN and cleaned with `git filter-branch`, so its commit history may contain oddities.

- **Verdict** — A focused browser visualization frontend with a documented OWL-to-VOWL conversion path and workable local deployment, but with a legacy toolchain and notable deployment-history hazards.

## Sources consulted

- `README.md`
- `docs/adr/README.md`
- `docs/adr/0001-docker-local-development.md`
- `docker/README.md`
- `doc/Docker/README.md`
- `util/VowlCssToD3RuleConverter/README.md`
