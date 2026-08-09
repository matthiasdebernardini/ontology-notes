# Run log — verify and repair the lecture course, the notes, and the published book

Evidence with quoted spans is in `EVIDENCE.md`. This file records what was checked, what
changed, and what could not be verified.

## Conflicts with the earlier goal files

`goals/ontology-harvest/goal.md` says every claim must be grounded in the source's own text.
`goals/ontology-harvest-fixes/goal.md` adds the corpus invariants. Both still bind and neither
conflicted with this run's instructions. One instruction was *added* by this run and is worth
naming: the per-lecture word range in `lectures/COURSE-PLAN.md` (2,700–3,100) was lifted.

## Task 1 — Ground the thirteen new notes

### What was checked

All thirteen notes, claim by claim, against the local captures. The unit of audit was the
factual proposition, not just names, dates, and numbers. Four parallel readers each took a
cluster of notes, grepped the captures, and reported quoted spans; every finding was then
applied by hand. `EVIDENCE.md` Part 2 carries the full table — verified rows included, not
only cuts.

### Dead captures

Three scrapes were known to have failed. All three confirmed dead:

- `ai-cyc-sowa-review.md` — 248 bytes of `\[Image: Im1\]` repetitions. Cited by no note.
- `crit-torquing-review.md` — MIT Anthropology 404 page. **Was** the intended source for the
  *torque* definition, which meant the definition in `bowker-star-sorting-things-out.md`
  traced to nothing.
- `pltr-crit-seer-seen.md` — 63-byte 403. Cited by no note.

A **fourth** dead capture was found that had not been flagged: `semweb-sciam-2001.md` is a
Scientific American paywall shell — 649 words of masthead, newsletter signup and "Popular
Stories", with no article body and zero occurrences of "Pete" or "Lucy". Every content claim
about the 2001 article traced only to it.

### Re-fetches

Five, all successful, all stored as new captures:

| capture | grounds |
| --- | --- |
| `research/firecrawl/semweb-sciam-2001-fulltext.md` | the article's full text, from an archived PDF |
| `research/firecrawl/crit-torquing-review-refetch.md` | the *torque* definition, from the Internet Archive copy of Helmreich's review essay |
| `research/firecrawl/pltr-crit-bverfg-pressrelease.md` | the German constitutional judgment of 16 February 2023 |
| `research/firecrawl/semweb-twobithistory-about.md` | the Sinclair Target byline |
| `research/dblp/lenat-cyc-1995.json` | *Commun. ACM* 38(11), 1995 for the Lenat article |

No re-fetch failed, so nothing was cut for want of a source.

### The invariant that was broken

**All thirteen notes were missing the `**Verdict**` field**, and `NOTE_INDEX.json` had been
hand-patched with `"Verdict": "none stated"` for each. The index therefore did not mirror the
notes. `python3 scripts/check.py` failed with 39 errors before this run. `uvx pytest tests -q`
passed anyway, because the test asserts the six-field schema against the *index*, not against
the note files — the fabricated field satisfied it.

Fixed by writing a real, grounded Verdict for each note and regenerating the index with
`scripts/rebuild_index.py`. `check.py` now passes.

### Corrections applied

Errors of fact, corrected:

1. **Quine's slogan was misquoted.** The note gave "to be is to be the value of a *bound*
   variable" in quotation marks. Quine writes "To be is to be the value of a variable"; the
   "bound variable" wording is Boolos's 1984 paper title.
2. **Dewey's 200s.** The note said "nine categories to Christianity and one to other
   religions." Shirky's block has nine subdivisions *in total*, one of which is "290 Other
   religions."
3. **Shirky's "three preconditions" do not exist.** He gives "a partial list of
   characteristics" in two groups of nine items, and explicitly does not offer it as a test.
4. **Doctorow's obstacle 4** is titled "Mission: Impossible — know thyself", not "Know thyself
   is impossible"; his Nielsen example says "log-books", not "paper diaries", and names
   *Sesame Street* alongside *Masterpiece Theater*.
5. **The ICD "took decades to negotiate."** The available source says "many years." No capture
   contains the word "decades".
6. **Cyc's cost.** "Decades of specialist labour" replaced with the paper's own figure, "a
   person-century of effort."
7. **Cyc's venue and year had no source at all** — the capture carries no date, and "1995
   CACM" came from the PDF filename. Now cited to DBLP.
8. **The retrospective's third phase** was described as "enterprise and scientific
   deployments." Target's third phase is adapting the standards to developer practice
   (JSON-LD, schema.org). The enterprise thread is Ontotext's and is now attributed to them.
9. **Palantir's Functions** were credited with a list the documentation assigns to *logic*.
10. **The German ruling** was reported as striking down Hamburg's law "and a similar Hesse
    law." The secondary source (WIRED) reads as contradicting this. The court's own press
    release confirms the note was right — both provisions are unconstitutional — but the
    remedies differ, and the note now says so: Hamburg's provision is void, Hesse's continued
    to apply under restriction until 30 September 2023. The "one click" quotation was also
    altered inside quotation marks and has been restored verbatim.
11. **The OntoLearner pitfall was inverted.** The note said hallucination and inconsistency
    "survive good prompting"; the source note says clear prompts *reduce* them.
12. **"Metacrap" was described as aimed at the Scientific American article.** It never
    mentions it, the Semantic Web, or Berners-Lee.

Attribution added where a claim was right but anonymous: Amit Singhal for "things, not
strings"; Terrence A. Brooks and Eric Nehrlich as the actual sources for most of the Bowker
and Star note; Bruno Latour for black-boxing; Leese (2023) for "not only describe the world
but also enact it"; Britta Eder as the named claimant; Guarino, Oberle and Staab rather than
"Guarino"; Sinclair Target for the Two-Bit History account; `notes/scigraph.md` as the
unnamed "concrete example" of a lossy graph mapping.

Passages that were the note author's own reasoning but read as sourced are now marked as
such: the OWL-versus-Palantir comparison (Palantir's documentation never mentions OWL, RDF,
the W3C, reasoners, or world assumptions), the Cyc LLM angle, the "replacement case" in the
language-model note, and the ranking of the three replace/build/use questions.

### Claims cut

Nineteen, listed with reasons in `EVIDENCE.md` Part 3. The load-bearing ones: Guarino's
construction described as "the direct descendant" of Quine's and as "what OWL's
model-theoretic semantics implements" (Guarino's chapter never mentions Quine); Wolff's
general/special split as "the direct ancestor" of the BFO/GO divide (BFO appears in zero
captures); "every enterprise semantic layer"; FIBO and finance as retrospectively named
Semantic Web successes (zero corpus-wide hits for FIBO in `research/`); the
"residual-category test" attributed to Bowker and Star (zero occurrences of "residual"
anywhere in `research/`); "genomics, museum records, and financial instruments" as Shirky's
examples; "graph databases with no formal semantics adopting the vocabulary of the field".

### What could not be verified

- **"Maria" Keet.** The capture never names the author; only the URL and a link to "my
  ontology engineering textbook". Reduced to "Keet".
- **The Doctorow PDF.** Two URLs are listed (well.com and a chnm.gmu.edu archived PDF) but
  only one capture exists, and it is print-paginated, so it is not determinable which URL it
  came from. Both left listed.
- **`theconversation.com` capture.** Present, listed, supports no claim in the note. Left in
  place rather than removed, since it was consulted.

## Task 2 — The four SYNTHESIS additions

### What was checked

Every `[text](notes/<slug>.md)` citation in "Where the idea came from", "Criticism worth
answering", "Operational ontologies: the other tradition", and "Ontologies after large
language models": does the path exist, and does that note state the claim attributed to it.

**No citation path was broken.** `scripts/check.py` verifies all 109 synthesis citations
resolve, and it passed on this axis before and after.

### Corrections applied

1. **"OWL has model-theoretic semantics, an open-world assumption, reasoners…" was cited to
   `owl-2-web-ontology-language.md` and `shacl-shapes-constraint-language.md`.** Neither note
   states it; the OWL note contains no occurrence of "open-world", and SHACL is unrelated to
   the sentence. Re-cited to `palantir-ontology.md` and `description-logics-dls.md`, which do
   state it, and the sentence now says the comparison is this corpus's rather than Palantir's.
2. **"The engineering programme that produced it, Cyc"** — no note says Cyc produced Gruber's
   definition; the Gruber note attributes it to the ARPA Knowledge Sharing Effort. The
   anaphora was broken.
3. **"the field's most expensive experiment"** — the note says "largest sustained attempt".
   Replaced, with the person-century figure.
4. **"kinetic elements, meaning action types, functions, and dynamic security"** — the note's
   kinetic third item is *interfaces*; security is a separate first-class element and the
   phrase "dynamic security" appears in no note. Corrected.
5. **"funders, curators, and governance"** cited to three notes, one of which
   (`gene-ontology-go.md`) says nothing about any of them, while five of the eight named
   domains carried no citation at all. Re-cited to `semantic-web-retrospective.md`, which
   states the claim in those words, plus the five missing domain notes.
6. **"their critique is the one the technical literature answers least"** — no note makes a
   claim about the technical literature's response. Downgraded to what the corpus supports.
7. **"implicit metadata … is reliable in a way declared metadata is not"** — the note asserts
   a distinction, not a ranking. Replaced with the note's own wording.
8. **"coined by Jacob Lorhard"** — priority is contested; the note says "used".
9. **"Guarino later reconstructed both formally"** — the reconstruction covers
   conceptualization only. "both" dropped.
10. **"the most visible product using the word"** — no note ranks visibility. Cut.
11. **"the design brief that RDF, OWL, and SPARQL answer"** — SPARQL was asserted without a
    citation and postdates the article by five years. Re-worded, and `notes/sparql-1-1.md`
    cited.

### Uncited sentences left in place

Four aphoristic sentences in these sections carry no citation and none is needed, because
they are the synthesis's own framing rather than factual claims: "Three critiques have
survived and each attacks a different layer"; the closing "failures of the model against the
world … failure of the world against the model"; "choosing between deriving what follows and
governing what may be done". These are argument, not assertion. Flagged here so the absence
is a decision rather than an oversight.

## Task 4 — The site generator

### Determinism and re-run safety

`scripts/build_site.py` deletes `site/src` on every run. Verified safe: the only
hand-written files under `site/` are `README.md` and `book.toml`, both at the top level,
both outside `src/`, and both the only files git tracks there. `site/src` and `site/book`
are gitignored. Running the generator twice in a row produces byte-identical output
(`diff -r`), and it uses no clock, no random source, and no dict iteration whose order
could vary — `CONCEPTS` and `NOTE_INDEX.json` both iterate in stable order and everything
sorted is sorted explicitly.

### SUMMARY coverage

Checked mechanically in both directions: every `.md` file the generator writes under
`site/src` appears in `SUMMARY.md`, and every path `SUMMARY.md` links to exists. Zero
orphans, zero dangling links. The 22 section headings use mdBook's draft-chapter form
`- [Section]()`, which is a sidebar heading with no page of its own — not a link to a
missing file.

### The link checker

New: `scripts/checklinks.py`, tracked, standard library only, directory as the first
argument. It checks every local `href` and `src` — relative and root-relative,
URL-encoded or not, including the raw `.txt` transcript paths — resolves directory
targets to `index.html`, checks `#fragment` targets against the `id` and `name` anchors
in the destination page, skips external schemes, prints each broken link with its source
file, and exits nonzero.

It earned its keep on the first run: 4 broken links, all of them cross-references to
notes I had just added to `notes/semantic-web-retrospective.md` under guessed slugs
(`cidoc-conceptual-reference-model-crm`, `fibo-financial-industry-business-ontology`;
the real slugs are `cidoc-crm-conceptual-reference-model` and `fibo`). Fixed. It now
reports 201 pages, 7,077 local links, 0 broken.

### The 26 CONCEPTS definitions

Audited against the corpus, term by term. Result: 9 kept as written, 16 rewritten from a
note's own text, 1 cut. Evidence and spans in `EVIDENCE.md` Part 4. The load-bearing ones:

- **Justification** — cut. The string "justification" occurs **zero times** in `notes/`.
  The corpus talks about *explanations*, so the entry became **Explanation**, written from
  `notes/elk.md`.
- **Punning** — the definition asserted OWL 2 punning as a working feature. The corpus's
  only mention, in `notes/yamlpyowl.md`, says most OWL reasoners *do not support it*,
  which is why that tool generates proxy individuals instead. Rewritten to say that.
- **Closed-world assumption** — "Databases do this" is supported by no note. The corpus's
  actual closed-world exemplars are F-logic, SPIN constraints, and Palantir's Ontology.
- **Semantic layer** — "because a semantic layer cannot act" was the definition's own
  invention; `notes/palantir-ontology.md` reports Palantir's disclaimer and gives no reason
  for it.
- **Subsumption** — "computed rather than declared" is contradicted by `rdfs:subClassOf`
  being a declared term and by `notes/tawny-owl.md`'s asserted/inferred split. It is both.
- **TBox** — "class **and property** definitions" is contradicted by `notes/sparql-dl.md`,
  which separates TBox, RBox and ABox; property axioms are the RBox.
- **Torque** — dropped both load-bearing halves of the note's definition (the mismatch is
  with *the person's own account of themselves*, and *the system wins*). Restored.
- **Unique name assumption** — the `owl:sameAs` clause is supported by no note.
- **Object type** — "given behaviour" is wrong by `notes/palantir-ontology.md`'s own
  division: behaviour is kinetic (action types, functions), not semantic.

### The 181 truncated glossary definitions

Checked all 181, not a sample, with a throwaway script that put each generated first
sentence beside its full "What it is" text and flagged short definitions, abbreviation
splits, hard 260-character truncations, and negations stranded in the remainder. 40 pairs
came back flagged; reading them, 3 were real defects and 37 were first sentences that
stand alone correctly.

The three, all fixed by rewriting the note's opening sentence, never the generated output:

- `quine-ontological-commitment` — the glossary entry read **"W.V.O."** The sentence
  opened with the initials.
- `cyc-lenat-1995` — the entry read **"Douglas B."** Same cause.
- `shirky-ontology-is-overrated` — the opening sentence ended on a quotation mark, which
  the sentence regex walks past, so the entry hit the 260-character hard truncation
  mid-quote.

The script was a throwaway and is not kept: the defect class it finds is now visible in a
single re-run of the same twenty lines, and a permanent script would need maintaining for
a check that fires once.

## Task 3 — The ten transcripts

### What was checked

Every factual proposition in all ten files, against the source notes
`lectures/COURSE-PLAN.md` lists for that lecture. Qualitative, causal and comparative
claims were audited on the same footing as names, dates and numbers. Six of the ten
carry a full written audit in this directory (`audit-04.md` through `audit-08.md`,
`audit-10.md`), each with a Verified table of quoted spans, a Cut list with reasons, a
Corrected list, and a Narration-fixes list. Lectures 1, 2, 3 and 9 were audited and
repaired in the same pass without a separate brief.

Totals across the six briefs: 242 verified claims with quoted spans, 104 cuts, 85
corrections.

### The scale of the problem, by file

| Lecture | Words before | Words after | What drove the change |
| --- | ---: | ---: | --- |
| 04 Cyc | 2,899 | 1,748 | −40%. The worst file in the course. |
| 05 Semantic Web | 3,005 | 2,661 | −11% |
| 06 Machinery | 3,005 | 2,708 | −10% |
| 07 Building one | 2,906 | 2,941 | parity; ~700 words replaced |
| 08 Criticisms | 3,434 | 3,364 | −2% |
| 10 Politics | 2,789 | 2,806 | parity; cut then re-spent on sourced material |

**Lecture four was 40 percent invented.** Not embellished — invented. The entire
expert-systems opening (the commercial AI market of the early 1980s, the two walls, the
knowledge-acquisition bottleneck, the medical system reasoning about a decade-dead
patient), the entire KL-ONE and frames history (Minsky's Restaurant frame, Bill Woods's
1980 paper "What's in a Link?", KL-ONE's automatic classification), and the entire
KIF/Ontolingua section trace to nothing. Greps across `notes/` return **zero** hits for
KL-ONE, Minsky, Woods, KIF, and "Knowledge Interchange Format". The Cyc etymology
("from the middle of 'encyclopedia'") was stated as fact with no note behind it. One
invented item was appended to a list Lenat actually gives, and one invented property
("stable — it doesn't change when the vendor ships a new version") to a set of three the
note names exactly.

The other named fabrications, one per file, are in the briefs. The largest single one
outside lecture four is in lecture eight: **118 words putting an argument in Dave
McComb's mouth that he never makes** — a drug-interaction example, a "bounded domain"
defence, and a hundred-thousand-a-year volume claim, none of which appear in the capture
or the note. McComb's actual reply is that Shirky's own article is a syllogism. A further
passage then adjudicated the exchange that did not happen, and leaned on Shirky's "three
preconditions", which do not exist either (see Task 1, correction 3).

### Cross-file checks, which no per-file audit could do

These were run over the whole set after the per-file repairs landed.

**One seam, found and fixed.** Task 1 established that reading the standards stack as a
set of answers to the 2001 Scientific American article is this course's reconstruction
and not a documented chain of cause and effect, and lecture five gained an explicit
caveat saying so. Lecture six's opening still asserted the mapping flatly: "each layer
answers a requirement set out in the Scientific American article of two thousand and
one." Lecture six now carries the caveat forward.

**Back-references, all ten verified against the text of the lecture they cite.** Lecture
three's summary of two matches lecture two's closing; four's "at the end of the last one
I promised you the most expensive experiment" matches three's closing; five's
"military-funded programme about reuse" survives lecture four's 40% cut (ARPA and the
Knowledge Sharing Effort are both still there, now correctly attributed); seven's summary
of four, five and six is accurate; eight's "a governance body that happens to produce a
file" matches seven's closing; ten's summary of nine matches nine's closing. No lecture
credits an earlier one with material it does not contain.

**Endings.** Exactly one "claim to keep" per file, all ten at the end. No orphaned
mid-file closings survive — lecture four had three of them, all cut.

**Restated points.** Every sentence pair in every file was compared by four-word shingle
overlap. Three pairs came back above the threshold; reading them, all three are
deliberate callbacks (lecture four's closing restating its own definition, lecture six
reusing its worked flight example, lecture eight paying off the periodic-table example).
No splice-scars.

### Narration fixes applied in this pass

The per-file briefs each carry a narration list. These are the ones that only a
whole-corpus scan finds, all now fixed:

- **`W3C` written as an abbreviation** in lectures five and nine, eight occurrences.
  Spoken aloud that is "double-u three see". Now "W three C", matching lecture one.
- **`OWL 2` written with a digit** in lecture six, six occurrences, where lecture five
  already writes "OWL two".
- **Five years written as digits** in lecture eight (May 2001, 2005, 1999, November 2003,
  2015) where every other lecture spells them out.
- **OWL unexpanded on first use in lecture nine.** A listener starting at nine met "OWL"
  cold.
- **`AI` unexpanded on first use in lecture nine.** Now "artificial-intelligence agents".
- **`PKK` unexpanded in lecture ten.** Expanded to "the P-K-K, a banned militant Kurdish
  nationalist organisation" — the gloss is the capture's own wording
  (`research/exa/palantir-crit.json`), not general knowledge supplied from memory.

A full scan confirms zero markdown, zero headings, zero bullets, zero code fences, zero
spoken URLs and zero remaining digits across all ten files.

### No new notes were created

Every claim that traced to nothing was cut rather than promoted to a note. The judgement
in each case: the material was fabricated detail dressed as history (lecture four's
KL-ONE and expert-systems sections, lecture eight's McComb argument), not a real gap in
the corpus. Creating notes would have meant sourcing claims that were invented in the
first place. The corpus count is therefore unchanged at 181 notes, and the hard-coded
counts in `tests/` did not need updating for this task.

### What could not be verified

- **Lecture four's Cyc etymology.** "Cyc, from the middle of 'encyclopedia'" is very
  probably true and is not in any note or capture. Cut rather than kept, per the rule.
  Re-sourcing it was not attempted because it carries no weight in the argument.
- **Lecture eight's Aaron Swartz block** (~330 words) was cut for structure rather than
  for grounding — it is fully sourced in `notes/semantic-web-retrospective.md`. It is
  reinstatable verbatim and `audit-08.md` says so.
- Each brief ends with a **"Depth still available"** section listing grounded material
  the lecture does not yet use. That is the input to Task 5, and it is evidence that the
  cuts were not the notes running dry.

---

## Task 5 — Depth

Done in a separate session after the audit pass. The audit cut ungrounded material;
this task spends what the notes still hold. The input was the "Depth still available"
section each per-file brief ends with — a quoted inventory of grounded material the
transcript did not use — plus, for the four lectures with no brief, an inventory built
from scratch against the notes `COURSE-PLAN.md` lists.

The rule was unchanged: every added proposition traces to a span in a note listed for
that lecture. Nothing was added from general knowledge, and nothing was added because a
file looked short.

### What shipped, by file

| Lecture | Before | After | Change | Principal sources drawn on |
| --- | ---: | ---: | ---: | --- |
| 01 Three things people mean | 2,699 | 3,143 | +444 | `skos-simple-knowledge-organization-system`, `scigraph`, `SYNTHESIS.md` |
| 02 Aristotle to Wolff | 2,815 | 2,815 | 0 | unchanged — see below |
| 03 Quine | 2,526 | 3,091 | +565 | `ontology-matching`, `alignment-api` |
| 04 Cyc | 2,192 | 2,780 | +588 | `description-logics-dls`, `gruber-ontology-definition`, `cyc-lenat-1995` |
| 05 Semantic Web | 2,669 | 3,913 | +1,244 | `sparql-1-1`, `json-ld`, `rdf-schema-rdfs-1-1`, `shacl-...`, `semantic-web-2001-vision` |
| 06 Machinery | 2,735 | 4,055 | +1,320 | `dl-query-class-expression`, `openllet`, `hermit`, `elk`, `owl-2-...` |
| 07 Building one | 2,941 | 3,986 | +1,045 | `gufo`, `common-core-ontologies-cco`, `ontologydesignpatterns-org`, `elot`, `logmap` |
| 08 Criticisms | 3,377 | 4,416 | +1,039 | `shirky-ontology-is-overrated`, `bowker-star-sorting-things-out`, `doctorow-metacrap`, `semantic-web-retrospective` |
| 09 Palantir | 3,103 | 4,140 | +1,037 | `palantir-ontology`, `shacl-shapes-constraint-language`, `owl-2-...` |
| 10 Politics and next | 2,812 | 3,751 | +939 | `palantir-ontology-critique`, `bowker-star-...`, `llm-ontology-debate`, `ontolearner`, `elot` |
| **Total** | **27,869** | **36,090** | **+8,221** | |

Course duration: two hours forty at one hundred and forty-five words per minute before,
four hours nine after. Under the five-hour soft ceiling.

### The largest single additions

- **Lecture six** gained the most because one of its listed sources,
  `notes/dl-query-class-expression.md`, was used nowhere in the course. It now supports a
  whole beat on interrogating a classified ontology and two sourced failure modes for the
  "why is nothing coming back" case. It also gained relation checking, which
  `description-logics-dls.md` names as a fourth inference task and the lecture omitted;
  a sourced unintended-entailment example from `openllet.md` replacing an illustrative
  one; and a short honest beat on version compatibility as the day-to-day cost of the
  stack, from `elk`, `hermit` and `openllet`.
- **Lecture nine** gained the action and function model the goal specifically flagged as
  under-served: action types as rules, parameters and submission criteria; functions as
  business logic of arbitrary complexity under a fixed permissioned surface; Palantir's
  own anti-retrieval-augmented-generation positioning and its "tool factory" framing. It
  also gained the caveat that Palantir's documentation never mentions OWL, RDF, the W3C,
  reasoners or world assumptions, so the head-to-head comparison is the lecturer's and not
  Palantir's — the lecture previously ran that comparison with no such disclaimer.
  `notes/shacl-shapes-constraint-language.md` was a listed source used zero times; it now
  carries the SHACL objection and the answer to it.
- **Lecture eight** gained Shirky's positive programme, which the lecture omitted
  entirely: links and tags, the ISBN and the web address as unique labels that let
  libraries merge without merging their categorisation schemes, and tags as value
  produced by forgoing classification. Also Helmreich's apartheid reclassification case in
  full rather than gestured at, the voodoo-categorisation argument as the bridge into
  Bowker and Star, Doctorow's language-model payoff, and the Schema.org sequencing lesson.
- **Lecture five** gained the incentive objection from `semantic-web-2001-vision.md` —
  the hinge of lecture eight, deliberately stated here and deferred there — plus SPARQL's
  security surface, the two RDFS traps, and the JSON-LD mechanism and adoption list.

### Lecture two, unchanged

Lecture two was re-expanded in the previous session from `ontology-word-history.md`,
`bfo-basic-formal-ontology.md` and `common-core-ontologies-cco.md`, and that work is the
first commit of this session. Its notes are the thinnest in the course: the word-history
note is the only substantial one, and the two upper-ontology notes serve lecture seven's
purposes, not lecture two's. Nothing further was added, because nothing further was
there. Leaving it at nineteen minutes is the correct outcome, not a gap.

### One grounding error found and fixed

Lecture one attributed "the objects, concepts, and other entities that are presumed to
exist in some area of interest" to Genesereth and Nilsson. `notes/gruber-ontology-definition.md`
says otherwise: "That wording is Gruber's own 2009 restatement; Genesereth and Nilsson's
original says 'assumed to exist.'" Lecture one now says the quoted wording is Gruber's
restatement, and lecture four's new passage on the two wordings refers back to that
correctly rather than correcting a claim the file no longer makes.

### Material deliberately left unused

Not everything in the depth inventories was spendable. The recurring reasons:

- **Unspeakable as narration.** API identifiers, `AutoRetrieverLearner(batch_size=...)`,
  Hit@K and MRR, format lists, media types. The narration bans code, and spelling them
  out buys a listener nothing.
- **Would need an expansion no note supplies.** ISO 23726-3, ODPA, NeOn, CURIE,
  Notation3. Expanding an acronym from memory is the exact failure this review exists to
  prevent, so those items were dropped rather than glossed.
- **Belongs to another lecture.** TBox and ABox, the open-world assumption and the four
  inference tasks were left out of lecture four because lecture six's claim to retain is
  built on them. The Genesereth and Nilsson conceptualization material stayed in lecture
  one. Alignment tooling stayed in lecture seven, not lecture three.
- **Would re-create a seam the audit cut.** The Aaron Swartz block and the
  agent-layer-centralisation point were both left out of lecture eight: the first is
  lecture five's subject, the second is a fourth kind of failure landing immediately
  before a close whose claim is "three critiques, three layers."
- **Tool trivia.** WIDOCO's local-filesystem section trap, ROBOT's PowerShell
  byte-order-mark warning, LogMap's format list, OBO Foundry's catalog export formats.
  Grounded, but no argumentative payload.

### Narration constraints re-verified after the pass

A scan across all ten files confirms: zero digits, zero markdown, zero headings, zero
bullets, zero code, zero URLs, exactly one closing claim per file, and every file still
opening with `Lecture <Number>.`. Acronyms introduced by the new material are expanded on
first use in their own file — ISBN in lecture eight, CRUD in lecture one, the Resource
Description Framework and the Shapes Constraint Language in lecture nine, retrieval-augmented
generation written out rather than initialised in lectures nine and ten.

`lectures/COURSE-PLAN.md` was updated in the same task: the 2,700 to 3,100 word band is
gone, replaced by a table of shipped counts and the true total duration. The plan and the
transcripts now agree.
