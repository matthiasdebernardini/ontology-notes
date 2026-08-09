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
