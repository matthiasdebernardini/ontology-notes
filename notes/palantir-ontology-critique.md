# Criticism of Operational Ontologies (Palantir)

**What it is**
The research and legal record on what happens when a vendor ontology is installed inside a state institution. The most direct study is Galis and Karlsson's 2024 paper on POL-INTEL, the Danish police's customisation of Palantir's Gotham, based on interviews with Palantir engineers and police-officer users.

**Key concepts**
- **Ontology in two senses at once.** The authors write that "the concept of ontology should be understood in a twofold, albeit interconnected, way: it stands for its usual philosophical burden, but also refers to a centralized concept repository." They then borrow Barry Smith's terminological split between theory-focused R-ontologies and pragmatically oriented E-ontologies, and argue that "the platform's E-ontology cannot be separated from Palantir's and/or the police."
- **The ontology is political.** "POL-INTEL's ontology is inherently political, as it is articulated by an assemblage of data, ideological positions, and economic concerns that are translated into the Danish context." Such devices, they write, quoting Leese, "not only describe the world but also enact it."
- **The getaway-vehicle example.** A car's record is mirrored from the Motor Vehicle registry. Inside the platform, viewed by an officer applying filters, it is potentially seen as a getaway vehicle. The category is produced by the interplay of the platform's concepts and the officer's analytical role, not by the registry.
- **Platformisation redistributes skill.** The paper reports new distributions of capability between the platform and the officer, with consequences for organisational life and accountability.
- **The German constitutional ruling.** In its judgment of 16 February 2023 (1 BvR 1547/19, 1 BvR 2634/20) the Bundesverfassungsgericht "held that § 25a(1) first alternative of the Security and Public Order Act for the Land Hesse … and § 49(1) first alternative of the Act on Data Processing by the Police for the Land Hamburg … are unconstitutional." The remedies differ: the Hamburg provision "is void," while the Hesse provision "will continue to apply, subject to the restrictions set out below, until new provisions have been enacted, and in any case no later than 30 September 2023." The court's reasoning is that the powers "allow the police, with just one click, to create comprehensive profiles of persons, groups and circles," and "may also subject many persons who are legally innocent to further police measures." Reporting the ruling, WIRED noted the court "issued strict guidelines for the first time about how automatic data analysis tools like Palantir's can be used by police" and "warned against the inclusion of data belonging to bystanders, such as witnesses or lawyers." One of the eleven claimants was Britta Eder, a Hamburg defence lawyer whose "client list includes anti-fascists, people who campaign against nuclear power, and members of the PKK."

**How you'd use it**
Use this as the applied version of Bowker and Star — see [bowker-star-sorting-things-out.md](bowker-star-sorting-things-out.md), where torque is the twisting that happens when a person's own account of themselves cannot be aligned with the classification system. It becomes concrete when the classification is enforced by a state platform: the residual categories, the link types that make two people related, and the thresholds inside a function are policy choices with legal consequences, made by engineers. When reviewing an operational ontology, ask which object and link types create legal exposure, whose data enters as a by-product of proximity rather than suspicion, and whether an action's audit trail can reconstruct why a person was surfaced.

**LLM angle**
Adding agents that both query the ontology and invoke its actions increases the volume of decisions taken through these categories, and the governance and audit questions scale with it.

**Pitfalls & lessons**
The criticism is not that the modelling is technically wrong. Galis and Karlsson grant that these platforms "*pragmatically* integrate, analyze, and visualize data" — and then land the distinction: "Pragmatically, not agnostically. Data integration and analysis platforms are formatted, framed, and encoded with concepts: through their ontology, they perform politics." They are blunter still elsewhere: "platforms such as POL-INTEL are not encoded with democratic values or other modernist sensibilities." The failure mode is treating a delivered ontology as a neutral description of the domain rather than as an encoded set of choices about what counts.

**Verdict**
Worth deeper study, and the place to start if you want the consequences argument rather than the technique. It is the only source in this corpus where a modelling decision has a court ruling attached to it.

## Sources consulted
- https://doi.org/10.1080/1369118X.2024.2410255 (Galis and Karlsson, *Information, Communication & Society* 27:13, 2438-2456)
- https://www.bundesverfassungsgericht.de/SharedDocs/Pressemitteilungen/EN/2023/bvg23-018.html (judgment of 16 February 2023)
- https://www.wired.com/story/palantir-germany-gotham-dragnet/
- https://theconversation.com/when-the-government-can-see-everything-how-one-company-palantir-is-mapping-the-nations-data-263178
- `research/firecrawl/pltr-crit-polintel.md`
- `research/firecrawl/pltr-crit-wired-germany.md`
- `research/firecrawl/pltr-crit-conversation.md`
- `research/firecrawl/pltr-crit-bverfg-pressrelease.md`
- `research/firecrawl/pltr-crit-seer-seen.md` (failed scrape: HTTP 403; not relied on)
