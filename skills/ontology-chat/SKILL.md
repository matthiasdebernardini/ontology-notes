---
name: ontology-chat
description: >-
  Chat with the source-grounded awesome-ontology knowledge base: explain ontology concepts, compare standards/upper ontologies/tools, recommend workflows, explore LLM+ontology patterns, trace claims to sources, and build a reading path. Use this whenever the user asks about ontologies, RDF/OWL/SKOS/SHACL, knowledge graphs, ontology tooling or reasoners, ontology alignment, ontology learning, or combining ontologies with LLMs—even if they do not explicitly say “use the knowledge base.”
compatibility: Requires Python 3.10+ and an ontology-notes checkout containing manifest.json, NOTE_INDEX.json, notes/, and SYNTHESIS.md.
---

# Ontology Chat

Answer from the local ontology knowledge base rather than from memory.

## Locate the knowledge base

Resolve `scripts/ontology_kb.py` relative to this `SKILL.md`. The CLI locates the knowledge-base root in this order:

1. An explicit `--root PATH`
2. `ONTOLOGY_KB_ROOT`
3. `~/.config/ontology-chat/config.json`
4. The current directory and its parents
5. The skill source directory and its parents

If discovery fails, explain how to run the repository's `scripts/install.py` or set `ONTOLOGY_KB_ROOT`. Do not silently answer from prior knowledge.

Start unfamiliar sessions with:

```text
python3 <skill-dir>/scripts/ontology_kb.py status --json
```

## Choose the response mode

Infer the mode from the question:

- **Explain:** define a concept and connect it to concrete standards or projects.
- **Compare:** retrieve evidence for every compared item and state differences dimension by dimension.
- **Recommend:** derive criteria from the notes, present tradeoffs, and label the final recommendation as editorial.
- **How-to:** assemble a grounded workflow from documented tools and formats.
- **LLM patterns:** distinguish direct LLM implementations from catalog mentions, classical ML, embeddings, and generic knowledge-graph use.
- **Source audit:** trace a claim from synthesis to notes and, when locally available, to fetched text or repository documentation.
- **Learning path:** order readings from foundational concepts to tools and advanced patterns.
- **Explore:** surface related entries, sections, caveats, and follow-up questions.

## Retrieval workflow

1. Identify any explicitly named project, standard, ontology, or vocabulary. Run `sources <name> --json` first so skipped entries and recorded evidence gaps are visible before broader search. If it is skipped, lead with that limitation; indirect mentions in other notes may be summarized only as secondary evidence.
2. Turn the remaining question into two to four short, concrete search queries. Include the names of compared items when known.
3. Run retrieval for each query:

```text
python3 <skill-dir>/scripts/ontology_kb.py search "<query>" --limit 8 --json
```

Useful filters are `--section` and `--kind`.
4. Merge the results and open the best four to eight `notes/<slug>.md` files. Do not treat snippets as sufficient evidence.
5. For comparisons, ensure every named item has its own note. Use `show <slug>` if retrieval did not surface it.
6. Read `SYNTHESIS.md` only for orientation and cross-source structure. Verify its claims against the cited notes before repeating them.
7. For a disputed, surprising, or source-audit claim, run `sources <slug> --json`. If `sources/<slug>.txt` or `repos/<slug>/` is present, inspect the relevant source passage or README/docs. Public installations may omit these third-party artifacts; disclose that limitation instead of improvising.
8. Use `related <slug> --limit 8 --json` only after identifying a useful anchor note.

## Grounding rules

- Base factual claims on opened notes. Never fill a gap from general ontology knowledge.
- Cite every substantive paragraph or bullet with repository-relative Markdown links such as `[OntoLearner](notes/ontolearner.md)`.
- Attribute a source-specific claim to that source. Use multiple citations for cross-source conclusions.
- Explicitly label advice assembled from evidence as **Recommendation** or **Editorial synthesis**.
- Preserve qualifications including version age, archived status, incomplete documentation, profile limits, scaling limits, and catalog-only evidence.
- Do not turn “a guide is listed” into evidence of the guide's contents.
- Do not call ordinary knowledge graphs, embeddings, symbolic reasoning, or classical ML “LLM integration.”
- If an explicitly named entry is skipped, say so at the start and quote or closely paraphrase its recorded `skip_reason`. Do not substitute indirect mentions for a nonexistent dedicated note or fabricate its contents.
- If the knowledge base does not support the answer, say so and name the missing evidence.

## Default answer shape

Use the lightest structure that fits:

1. Direct answer
2. Evidence-backed explanation or comparison
3. Important caveats
4. Optional next question or reading suggestion

Avoid dumping retrieval scores or internal search steps unless the user asks for an audit. Prefer a small number of strong citations over a long bibliography.

## CLI reference

```text
ontology_kb.py search <query> [--limit N] [--section TEXT] [--kind KIND] [--json]
ontology_kb.py show <slug-or-name> [--json]
ontology_kb.py related <slug-or-name> [--limit N] [--json]
ontology_kb.py sources <slug-or-name> [--json]
ontology_kb.py status [--json]
```

Options may appear before or after the subcommand. The CLI is deterministic, dependency-free, and performs no network requests.
