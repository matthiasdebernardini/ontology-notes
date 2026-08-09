# Criticism of Operational Ontologies (Palantir)

**What it is**
The research and legal record on what happens when a vendor ontology is installed inside a state institution. The most direct study is Galis and Karlsson's 2024 paper on POL-INTEL, the Danish police's customisation of Palantir's Gotham, based on interviews with Palantir engineers and police-officer users.

**Key concepts**
- **Ontology in two senses at once.** The authors are explicit that they mean both the philosophical sense and the computer-science sense of a centralised concept repository, and that the two cannot be separated in practice.
- **The ontology is political.** They argue POL-INTEL's ontology is articulated by an assemblage of data, ideological positions, and economic concerns, translated into the Danish context. Platforms "not only describe the world but also enact it."
- **The getaway-vehicle example.** A car's record is mirrored from the Motor Vehicle registry. Inside the platform, viewed by an officer applying filters, it is potentially seen as a getaway vehicle. The category is produced by the interplay of the platform's concepts and the officer's analytical role, not by the registry.
- **Platformisation redistributes skill.** The paper reports new distributions of capability between the platform and the officer, with consequences for organisational life and accountability.
- **The German constitutional ruling.** In February 2023 the Bundesverfassungsgericht struck down Hamburg's automated-data-analysis law, and a similar Hesse law, as unconstitutional, and issued the first strict guidelines on how tools such as Palantir's may be used by police. The court warned against including bystander data — witnesses, lawyers — and said the laws let police "with just one click, create comprehensive profiles of persons." One of the eleven claimants was a Hamburg defence lawyer whose contacts include her clients.

**How you'd use it**
Use this as the applied version of Bowker and Star. Their torque concept becomes concrete when the classification is enforced by a state platform: the residual categories, the link types that make two people related, and the thresholds inside a function are policy choices with legal consequences, made by engineers. When reviewing an operational ontology, ask which object and link types create legal exposure, whose data enters as a by-product of proximity rather than suspicion, and whether an action's audit trail can reconstruct why a person was surfaced.

**LLM angle**
Adding agents that both query the ontology and invoke its actions increases the volume of decisions taken through these categories, and the governance and audit questions scale with it.

**Pitfalls & lessons**
The criticism is not that the modelling is technically wrong. Galis and Karlsson are careful that these platforms work pragmatically rather than agnostically: they integrate and visualise data effectively, and the categories they carry come along with that effectiveness. The failure mode is treating a delivered ontology as a neutral description of the domain rather than as an encoded set of choices about what counts.

## Sources consulted
- https://doi.org/10.1080/1369118X.2024.2410255 (Galis and Karlsson, *Information, Communication & Society* 27:13)
- https://www.wired.com/story/palantir-germany-gotham-dragnet/
- https://theconversation.com/when-the-government-can-see-everything-how-one-company-palantir-is-mapping-the-nations-data-263178
- `research/firecrawl/pltr-crit-polintel.md`
- `research/firecrawl/pltr-crit-wired-germany.md`
- `research/firecrawl/pltr-crit-conversation.md`
