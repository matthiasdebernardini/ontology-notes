# Goal: Verify and repair the lecture course, the added notes, and the published book

Working directory: the repository root. Read `goals/ontology-harvest/goal.md`
and `goals/ontology-harvest-fixes/goal.md` first — their rules still bind.
Above all: every claim in this repository must be grounded in a source this
repository actually holds. Nothing is asserted because it sounds right.

A previous agent (Claude) did four things in one session, without an
independent review of any of them:

1. Added 13 notes covering history, criticism, and Palantir — gaps the
   original harvest left. Reconciled `NOTE_INDEX.json` (181) and
   `manifest.json` (201), updated the hard-coded counts in `tests/`.
2. Added four sections to `SYNTHESIS.md`.
3. Wrote ten lecture transcripts in `lectures/transcripts/`, then extended
   every one of them in a second pass because the first draft ran short.
4. Wrote `scripts/build_site.py`, which generates an mdBook source tree, and
   published the result to Cloudflare Pages at https://ontology-course.pages.dev.

Your job is to check all of it and fix what is wrong. Assume errors exist.
Finding none in a section is a claim you must earn — record what you verified,
not only what you cut, or "no errors found" is indistinguishable from "did not
look".

## Git

`goals/`, `research/`, and `sources/` are gitignored. Your deliverables in
`goals/lecture-course-review/` must still be committed: stage them with
`git add -f goals/lecture-course-review/`. Because `research/` and `sources/`
do not survive a clone, every grounding verdict in the evidence map must quote
the supporting span, not merely point at a local file.

## Environment

- `mdbook` is at `~/.local/bin/mdbook` (v0.5.4). Build: `~/.local/bin/mdbook build site`.
- Regenerate the site source first: `python3 scripts/build_site.py`. Everything
  under `site/src` and `site/book` is generated and gitignored. Never edit it —
  edit the notes, the transcripts, or the generator.
- Tests: `uvx pytest tests -q` (pytest is not installed globally).
- Corpus health: `python3 skills/ontology-chat/scripts/ontology_kb.py status`.
- Deploy: `wrangler pages deploy site/book --project-name ontology-course --branch main --commit-dirty=true`.
  Wrangler is authenticated. Deploy only after the checks below pass.
- `research/` holds the raw captures behind the 13 new notes: `research/exa/*.json`
  are search results, `research/firecrawl/*.md` are scraped pages. Like
  `sources/`, it is gitignored and local-only. It is your evidence base.

## The 13 notes under review

`ontology-word-history`, `quine-ontological-commitment`,
`gruber-ontology-definition`, `cyc-lenat-1995`, `semantic-web-2001-vision`,
`semantic-web-retrospective`, `knowledge-graph-turn`, `doctorow-metacrap`,
`shirky-ontology-is-overrated`, `bowker-star-sorting-things-out`,
`palantir-ontology`, `palantir-ontology-critique`, `llm-ontology-debate`.

## Task 1 — Ground the new notes

The captures are not one-to-one with the notes: 36 files in
`research/firecrawl/` plus two Bowker and Star reviews in
`research/.firecrawl/` back 13 notes, several notes cite multiple URLs, and
some cited URLs have no capture. Start by building an evidence map at
`goals/lecture-course-review/EVIDENCE.md`: one row per (note, cited URL) pair,
with the capture file that holds it, the scrape status, and — as you audit —
the span that supports each load-bearing claim, quoted. A URL with no capture
means the claim citing it is unverified until you re-fetch or re-source it.

Then check every factual claim in each of the 13 notes against its mapped
capture. Three scrapes failed during the original run (Sowa's Cyc review, one
Temple PDF, one Bowker and Star review returned 403). Any claim that traces
only to a failed scrape is unsupported — cut it or re-source it.

Watch for: dates, first-publication claims, attributions of coinage, numeric
claims (Cyc's axiom count, Wikidata's size), and any sentence that reads as
common knowledge rather than as something a specific source said. Verify the
six-field template holds and that `## Sources consulted` lists real URLs.

Where a claim is right but the note does not say who said it, add the
attribution. Where a claim cannot be supported, cut it rather than soften it.

## Task 2 — Check the SYNTHESIS additions

Four sections were added: "Where the idea came from", "Criticism worth
answering", "Operational ontologies: the other tradition", "Ontologies after
large language models". Every citation must be a `notes/<slug>.md` path that
exists and that states the claim attributed to it. The existing invariant.

## Task 3 — Audit the transcripts

This is where the risk concentrates, because the transcripts were written
fast and then extended by a second pass that inserted material before each
closing line.

Check each of the ten files for:

- **Claims that trace to nothing.** The unit of audit is the factual
  proposition, not just names, dates, and numbers: qualitative, causal, and
  comparative claims ("X failed because Y", "most deployments use Z") need
  grounding too. Every factual paragraph must map to one of the lecture's
  listed source notes in `lectures/COURSE-PLAN.md`. Anything that traces to no
  note is either wrong or is a note that should exist — decide which. If you
  create a note, create ALL of its machinery: the note file with the six
  fields, its `manifest.json` record with status `noted`, its `NOTE_INDEX.json`
  entry, a stored source capture, and the updated hard-coded counts in
  `tests/`. A note without its index and manifest records breaks the corpus
  invariants.
- **Seams.** The extension pass spliced new segments in. Read for abrupt
  transitions, restated points, and contradictions between the original and
  the added material.
- **Endings.** Each file states one claim to retain, once, at the end. Confirm
  no file has two closings or an orphaned closing line mid-file.
- **Narration constraints.** No markdown, no headings, no bullets, no code, no
  URLs spoken aloud. Acronyms expanded on first use *in every file*, because a
  listener may start anywhere. Numbers and Latin written as spoken.
- **Continuity.** Each opens by saying where it sits in the arc. Check the
  back-references are accurate: lecture six should not claim lecture five
  covered something it did not.

Read them as a listener on a walk, not as a reader. Sentences that need
re-reading are defects here.

## Task 4 — Audit the site generator

`scripts/build_site.py` is the only hand-written code added. Check that:

- It is deterministic and safe to re-run. It deletes `site/src` on each run —
  confirm nothing hand-written can end up there and be lost.
- `SUMMARY.md` covers every generated page, with no orphans and no drafts
  pointing at missing files.
- Internal links resolve. Write a link checker over the built HTML in
  `site/book` and leave it at `scripts/checklinks.py` (tracked, so it survives
  the push and future builds can reuse it). It must: check every local `href`
  and `src` (relative and root-relative) including URL-encoded paths and the
  raw `.txt` paths; check `#fragment` targets against the anchors in the
  destination page; skip external `http(s)` links; exit nonzero on any broken
  link. mdBook does not check links.
- The 26 hand-written glossary definitions in `CONCEPTS` inside
  `scripts/build_site.py` were written from memory — the least-verified prose
  in the repository, and currently exempt from the grounding rule everything
  else obeys. Fix that: for each definition, either cite a note that states it
  (add the pairing to the evidence map) or rewrite it from a note's own text.
  A definition no note supports gets corrected or cut.
- The other 181 glossary entries truncate each note's "What it is" field to
  its first sentence. Check all 181, not a sample — it is mechanical, so
  script it: extract each generated definition, put it beside its full field
  text, and read the pairs for truncations that invert or strand a meaning
  (a first sentence that is pure throat-clearing, a negation split from its
  clause). Fix by improving the note's opening sentence, never by hand-editing
  generated output.

## Task 5 — Depth

The ten lectures total roughly 29,000 words, about three hours twenty at 145
words per minute. `lectures/COURSE-PLAN.md` currently specifies 2,700 to 3,100
words per lecture. That cap is hereby lifted: **quality is the target, length
is a by-product.** The user has said explicitly that lectures running long is
fine; five hours total is a soft ceiling, not a quota, and there is no floor.

Extend each lecture exactly as far as its source notes carry it and no
further: depth on the reasoning services, on ontology alignment, on the
upper-ontology disagreements, on the Palantir action and function model, on
the Bowker and Star cases. Do not pad, do not restate, do not add a lecture
that has no notes behind it. A lecture left at its current length because its
notes are exhausted is a correct outcome — say so in the run log.

Update `lectures/COURSE-PLAN.md` in the same task so the stated per-lecture
word range and total duration match what you actually shipped. The plan and
the transcripts must not disagree.

Do this last. If Tasks 1 to 4 consume the run, stop after Task 4 — a corrected
three-hour course beats an unverified five-hour one.

## Done means

Two completion states. Both require every numbered item below.

**Partial (Tasks 1–4 done, Task 5 not attempted or unfinished):** legitimate.
Deploy the corrected site — deployment is required after Task 4, not deferred
to Task 5 — and say in the run log that Task 5 was not done and why.

**Full:** Task 5 shipped, `COURSE-PLAN.md` updated to match, site redeployed
after it.

1. `uvx pytest tests -q` passes, with the hard-coded note counts updated if the
   count changed.
2. `ontology_kb.py status` reports healthy: indexed notes equal manifest
   `noted` entries, no orphans, no unindexed notes.
3. `python3 scripts/build_site.py && ~/.local/bin/mdbook build site` succeeds.
4. `python3 scripts/checklinks.py site/book` exits 0.
5. After deploy, every URL below returns HTTP 200 after redirects with the
   named content type (`curl -sL -o /dev/null -w '%{http_code} %{content_type}'`):
   - `https://ontology-course.pages.dev/` — `text/html`
   - `https://ontology-course.pages.dev/glossary` — `text/html`
   - `https://ontology-course.pages.dev/lectures/` — `text/html`
   - `https://ontology-course.pages.dev/synthesis` — `text/html`
   - all ten `https://ontology-course.pages.dev/lectures/transcripts/<slug>.txt`
     — `text/plain`, and the body starts with `Lecture <Number>.`
6. The evidence map at `goals/lecture-course-review/EVIDENCE.md` covers all 13
   notes and all 26 CONCEPTS definitions, with quoted spans for the
   load-bearing claims — verified rows included, not only cuts.
7. A run log at `goals/lecture-course-review/CHANGES.md`: per task, what you
   checked, what you changed, what you could not verify and why. List every
   claim you cut and the reason. An honest list of unverifiable claims is
   worth more than a clean report. Both files committed via
   `git add -f goals/lecture-course-review/`.
8. One commit per task, pushed to `main` on
   https://github.com/matthiasdebernardini/ontology-notes.
