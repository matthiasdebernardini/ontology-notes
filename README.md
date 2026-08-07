# Ontology Notes

A citation-oriented knowledge base for ontology engineering, Semantic Web
standards, knowledge graphs, reasoners, editors, vocabularies, and related
tooling.

The harvest inventory contains **188 entries**. Of those, **168 have structured
notes** and **20 are retained as skipped entries with reasons**, so the corpus is
both useful and auditable rather than silently incomplete.

## What is included

| Path | Purpose |
| --- | --- |
| `notes/` | 168 human-readable Markdown knowledge notes |
| `NOTE_INDEX.json` | Machine-readable index of the same 168 notes |
| `SYNTHESIS.md` | Cross-source explanation of the ontology ecosystem |
| `manifest.json` | The full 188-entry harvest ledger, including skipped items |
| `README.awesome-ontology.md` | Curated source inventory grouped by topic |
| `skills/ontology-chat/` | Agent skill and dependency-free knowledge-base query CLI |
| `scripts/install.py` | Safe local skill installer |

Generated knowledge artifacts (`notes/`, `NOTE_INDEX.json`, and
`SYNTHESIS.md`) are intentionally part of the distributable repository. Raw
source captures and cloned upstream repositories are not.

## Ontology Chat skill

`ontology-chat` gives a compatible agent a local, structured way to answer
questions from this corpus. It uses the note index to discover relevant
entries, reads the underlying notes for evidence, and cites repository-relative
paths in its answer. It is suited to questions such as:

- How do RDF, RDFS, OWL, SHACL, and SKOS differ?
- Which ontology editor or reasoner fits a particular workflow?
- Compare two vocabularies, tools, or upper ontologies.
- Trace a claim back to the notes and their source URLs.

The corpus is local and inspectable. The skill should say when the available
notes do not support a claim rather than presenting the repository as an
exhaustive or current catalog.

The skill's dependency-free CLI can also be used directly:

```sh
python3 skills/ontology-chat/scripts/ontology_kb.py status
python3 skills/ontology-chat/scripts/ontology_kb.py search "ontology alignment" -n 5
python3 skills/ontology-chat/scripts/ontology_kb.py show owl-2-web-ontology-language
python3 skills/ontology-chat/scripts/ontology_kb.py related protege -n 5
python3 skills/ontology-chat/scripts/ontology_kb.py --json sources protege
```

Available commands are `status`, `search`, `show`, `related`, and `sources`.
Pass `--json` for structured output or `--root PATH` to select a different
checkout. Root discovery otherwise checks `ONTOLOGY_KB_ROOT`, the installed
user config, and then ancestors of the current directory.

## Query without installing

The bundled retrieval CLI has no third-party dependencies:

```sh
python3 skills/ontology-chat/scripts/ontology_kb.py search "How do ontologies and LLMs work together?" --limit 8
python3 skills/ontology-chat/scripts/ontology_kb.py show ontolearner
python3 skills/ontology-chat/scripts/ontology_kb.py status
```

Add `--json` for agent-friendly output. The CLI also provides `related` and `sources` commands.

## Install the skill

Python 3 is the only requirement. Preview the installation first:

```sh
python3 scripts/install.py --dry-run
```

Install with the default symlink mode:

```sh
python3 scripts/install.py
```

This links `skills/ontology-chat` to
`~/.agents/skills/ontology-chat` and records the absolute knowledge-base root
in `~/.config/ontology-chat/config.json`. To install a standalone copy instead:

```sh
python3 scripts/install.py --copy
```

If a conflicting target or knowledge-base root already exists, the installer
stops. Re-run with `--force` only after reviewing the dry-run plan. Anything it
replaces is first moved or copied to a timestamped backup; the installer never
deletes an existing skill or configuration.

```sh
python3 scripts/install.py --dry-run --force
python3 scripts/install.py --force
```

Run `python3 scripts/install.py --help` for all options.

## Uninstall safely

The following commands are instructions only; the installer does not run them.
They disable the installed skill and configuration by moving them to timestamped
backup names instead of deleting them:

```sh
mv "$HOME/.agents/skills/ontology-chat" "$HOME/.agents/skills/ontology-chat.uninstalled-$(date -u +%Y%m%dT%H%M%SZ)"
mv "$HOME/.config/ontology-chat" "$HOME/.config/ontology-chat.uninstalled-$(date -u +%Y%m%dT%H%M%SZ)"
```

If either path does not exist, skip that command. To roll back a forced install,
move the relevant timestamped `.backup-*` path back into place after first
moving the current path aside.

## Method and limitations

The corpus began with the curated inventory in `README.awesome-ontology.md`.
Each eligible entry was reviewed against its upstream repository,
specification, paper, or project site and summarized into a structured note.
`manifest.json` records harvest status; `NOTE_INDEX.json` makes note fields
searchable; and `SYNTHESIS.md` connects recurring concepts across sources.
See [ATTRIBUTION.md](ATTRIBUTION.md) for provenance and reuse guidance.

These notes are research aids, not standards text. Projects evolve, upstream
pages can disappear, and a summary can omit nuance. Follow the source URLs in a
note and consult the current normative specification before making production,
legal, clinical, or safety-critical decisions.

## Licensing

This repository is dual-licensed by file type:

- **Code and agent tooling** (`scripts/`, `skills/`, and tests): MIT; see
  [LICENSE-MIT](LICENSE-MIT).
- **Knowledge-base and project documentation** (`notes/`, `NOTE_INDEX.json`,
  `SYNTHESIS.md`, `manifest.json`, `README.awesome-ontology.md`, `README.md`,
  and `ATTRIBUTION.md`): Creative Commons Attribution 4.0 International; see
  [LICENSE-CC-BY-4.0](LICENSE-CC-BY-4.0).

Third-party names, quotations, specifications, and linked materials remain
subject to their respective owners' rights and licenses.
