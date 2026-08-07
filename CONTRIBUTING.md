# Contributing

Contributions are welcome when they preserve the knowledge base's source trail.

## Notes

Every noted manifest entry has one `notes/<slug>.md` file with all six fields: **What it is**, **Key concepts**, **How you'd use it**, **LLM angle**, **Pitfalls & lessons**, and **Verdict**. Ground every factual claim in the upstream material named under `Sources consulted`; write `none stated` rather than filling a gap from general knowledge. Preserve version, maintenance, scope, and evidence limitations.

After editing notes or manifest records, regenerate and validate:

```sh
python3 scripts/rebuild_index.py
python3 scripts/check.py
python3 -m unittest discover -s tests -v
```

Raw captures under `sources/` and cloned repositories under `repos/` are intentionally not distributed. A contribution must remain reviewable through its public upstream URL.

## Ontology Chat

Keep the retrieval CLI dependency-free and deterministic. New behavior should include tests. Skill answers must cite opened notes, distinguish source claims from editorial recommendations, and abstain when the corpus has no evidence. Validate the skill metadata with a YAML parser before submitting.

## Licensing

By contributing code, you agree to license it under MIT. By contributing knowledge-base content or documentation, you agree to license it under CC BY 4.0. Do not submit material you do not have permission to redistribute.
