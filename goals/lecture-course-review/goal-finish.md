# Goal: Finish the review run — Task 5 depth and the Done-means checklist

Working directory: the repository root. This is a continuation with a fresh
session. A previous run executed `goals/lecture-course-review/goal.md` — read
it first; every rule in it still binds, especially: every factual proposition
in a transcript must trace to a note in `notes/`, quality over length, do not
pad, never edit anything under `site/src` or `site/book` (generated).

## State you are inheriting

- Tasks 1–4 of the original goal are DONE and committed locally: four commits
  on `main` ahead of `origin/main`. Do not redo them. Their record is in
  `goals/lecture-course-review/CHANGES.md` and `EVIDENCE.md`.
- Task 5 (depth) is HALF-DONE. The transcript audit cut ungrounded material
  (lecture four lost its invented KL-ONE/KIF history and is now ~2,200 words).
  The previous session re-expanded lectures 02 and 04 partway and died;
  their current working-tree state is coherent but uncommitted.
- `goals/lecture-course-review/run.log` shows as a staged deletion — keep the
  deletion; the log does not belong in the repo.
- The previous session kept crashing on auto-compaction; that is why you are
  a fresh session. Work in small commits so a crash loses little.

## Task 5, remaining

For each lecture whose source notes (listed in `lectures/COURSE-PLAN.md`)
contain substantive material the transcript does not yet use, extend it with
that material. Quality is the target, length a by-product; five hours total is
a soft ceiling, no floor; a lecture whose notes are exhausted stays as it is.
Every added proposition must trace to a note. Respect the narration
constraints: no markdown, no bullets, no URLs, acronyms expanded on first use
per file, one closing claim per file.

Lecture four especially: it is the shortest after the cuts. Its grounded
sources are `notes/cyc-lenat-1995.md` and `notes/gruber-ontology-definition.md`
plus whatever else COURSE-PLAN lists — use their unexploited depth.

Commit per lecture or per small batch. When done, update
`lectures/COURSE-PLAN.md` so per-lecture word counts and the total duration
match what shipped.

## Done-means checklist (all required)

1. `uvx pytest tests -q` passes.
2. `python3 skills/ontology-chat/scripts/ontology_kb.py status` reports healthy.
3. `python3 scripts/build_site.py && ~/.local/bin/mdbook build site` succeeds.
4. `python3 scripts/checklinks.py site/book` exits 0.
5. Deploy: `wrangler pages deploy site/book --project-name ontology-course --branch main --commit-dirty=true`.
6. Verify with `curl -sL -o /dev/null -w '%{http_code} %{content_type}'`:
   `https://ontology-course.pages.dev/`, `/glossary`, `/lectures/`,
   `/synthesis` → 200 `text/html`; all ten
   `/lectures/transcripts/<slug>.txt` → 200 `text/plain`, body starting
   `Lecture <Number>.`
7. Append a Task 5 section to `goals/lecture-course-review/CHANGES.md`: which
   lectures grew, by how much, from which notes; which stayed and why. Update
   `EVIDENCE.md` if you added grounded claims worth recording.
8. Commit everything (stage goal artifacts with
   `git add -f goals/lecture-course-review/`) and push ALL local commits to
   `origin main`.
