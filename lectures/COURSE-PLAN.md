# Ontologies: A Ten-Lecture Course

Ten lectures, twenty to thirty minutes each, about four hours ten total at a
narration pace of one hundred and forty-five words per minute. Written to be
listened to rather than read. Transcripts live in `transcripts/` as plain text
files, numbered in listening order.

Length follows the sources. Each lecture runs exactly as far as the notes
listed for it carry it, and no further, so the files differ in length by a
third or more. Shipped word counts:

| # | Lecture | Words | Approx. minutes |
| --- | --- | ---: | ---: |
| 1 | Three Things People Mean by "Ontology" | 3,143 | 22 |
| 2 | From Aristotle to Wolff | 2,815 | 19 |
| 3 | Quine, and Ontology as a Property of Theories | 3,091 | 21 |
| 4 | The Cathedral: Cyc | 2,780 | 19 |
| 5 | The Semantic Web | 3,913 | 27 |
| 6 | How the Machinery Actually Works | 4,470 | 31 |
| 7 | Building One for Real | 4,081 | 28 |
| 8 | The Criticisms That Landed | 4,414 | 30 |
| 9 | Palantir: The Ontology as an Operational Layer | 4,140 | 29 |
| 10 | The Politics of an Installed Ontology | 3,751 | 26 |
| | **Total** | **36,598** | **252** |

Every claim traces to a note in this repository. The source notes are listed
per lecture below, and the transcripts name their sources aloud where it
matters.

## Design constraints

- **Solo lecturer.** One voice, spoken prose, no bullets, no code, no URLs, no
  section headings inside the transcript. Anything a narrator cannot say out
  loud has been cut or rewritten.
- **One sitting per file.** Twenty to thirty minutes at about 145 words per
  minute. There is no word target. Quality is the constraint and length is the
  by-product: a lecture stops when its notes are spent.
- **Self-contained openings.** Each lecture starts by saying where it is in the
  arc, because listeners on a walk lose the thread between sessions.
- **One recap beat.** Each lecture ends by stating the single claim it wants
  retained, then stops. No summary-of-the-summary.
- **Acronyms expanded on first use** in every lecture, since listeners may
  start anywhere.

## The arc

Lectures one to three establish what the word means and where it came from.
Four to seven are the engineering tradition, ending with how you would actually
build one. Eight is the criticism. Nine and ten are Palantir and the present.
The criticism deliberately lands *after* the listener knows how the machinery
works, so it argues with something concrete.

## Lecture plans

### 1. Three Things People Mean by "Ontology"

**Claim to retain:** The word names a philosophical discipline, a specific
theory of what exists, and a machine-readable file. Most confusion in this
field is one of those three senses being swapped for another.

**Beats:** the airport-conversation problem; sense one, the branch of
philosophy; sense two, a particular philosopher's ontology; sense three, the
artifact; Gruber's definition read slowly; why "explicit" and "shared" are the
load-bearing words; what an ontology is not (a database schema, a taxonomy, a
knowledge graph); the promise of the series.

**Sources:** `notes/gruber-ontology-definition.md`,
`notes/ontology-word-history.md`, `notes/skos-simple-knowledge-organization-system.md`,
`notes/scigraph.md`, `SYNTHESIS.md`.

### 2. From Aristotle to Wolff: Where the Word Came From

**Claim to retain:** Ontology began as the search for the single true account
of being, and the engineering version quietly dropped that ambition while
keeping the vocabulary.

**Beats:** Aristotle's "being qua being" and why first philosophy is not
physics; the two-thousand-year gap before the word; Lorhard 1606; Goclenius
1613 and the Clauberg misattribution; Wolff 1730 and the demonstrative method;
general versus special metaphysics as the ancestor of upper versus domain
ontologies; Kant's demolition; Husserl's formal ontology; what survived the
transfer to computing and what did not.

**Sources:** `notes/ontology-word-history.md`, `notes/bfo-basic-formal-ontology.md`,
`notes/common-core-ontologies-cco.md`.

### 3. Quine, and Ontology as a Property of Theories

**Claim to retain:** To be is to be the value of a variable — Quine's own
wording, not the familiar "bound variable" version, which is Boolos's later
title. Ask not what exists, but what your model must quantify over to be true.

**Beats:** the problem of non-being; the move from world to theory; the criterion stated plainly; worked example on an
employee schema; why the criterion is silent about truth; why that silence
makes ontology alignment permanent rather than embarrassing; the structural resemblance between
Quine's criterion and Guarino's construction, which cites neither the other.

**Sources:** `notes/quine-ontological-commitment.md`,
`notes/gruber-ontology-definition.md`, `notes/ontology-matching.md`,
`notes/alignment-api.md`.

### 4. The Cathedral: Cyc, and the Birth of the Engineering Sense

**Claim to retain:** The computer-science sense of "ontology" was invented to
solve a sharing problem between knowledge-based systems, and its founding
project bet everything on a critical mass it never reached.

**Beats:** expert systems and the knowledge-acquisition bottleneck; Lenat and
Shepherd starting Cyc in 1984 knowing the odds; what codifying common sense
requires — causality, time, space, substances, intention, belief; the peanut
butter and table example; a million hand-crafted axioms; the DARPA Knowledge
Sharing Effort and why sharing, not reasoning, produced the definition; Gruber
1993; Borst's addition of "shared"; the lesson about deferred payoff.

**Sources:** `notes/cyc-lenat-1995.md`, `notes/gruber-ontology-definition.md`,
`notes/cyc.md`, `notes/description-logics-dls.md`.

### 5. The Semantic Web: A Vision and the Stack It Built

**Claim to retain:** Every awkward feature of the standards is an answer to a
requirement in the 2001 article, and most of those requirements assumed an
open web of strangers.

**Beats:** the Pete and Lucy scenario read out; what it demands technically;
RDF as the merge-without-coordination data model; the URI as global identity;
why triples and not tables; RDFS as the small vocabulary; OWL as the
expressive one; SPARQL as the query layer; SHACL and ShEx as the validation
layer that arrived late and mattered more than expected; serializations as
spelling rather than substance; the four phases and where the energy went.

**Sources:** `notes/semantic-web-2001-vision.md`,
`notes/rdf-resource-description-framework-1-1.md`,
`notes/rdf-schema-rdfs-1-1.md`, `notes/owl-2-web-ontology-language.md`,
`notes/sparql-1-1.md`, `notes/shacl-shapes-constraint-language.md`,
`notes/turtle.md`, `notes/json-ld.md`.

### 6. How the Machinery Actually Works

**Claim to retain:** Open-world semantics is the single idea that most often
breaks a database engineer's intuition, and every strange behaviour of a
reasoner follows from it.

**Beats:** description logic as the mental model; concepts as sets, roles as
pairs; TBox and ABox; what a reasoner computes — subsumption, membership,
consistency; the classification example; the open-world assumption spelled out
with a worked case; no unique name assumption; why absence proves nothing; the
expressivity and complexity trade; OWL profiles EL, QL, RL and what each buys;
why validation with SHACL is a different job from inference with a reasoner.

**Sources:** `notes/description-logics-dls.md`,
`notes/owl-2-web-ontology-language.md`, `notes/elk.md`, `notes/hermit.md`,
`notes/openllet.md`, `notes/shacl-shapes-constraint-language.md`,
`notes/dl-query-class-expression.md`.

### 7. Building One for Real

**Claim to retain:** An ontology project is a governance project with a file
attached. The modelling is the easy half.

**Beats:** competency questions before classes; layered reuse and why BFO
excludes scientific terms; mid-level ontologies; picking a foundation and what
DOLCE, gist, and gUFO each commit you to; design patterns and why the pattern
catalogue is not a certification; identifiers and the label-carries-meaning
rule; Protégé and the editor spectrum; automation with ROBOT and documentation
with WIDOCO; alignment as its own discipline; version and profile compatibility
as an operational fact; the scope-creep failure mode.

**Sources:** `notes/bfo-basic-formal-ontology.md`,
`notes/common-core-ontologies-cco.md`, `notes/gist.md`, `notes/gufo.md`,
`notes/dolce-descriptive-ontology-for-linguistic-and-cognitive-engineering.md`,
`notes/ontologydesignpatterns-org.md`, `notes/protege.md`, `notes/robot.md`,
`notes/widoco.md`, `notes/obo-foundry.md`, `notes/elot.md`,
`notes/agreementmakerlight-aml.md`, `notes/logmap.md`.

### 8. The Criticisms That Landed

**Claim to retain:** Three critiques, three different layers. Incentives,
applicability, and consequences. The third is the one the field still has not
answered.

**Beats:** Doctorow's seven obstacles with the eBay and Nielsen examples;
schemas are not neutral, washing machines both ways; what Doctorow concedes
about implicit metadata; Shirky's periodic table and noble gases; Dewey's 200s
and the Library of Congress on Asia and Africa; there is no shelf; the parable
of the Yahoo ontologist; Shirky's real preconditions restated as a checklist;
Bowker and Star on the International Classification of Diseases, apartheid
reclassification, and the Nursing Interventions Classification; torque;
black-boxing; what each critique does and does not prove.

**Sources:** `notes/doctorow-metacrap.md`,
`notes/shirky-ontology-is-overrated.md`,
`notes/bowker-star-sorting-things-out.md`,
`notes/semantic-web-retrospective.md`.

### 9. Palantir: The Ontology as an Operational Layer

**Claim to retain:** Palantir's Ontology adds verbs and permissions to the
nouns, which is exactly what the W3C stack cannot express, and it drops the
logic, which is exactly what the W3C stack is for.

**Beats:** what Palantir actually says in its own architecture documentation;
the fourfold integration of data, logic, action, and security; object types,
objects, object sets, link types and their two sides; the dataset analogy
Palantir itself offers; action types as transactions with parameters,
validation, and side effects; functions and interfaces; writeback, so decisions
become data; digital twin framing; the explicit claim that it is not a semantic
layer; the head-to-head with OWL on open versus closed world, reasoning, and
federation; why the agent story makes actions the important half.

**Sources:** `notes/palantir-ontology.md`,
`notes/owl-2-web-ontology-language.md`, `notes/shacl-shapes-constraint-language.md`,
`notes/gruber-ontology-definition.md`.

### 10. The Politics of an Installed Ontology, and What Comes Next

**Claim to retain:** Once an ontology drives actions inside an institution, its
categories stop describing the world and start producing it. Everything in
lecture eight becomes a legal question.

**Beats:** the Danish POL-INTEL study and its two senses of ontology; the
getaway-vehicle example; platformisation and the redistribution of skill; the
German constitutional court ruling of February 2023 and the bystander problem;
why this is Bowker and Star with a contract attached; what a responsible
review of an operational ontology asks; then the present — can a language model
replace an ontology, build one, use one; the three answers; the guarded pattern
from ELOT; closing verdict on when to build one and when not to.

**Sources:** `notes/palantir-ontology-critique.md`,
`notes/bowker-star-sorting-things-out.md`, `notes/llm-ontology-debate.md`,
`notes/ontolearner.md`, `notes/ontoaligner.md`, `notes/elot.md`.

## Listening in ElevenReader

Upload the ten files in `transcripts/` in order. They are plain text with no
markup, so nothing is read aloud that should not be. See `VOICE.md` for the
narrator setup.
