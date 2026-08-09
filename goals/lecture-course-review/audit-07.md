# Audit — Lecture 7, "Building One for Real"

Target: `lectures/transcripts/07-building-one-for-real.txt`
Permitted sources: the thirteen notes listed for lecture 7 in `lectures/COURSE-PLAN.md`.
Word count: 2,906 before → 2,941 after (no net lengthening; ~700 words of unsourced
material cut, ~700 words of grounded material substituted or tightened in place).

## Verified

| Claim in lecture | Note | Supporting span |
|---|---|---|
| BFO's defining trait is exclusion of specialised science terms | `notes/bfo-basic-formal-ontology.md` | "As a genuine upper ontology, it deliberately excludes physical, chemical, biological, and other terms belonging to specialized sciences." |
| More than five hundred and fifty efforts use BFO beneath their own models | `notes/bfo-basic-formal-ontology.md` | "adoption by more than 550 ontology-driven efforts"; "Use BFO as a domain-independent top-level framework beneath a specialized ontology" |
| Don't expect BFO to supply scientific vocabulary | `notes/bfo-basic-formal-ontology.md` | "Do not expect BFO itself to supply specialized scientific-domain terms; the site explicitly places those outside its scope." |
| Three-layer architecture, CCO in the middle | `notes/common-core-ontologies-cco.md` | "CCO occupies the mid-level between BFO's most generic categories and domain-specific ontologies" |
| CCO is eleven modules extending BFO; the module list read aloud | `notes/common-core-ontologies-cco.md` | "a suite of eleven ontologies… mid-level ontology extending the ISO-standard top-level Basic Formal Ontology (BFO)"; "geospatial entities, information entities, events, time, agents, qualities, measurement units, currencies, facilities, artifacts, and extended relations" |
| Competency questions are the field's own framing, not the narrator's | `notes/common-core-ontologies-cco.md` | "Documented design patterns are motivated by use cases and competency questions, and include a Mermaid graph, a visualization, and a SPARQL query." |
| Publish domain extensions rather than growing the core | `notes/common-core-ontologies-cco.md` | "its authors explicitly encourage users to publish their own domain extensions rather than expanding CCO indefinitely with domain content" |
| DOLCE: stable since 2002, first-order logic, published consistency proof | `notes/dolce-...md` | "it has remained stable since its 2002/2003 release, is formally specified in first-order logic, and has a published consistency proof" |
| The OWL DOLCE is an adaptation, not the release | `notes/dolce-...md` | "The OWL models depart from official DOLCE: they omit modality and temporal indexing, while adding descriptions and situations that official DOLCE does not cover." |
| gist: ~100 classes, enterprise, disjointness, no inverse properties | `notes/gist.md` | "roughly 100 classes and a similar number of attributes and relationships"; "extensive high-level disjointness to expose inconsistent typing; sparing domain/range constraints; and no inverse properties" |
| gUFO is a lightweight OWL 2 DL implementation of a UFO subset | `notes/gufo.md` | "a lightweight implementation of the Unified Foundational Ontology for Semantic Web OWL 2 DL applications. It selects a subset of UFO-A and UFO-B" |
| gUFO's individuals/types split | `notes/gufo.md` | "separates a taxonomy of individuals—such as objects, aspects, events, and situations—from a taxonomy of types, including kinds, phases, roles, categories, and relationship types" |
| gUFO omits constraints that would break decidability; proper parthood example | `notes/gufo.md` | "Some intended constraints are not declared when they would violate OWL 2 DL decidability rules; for example, proper parthood is described as asymmetric and irreflexive, but those characteristics are omitted from the implementation." |
| OBO Foundry pairs a catalog with published principles; searchable, submittable | `notes/obo-foundry.md` | "Its site combines principles and best-practice material with community resources and an ontology catalog"; "Search or filter the ontology table…, consult the principles and tutorial, …, or submit an ontology for consideration." |
| Inclusion is not endorsement (OBO) | `notes/obo-foundry.md` | "The home page… does not itself establish that every listed ontology satisfies every principle; ontology selection still calls for examining the relevant entry and metadata." |
| Inclusion is not certification (design-pattern portal) | `notes/ontologydesignpatterns-org.md` | "the page still marks 'Certified content OP' as 'Due to come,' so catalogue presence should not be mistaken for certification" |
| Labels carry meaning, identifiers stay opaque | `notes/elot.md` | "labels, not CURIEs, should carry human-readable meaning" |
| CCO's version 2 changed the IRI namespace and adopted opaque identifiers | `notes/common-core-ontologies-cco.md` | "Version 2.0 changed the IRI namespace and adopted opaque local identifiers; the release summary says there were no other ontology changes from v1.7 to v2.0." |
| Numeric counters are invalid XML names; slugs are lossy | `notes/elot.md` | "Numeric-only counter identifiers are technically invalid XML NCNames, so an alphabetic counter template is recommended. ACME slugs are lossy and have finite per-slug/day random entropy" |
| Identifier policy belongs to the ontology, with a documented menu | `notes/elot.md` | "Identifier policy belongs to each ontology rather than to ELOT globally: documented schemes include UUIDs, label-derived slugs, formatted counters, and ACME identifiers, and custom schemes can be registered." |
| Protégé desktop vs WebProtégé; OWL 2, reasoning, querying, plug-ins | `notes/protege.md` | "available as a local desktop application and as WebProtégé for collaborative browser-based editing"; "OWL 2; ontology modelling; reasoning and querying; collaboration; Java plug-in architecture" |
| CCO's own instructions assume Protégé | `notes/common-core-ontologies-cco.md` | "Clone the repository and import `AllCoreOntology.ttl` into Protégé to assemble the eleven modules" |
| ELOT: one notebook is source and documentation; outline carries formal meaning | `notes/elot.md` | "one plain-text Org notebook is both the ontology source and its documentation"; "headlines declare classes, properties, and individuals, while nesting expresses subclass or subproperty hierarchy" |
| ELOT axioms in Manchester syntax; queries and diagrams in the same file | `notes/elot.md` | "axiom values written in Manchester Syntax"; "SPARQL `SELECT`/`CONSTRUCT` blocks and rdfpuml/PlantUML output form part of the same document" |
| ELOT used in scores of projects including an ISO standard | `notes/elot.md` | "the README says it has been used in scores of ontology projects, including ISO 23726-3" |
| ROBOT's command list, read aloud verbatim | `notes/robot.md` | "annotation, conversion, diffing, extraction, filtering, materialization, merging, querying, reasoning, repair, reporting, templating, profile validation, and verification" |
| ROBOT is CLI or library | `notes/robot.md` | "available as a command-line program or as a library for JVM languages" |
| ELOT depends on ROBOT for conversion, queries, reasoning, reports | `notes/elot.md` | "ROBOT is optional but required for conversion, SPARQL, reasoning, and report tools." |
| WIDOCO expansion and capability set | `notes/widoco.md` | "WIDOCO (WIzard for DOCumenting Ontologies) generates enriched, customizable, human-readable ontology documentation…integrates WebVOWL visualization, OOPS! evaluation, Licensius license metadata, PROV-O provenance, and Bubastis-based version changelogs." |
| Keep publication metadata in the ontology, not a side file | `notes/widoco.md` | "the docs recommend this over a separate `.properties` file because embedded metadata is easier to maintain across releases" |
| Version identifier + previous-version link is what makes a changelog possible | `notes/widoco.md` | "version IRI and version information, creation date, and a link to the previous version. WIDOCO uses the previous-version relation to generate changelogs" |
| Term statuses run unstable / testing / stable / archaic; annotations carry deprecation | `notes/widoco.md` | "optional term annotations cover examples, original source, rationale, deprecation, and status. Supported term statuses include `unstable`, `testing`, `stable`, and `archaic`." |
| Definitions are a published principle | `notes/obo-foundry.md` | "The listed principles cover openness, common format, identifier space, versioning, scope, textual definitions, relations, documentation…" |
| Six of sixteen OBO principles are about not breaking downstream users | `notes/obo-foundry.md` | same list — identifier space, versioning, change notification, maintenance, term-meaning stability, responsiveness (6 of the 16 enumerated) |
| AML is automated, efficient, element-level with background knowledge | `notes/agreementmakerlight-aml.md` | "an automated, efficient ontology-matching system with a flexible, extensible framework… emphasizes element-level matching techniques supported by background knowledge" |
| AML's three modes; alignment as required repair input | `notes/agreementmakerlight-aml.md` | "AML distinguishes automatic match, configurable manual match, and alignment-repair modes"; "An alignment can be supplied as a reference during matching or as the required input to alignment repair." |
| AML saves nothing without an output path | `notes/agreementmakerlight-aml.md` | "AML does not save results unless an output path is given." |
| AML reports strong results on shared evaluation tracks | `notes/agreementmakerlight-aml.md` | "the project reports strong results across several OAEI tracks" |
| LogMap: scale, classes/properties/instances, reasoning + repair | `notes/logmap.md` | "highly scalable ontology matching system with built-in reasoning and inconsistency-repair capabilities. It extracts mappings between classes, properties, and instances… tens or even hundreds of thousands of classes" |
| Large alignment tasks divide into subtasks (documented module) | `notes/logmap.md` | "A large alignment task can be divided into manageable subtasks; the repository describes this as a dedicated LogMap module." |
| Newer Java needs VM arguments; heap up to twenty-five gigabytes | `notes/logmap.md` | "Newer Java versions require documented VM arguments… the suggested configuration also allows a heap up to 25 GB." |
| gist's release fourteen broke compatibility; migration scripts supplied; next release compatible | `notes/gist.md` | "Major release 14.0.0 broke compatibility with earlier versions, although migration scripts were supplied; 14.1.0 is backward-compatible with 14.0.0." |
| gist namespace rules forbid defining your own terms there | `notes/gist.md` | "gist concepts must remain in the gist namespace, and users must not define their own terms there" |
| OWL API / Protégé version differences produce spurious diffs, and the token-change remedy | `notes/common-core-ontologies-cco.md` | "Different OWL API and Protégé versions can generate spurious formatting diffs; contributors are told to make a token change and inspect the diff before substantive edits, then verify that the result loads correctly in Protégé." |
| CCO has a Governance Board that tells users which release to wait for | `notes/common-core-ontologies-cco.md` | "The Governance Board recommends waiting until after 4.0 to update, while users needing current changes should pull from `develop`." |
| The guarded LLM-edit pattern, and its stated limit | `notes/elot.md` | "File writes are project-scoped, disabled by default, confirmation-gated, and revalidated with rollback"; "Automatic LLM mutation validation checks lint and OWL parsing, not semantic consistency; run the separate consistency check after edits." |

## Cut

Every item below traced to **no** note in lecture 7's permitted list. Several are true
and sourced elsewhere in the repo but under notes assigned to other lectures; per the
audit rule they are cut here, not softened.

| Cut text (verbatim) | Reason |
|---|---|
| "BFO… is the most widely adopted upper ontology" | Superlative. `bfo-basic-formal-ontology.md` gives an adoption count, never a ranking. Replaced by the count. |
| "things that persist versus things that happen, independent things versus things that depend on a bearer" | The continuant/occurrent and independent/dependent split is nowhere in the BFO note. Presented as sourced BFO content; unsupported. |
| "The Digital Buildings ontology from Google states this as explicit guidance: reuse existing types before proposing validated extensions." | Traces to `notes/digital-buildings-ontology-dbo.md`, not a lecture 7 source. |
| "BioPortal for biomedical ontologies, with browsing, annotation, recommendation, and mappings." | `notes/bioportal.md` — not a permitted source. |
| "Linked Open Vocabularies, which catalogues vocabularies and individual terms." | `notes/linked-open-vocabularies.md` — not permitted. |
| "BARTOC, which spans terminologies and registries broadly." | `notes/bartoc-...md` — not permitted. |
| "DBpedia Archivo, which automatically discovers ontologies on the web, keeps persistent snapshots, and rates them on retrievability, licensing, and consistency." + "Archivo's star ratings are described by its own authors as minimum-viability signals rather than a quality ranking." | `notes/dbpedia-archivo.md` — not permitted. |
| "Curated lists warn that they contain abandoned, stalled, and incomplete entries." | Traces to the awesome-list notes; not permitted, and "curated lists" is anonymous. |
| "the caution that **every one** of those catalogues states about itself" | Universal quantifier over catalogues the lecture no longer names and the notes never survey. Narrowed to the two catalogues whose notes state it. |
| "Its DL Query tab lets you search a classified ontology using Manchester syntax class expressions, which is the fastest way to check whether your model means what you think." | `notes/dl-query-class-expression.md` — not permitted; `protege.md` says nothing about a DL Query tab, and "fastest way" is an unsupported superlative. |
| "Eddy uses a visual language called Graphol with design-time validation." | `notes/eddy.md` — not permitted. |
| "Fluent Editor uses controlled natural language, so domain experts author sentences rather than axioms." | `notes/fluent-editor.md` — not permitted. |
| "OWLGrEd does whole-ontology graphical editing." | `notes/owlgred.md` — not permitted. |
| "VocBench handles collaborative multilingual work across OWL, SKOS, and lexical resources, which matters enormously in public-sector and cultural-heritage settings." | `notes/vocbench.md` — not permitted; the "matters enormously" clause is unsourced anywhere. |
| "Tawny-OWL constructs ontologies programmatically in a Clojure library." | `notes/tawny-owl.md` — not permitted. |
| "LinkML lets you author a schema once in YAML and generate SHACL, ShEx, OWL, JSON Schema, SQL, and language types from it, which is the pragmatic choice when your ontology needs to reach systems that will never speak RDF." | `notes/linkml.md` — not permitted; also the longest unspeakable acronym run in the file. |
| "OnToology watches a repository and proposes generated documentation and diagrams when things change." | `notes/ontoology.md` — not permitted. |
| "OntoAligner offers a modular pipeline spanning classical, retrieval-based, embedding-based, and language-model matchers, with ensembles." | `notes/ontoaligner.md` — not permitted. |
| "The Alignment API gives you a shareable format so correspondences are artifacts rather than scripts." | `notes/alignment-api.md` — not permitted (it is a lecture 3 source). |
| "And there's an annual evaluation initiative that benchmarks matchers on standard tasks, which is the honest place to check claims." | `notes/ontology-alignment-evaluation-initiative-oaei.md` — not permitted. Replaced by AML's own note-supported "reports strong results across several shared evaluation tracks". |
| "Direct all-pairs matching with a language model is quadratic, and the documentation puts the practical ceiling at roughly two hundred concepts, which is small." | Ontoaligner material; not permitted. This was the most specific number in the alignment section and it had no permitted source. |
| "And matching thresholds tend to be dataset-specific, so a configuration tuned on one pair of ontologies will not transfer." | Same source, same problem. |
| "HermiT documents specific compatibility boundaries with particular API versions." | `notes/hermit.md` — a lecture 6 source, not a lecture 7 source. Replaced with LogMap's own documented API-branch rot. |
| "The Gene Ontology has a consortium with funding and curators. … CIDOC CRM has a standards committee. FIBO has an industry body." | `gene-ontology-go.md`, `cidoc-crm-...md`, `fibo.md` — none permitted. Replaced with the two governance bodies the permitted notes do document (OBO Foundry principles/submission route, CCO Governance Board) plus gist's migration and namespace rules. |
| "The convention that's emerged in the biomedical world is worth copying: identifiers are never reused and never deleted. A term that turns out to be wrong is marked as obsolete, keeps its identifier forever, gains an explanation of why it was obsoleted, and where possible points to its replacement. So a dataset from 2011 that cites an obsolete term still resolves…" (plus the following "Compare that to the alternative…" paragraph) | **Would need a new note.** `obo-foundry.md` lists "identifier space", "versioning" and "term-meaning stability" as principles but states nothing about obsolescence conventions, never-reuse, replacement pointers, or resolution of old identifiers. Largest single cut in the pass. Flagged for a future note on OBO identifier/deprecation policy. |
| "OWL supports version identifiers directly — a version identifier alongside the ontology identifier" | `notes/owl-2-web-ontology-language.md` is a lecture 5/6/9 source, not a lecture 7 source. Re-attributed to WIDOCO's metadata guidance, which does state version IRI + version information + previous-version link. |
| "four thousand classes, … classification takes forty minutes, and no consuming system uses more than eighty terms" | Three invented numbers presented as reportage. Replaced with unquantified narrator observation. |
| "a query that gives a number that's four percent wrong" | Invented statistic. Number removed, illustration kept. |
| "Debates about whether something is a continuant or an occurrent run for weeks" | Same unsourced BFO vocabulary as the earlier cut; generalised to "debates about foundational categories". |
| "skipping it is the most common cause of the failure mode we'll come to at the end" | Unsupported causal claim about the field's failures. |
| "It's the single most effective control on scope in this discipline" | Superlative about the discipline → re-marked as the narrator's ("the strongest control on scope I know of"). |
| "The successful ontologies in this field all have answers to those questions" | Universal claim about "all successful ontologies"; narrowed to the projects in the lecture's own sources. |
| "…and most that didn't, didn't." | Unsupported claim about most failed projects. |

## Corrected

| Before | After | Forcing span |
|---|---|---|
| "BFO … is the most widely adopted upper ontology" | "more than five hundred and fifty ontology-driven efforts do exactly that" | `bfo…md`: "adoption by more than 550 ontology-driven efforts" |
| "DOLCE's official release is a first-order logic axiomatisation, which means it commits harder and computes less easily." | "…is formally specified in first-order logic, and has a published consistency proof. The catch its own documentation states is that the versions in OWL … are re-engineerings rather than identical releases" | `dolce…md`: "The OWL models depart from official DOLCE: they omit modality and temporal indexing…" — the note documents an adaptation gap, not a "commits harder / computes less" trade the narrator inferred. |
| "gUFO is a lightweight OWL 2 DL implementation of a selected subset of the Unified Foundational Ontology." (stated and dropped) | Same, plus the design-contract caveat about undeclared constraints | `gufo.md`: "Some intended constraints are not declared when they would violate OWL 2 DL decidability rules…" |
| "The Common Core Ontologies tell adopters to publish domain extensions rather than expanding the common core indefinitely." (anonymous "tell adopters") | "their authors explicitly encourage users to publish their own domain extensions" | `common-core…md`: "its authors explicitly encourage users…" |
| "OntologyDesignPatterns dot org says explicitly that presence in the catalogue is not certification." | "The ontology design patterns portal … still marks certified content as due to come, so presence in that catalogue is not certification" | `ontologydesignpatterns-org.md`: the site marks "Certified content OP" as "Due to come" — it does not "say explicitly" the stronger thing. Also removes a spoken URL. |
| "The literate ontology tooling documents the specific traps" (anonymous) | "ELOT — the literate ontology-engineering environment — …" | `elot.md`, attribution restored + acronym introduced. |
| "a permanent lie embedded in a URI" | "a permanent lie in a name" (with IRI introduced and expanded earlier, per CCO) | `common-core…md` uses IRI; URI never appears in a permitted note. |
| "Protégé is the general-purpose default." | "Protégé is a free, open-source OWL ontology editor covering the whole lifecycle." | `protege.md`: "free, open-source OWL ontology editor" / verdict "covering the full OWL 2 ontology-development lifecycle". "Default" was a market claim. |
| "LogMap … which matters because naively merging two consistent ontologies routinely produces an inconsistent one" | "it integrates reasoning and mapping repair to minimise logical inconsistencies in the alignments it produces" | `logmap.md`: "Reasoning and mapping repair are integrated to minimize logical inconsistencies in produced alignments." The "routinely produces an inconsistent one" frequency claim had no source. |
| "Which means all of it in continuous integration. Every pull request classifies the ontology…" (stated as fact) | "my argument is that this is the point. Put it in continuous integration…" | Narrator's recommendation, now marked; `robot.md` supports only the command surface. |
| "WIDOCO generates standards-aware documentation with provenance, visualisations, evaluation, and version changelogs." | Same content, expanded acronym, plus the note's metadata-in-annotations advice | `widoco.md` — attribution and expansion added. |
| "Gist had a major release that broke compatibility and required migrations." | "its major release fourteen broke compatibility…, migration scripts were supplied, and the following release was backward-compatible again" | `gist.md`: "Major release 14.0.0 broke compatibility…; 14.1.0 is backward-compatible with 14.0.0." |
| "Different versions of the OWL API and Protégé can produce spurious differences in files" (no remedy) | Same, plus "make a token change, inspect the diff…, and confirm the result still loads" | `common-core…md` states the remedy the lecture had dropped. |

## Narration fixes

**Acronyms — all twelve now expanded or glossed on first use in this file.**
BFO → "the Basic Formal Ontology". CCO → "The Common Core Ontologies, CCO". DOLCE →
"the Descriptive Ontology for Linguistic and Cognitive Engineering". UFO → "the Unified
Foundational Ontology" (introduced at gUFO). OBO → "the Open Biological and Biomedical
Ontology Foundry", and ROBOT's gloss repeats "Open Biomedical Ontologies". OWL → "OWL,
the Web Ontology Language" at first use (DOLCE paragraph, before every later OWL
mention). IRI → "the Internationalized Resource Identifier, the global name of a term".
AML → "AgreementMakerLight, AML". WIDOCO → "the Wizard for Documenting Ontologies"
(the note's own expansion). ELOT → glossed as "the literate ontology-engineering
environment"; **the note gives no letter expansion**, so none was invented — flagged
here rather than fabricated. ROBOT likewise has no expansion in `robot.md`, so it is
glossed by function.

**Numbers and Latin.** "550" → "five hundred and fifty". "14.0.0/14.1.0" → "release
fourteen … the following release". "2.0" → "version two". "25 GB" → "twenty-five
gigabytes". "OWL 2 DL" → "OWL two applications in the description-logic profile".
"2011" cut with its paragraph. No Latin abbreviations remained.

**No markdown, code, or spoken syntax.** Removed `AllCoreOntology.ttl` (now "their
all-core file"), `store/config.ini` (now "a settings file"), "SHACL, ShEx, OWL, JSON
Schema, SQL" list, "OntologyDesignPatterns dot org", "README" (→ "its documentation"),
and the ISO number `23726-3` (→ "an ISO standard"). No headings, bullets or URLs
remain; grep for `http`, `.org`, `|`, leading `#`/`-`/`*` returns nothing.

**Seams.** The file had been written once and then had roughly 1,100 words spliced in
before the closing. The splice markers are gone:
- "Let me finish with the thing this lecture has been circling." (mid-file closing at
  the old line 71) — removed; the governance material it introduced now sits at the end
  where the plan puts it.
- "Let me add three practical things that don't fit the decision sequence but that
  you'll hit in the first six months." — removed. Versioning and documentation were not
  addenda; they are now decisions eight and nine inside the sequence they belong to.
- "One final warning, and it's about a failure I've seen enough to name." — removed; it
  introduced a fourth failure mode after the text had promised three.
- **Contradiction repaired:** "Now, three failure modes, and then I'll stop" was
  followed by forty more lines and a fourth failure mode. Now "Now, four failure modes",
  and the lecture does stop after them.
- **Duplication repaired:** WIDOCO was described twice (automation section and
  documentation section) with overlapping capability lists; the second is now a
  back-reference ("WIDOCO renders all of this; it cannot write the definitions").
- **Duplication repaired:** the competency-questions-as-tests point was made three
  times (decision one, decision six, closing); now once each, with the middle one
  reduced to a single clause.

**Endings.** Exactly one closing statement, at the very end, and it is the plan's:
"an ontology project is a governance project with a file attached. The modelling is the
easy half." The orphaned mid-file closing is gone. The sign-off ("Next time, the case
against everything I've just told you") matches lecture 8, "The Criticisms That Landed".

**Continuity.** The opening now states the position in the arc explicitly (first three =
history; four to six = engineering tradition, ending with the machinery) and names
lecture six's actual content — verified against
`lectures/transcripts/06-how-the-machinery-works.txt`, which closes on "a reasoner
computes what your axioms force to be true in every world that satisfies them… unstated
means unknown, never false", and whose own sign-off promises "we put all of this into
practice, and find out why an ontology project is really a governance project with a
file attached". Lecture 7 now delivers that promise verbatim.
Back-references checked: lecture three (Quine's criterion; alignment permanence) matches
the plan's lecture 3 beats "the criterion stated plainly" and "why that silence makes
ontology alignment permanent". Lecture four's "Cyc's forty years" matches
`04-cyc-and-the-engineering-sense.txt` line 33, "a project that has run for forty years";
the reference is now explicitly marked as a callback. The former back-reference "which
lecture four should have warned you about" was vague about *what* lecture four warned;
it now names the failure (deferred payoff / completeness) directly.

## Depth still available

Grounded material in the thirteen notes that the lecture does not yet use. All quoted.

- **LogMap's LLM angle** — the strongest unused item, and it sets up lecture ten:
  "the README states that LogMap supports LLM validation during matching and points to
  LogMapLLM work described as using large language models as oracles for ontology
  alignment. It also documents related work that augments alignment with semantic or
  knowledge-graph embeddings and distant supervision." Also "A separate LogMap variant
  targets violations of the conservativity principle."
- **CCO's live modernisation** — "The repository is undergoing modernization through
  planned 3.0 and 4.0 structural changes… users needing current changes should pull from
  `develop`." A concrete governance-in-motion example.
- **CCO patterns as reusable assets** — "documented patterns can be reused for RDF data
  mapping and SPARQL querying" and "The documentation explicitly recommends reusing CCO
  design patterns in knowledge graphs to speed data mapping and querying and improve
  consistency and interoperability."
- **ELOT's SKOS trick** — "Under an Individuals section, an inherited and overridable
  `ELOT-subheading-relation` can make immediate-parent nesting assert relations such as
  `skos:broader`, so the outline is also the source of a SKOS hierarchy."
- **ELOT's honesty about its own docs** — "The long-form manual is explicitly under
  construction; several manual files are stubs or drafts and may be inaccurate." Plus the
  editor-parity gap: "the documented VS Code matrix marks SPARQL, AI-assisted authoring,
  and diagrams as planned rather than available." A rare tool that documents its own
  incompleteness — good material for the "read the pitfalls section" theme.
- **ELOT's two-call constraint** — "A newly minted CURIE also cannot be used as an axiom
  subject in the same batch, so insertion and axiom editing require two calls." Concrete
  automation gotcha.
- **WIDOCO's publication surface beyond HTML** — "WIDOCO supports content negotiation,
  multiple ontology serializations, JSON-LD snippets in generated HTML, imported-ontology
  handling, evaluation reports, and diagrams." Plus the deployment trap: "Generated
  split-section HTML may appear incomplete when opened directly from the local filesystem
  because browsers block local section loading."
- **WIDOCO's metadata resolution limit** — "Entity-valued creator/contributor/publisher
  metadata is resolved only inside the ontology; external URI resolution is not
  supported."
- **ROBOT's install trap** — "The source specifically warns that PowerShell versions
  before 6 write a byte-order mark that breaks the generated Windows batch file." Also
  the library path: "compose `robot-core` operations—for example, loading an ontology and
  term list, extracting a core subset, and saving the result."
- **AML's Java compatibility warning** — "The documented release was tested with Oracle
  Java 1.7, 1.8, and 1.9, while OpenJDK compatibility is not guaranteed. The authors also
  report Maven compilation errors and advise downloading the release instead of building
  with Maven." A concrete instance of the "pin your toolchain" argument.
- **LogMap's format coverage and platform wrappers** — "Supply formats supported by OWL
  API, including RDF/XML, OWL/XML, OWL Functional Syntax, OBO, KRSS, and Turtle (N3)";
  "For OAEI workflows, use LogMap's MELT-platform wrapper/interface."
- **gist's licensing and serialisations** — "CC BY 4.0 use requires attribution";
  "Releases include Turtle, RDF/XML, and JSON-LD serializations plus documentation and
  migration material." Licence terms are a governance fact the lecture only gestures at.
- **DOLCE's methodological lineage** — "Originally a WonderWeb Foundational Ontologies
  Library module"; "OntoClean; roles, qualities, functions, organizations, artifacts, and
  group agency"; and the OWL choice: "evaluate DOLCE Lite or DUL as adaptations rather
  than identical releases."
- **gUFO's usage pattern** — "a domain class can both specialize `gufo:Object` and
  instantiate `gufo:Kind`, while concrete occurrences can instantiate `gufo:Event` and
  use the supplied temporal properties." A worked example of what adopting a foundation
  actually looks like at the class level.
- **BFO's support apparatus** — "consulting the project's guidebook, publications,
  tutorials, release history, and user forums as needed."
- **OBO Foundry's participation routes** — "mailing lists, Slack, working groups, and
  GitHub reports or suggestions", and "Catalog metadata can be downloaded as YAML,
  JSON-LD, or RDF/Turtle."
- **The design-patterns portal's full shape** — "run by ODPA. It began under the NeOn
  project and combines pattern catalogues with training, events, reviews, modeling
  issues, and community submissions"; "modeling issues linked to patterns; exemplary
  ontologies; open and quality-committee review." The plan's beat "design patterns and
  why the pattern catalogue is not a certification" is currently only half-served — the
  lecture uses the caution but never explains what a design pattern *is*.
