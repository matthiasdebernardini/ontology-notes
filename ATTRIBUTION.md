# Attribution and methodology

## Preferred attribution

When redistributing or adapting the knowledge-base content, a suitable credit
is:

> Ontology Notes contributors, *Ontology Notes Knowledge Base*, licensed under
> CC BY 4.0. Changes were made.

If no changes were made, omit “Changes were made.” Include the canonical repository URL: https://github.com/matthiasdebernardini/ontology-notes. Attribution may be
provided in a README, credits page, bibliography, or other location reasonable
for the medium. See `LICENSE-CC-BY-4.0` for the controlling license terms.

## Upstream curated inventory

The seed inventory `README.awesome-ontology.md` comes from [ozekik/awesome-ontology](https://github.com/ozekik/awesome-ontology), curated by its contributors and distributed under the Creative Commons Attribution 4.0 International license. This project parsed, classified, and expanded that inventory; it is not an official upstream release.

## What the attribution covers

CC BY 4.0 applies to the original summaries, synthesis, indexes, inventory, and
project documentation identified in `README.md`. The MIT license applies to the
code and agent tooling. Merely naming or linking an upstream project does not
change that project's license, and third-party quotations, trademarks,
standards text, linked pages, and repository contents remain subject to their
respective owners' rights.

Individual notes retain source URLs so readers can credit and verify the
underlying projects as appropriate. This project is not affiliated with or
endorsed by those projects, standards bodies, or authors.

## Methodology

1. The curated `README.awesome-ontology.md` inventory was normalized into the
   188-entry `manifest.json` harvest ledger.
2. Eligible repositories, specifications, papers, and project sites were read
   from their upstream materials.
3. Findings were summarized into 168 structured Markdown notes under `notes/`.
   Twenty entries that could not or should not be summarized remain visible in
   the manifest with skip reasons.
4. The structured note fields were assembled into `NOTE_INDEX.json` for local
   retrieval, and recurring themes were connected in `SYNTHESIS.md`.
5. Repository-relative note citations and upstream URLs provide an audit trail;
   readers should confirm consequential claims against current primary sources.

The notes are selective research summaries, not mirrors of upstream works and
not substitutes for normative specifications. Corrections should preserve the
source trail and distinguish sourced facts from editorial synthesis.
