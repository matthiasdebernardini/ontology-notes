# Audit — Lecture 10, "The Politics of an Installed Ontology, and What Comes Next"

File audited and corrected in place: `lectures/transcripts/10-politics-and-what-comes-next.txt`.
Permitted sources: `notes/palantir-ontology-critique.md`, `notes/bowker-star-sorting-things-out.md`,
`notes/llm-ontology-debate.md`, `notes/ontolearner.md`, `notes/ontoaligner.md`, `notes/elot.md`.
Word count before 2,789 → after 2,806 (parity; the pass cut more than it added, then re-spent the
budget on grounded replacements for cut material).

## Verified

| Claim in transcript | Note | Supporting span |
|---|---|---|
| Paper by Vasilis Galis and Björn Karlsson, IT University of Copenhagen, 2024, on POL-INTEL | palantir-ontology-critique | "Vasilis Galis and Björn Karlsson's 2024 paper, written at the IT University of Copenhagen, on POL-INTEL, the Danish police's customisation of Palantir's Gotham" |
| Journal is *Information, Communication & Society* | palantir-ontology-critique (Sources) | "Galis and Karlsson, *Information, Communication & Society* 27:13, 2438-2456" |
| Interviews with Palantir engineers and police-officer users | palantir-ontology-critique | "based on interviews with Palantir engineers and police-officer users" |
| Ontology in two senses at once: philosophical burden plus centralised concept repository | palantir-ontology-critique | "understood in a twofold, albeit interconnected, way: it stands for its usual philosophical burden, but also refers to a centralized concept repository" |
| Ontology inherently political; assemblage of data, ideological positions, economic concerns, translated into the Danish context | palantir-ontology-critique | "POL-INTEL's ontology is inherently political, as it is articulated by an assemblage of data, ideological positions, and economic concerns that are translated into the Danish context." |
| Getaway-vehicle example: registry record, officer's filters, category produced by the interplay, not the registry | palantir-ontology-critique | "A car's record is mirrored from the Motor Vehicle registry… The category is produced by the interplay of the platform's concepts and the officer's analytical role, not by the registry." |
| Platformisation redistributes skill; consequences for organisational life and accountability | palantir-ontology-critique | "new distributions of capability between the platform and the officer, with consequences for organisational life and accountability" |
| The criticism is not that the modelling is technically wrong | palantir-ontology-critique | "The criticism is not that the modelling is technically wrong." |
| "pragmatically integrate, analyse, visualise… Pragmatically, not agnostically… through their ontology, they perform politics" | palantir-ontology-critique | "*pragmatically* integrate, analyze, and visualize data" … "Pragmatically, not agnostically. Data integration and analysis platforms are formatted, framed, and encoded with concepts: through their ontology, they perform politics." |
| Ruling date, court, both provisions unconstitutional | palantir-ontology-critique | "In its judgment of 16 February 2023 … the Bundesverfassungsgericht 'held that § 25a(1) … Hesse … and § 49(1) … Hamburg … are unconstitutional.'" |
| WIRED: strict guidelines for the first time; warned about bystanders, witnesses or lawyers | palantir-ontology-critique | "issued strict guidelines for the first time about how automatic data analysis tools like Palantir's can be used by police" and "warned against the inclusion of data belonging to bystanders, such as witnesses or lawyers" |
| Eleven claimants; Britta Eder a Hamburg defence lawyer | palantir-ontology-critique | "One of the eleven claimants was Britta Eder, a Hamburg defence lawyer" |
| Review questions: which link types create legal exposure; proximity rather than suspicion; audit trail reconstructing why a person was surfaced | palantir-ontology-critique | "ask which object and link types create legal exposure, whose data enters as a by-product of proximity rather than suspicion, and whether an action's audit trail can reconstruct why a person was surfaced" |
| Torque question: when a real case does not fit a category, who bears the cost | bowker-star | "Use torque as a review question on any operational ontology: when a real case does not fit a category, who bears the cost?" |
| ICD is a classification that mainly describes (used as the contrast case) | bowker-star | "**The International Classification of Diseases.** … 'developing this classification took many years and there are still many disagreements over it.'" |
| Agents raise the volume of decisions taken through the categories; governance and audit scale with it | palantir-ontology-critique (LLM angle) | "Adding agents that both query the ontology and invoke its actions increases the volume of decisions taken through these categories, and the governance and audit questions scale with it." |
| Sun and colleagues, PVLDB 2024, ask whether LLMs are a good replacement of taxonomies and test it | llm-ontology-debate | "Sun and colleagues ask 'Are Large Language Models a Good Replacement of Taxonomies?' in *PVLDB* 17(11), 2024, and test it empirically." |
| Miserably poorly on specialised taxonomies and leaf entities; up to 30% accuracy drop; keep the tree in specialised domains | llm-ontology-debate | "LLMs perform miserably poorly in handling specialized taxonomies and leaf-level entities… drops by up to 30%…" / "continue with the current tree-structure taxonomies in specialized domains to ensure reliability" |
| Keet: models are not knowledge bases; no repeatability; two runs, two ontologies | llm-ontology-debate | "the LLMs do not store the (structured) facts, (axiomatised) sentences, and rules… nor does an LLM offer the reliability that it would return the same answer… 'two different runs then may lead to two different ontologies.'" |
| Keet: consensus is not established because a model said so | llm-ontology-debate | "this doesn't entail that the humans in the project have reached consensus just because an LLM said so" |
| Direct all-pairs matching quadratic, ~200 concepts or fewer | ontoaligner | "Direct LLM matching has quadratic complexity and is documented as suitable for small ontologies (about 200 concepts or fewer)" |
| Thresholds dataset- and use-case-specific | ontoaligner | "Matching thresholds are dataset- and use-case-specific" |
| Pure LLMs for well-known domains, RAG for specialised | ontolearner | "recommend pure LLMs mainly for general or well-known domains, RAG for specialized domains" |
| ELOT: one plain-text notebook is both source and documentation | elot | "one plain-text Org notebook is both the ontology source and its documentation" |
| ELOT model integration surface and guards | elot | "lets an LLM inspect resources and conventions, search labels, lint, query with SPARQL, run ROBOT-backed consistency/unsatisfiability/explanation checks, mint policy-compliant identifiers… File writes are project-scoped, disabled by default, confirmation-gated, and revalidated with rollback" |
| Validation checks lint and OWL parsing, not semantic consistency | elot | "Automatic LLM mutation validation checks lint and OWL parsing, not semantic consistency; run the separate consistency check after edits." |
| Ontology-grounded retrieval: 27% fact-based reasoning gain, 30% faster attribution | llm-ontology-debate | "reports '30% faster attribution of responses to context' alongside a 27% gain in fact-based reasoning accuracy" |
| Division of labour (propose vs reject) is the narrator's summary | llm-ontology-debate | "**A division of labour, which is my summary rather than any source's.**" |
| Weakest / mixed / strongest ranking is the narrator's reading | llm-ontology-debate | "My reading of the evidence in this corpus, not a finding any source states: it is weakest on the first, mixed and improving on the second, and strongest on the third." |

Back-references verified against the neighbouring transcripts:

| Back-reference | Verified against |
|---|---|
| Lecture nine recap (object/link types, action types and functions, security woven through, writeback of user decisions) | `09-palantir-operational-layer.txt` closing claim |
| Link type is bidirectional and independently traversable from both sides | `09` — "A link type is bidirectional and has two sides… each side is traversable independently with its own name." |
| Lecture nine ended on governed agents invoking named actions | `09` — "An agent that can only invoke a fixed set of named actions, each with a typed parameter schema… that's a governed system." |
| Torque and black-boxing are lecture eight | `08` — "Their central concept is torque." |
| The incentive audit is lecture eight | `08` — "the constructive form of Doctorow's critique is an incentive audit" |
| Lenat: reading text cannot supply common sense | `04` — "Reading text cannot supply it either, because the writers leave it out." |
| The word entered computing through a sharing problem | `04` claim to keep — "invented to solve a sharing problem… not a reasoning problem" |
| "shared" is lecture four's word | `04` — "why the definition eventually acquired the word 'shared'" |
| Lorhard 1606 coinage; Wolff 1730 | `02` — "that date is sixteen oh six… Jacob Lorhard"; "Christian Wolff… published Philosophia prima sive ontologia in seventeen thirty" |
| OWL is lecture five | `COURSE-PLAN.md` lecture 5 beats — "OWL as the expressive one" |

## Cut

| Cut text (verbatim) | Reason |
|---|---|
| "and her connection to her own mother is one hop from all of it" | **Fabricated detail about a named living person.** No note mentions Britta Eder's mother, or any family member. Invented. |
| "Anti-fascists. Anti-nuclear campaigners. Members of a banned Kurdish organisation." (as separate sentence fragments describing her *contact list*) | "banned" is not in the note; the note says "members of the PKK" with no legal characterisation. Replaced with the note's own wording. |
| "Five years ago you built a knowledge graph so that analysts could query it. Now a substantial fraction of graph projects exist so that a model has something reliable to stand on. The consumer changed, and the requirements changed with it — identifiers and provenance matter more, elaborate inference matters less, and coverage matters enormously, because a model will confidently improvise over any gap in the graph rather than reporting that it found nothing." | Entire paragraph traces to no listed note. Trend claim, unsourced quantification ("a substantial fraction"), unsourced requirement ranking. Would need a new note. |
| "Expert systems were going to encode professional knowledge, and they hit the acquisition bottleneck. Cyc was going to reach critical mass and start reading, and it didn't. The Semantic Web was going to make the whole web machine-readable, and the economics said no. Each time, the specific promise failed and a durable capability survived — inference engines, microtheories and modularity, and a standards stack that quietly runs biology and finance." | None of it traces to a listed note. "a standards stack that quietly runs biology and finance" is an unsourced empirical claim. The paragraph's one usable idea (cost shifts from drafting to agreement) was kept as the narrator's. |
| "The strong claim, that models make explicit knowledge representation unnecessary, will not survive contact with any domain where being wrong is expensive." | Forecast stated as fact; no note supports it. The surviving sentences say the same thing in the marked-verdict section. |
| "four thousand classes nobody agreed to" | Invented number. Replaced with "a model of the business nobody in the business agreed to". |
| "Borst added the word 'shared' to the definition in 1997 for a reason, and a generated ontology fails that clause by construction." | 1997/Borst is not in any of the six permitted notes (it lives in `gruber-ontology-definition.md`). Replaced with a lecture-four back-reference plus Keet's consensus point, which *is* permitted. |
| "a make, a model, a registration, an owner" | Elaboration of the registry record not present in the note. |
| "selects a date range, looks at a map of incidents" | Officer's actions beyond "applying filters"; not in the note. |
| "A car flagged as a possible getaway vehicle produces a stop, a conversation, a record." | Downstream consequences not documented anywhere in the note. |
| "The paper's point is that you cannot pull those apart and say which one made the category — the platform's model, or the officer's filters, or the institutional purpose that made both of them available at that moment." | Attributed to the paper; the note's sentence stops at "not by the registry". |
| "and I would guess they made it in an afternoon" | Speculation about the conduct of real, unnamed engineers. |
| "There's a paper in the VLDB proceedings" (read aloud as an initialism) | Narration defect plus an expansion no note supplies; rewritten as "a two thousand and twenty-four paper in the database-systems literature". |

## Corrected

| Before | After | Note span that forced it |
|---|---|---|
| "Germany's Federal Constitutional Court struck down a Hamburg law permitting automated data analysis by police, along with a similar law in Hesse" | "held that two provisions permitting automated data analysis by police, one in Hesse and one in Hamburg, are unconstitutional. The remedies differ… The Hamburg provision is void. The Hesse provision was left to continue to apply, subject to restrictions… no later than the thirtieth of September two thousand and twenty-three." | "The remedies differ: the Hamburg provision 'is void,' while the Hesse provision 'will continue to apply, subject to the restrictions set out below, until new provisions have been enacted, and in any case no later than 30 September 2023.'" |
| "The court's language, in the reporting, is that the laws allowed police, with just one click, to create comprehensive profiles of persons." | "The court's reasoning, in its own words, is that the powers allow the police, with just one click, to create comprehensive profiles of persons, groups and circles, and may also subject many persons who are legally innocent to further police measures." | "The court's reasoning is that the powers 'allow the police, with just one click, to create comprehensive profiles of persons, groups and circles,' and 'may also subject many persons who are legally innocent to further police measures.'" — quotation was truncated *and* misattributed to reporting |
| "Her contact list is full of people the state considers criminals, because she defends them." | "Her client list includes anti-fascists, people who campaign against nuclear power, and members of the PKK." | "whose 'client list includes anti-fascists, people who campaign against nuclear power, and members of the PKK'" — the note says client list, not contact list, and states no view about what the state considers them |
| "they use a phrase I'd like you to keep: these platforms do not only describe the world, they enact it" | "a phrase … which they take from Leese: devices like this do not only describe the world but also enact it" | "Such devices, they write, quoting Leese, 'not only describe the world but also enact it.'" |
| "Their argument is that in a working system you cannot separate them, because the repository is where the claim about what exists gets enforced." | "They then borrow Barry Smith's split between theory-focused R-ontologies and pragmatic E-ontologies, and find that the platform's E-ontology cannot be separated from Palantir's or the police's." | "They then borrow Barry Smith's terminological split between theory-focused R-ontologies and pragmatically oriented E-ontologies, and argue that 'the platform's E-ontology cannot be separated from Palantir's and/or the police.'" — the transcript attached "cannot be separated" to the wrong pair of things |
| "Hallucination and inconsistency survive good prompting, so labels and relationships still need validating…" | "clear prompts and structured output do reduce hallucination and inconsistency. What they do not do is remove the need to validate relationships and labels against representative held-out data, multiple metrics, and classical baselines." | ontolearner: "Clear prompts and structured output reduce hallucination and inconsistency; relationships and labels should be validated, and evaluation should use representative held-out data, multiple metrics, domain-specific criteria, and classical baselines." — the claim was **inverted** |
| "The substitution does not hold uniformly, and it degrades outside common, well-represented domains." | "models perform miserably poorly in handling specialised taxonomies and leaf-level entities, and the question-answering accuracy of the best model drops by up to thirty per cent…" | llm-ontology-debate quotes the result and the 30% figure; the vague paraphrase discarded the measurement |
| "the four properties I mentioned in lecture four. An axiom is inspectable, consistent, attributable, and stable." | "the three properties I flagged in lecture four as my own argument rather than Lenat's. An axiom is inspectable… consistent… And it can be audited" | Lecture four states **three** properties and flags them as the narrator's, not Lenat's: "What the axiom gave you that the model does not is three properties." "Stable" was never there; the repeatability point now sits with Keet, where a note supports it. |
| "Maria Keet has argued that generating an ontology from a language model is harder than it looks, because the output has to satisfy logical constraints and domain commitments that a fluent generator has no way to guarantee." | Keet's own two objections, in her order: models are not knowledge bases (no repeatability, two runs two ontologies); and the logical one | llm-ontology-debate, "Keet's objection" — the invented "because" clause was replaced with what she actually argues |
| "the ontology is articulated by an assemblage… Their central finding" | "Their central claim" | The note calls it their argument/claim, not a finding; a finding implies measurement they did not do |
| "Which object and link types create legal or ethical exposure?" | "Which object and link types create legal exposure?" | Note says "legal exposure"; "ethical" was added |
| "mirrored into POL-INTEL from the Danish Motor Vehicle registry" | "mirrored into the platform from the Motor Vehicle registry" | Note says "the Motor Vehicle registry" |
| "which is Gruber's 1993 definition arriving somewhere he could not have predicted" | "which is Gruber's definition from lecture four arriving somewhere he could not have predicted" | The 1993 date is not in any permitted note; converted to a verified back-reference |
| "The pattern that keeps emerging is a division of labour" | "The pattern I would draw out of that is a division of labour, and it is my summary rather than any source's finding." | "A division of labour, **which is my summary rather than any source's**." |
| "Question three… Here the answer is strongest" | "Here I would say the answer is strongest, and that ranking of the three questions is my reading of the evidence rather than a finding any source states." | "My reading of the evidence in this corpus, not a finding any source states" |
| "The paper also documents a second effect… the officer's expertise shifts from knowing a neighbourhood to knowing how to query." (presented as the paper's) | Note's wording first, then "The gloss is mine — the officer's expertise shifts…" | The note reports "new distributions of capability… with consequences for organisational life and accountability" and nothing about neighbourhoods or queries |
| "This is Bowker and Star's torque… And it's more consequential than their examples…" (presented as established) | "The comparison I would add is mine, not theirs." | bowker-star note offers torque as a review question; the ICD-vs-platform ranking is the narrator's |
| "So here is the review I'd want run… drawn from all of this." / verdict presented flat | Verdict now opens "It is mine, not a rule any source states." | No note states build/don't-build rules; the plan calls this the narrator's closing verdict |

## Narration fixes

**Acronyms (first use in this file).**
- LLM — added: "Large language models — LLMs, systems trained on enormous quantities of text to predict and produce more of it".
- OWL — added: "OWL being the Web Ontology Language from lecture five".
- ELOT — no note gives an expansion, so it is glossed rather than expanded: "ELOT is a literate ontology-engineering environment, where one plain-text notebook is both the ontology source and its documentation." Inventing an expansion would have been a fabrication.
- POL-INTEL — likewise no source expands it; now handled explicitly for the listener: "which is not an acronym anybody expands — it is simply the name of the Danish police's customisation of Palantir's Gotham platform."
- RDF — not used in this file; nothing to expand.
- PKK — left unexpanded because no permitted note expands it, and the earlier draft's gloss ("a banned Kurdish organisation") was an unsourced legal characterisation.

**Numbers and citations spoken.**
- "February 2023" → "February two thousand and twenty-three"; "the sixteenth of February"; "the thirtieth of September two thousand and twenty-three".
- "published in 2024" → "two thousand and twenty-four".
- The docket "1 BvR 1547/19, 1 BvR 2634/20" is **not** read aloud. It cannot be spoken without turning into punctuation; the date plus the court identifies the judgment.
- "roughly two hundred concepts", "thirty per cent", "twenty-seven per cent", "sixteen oh six", "seventeen thirty" all spelled as spoken.
- "VLDB proceedings" removed as an unspeakable initialism.

**Seams.** The hard pivot at "Right. Second half. Where does all of this stand now that we have machines that can read?" is gone. The two halves are now joined by an argument rather than a bookmark: the four review questions all assume a human asker, an agent in that seat raises the volume of decisions taken through the categories, "which is where the rest of this lecture goes". Two spliced-in restatements were also removed: the bystander problem was being explained twice (once in the ruling paragraph, once in the review questions — the second is now a callback), and "Generate and verify" was stated twice in adjacent sections.

**Endings.** The file previously had three closing gestures: "The expensive part is now, and always was, agreement" (mid-file), the ten-lecture arc recap, and an unlabelled two-sentence claim that did not match the course plan. Now there is one course close (the arc recap, one clause per lecture, verified against lectures two through nine), then the house marker "So, the claim to keep.", then the plan's exact claim to retain, then the file stops. The mid-file "agreement" line has been demoted into the body of the argument.

**Continuity.** The opening states position in the arc ("the last of ten talks"), recaps lecture nine accurately, and names both halves. Every back-reference was checked against the transcript it points at — see the second table under Verified. Two were wrong and are fixed: lecture four states three properties, not four, and states them as the narrator's own argument; the arc recap's "a seventeenth-century coinage that made it a science" conflated Lorhard's 1606 coinage with Wolff's 1730 demonstrative method, and is now split.

## Depth still available

Grounded material in the six notes that the lecture does not yet use. All quoted here so a later pass can extend without re-reading.

1. **The bluntest line in the critique note, unused.** palantir-ontology-critique: "platforms such as POL-INTEL are not encoded with democratic values or other modernist sensibilities."
2. **The named failure mode of the whole lecture, unused.** palantir-ontology-critique: "The failure mode is treating a delivered ontology as a neutral description of the domain rather than as an encoded set of choices about what counts."
3. **The specific provisions.** palantir-ontology-critique: "§ 25a(1) first alternative of the Security and Public Order Act for the Land Hesse … and § 49(1) first alternative of the Act on Data Processing by the Police for the Land Hamburg". A spoken form ("section twenty-five a") would let the lecture say exactly what was struck.
4. **Bowker and Star's sharpest sentence, unused.** bowker-star, via Helmreich: "there is no experience of torque for those in power" — directly answers the review question about who bears the cost.
5. **Torque's actual definition, unused in this lecture.** bowker-star: torque is what unfolds when "the 'time' of the body and of [its] multiple identities cannot be aligned with the 'time' of the classification system'", and "individual biographies are twisted into tortured shapes".
6. **The residual-category lesson, unused.** bowker-star, Nehrlich: "there will always be elements which do not slot neatly into a category. But it is important to remember that this is not a reflection of the element — it is a reflection of the inadequacy of the system." (His example is the platypus.)
7. **Sun's alternative division of labour** — cut from this pass for length, and stronger than the narrator's own: "the entities near the roots move into the model's weights, while the entities near the leaves stay in the tree."
8. **The replacement case stated fairly.** llm-ontology-debate: models "demonstrate an impressive ability to internalize knowledge and answer natural language questions", "sparking a growing debate about whether traditional knowledge graphs will be replaced by LLMs in real applications".
9. **Keet's whales example in full**, currently compressed to "a widely written-up misconception": "if a majority is ignorant of the fact that, say, whales are mammals and wrote about their misconception, an LLM may propose them to be fish, but that would make the ontology inconsistent if the rest of animal classification was represented properly. Inconsistent ontologies are bad computationally."
10. **The OG-RAG gap statement**, cut for length: "existing retrieval-augmented models, such as RAG, offer improvements but fail to account for structured domain knowledge… ontologies, which conceptually organize domain knowledge by defining entities and their interrelationships, offer a structured representation to address this gap."
11. **The reverse direction, unused.** llm-ontology-debate: "LLMs also enable ontology extraction from both structured and unstructured data."
12. **The three LLMs4OL tasks**, which would make "can a model build one?" concrete. ontolearner: "**term typing** (map a lexical term to a class), **taxonomy discovery** (find hierarchical `is-a`/subclass relations), and **non-taxonomic relation extraction**"; plus **Text2Onto**, which "separately extracts terms and types from raw text".
13. **The escalation ladder for reliability.** ontolearner: "pure LLMs mainly for general or well-known domains, RAG for specialized domains, and LLM/symbolic or multi-model ensembles for higher-stakes reliability."
14. **A concrete operational limit.** ontolearner: "Large retrieval contexts can cause memory problems; `AutoRetrieverLearner(batch_size=...)` computes similarities in smaller batches."
15. **Why alignment output needs scoring, not just matching.** ontoaligner: evaluation "reports precision, recall, F-score, and intersection; ranked candidate outputs can also be measured with Hit@K and MRR", and ensembles fuse matchers "through weighted voting, reciprocal-rank fusion, Borda, Condorcet, or score averaging".
16. **The reranking trap.** ontoaligner: "reranking is useful only when each source still has multiple target candidates — not after a single-target matcher has made its final selection."
17. **ELOT's two-call rule and identifier pitfalls**, which make the "guarded" claim concrete. elot: "A newly minted CURIE also cannot be used as an axiom subject in the same batch, so insertion and axiom editing require two calls"; "Numeric-only counter identifiers are technically invalid XML NCNames"; "labels, not CURIEs, should carry human-readable meaning."
18. **ELOT's honesty about its own docs**, a nice governance beat: "The long-form manual is explicitly under construction; several manual files are stubs or drafts and may be inaccurate."
19. **ELOT in production**, unused: "the README says it has been used in scores of ontology projects, including ISO 23726-3."
