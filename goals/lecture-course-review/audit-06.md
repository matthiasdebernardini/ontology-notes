# Audit: lectures/transcripts/06-how-the-machinery-works.txt

Permitted sources: `notes/description-logics-dls.md`, `notes/owl-2-web-ontology-language.md`,
`notes/elk.md`, `notes/hermit.md`, `notes/openllet.md`,
`notes/shacl-shapes-constraint-language.md`, `notes/dl-query-class-expression.md`.

Word count 3,005 → 2,708 (−297, −10%). Correction pass only. Roughly 700 words
of unsupported material were cut and roughly 400 words of note-quoted material
were substituted in their place, so the net change understates the churn.

## Verified

| Claim in lecture | Note | Supporting span |
|---|---|---|
| A description logic is a formal knowledge-representation language, more expressive than propositional logic and less expressive than first-order logic | description-logics-dls.md | "a family of formal knowledge-representation languages, generally more expressive than propositional logic and less expressive than first-order logic" |
| Description logics are the logical foundation of OWL and its profiles | description-logics-dls.md | "The source identifies DLs as the logical foundation for OWL and its profiles" |
| Concepts denote sets; roles denote sets of ordered pairs; individuals denote members | description-logics-dls.md | "DL semantics interpret concepts as sets of individuals and roles as sets of ordered pairs"; "Concepts correspond to classes or unary predicates, roles to properties or binary predicates, and individuals to constants" |
| The TBox states general rules about concepts; the ABox states facts about individuals | description-logics-dls.md | "A TBox states concept hierarchies; an ABox states facts about individuals" |
| A reasoner computes subsumption, instance checking, and consistency | description-logics-dls.md | "Common inference tasks include instance checking, relation checking, subsumption, and concept-consistency checking" |
| Classification is a standard reasoner operation producing an inferred hierarchy | elk.md / openllet.md / hermit.md | ELK "can classify an ontology and produce a taxonomy"; Openllet: "computing a class hierarchy (optionally with instances)"; HermiT "can check consistency, identify class subsumption relationships, classify ontologies" |
| Classification is the button you press in an editor and the inferred hierarchy is what you read afterwards | dl-query-class-expression.md | "Start FaCT++ or HermiT to classify the active ontology, confirm that the inferred class hierarchy is populated" |
| Finding unsatisfiable concepts is a separate service reasoners list | openllet.md | "deciding whether an ontology is consistent, finding unsatisfiable concepts, computing a class hierarchy" |
| OWL is open-world: not stated means unknown, not false | description-logics-dls.md | "DL does not generally assume unique names or a closed world"; "lack of a fact does not imply its negation" |
| No unique name assumption: two identifiers may denote one thing | description-logics-dls.md | "different names need not denote different things" |
| SHACL is a W3C recommendation constraining an RDF graph's content, structure and meaning | shacl-shapes-constraint-language.md | "a W3C Recommendation for describing RDF graphs through constraints on their content, structure, and meaning" |
| You write shapes, say what they target, feed in a data graph and a shapes graph, get a report with severities | shacl-shapes-constraint-language.md | "Validation consumes a data graph and a shapes graph and emits an RDF validation-report graph with severities such as Violation, Warning, and Info"; "targets select where shapes apply" |
| Adding operators and complicating the hierarchy usually increases the computational complexity of inference | description-logics-dls.md | "Adding operators and making the TBox more complicated usually increases the computational complexity of inference" |
| Many core reasoning problems in the family are decidable, by deliberate balance | description-logics-dls.md | "while balancing expressive power against reasoning complexity; many core reasoning problems are decidable" |
| OWL 2 has three profiles, EL, QL and RL, each restricting expressivity for one stated benefit | owl-2-web-ontology-language.md | "The EL, QL, and RL profiles restrict expressivity to gain particular computational or implementation benefits: large-ontology reasoning, relational querying, or rule-based RDF processing" |
| EL buys large-ontology reasoning; QL buys relational querying; RL buys rule-based RDF processing | owl-2-web-ontology-language.md | same span as above |
| ELK implements a polynomial-time procedure for a fragment of OWL 2 EL | elk.md | "It implements a polynomial-time, goal-directed consequence-based procedure for a fragment of OWL 2 EL" |
| ELK can use several cores, and recomputes only what depended on changed axioms, giving near-real-time hierarchy updates | elk.md | "it can use multiple processor cores"; "recomputes only results that depend on those axioms, which can make class-hierarchy updates nearly real time in many cases" |
| Rule-based OWL 2 RL reasoning is sound but may be incomplete outside the structural definition and query conditions | owl-2-web-ontology-language.md | "Rule-based OWL 2 RL reasoning over an arbitrary RDF graph is sound but may be incomplete unless the ontology meets the RL structural definition and the stated query conditions" |
| HermiT uses a hypertableau calculus and works to the direct semantics | hermit.md | "based on a hypertableau calculus"; "The site emphasizes OWL 2 direct semantics" |
| HermiT's authors claim it passes all OWL 2 conformance tests for direct-semantics reasoners | hermit.md | "says HermiT passes all OWL 2 conformance tests for direct-semantics reasoners" |
| Openllet is a Java OWL 2 DL reasoner doing consistency, unsatisfiable concepts, classification, entailment, explanation, and query answering | openllet.md | "ontology consistency checking, taxonomy/class-hierarchy classification, entailment checking, inference explanations, and SPARQL or SPARQL-DL query answering" |
| The performance triggers: general concept inclusions, large disjunctions, large cardinalities, interacting existential restrictions, large different-individual sets | openllet.md | "general concept inclusions, large disjunctions, large cardinalities, interacting existential restrictions, and large `DifferentIndividuals` sets" |
| Those constructs cause nondeterminism, generated individuals, or high memory use in tableau reasoning | openllet.md | "can create nondeterminism, generated individuals, or high memory use in tableau-based reasoning" |
| Openllet ships a lint tool for exactly these patterns, whose repairs are not semantically equivalent and whose findings are often warnings requiring remodelling | openllet.md | "Pellint explicitly warns that its repairs are not semantically equivalent to the constructs they replace"; "several Pellint findings are warnings only and require remodeling the ontology" |
| Reasoners implement explanation: step-by-step derivation of a consequence from axioms | elk.md / openllet.md | ELK "can show, step by step, how a logical consequence follows from ontology axioms"; Openllet: "explaining inferences" |
| Choose a profile when its stated trade-off matches the application | owl-2-web-ontology-language.md | "Select EL, QL, or RL when its stated performance/implementation trade-off matches the application" |

## Cut

| Cut text (verbatim) | Reason |
|---|---|
| "OWL 2 EL is designed for large biomedical ontologies." | Unsupported. The OWL 2 note says EL buys "large-ontology reasoning" with no domain attached. `description-logics-dls.md` lists "biomedical informatics" as an application of DLs generally, not as EL's design target. Replaced with the note's wording. |
| "It gives up disjunction, negation, and universal restrictions" | Unsupported. No permitted note states what EL drops. |
| "in return classification runs in polynomial time. That's why a reasoner like ELK can classify an ontology with hundreds of thousands of classes in seconds." | Wrong attribution plus an invented number. The ELK note grants a polynomial-time procedure to ELK for *a fragment* of OWL 2 EL, not to profile classification in general, and states no scale or timing figure anywhere. |
| "The Gene Ontology and its relatives live here, and the restrictions turn out not to hurt, because biology mostly wants 'this is a kind of that, and it participates in this process.'" | Unsupported. The Gene Ontology appears in no permitted note; the claim that it sits in EL appears nowhere in the repository. |
| "queries against an ontology can be rewritten into ordinary database queries and run against your existing relational store. You keep your data where it is, and the ontology becomes a query rewriting layer." | Unsupported mechanism. The note says only "relational querying". |
| "designed to be implementable as forward-chaining rules over RDF" / "A library called OWL-RL does exactly that." | "Forward-chaining" and the OWL-RL library are not in any permitted note. |
| "Description logic research spent two decades charting this landscape" | Unsourced number, and it contradicts lecture five, which says "their thirty years of work". |
| "and every conclusion follows from it, so every answer it gives you is worthless" | Ex falso quodlibet stated as if sourced. In no permitted note. |
| "and it usually means two of your restrictions contradict each other" | Narrator's inference presented as fact about unsatisfiability. |
| "use SHACL or ShEx" | ShEx is in no permitted note for this lecture. |
| "and if your ontology says a person has exactly one employee number, and those two identifiers have different numbers, the reasoner will conclude they must be different individuals" | Unsupported derivation (requires functionality assumptions no note states), and it was a second-pass splice that broke the paragraph's build to its punchline. |
| "A biomedical terminology with half a million classes" | Invented number plus the same unsupported biomedical/EL link. |
| "and it's worth confirming that you do, because a surprising number of ontologies that use DL features never ask a question that depends on them" | Unsupported empirical claim about the field. |
| "given an inferred statement, produce a minimal set of axioms that entails it. Minimal meaning that if you removed any one of them, the conclusion would no longer follow." | The word "justification" and the minimality property appear in no permitted note. The notes document "explanations" — a step-by-step derivation. Replaced with what the notes actually claim. |
| "The materialised graph can be much bigger than the source — a transitive relation over a deep hierarchy explodes combinatorially." / "which is a genuinely hard problem called truth maintenance" | Unsupported. "Truth maintenance" appears nowhere in the seven notes. |
| "In practice most large deployments materialise a tractable profile nightly and accept the limits, because predictable query performance beats expressive power in production. That is a very common shape for this technology to take in the wild, and it's worth knowing that the theoretically interesting part often gets run in a batch job at two in the morning." | Unsupported empirical claim about deployments. |
| The whole punning section (three paragraphs, "OWL has a feature called punning…" through "…rather than relying on a pun") | Punning is in no permitted note. The OWL 2 note's list of OWL 2 additions is "keys, property chains, richer datatypes, qualified cardinalities, additional property characteristics, and enhanced annotations" — punning is not among them. "That confusion … has a proper name in the literature, and it's the class-instance mismatch" is likewise unsupported; the only repository mention of punning is in the Owlready2 note, not a source for this lecture. |
| "Reasoners are not uniformly slow. They're fast on most real ontologies and catastrophic on a small number of specific patterns" | Unsupported empirical claim, and the paragraph it opened restated the trigger list already given earlier in the lecture. |
| "High cardinality restrictions — this thing has at least fifty of those — force it to construct fifty distinct individuals to check." / "many assertions that individuals are pairwise different produce a quadratic pile of work" | Invented numbers and an invented complexity class. The grounded mechanism ("generated individuals", "high memory use", "nondeterminism") was kept in the single surviving treatment. |
| The whole modularity paragraph ("Which brings me to modularity … without inheriting its whole reasoning cost.") including the ROBOT module-extraction claim and "two hundred terms instead of two hundred thousand" | No permitted note covers modularity, imports, or ROBOT. ROBOT is a lecture-seven source. Would require a new note. |

## Corrected

| Before | After | Forcing span |
|---|---|---|
| "in return classification runs in polynomial time. That's why a reasoner like ELK can classify an ontology with hundreds of thousands of classes in seconds." | "ELK is a reasoner built for that profile … it implements a polynomial-time procedure for a fragment of OWL 2 EL, it can put several processor cores on the job at once, and when your axioms change it recomputes only the results that depended on them, which can bring a class-hierarchy update to something near real time." | elk.md: "a polynomial-time, goal-directed consequence-based procedure for a fragment of OWL 2 EL"; "can use multiple processor cores"; "recomputes only results that depend on those axioms, which can make class-hierarchy updates nearly real time in many cases" |
| "The caveat in the specification is worth knowing: rule-based RL reasoning can be sound but incomplete outside the structural conditions the spec sets out" | "Rule-based OWL 2 RL reasoning over an arbitrary RDF graph is sound, but it may be incomplete unless the ontology meets the RL structural definition and the query conditions the spec sets out." | owl-2-web-ontology-language.md, near-verbatim |
| "Openllet, which offers broad OWL 2 DL services" | "Openllet is a Java reasoner for OWL 2 DL that will check whether an ontology is consistent, find the unsatisfiable concepts, compute the class hierarchy, check whether an axiom is entailed, explain an inference, and answer queries." | openllet.md **What it is** and **Key concepts** |
| "large disjunctions, high cardinality restrictions, deep existential expansion, and many assertions that individuals are different from one another" | "General concept inclusions. Large disjunctions. Large cardinalities. Interacting existential restrictions. And large sets of assertions that individuals are all different from one another." | openllet.md: the list is five items, not four; GCIs were missing and "deep existential expansion" is the note's "interacting existential restrictions" |
| "Every operator you add … moves the worst-case complexity of reasoning up a rung" | "adding operators, and letting the concept hierarchy get more complicated, usually increases the computational complexity of inference" | description-logics-dls.md: the note says "usually increases", not "every operator … up a rung" |
| "So reasoners and editors implement justification" | "So the reasoners implement explanation. ELK will show you, step by step, how a logical consequence follows from your axioms. Openllet lists explaining inferences as one of its services…" | elk.md **Explanations**; openllet.md "explaining inferences" |
| "That's the most valuable error message in the field." | "I'd argue that's the most valuable error message in the field." | Unsourced superlative → marked as the narrator's |
| "The second thing is the choice between materialising and querying, because it's the main architectural decision you'll actually make." | "The second thing is the choice between computing entailments ahead of time and computing them when asked. This part is my own engineering reading rather than anything the specifications hand you, so take it as that." | No note covers the materialise-versus-query trade → surviving compressed version is marked as the narrator's own |
| "Here's why. The Semantic Web was built for a web of anonymous publishers." | "Here's why, and it goes straight back to last time. The Semantic Web was built for a web of strangers publishing independently." | The rationale belongs to lecture five's sources, not lecture six's; converted from bare assertion to an explicit back-reference that lecture five does support ("OWL was built for an open web where any publisher might hold the missing fact") |

## Narration fixes

**Acronyms.** DL was used at "full OWL 2 DL" and "Full DL" with no expansion anywhere
in the file; OWL was never expanded at all. Both now land in the first paragraph
of the mental-model section: "A description logic — DL for short … the logical
foundation of OWL, the Web Ontology Language." SHACL was named three times and
never expanded; it is now "the Shapes Constraint Language". RDF and W3C entered
with the SHACL definition and are now "RDF, the Resource Description Framework"
and "the World Wide Web Consortium". EL, QL and RL are introduced together —
"the specification names them by letters: EL, QL, and RL" — and each then gets
its one-line gloss from the note ("EL buys reasoning over large ontologies", and
so on), which is the only expansion the permitted notes license. TBox and ABox
were already glossed in place. RBox, SPARQL, OWA and UNA do not occur in the
file, so nothing was added for them.

**Numbers and Latin.** "the 2001 Semantic Web article" was the only digit string
in the file; it is now "the Scientific American article of two thousand and one",
matching the spelled-out convention of lectures two and four. No Latin
abbreviations were present. "Ex falso quodlibet" reasoning was present in
paraphrase and was cut for grounding reasons, not spelling ones.

**Markup and syntax read aloud.** "aircraft AND have more than one aisle" and
"flights AND whose assigned aircraft is a widebody" read as Manchester-syntax
operators in shouted capitals; both are now ordinary prose conjunctions. No
headings, bullets, code, or URLs were present.

**Seams.** The file had a clear second-pass splice. Four repairs:

1. "One more thing before I close" appeared with roughly forty percent of the
   lecture still to run. Now "Now, something about what reasoners are actually
   good for in practice".
2. "Let me give you two more things" was followed by three more things — the two
   promised, then a punning section, then a performance section, then modularity.
   The punning and modularity sections are gone on grounding grounds, so the
   promise is now kept exactly.
3. The performance section restated the reasoner-cliff trigger list already given
   in the OWL 2 DL paragraph, in different and less accurate words. The two
   treatments are merged into one, at the earlier position, using the note's
   five-item list and the note's mechanism ("nondeterminism, generated
   individuals, or high memory use"). The diagnostic line — "the diagnostic is
   not 'reasoners are slow.' It's: which one of those did I just add?" — was kept
   and moved up into the merged paragraph.
4. The no-unique-name paragraph had a clause spliced in before its punchline
   that ran the inference in the opposite direction, then said "It can also run
   the other way" — leaving the listener with three directions and no punchline.
   The splice is cut and the paragraph now builds to the "two names, one
   aircraft" case in one move.

**Endings.** The file had three closing gestures: "One more thing before I
close" (mid-file), "Let me close the technical part with something practical
about performance" (also mid-file), and the actual claim-to-keep. Both orphans
are gone. The single closing is now at the very end and states the plan's claim
in the plan's terms: "Open-world semantics is the single idea that most often
breaks a database engineer's intuition, and every strange behaviour of a reasoner
follows from it." The previous closing stacked four separate claims — sets and
pairs, TBox and ABox, open world, expressivity-versus-computation — which is a
summary, not a claim to retain; the machinery items are now demoted in one clause
so the open-world claim lands alone.

**Continuity.** The opening back-reference was checked against lecture five and
is accurate: lecture five does walk the stack layer by layer and does derive each
layer from the two-thousand-and-one article's requirements. Lecture five also
promises "lecture six explains that trade properly" about the profiles, which
lecture six now does with the note's own wording, and ends with "we open the box
and … meet the one assumption that breaks everybody's intuition" — which is the
open-world material this lecture leads with. One inherited inconsistency was
removed: lecture five says the description-logic community had "thirty years of
work"; lecture six said the research "spent two decades" charting complexity.
The number is gone. The forward-reference to lecture seven ("a governance project
with a file attached") matches the plan's claim for lecture seven verbatim.

## Depth still available

Grounded material in the seven permitted notes that the lecture does not yet use.

**`notes/dl-query-class-expression.md` is entirely unused.** It is a listed source
and contributes nothing at present. It supports a whole beat on how you actually
interrogate a classified ontology: "The DL Query tab is a Protégé Desktop feature
for searching a classified ontology with class expressions based on Manchester
OWL syntax"; "Queries can retrieve individuals or classes according to inferred
relationships, including subclasses and superclasses of an expression"; "A useful
query can be added to the ontology as a newly named defined OWL class." It also
supplies two grounded failure modes for the "why is nothing coming back" case:
"Queries only run on a classified ontology, and individual matches are not shown
unless the 'Individuals' result option is checked"; "If the inferred hierarchy
contains only `Thing`, the ontology may not have been classified successfully."
And it names a fourth reasoner: "Start FaCT++ or HermiT to classify the active
ontology." Note the narration constraint: any Manchester expression must be
spoken as prose.

**Relation checking is a missing inference task.** The lecture says "four things,
mainly" and lists subsumption, classification, instance checking and consistency.
`description-logics-dls.md` lists "instance checking, relation checking,
subsumption, and concept-consistency checking". Relation checking — does this
pair stand in this role — is grounded and absent.

**A grounded unintended-entailment example.** `openllet.md`: "defining a named
class as equivalent to an `allValuesFrom` restriction may classify things with no
value for that property under the named class." This is a concrete open-world
surprise, sourced, and stronger than the invented order/line-item case because it
is documented behaviour rather than illustration.

**Axiom-level versus ontology-level patterns.** `openllet.md`: "Pellint
distinguishes axiom-level modeling patterns from patterns established across a
whole ontology." That distinction supports the "which of those did I just add"
diagnostic and is not used.

**HermiT's rule-reasoning limit.** `hermit.md`: "Reasoning with DL Safe rules is
incomplete when the ontology has property chains or transitivity axioms and rule
bodies use complex properties." A second, independently sourced instance of the
sound-but-incomplete pattern the RL paragraph already establishes — and it lands
on a DL reasoner, which makes the point general. `hermit.md` also documents DL
Safe rules as a supported feature, which the lecture never mentions.

**Two semantics, and the syntactic price of OWL 2 DL.**
`owl-2-web-ontology-language.md`: "Direct Semantics supports OWL 2 DL and
description-logic reasoning, while RDF-Based Semantics applies to any OWL 2
ontology as an RDF graph", and "OWL 2 DL requires syntactic conditions — for
example, transitive properties cannot appear in number restrictions." Lecture
five sets up the two-semantics split as a negotiated settlement; lecture six
currently says "works to the direct semantics" without cashing out what the
restriction costs the author. The transitivity-in-cardinality rule is a concrete,
sourced example of a decidability boundary.

**OWL 2's additions over OWL 1.** `owl-2-web-ontology-language.md`: "keys,
property chains, richer datatypes, qualified cardinalities, additional property
characteristics, and enhanced annotations." Keys in particular bear directly on
the no-unique-name section — they are the sourced mechanism for saying when two
identifiers denote one thing — and would replace the employee-number clause that
had to be cut.

**Syntaxes as spelling.** `owl-2-web-ontology-language.md`: "RDF/XML is the
mandatory interchange syntax for conformant tools; OWL/XML, Functional Syntax,
Manchester Syntax, and Turtle serve other processing or readability needs." Pairs
with `elk.md`: "The standalone CLI cannot parse RDF/XML and accepts only OWL 2
Functional-Style Syntax, so other OWL formats must first be converted." That is a
real, sourced operational trap.

**Operational friction as a theme.** `elk.md`: "larger classifications may also
require increasing the Java heap." `openllet.md`: "Since 2.6.5, Java 11 is
required"; "The documented Protégé plugin requires a Protégé version using OWL
API 5.1.x and is not compatible with Protégé's main branch"; and the README
"needs 'a lot more tests.'" `hermit.md`: "The documented OWL API compatibility
excludes 3.0.x, and Protégé alpha/beta versions require different HermiT lines";
"nightly builds are experimental and not guaranteed to work"; the documented
release is "HermiT 1.3.8, built on OWL API 3.4.3". None of this is in the
lecture, and together it grounds a short, honest beat about version compatibility
being the day-to-day cost of this stack.

**SHACL depth.** `shacl-shapes-constraint-language.md` supports considerably more
than the lecture uses: "It supports built-in constraints, extension through
SPARQL or JavaScript, and SHACL Rules for inferring new statements" — SHACL Rules
is a sourced complication of the clean "reasoner infers, SHACL validates" split
the lecture draws. Also "Node shapes constrain nodes, property shapes constrain
values reached through paths", the constraint kinds ("datatype, minimum count,
length, ranges, patterns, and logical combinations"), and two sourced pitfalls:
"Targeting a class also targets members of its subclasses through
`rdfs:subClassOf`" and "When a property shape is included by a node shape, the
property shape's own targets are ignored, so placement changes targeting
behaviour."

**Where description logics are actually used.** `description-logics-dls.md`:
"applications in ontologies, the Semantic Web, biomedical informatics, defense,
climate modeling, and industrial knowledge graphs." This is the sourced way to
talk about biomedical work, as an application area of DLs, not as EL's design
brief.

**Openllet's query story.** `openllet.md` documents "SPARQL or SPARQL-DL query
answering through Jena, OWL API, or its command-line interface." The lecture's
materialise-versus-query section talks about querying with a reasoner in the loop
without naming the sourced example of a reasoner that does it. Note that SPARQL
would then need expanding on first use.
