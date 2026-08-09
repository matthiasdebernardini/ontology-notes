# Audit: lectures/transcripts/04-cyc-and-the-engineering-sense.txt

Permitted sources: `notes/cyc-lenat-1995.md`, `notes/gruber-ontology-definition.md`,
`notes/cyc.md`, `notes/description-logics-dls.md`.

Word count 2,899 → 1,748 (−1,151, −40%). Correction pass only; nothing added
that is not quoted from a permitted note.

## Verified

| Claim in lecture | Note | Supporting span |
|---|---|---|
| Machine learning and natural language understanding both stall without background knowledge | cyc-lenat-1995.md | "Lenat's premise was that machine learning and natural-language understanding both stall without a large base of background knowledge" |
| Somebody had to enter it by hand until the system reached critical mass and could take over its own learning | cyc-lenat-1995.md | "so somebody had to enter that knowledge by hand until the system reached critical mass and could take over its own learning" |
| Lenat and Mary Shepherd began Cyc in nineteen eighty-four | cyc-lenat-1995.md | "describes the Cyc project, begun with Mary Shepherd in 1984" |
| Article title "CYC: A Large-Scale Investment in Knowledge Infrastructure" | cyc-lenat-1995.md | Douglas Lenat's article "CYC: A Large-Scale Investment in Knowledge Infrastructure" |
| Published in *Communications of the ACM* in nineteen ninety-five | cyc-lenat-1995.md | "It appeared in *Communications of the ACM* 38(11) in 1995, per its DBLP record." |
| The "little chance of success" quotation | cyc-lenat-1995.md | "Mary Shepherd and I embarked on that task in 1984, knowing we had little chance of success, but seeing no alternative but to try." |
| The list of what common sense requires | cyc-lenat-1995.md | "causality, time, space, substances, intention, contradiction, uncertainty, belief, and emotion as things that must be represented" |
| "You cannot remember events that have not happened yet" | cyc-lenat-1995.md | quoted verbatim in **Key concepts** |
| Peanut butter / table example | cyc-lenat-1995.md | "if you cut a lump of peanut butter in half, each half is also a lump of peanut butter; but if you cut a table in half, neither half is a table" |
| Statistics/colocation/frequency quotation | cyc-lenat-1995.md | "statistics, colocation, and frequency do not resolve such questions. But the task goes from impossible to trivial if one already knows a few things about boxes and pens." |
| Roughly a hundred thousand general concepts | cyc-lenat-1995.md | "a universal schema of roughly 10⁵ general concepts spanning human reality" |
| About a million handcrafted axioms, millions more inferred and cached | cyc-lenat-1995.md | "about a million commonsense axioms 'handcrafted for and entered into CYC's knowledge base, and millions more … inferred and cached by CYC'" |
| A person-century of effort since nineteen eighty-four | cyc-lenat-1995.md | "'a person-century of effort' since 1984" |
| It is the only corpus document that prices hand-codified knowledge | cyc-lenat-1995.md | "It is the only document in this corpus that states the price of hand-codified knowledge as a number" |
| Every "we will just model our domain properly" plan bets against that number | cyc-lenat-1995.md | "is the number every 'we will just model our domain properly' plan is implicitly betting against" |
| Micro-theories: own context, small, solid, flat | cyc-lenat-1995.md | "micro-theories, each of which 'inhabits its own context' and is 'relatively small, solid, and flat'" |
| Cyc never reached critical mass; payoff deferred to a threshold that had not arrived | cyc-lenat-1995.md | "the project's payoff was always deferred to a critical mass that had not yet arrived" |
| Threshold-shaped value is a bet on the threshold; layered alternative answers competency questions early | cyc-lenat-1995.md | "A knowledge base whose value depends on reaching a threshold, rather than on being useful at every stage, is a bet on the threshold. Compare the layered approach the rest of this corpus recommends, where a small ontology answers real competency questions early." |
| Cyc sold today as a commercial platform, reasoning from codified common sense rather than statistics | cyc.md | "an enterprise machine-reasoning AI platform that uses codified human common sense and knowledge rather than patterns and statistics" |
| Pitched at healthcare operations | cyc.md | "emphasizes healthcare operations products, including charge capture, denial management, post-acute-care forecasting, and staffing" |
| Cyc sells on explainability and auditability | cyc.md | "explainability and auditability" (**Key concepts**) |
| Gruber, nineteen ninety-three: "an explicit specification of a conceptualization" | gruber-ontology-definition.md | "Tom Gruber's 1993 work … defined an ontology as 'an explicit specification of a conceptualization'" |
| Gruber's acknowledgements place the work inside the ARPA (later DARPA) Knowledge Sharing Effort | gruber-ontology-definition.md | "written inside what his own acknowledgements call the ARPA (later DARPA) Knowledge Sharing Effort" |
| Ontology as interface specification, not internal encoding | gruber-ontology-definition.md | "ontology as an interface specification rather than an internal encoding" |
| The language two agents use to talk about a domain; not obliged to store it that way internally | gruber-ontology-definition.md | "an ontology is the language two agents use to talk to each other about a domain. An agent that supports the interface is not obliged to store its knowledge that way internally." |
| "The agents sharing a vocabulary need not share a knowledge base; each knows things the other does not." | gruber-ontology-definition.md | quoted verbatim |
| An ontology can sit above systems sharing nothing but the vocabulary | gruber-ontology-definition.md | "That is why an ontology can sit above heterogeneous systems that share nothing but the vocabulary." |
| Borst, nineteen ninety-seven: "a formal specification of a shared conceptualization", adding consensus | gruber-ontology-definition.md | "Borst's 1997 revision to 'a formal specification of a shared conceptualization,' which adds consensus" |
| *Explicit* and *shared* are the load-bearing words | gruber-ontology-definition.md | "The load-bearing words are *explicit* … and, after Borst, *shared* — more than one party agreed." |
| DLs: more expressive than propositional, less than first-order; concepts, roles, individuals, axioms; expressivity traded against complexity | description-logics-dls.md | "generally more expressive than propositional logic and less expressive than first-order logic. They model concepts, roles, individuals, and axioms while balancing expressive power against reasoning complexity" |
| Many core reasoning problems are decidable | description-logics-dls.md | "many core reasoning problems are decidable" |
| DLs are the logical foundation for OWL and its profiles | description-logics-dls.md | "The source identifies DLs as the logical foundation for OWL and its profiles" |
| More operators / more complicated hierarchy raises inference complexity | description-logics-dls.md | "Adding operators and making the TBox more complicated usually increases the computational complexity of inference." |
| The inspectable / consistent / auditable counter-claim is the narrator's, not Lenat's | cyc-lenat-1995.md | "the counter-claim that what a model absorbs is not inspectable, not consistent, and cannot be audited is mine" |
| Large language models contest Cyc's motivating claim by absorbing that background from text | cyc-lenat-1995.md | "That is the claim large language models most directly contest, since they absorb an enormous amount of that background from text without anyone hand-writing axioms." |
| The 1995 paper says nothing about language models | cyc-lenat-1995.md | "The paper is from 1995 and says nothing about them" |

## Cut

Every item below traces to no permitted note. Cut, not softened.

| Cut text (verbatim, abridged where long) | Reason |
|---|---|
| "It's the early 1980s. Artificial intelligence has a commercial product for the first time, and it's called the expert system." | No permitted note mentions expert systems, their commercialisation, or the date. |
| "Take a narrow domain — diagnosing bacterial infections, configuring a mainframe order, prospecting for minerals. Interview the human experts… For a few years this was the most convincing thing AI had ever produced, and companies bought it." | Entire expert-system mechanism and market history unsourced in the four notes. |
| "Then everyone hit the same two walls." / "The first wall was the knowledge acquisition bottleneck… human labour does not scale." | The phrase "knowledge acquisition bottleneck" appears nowhere in `notes/`; only in COURSE-PLAN.md, which is not a source. The note grounds only "machine learning and natural-language understanding both stall without a large base of background knowledge." |
| "The second wall was brittleness… A medical diagnosis system would happily reason about a patient who had been dead for a decade, because nothing in its rules said that dead people stop having symptoms." | Anecdote absent from all four notes. Presented as historical fact. |
| "Doug Lenat looked at that second wall and drew a conclusion that was either the great insight of the era or its great mistake, and the argument is still live." | Depends on the cut "second wall"; the editorial framing is unsourced. |
| "It was called Cyc, from the middle of 'encyclopedia.'" | Etymology stated as fact; no permitted note gives it. |
| "planning" (appended to Lenat's list of what common sense requires) | Note's list ends at "emotion". "planning" is an invented eleventh item. |
| "Not just representing those things, but reasoning about them efficiently, and working out sets of categories and attributes that carve up the world usefully." | No note support for the efficiency or category-design claims. |
| "Lenat's point about these assertions is that they are unlikely to appear in any textbook, dictionary, magazine, or encyclopedia, even one written for children. They're too fundamental. Stating them aloud to another person would be confusing or insulting." | Attributed to Lenat; no permitted note contains it. Would need a new note. |
| "Inside the naive-physics microtheory, heavy things fall. Inside the cartoon-physics microtheory, they hang in the air until noticed." | Invented illustration attributed to Cyc. |
| "The Gene Ontology was useful when it had a few thousand terms, because biologists could annotate genes with it and compare results across species that day… The Financial Industry Business Ontology, CIDOC CRM for museums, the Digital Buildings ontology — all of them deliver value continuously rather than at a threshold." | Those notes exist in the repo but are NOT permitted sources for lecture four, and the specific "useful at a few thousand terms" claim is not in them either. The underlying lesson survives via the grounded layered-approach span. |
| "Lots of groups were building knowledge-based systems. Every one of them was building its knowledge base from scratch. And none of the knowledge bases could talk to each other, because each had invented its own vocabulary, its own way of representing time, its own conventions for what counted as an entity." | Historical claim about the state of the field; not in any permitted note. Replaced by the grounded Gruber span on heterogeneous systems. |
| "That's a colossal waste, and in the early nineties DARPA … paid for a programme to fix it. It was called the Knowledge Sharing Effort." | Funding, date and causal story unsourced. See Corrected. |
| "The problem it addressed was not 'how do we reason better.' It was 'how do we reuse what somebody else already built.'" | Stated as the programme's documented mission; the note only names the programme. Reframed as a reading of the name plus Gruber's own framing. |
| Entire KL-ONE / frames section: "Through the 1970s and 80s, a family of knowledge representation systems descending from one called KL-ONE…"; "One camp built frames, and the idea came from Marvin Minsky… A Restaurant frame has slots for the food, the staff, the paying."; "in 1980 a researcher named Bill Woods wrote a paper called 'What's in a Link?'…"; "KL-ONE was the response… That operation, automatic classification, was KL-ONE's headline capability" | Grep across `notes/` returns zero hits for KL-ONE, Minsky, or Woods. Nothing in `description-logics-dls.md` is historical — it is a synchronic description of the formalism. All of it would require new notes. |
| "Researchers discovered that some of the languages they'd built were undecidable… an enormous amount of careful work went into mapping exactly which combinations of features were tractable… a map that took twenty years to draw." | Unsourced history and an invented duration. The complexity trade-off survives via the grounded "adding operators … increases the computational complexity" span. |
| "a diagram whose arrows have no defined meaning cannot be computed with, only looked at." / "Which, I'd point out, is the state of most architecture diagrams… If nobody can say what the arrow means, you have a picture." | Depends entirely on the cut Woods material, and is an orphaned mid-file closing (see Narration fixes). |
| "Compare that to how ontology engineering handles the same problem now. Modularisation. Import closures. Named graphs. Application profiles." + "Cyc got there in the eighties, and the field partly reinvented it." | No permitted note discusses modularisation, import closures, named graphs or application profiles; the reinvention claim is unsupported priority attribution. |
| "Lenat said statistical systems fail without background knowledge, and for thirty years he looked wrong in the short term and right in the long term." | "Thirty years" invented; the whole passage restates the earlier LLM section (seam). |
| Entire KIF / Ontolingua section: "One was a language called KIF, the Knowledge Interchange Format… Another was Ontolingua, a server for authoring and translating ontologies… Neither is in use today. But the design assumption underneath both of them … is the assumption behind RDF, behind the multiple serialisations we covered last lecture, and behind every 'export to' button." | KIF and "Knowledge Interchange Format" appear nowhere in `notes/`. Ontolingua appears only as a name in an unrelated tool-list note, with no such history. Also contained a false back-reference (see Narration fixes). |
| "The Knowledge Sharing Effort failed to produce a lasting standard and succeeded in establishing a lasting architecture. That's a more common outcome in this field than people admit…" | Unsourced verdict on the programme, and a third mid-file closing. |
| "Ask a current model whether half a table is a table, and it will tell you no, and explain why, without anyone having hand-crafted an axiom." | Empirical claim about current model behaviour, unsourced. Replaced by the note's own framing of what models contest. |
| Two of the four claimed axiom properties: "It's attributable — somebody entered it and you can ask why. And it's stable — it gives the same answer every time, and it doesn't change when the vendor ships a new version." | The note's counter-claim names exactly three properties: not inspectable, not consistent, cannot be audited. "Stable / vendor version" is an invented fourth. |

## Corrected

| Before | After | Note span forcing the change |
|---|---|---|
| "in the early nineties DARPA — the Defense Advanced Research Projects Agency, the American military research funder — paid for a programme to fix it. It was called the Knowledge Sharing Effort" | "Gruber's own acknowledgements place the work inside the ARPA Knowledge Sharing Effort. ARPA is the Advanced Research Projects Agency, the American military research funder, later renamed DARPA with Defense on the front." | gruber-ontology-definition.md: "written inside what his own acknowledgements call the ARPA (later DARPA) Knowledge Sharing Effort". The note is explicit that the contemporaneous name was ARPA; it says nothing about who paid. |
| "a universal schema of general concepts, roughly a million hand-crafted commonsense axioms" | "a universal schema of roughly a hundred thousand general concepts spanning human reality, about a million commonsense axioms handcrafted for and entered into Cyc's knowledge base" | cyc-lenat-1995.md: "a universal schema of roughly 10⁵ general concepts spanning human reality". The lecture dropped the number the note supplies. |
| "description logics, which are a family of decidable fragments of first-order logic" | "a family of formal knowledge-representation languages, more expressive than propositional logic and less expressive than first-order logic … Many of their core reasoning problems are decidable" | description-logics-dls.md: "generally more expressive than propositional logic and less expressive than first-order logic … many core reasoning problems are decidable." "Decidable fragments" overstates: the note quantifies over problems, not languages. |
| "microtheories, which are locally consistent contexts" (paraphrase, unattributed) | "Micro-theories. Each one, in the paper's own words, 'inhabits its own context,' and each is 'relatively small, solid, and flat.'" | cyc-lenat-1995.md quotes exactly those phrases. Attribution added; the lecture's own gloss demoted to a flagged inference. |
| "Rather than demanding that the entire knowledge base be consistent — which is impossible for common sense, since ordinary human beliefs contradict each other constantly" | "Now, the reason I think that matters is mine and not the paper's, so take it as my inference. Demanding that one enormous knowledge base be consistent from end to end is a losing requirement." | The note describes micro-theories but makes no claim about global consistency being impossible. Narrator's reasoning, now marked. |
| "Cyc is still going, four decades on, as a commercial product." | "Cyc is still going, and it is sold today as a commercial platform — machine reasoning built on codified human common sense rather than on patterns and statistics, pitched at operational work in healthcare, and pitched hard on explainability and auditability." | cyc.md gives the positioning verbatim; "four decades on" was arithmetic the note does not do. |
| "It's the distinction between what philosophers call mass nouns and count nouns…" (stated as fact) | "What I'm about to say about it is my reading rather than Lenat's. It is the distinction between mass nouns and count nouns…" | The note reports only the example, not any linguistic analysis of it. Marked as the narrator's. |
| "The axiom is inspectable… It's consistent… It's attributable… And it's stable… A language model's answer has none of those four properties." | "The counter-argument I'd make is mine, not Lenat's, and I want to flag it as mine… three properties. It is inspectable… It is consistent… And it can be audited." | cyc-lenat-1995.md: "the counter-claim that what a model absorbs is not inspectable, not consistent, and cannot be audited is mine." The note flags its own authorship; the lecture had laundered it into sourced fact and inflated three properties to four. |
| "Lenat was wrong about the acquisition problem and right about the auditability problem" | "as I read it … Lenat may have been wrong about where the background knowledge would come from and right about what you lose when it arrives any other way" | Same span. The verdict is the note author's, not the paper's; hedged and marked. |

## Narration fixes

**Acronyms expanded on first use in this file.** OWL was previously used bare —
now "OWL, the Web Ontology Language". ACM added and expanded, "the A-C-M, the
Association for Computing Machinery, the main professional body of the field",
with the letters spaced so a text-to-speech narrator says them rather than
attempting a word. ARPA and DARPA both expanded. "AI" no longer appears
unexpanded: the one surviving use is "the artificial intelligence side".
DBLP, KIF, RDF and the bare "38(11)" are all gone with the material that
carried them.

**Numbers and Latin as spoken.** Every date is now words: nineteen eighty-four,
nineteen ninety-three, nineteen ninety-five, nineteen ninety-seven. The note's
"10⁵" is spoken as "roughly a hundred thousand", not read as an exponent. No
Latin abbreviations remain.

**Seams.** The file was a first draft with a second pass spliced in ahead of the
closing, and the joins were visible:
- "I mentioned KL-ONE in passing and I want to come back to it" — a splice
  announcing itself. Resolved: KL-ONE is ungrounded and the whole strand is cut.
- "Let me finish by putting Cyc back on the table" followed, twenty lines later,
  by "Now let me return to Cyc for a moment" — two finales for the same topic.
  Resolved: one Cyc return remains, at the end, and it is the LLM section.
- Micro-theories were introduced once and then re-introduced with "Cyc's
  microtheory idea, which I mentioned earlier". Resolved: one treatment.
- The Lenat verdict was delivered twice, in mutually inconsistent forms —
  "Lenat was wrong about the acquisition problem" versus "He was right that
  background knowledge is the bottleneck". Resolved: one verdict, hedged and
  marked as the narrator's.
- The Knowledge Sharing Effort was covered, closed, and then reopened with "Last
  thing on the Knowledge Sharing Effort". Resolved: one treatment.

**Endings.** Four closing-shaped statements existed. Three were orphaned
mid-file: "The lesson from that period is one sentence long, and it is the reason
this entire field exists…"; "Whether what came through that door is knowledge in
the sense he meant is the question we end this series with."; "The Knowledge
Sharing Effort failed to produce a lasting standard and succeeded in
establishing a lasting architecture." All three cut. One closing now remains,
at the very end, followed only by the one-line handoff to lecture five.

**Continuity.** The opening now places the lecture in the arc and picks up
lecture three's own handoff — lecture three ends "to the moment computer science
needed this word and went looking for it — and to the most expensive experiment
the field has ever run", so lecture four now opens by naming that promise.
Back-references verified: "We took that apart in lecture one" is correct
(COURSE-PLAN lecture one reads Gruber's definition slowly); "the whole subject
of lecture six" is correct (lecture six is description logics and OWL profiles);
"we end the series on it" is correct (lecture ten sources
`notes/llm-ontology-debate.md`); "Next time … the entire World Wide Web" is
correct (lecture five is the Semantic Web). One back-reference was false and is
gone: "the multiple serialisations we covered last lecture" — last lecture was
Quine, and serialisations are lecture five, still ahead. That sentence pointed
backwards at material the listener has not heard yet.

**Format.** No markdown, headings, bullets, code or spoken URLs. Lenat's list of
what common sense requires was a comma run that a narrator would flatten; it is
now short sentences, which is how a list is spoken. No line requires re-reading.

**Claim to retain.** Now matches COURSE-PLAN verbatim in substance: the
computer-science sense was invented to solve a sharing problem between
knowledge-based systems, and its founding project bet everything on a critical
mass it never reached. The previous version had drifted — it said "a sharing
problem, not a reasoning problem" and never used the phrase "critical mass".

## Depth still available

Grounded material in the four permitted notes that the lecture does not yet use.
A later extension pass can draw only from here.

**From `notes/description-logics-dls.md` — most of the note is unused, and this
is the largest untapped seam:**
- The TBox/ABox split: "A TBox states concept hierarchies; an ABox states facts
  about individuals." The lecture never mentions either. (Note: lecture six
  covers this, so an extension here should stay brief or defer.)
- The semantics: "DL semantics interpret concepts as sets of individuals and
  roles as sets of ordered pairs."
- The vocabulary mapping: "Concepts correspond to classes or unary predicates,
  roles to properties or binary predicates, and individuals to constants."
- The four inference tasks: "instance checking, relation checking, subsumption,
  and concept-consistency checking."
- Open world and no unique names: "DL does not generally assume unique names or
  a closed world"; "lack of a fact does not imply its negation, and different
  names need not denote different things."
- The application list, which is useful for showing the reach of the formalism:
  "applications in ontologies, the Semantic Web, biomedical informatics,
  defense, climate modeling, and industrial knowledge graphs."

**From `notes/gruber-ontology-definition.md`:**
- The definition of *conceptualization* itself, which the lecture never states:
  "the objects, concepts, and other entities that are presumed to exist in some
  area of interest and the relationships that hold among them."
- The wording dispute, which is a good twenty seconds of narration: "That
  wording is Gruber's own 2009 restatement; Genesereth and Nilsson's original
  says 'assumed to exist.'"
- The provenance of the second half of the definition: Genesereth and Nilsson
  "describe it as an abstract, simplified view of the world represented for some
  purpose, and who note that every knowledge base is committed to some
  conceptualization whether or not it admits it." That last clause connects
  directly back to lecture three's Quine material.
- Ontological commitment as "an agreement to use a vocabulary consistently".
- Guarino's repair work: Guarino, Oberle and Staab "wrote their 2009 chapter
  largely to repair the informality, noting that all the earlier definitions
  'were assuming an informal notion of conceptualization'." Also "Guarino's
  formal reconstruction of conceptualization as an intensional relational
  structure."
- Gruber's own concession: "the terms specification and conceptualization have
  caused much debate."
- The standing objection Gruber records and rejects, which is the sharpest
  unused item in the note: the definition "is overly broad, allowing for a range
  of specifications from simple glossaries to logical theories couched in
  predicate calculus" — plus the note's own verdict that "in practice it is what
  lets a team call any schema an ontology."
- The forward link to lecture nine: Palantir "sits on top of the digital assets
  integrated into the Palantir platform … and connects them to their real-world
  counterparts" in the same architectural terms, "though Palantir never invokes
  Gruber".

**From `notes/cyc-lenat-1995.md`:**
- The framing question the note says every ontology project faces, which would
  strengthen the lesson section: "how much of the world do we have to write down
  before the model earns its keep?"
- The note's verdict, usable as a reading recommendation: "Worth reading in full,
  and short… every later argument about whether models can replace ontologies is
  arguing with it."

**From `notes/cyc.md`:**
- The named products, which make the commercial story concrete rather than
  abstract: "charge capture, denial management, post-acute-care forecasting, and
  staffing."
- The capability list: "Logic-based machine reasoning; codified common-sense
  knowledge; dynamic real-world data; semantic context; autonomous
  decision-making."
- The deployment framing: "a knowledge and reasoning layer for complex
  operational workloads … using continuously enriched patient and order context
  to make auditable decisions." This is a direct bridge to lecture nine's
  operational-layer argument.
- The note's own scepticism, which the lecture should probably carry if it uses
  any of the above: "The fetched page makes broad product and performance claims
  but provides no technical ontology structure, evaluation details, or
  implementation guidance, so those claims cannot be assessed from this source
  alone."
