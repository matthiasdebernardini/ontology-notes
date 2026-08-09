# Evidence map

Grounding audit of the thirteen notes added in the history/criticism/Palantir pass, and of
the 26 hand-written `CONCEPTS` glossary definitions in `scripts/build_site.py`.

`research/` and `sources/` are gitignored and do not survive a clone, so every verdict below
quotes the supporting span rather than pointing at a local path.

Verdicts: **SUPPORTED** (a capture states it, span quoted) · **PARTIAL** (capture says
something weaker or different) · **UNSUPPORTED** (no capture states it) · **CONTRADICTED**
(a capture says otherwise) · **EDITORIAL** (the note's own reasoning, now marked as such in
the note text).

Rows marked *(fixed)* were changed in this run. Rows with no marker were verified and left
alone — the absence of a change is a finding, not an omission.

---

## Part 1 — Capture inventory

Three scrapes in the original run failed. All three are confirmed dead, and none is now
load-bearing:

| capture | size | what it actually contains | consequence |
| --- | --- | --- | --- |
| `research/firecrawl/ai-cyc-sowa-review.md` | 248 B | 41 repetitions of `\[Image: Im1\]` and a broken LaTeX fragment | cited by no note; no claim rests on it |
| `research/firecrawl/crit-torquing-review.md` | 226 B | `# Error 404: Page Not Found / MIT Anthropology` | was the intended source for the *torque* definition; **re-fetched** (below) |
| `research/firecrawl/pltr-crit-seer-seen.md` | 63 B | `# Forbidden / You don't have permission to access this resource.` | cited by no note; now listed as a failed scrape |

A fourth capture was found dead on inspection and had not been flagged:

| `research/firecrawl/semweb-sciam-2001.md` | 6.3 KB / 649 words | Scientific American paywall shell: masthead, newsletter signup, editor's letter, "Popular Stories". No article body. Zero occurrences of "Pete" or "Lucy". | the Pete-and-Lucy scenario and every content claim about the 2001 article traced only to this; **re-fetched** (below) |

### Re-fetches performed in this run

Stored as new captures under `research/firecrawl/` and `research/dblp/`.

| new capture | source | what it grounds |
| --- | --- | --- |
| `semweb-sciam-2001-fulltext.md` | archived PDF of the article at `www-sop.inria.fr/acacia/cours/essi2006/` | the full 2001 article text, 4,789 words, Pete-and-Lucy scenario included |
| `crit-torquing-review-refetch.md` | Internet Archive copy of Helmreich, "Torquing Things Out" | the *torque* definition, verbatim, with page references to the book |
| `pltr-crit-bverfg-pressrelease.md` | `bundesverfassungsgericht.de` press release for the judgment of 16 February 2023 | the German constitutional ruling: which provisions, which remedy, the "one click" quote |
| `semweb-twobithistory-about.md` | `twobithistory.org/about.html` | the byline "My name is Sinclair Target." |
| `research/dblp/lenat-cyc-1995.json` | DBLP publication record | *Commun. ACM* 38(11), 1995 for the Lenat article |

No re-fetch failed, so no claim was cut for want of a source. Two claims were cut for other
reasons (§ Part 3, items 4 and 10).

### URL → capture map

Every URL in every `## Sources consulted` block, after this run's edits.

| note | cited URL | capture | status |
| --- | --- | --- | --- |
| ontology-word-history | britannica.com/topic/ontology-metaphysics | `phil-britannica.md` | ok |
| ontology-word-history | ferratermora.org/essa_ontology.html | `phil-ferratermora.md` | ok |
| ontology-word-history | etymonline.com/word/ontology | `phil-etymonline.md` | ok (capture existed but was unlisted; *fixed*) |
| ontology-word-history | iaoa.org/…/Guarino2009_What_is_an_Ontology.pdf | `guarino-what-is-ontology.md` | ok (was unlisted; *fixed*) |
| ontology-word-history | — | `gruber-onto-design.md` | added: the note leans on it for "designed artifacts" (*fixed*) |
| quine | rintintin.colorado.edu/…/Quine.pdf | `quine-onwhatthereis.md` | ok |
| quine | plato.stanford.edu/entries/ontological-commitment/ | `quine-sep-commitment.md` | ok |
| quine | iaoa.org/…Guarino2009… | `guarino-what-is-ontology.md` | ok (was unlisted; *fixed*) |
| gruber | tomgruber.org/writing/definition-of-ontology/ | `gruber-definition.md` | ok |
| gruber | tomgruber.org/writing/onto-design.pdf | `gruber-onto-design.md` | ok (was unlisted; *fixed*) |
| gruber | iaoa.org/…Guarino2009… | `guarino-what-is-ontology.md` | ok |
| gruber | — | `pltr-ontology-overview.md` | added for the Palantir sentence (*fixed*) |
| cyc-lenat-1995 | faculty.cc.gatech.edu/…/lenat95cyc.pdf | `ai-lenat-cyc95.md` | ok |
| cyc-lenat-1995 | dblp.org/rec/journals/cacm/Lenat95 | `research/dblp/lenat-cyc-1995.json` | **new** — the capture carries no date; venue/year had no source (*fixed*) |
| semweb-2001 | scientificamerican.com/article/the-semantic-web/ | `semweb-sciam-2001.md` | **paywall stub**, now labelled as such in the note |
| semweb-2001 | www-sop.inria.fr/…Semantic%20Web…pdf | `semweb-sciam-2001-fulltext.md` | **new** (*fixed*) |
| semweb-2001 | twobithistory.org/2018/05/27/semantic-web.html | `semweb-twobithistory.md` | ok (was unlisted; *fixed*) |
| semweb-2001 | cs.ox.ac.uk/…/HoPH03a.pdf | `semweb-making-of-owl.md` | added for the open-world claim (*fixed*) |
| retrospective | twobithistory.org/2018/05/27/… | `semweb-twobithistory.md` | ok |
| retrospective | twobithistory.org/about.html | `semweb-twobithistory-about.md` | **new**, for the byline (*fixed*) |
| retrospective | semantic-web-journal.net/…/swj2303.pdf | `semweb-two-decades-on.md` | ok |
| retrospective | ontotext.com/blog/the-semantic-web-20-years-later/ | `semweb-ontotext-20yr.md` | ok |
| retrospective | cs.ox.ac.uk/…/HoPH03a.pdf | `semweb-making-of-owl.md` | ok |
| kg-turn | arstechnica.com/…/googles-knowledge-graph-and-microsofts-satori/ | `kg-arstechnica-2012.md` | ok |
| kg-turn | vldb.org/pvldb/vol16/p4130-dong.pdf | `kg-generations-vldb.md` | ok |
| kg-turn | technologyreview.com/2012/06/14/19504/… | **no firecrawl capture**; full text present in `research/exa/kg-revival.json` | exa file now listed (*fixed*) |
| doctorow | well.com/~doctorow/metacrap.htm | `crit-doctorow-metacrap.md` | ok |
| doctorow | chnm.gmu.edu/…/8_17.pdf | same file (print-paginated, so it is plausibly the PDF) | only one Doctorow capture exists for two listed URLs; not separable |
| shirky | shirky.com/essays/ontology-is-overrated-… | `crit-shirky-overrated.md` | ok |
| shirky | shirky.com/essays/the-semantic-web-syllogism-… | `crit-shirky-syllogism.md` | ok |
| shirky | semanticarts.com/shirky-syllogism-and-the-semantic-web/ | `crit-semanticarts-reply.md` | ok (was unlisted; *fixed*) |
| bowker-star | mitpress.mit.edu/9780262522953/sorting-things-out/ | `crit-sorting-things-out.md` | publisher page only: date, authors, case-study list |
| bowker-star | nehrlich.com/book/sortingthingsout.html | `research/.firecrawl/nehrlich.com-…md` | ok (was unlisted; *fixed*) |
| bowker-star | faculty.washington.edu/tabrooks/…/bowkerReview.htm | `research/.firecrawl/faculty.washington.edu-…md` | ok (was unlisted; *fixed*) |
| bowker-star | muse.jhu.edu/article/44230 | `crit-torquing-review-refetch.md` | **new** (*fixed*) |
| palantir | six palantir.com docs URLs | `pltr-ontology-system/-overview/-object-types/-link-types/-action-types/-platform-ontology.md` | ok; `pltr-platform-ontology.md` was unlisted (*fixed*) |
| palantir | blog.palantir.com/connecting-ai-to-decisions-… | `pltr-blog-ai-decisions.md` | **was load-bearing and entirely unlisted** (*fixed*) |
| palantir | palantir.com/docs/foundry/object-link-types/type-reference/ | `research/exa/palantir-ont.json` | added (*fixed*) |
| palantir-critique | doi.org/10.1080/1369118X.2024.2410255 | `pltr-crit-polintel.md` | ok |
| palantir-critique | bundesverfassungsgericht.de/…/bvg23-018.html | `pltr-crit-bverfg-pressrelease.md` | **new** (*fixed*) |
| palantir-critique | wired.com/story/palantir-germany-gotham-dragnet/ | `pltr-crit-wired-germany.md` | ok |
| palantir-critique | theconversation.com/…-263178 | `pltr-crit-conversation.md` | exists; supports no claim in the note |
| llm-debate | vldb.org/pvldb/vol17/p2919-sun.pdf | `llm-taxonomies-vldb.md` | ok |
| llm-debate | keet.wordpress.com/2025/03/26/… | `llm-keet-ontology.md` | ok |
| llm-debate | aclanthology.org/2025.emnlp-main.1674/ | **exa only** — `research/exa/llm-ont.json` result 5 | exa file now listed (*fixed*) |
| llm-debate | arxiv.org/abs/2511.05991v1 | **exa only** — `research/exa/llm-ont.json` result 8 | exa file now listed (*fixed*) |

No cited URL is left without a capture.

---

## Part 2 — Load-bearing claims, with spans

### notes/ontology-word-history.md

| claim | verdict | span |
| --- | --- | --- |
| Aristotle called it "first philosophy" in Book IV of the *Metaphysics* | SUPPORTED | "It was called 'first philosophy' by Aristotle in Book IV of his *Metaphysics*." — Britannica |
| "being qua being" and its gloss | SUPPORTED, now attributed *(fixed)* | "Aristotle … defined Ontology as the science of 'being qua being' … the study of attributes that belong to things because of their very nature." — Guarino, Oberle and Staab |
| trailing clause "rather than because of what kind of thing it happens to be" | UNSUPPORTED — **cut** *(fixed)* | no capture carries the contrast |
| Lorhard, *Ogdoas Scholastica*, 1606 | SUPPORTED, but priority contested *(fixed)* | "The Latin term *ontologia* … was felicitously invented by the German philosopher Jacob Lorhard … and first appeared in his work *Ogdoas Scholastica* (1st ed.) in 1606." — Britannica |
| Goclenius, *Lexicon philosophicum*, 1613 | SUPPORTED, and it is a rival priority claim, not a sequel *(fixed)* | "The first instance occurs in Rudolf Goclenius (*Lexicon philosophicum* … Francoforti, 1613)." — Ferrater Mora |
| "Clauberg is often credited but came later" | SUPPORTED, now named *(fixed)* | "A number of historians (R. Eucken, E. Gilson, Hans Pichler, Max Wundt, Heinz Heimsoeth) mention Johann Clauberg as the first philosopher who used the new term … This is not the case." — Ferrater Mora |
| Wolff 1730, *Philosophia prima sive ontologia* | SUPPORTED | "It entered general circulation after being popularized by … Christian Wolff … especially *Philosophia Prima sive Ontologia* (1730)." — Britannica |
| *scientia entis in genere, quatenus ens est* | SUPPORTED | "*Ontologia seu philosophia prima* is defined as *scientia entis in genere, quatenus ens est*" — Ferrater Mora |
| "Wolff's demonstrative method" | SUPPORTED, now quoted *(fixed)* | "Ontology uses a 'demonstrative [i.e., rational and deductive] method'" — Ferrater Mora |
| general vs special metaphysics, "(souls, world, God)" | PARTIAL — **re-worded to Britannica** *(fixed)* | "Wolff contrasted ontology, or general metaphysics, which applied to all things, with special metaphysical theories such as those of the soul, of bodies, or of God." |
| "the direct ancestor of the split between upper ontologies such as BFO and domain ontologies such as GO" | UNSUPPORTED — **cut, replaced with a marked editorial resemblance** *(fixed)* | "BFO" appears in **zero** captures; "Gene Ontology" appears in no cited capture. Nearest available: "the primary purpose of top-level ontologies lies in providing a broad view of the world suitable for many different target domains" — Guarino, Oberle and Staab |
| Kant's attack | SUPPORTED | "Kant launched an epoch-making attack against rational ontology in the sense of Wolff and Baumgarten" — Ferrater Mora |
| Husserl's "formal ontology"; Heidegger's *Dasein* | SUPPORTED | "Edmund Husserl, who called Wolff's general metaphysics 'formal ontology'"; "the analysis of human existence, or *Dasein* (Martin Heidegger)" — Britannica |
| "Wolff's ontology aimed to be the single true account of being" | PARTIAL — **trimmed to the deductive half** *(fixed)* | only the method is sourced |
| "vendors slide between the two senses … smuggles in a claim of objectivity" | EDITORIAL — **now marked as the author's warning** *(fixed)* | — |

### notes/quine-ontological-commitment.md

| claim | verdict | span |
| --- | --- | --- |
| 1948, "On What There Is" | SUPPORTED | "Quine, W. V., 1948, 'On What There Is', *The Review of Metaphysics*" — SEP |
| the denial problem | SUPPORTED | "I cannot admit that there are some things which McX countenances and I do not, for in admitting that there are such things I should be contradicting my own rejection of them." |
| the criterion itself | SUPPORTED, now quoted *(fixed)* | "a theory is committed to those and only those entities to which the bound variables of the theory must be capable of referring in order that the affirmations made in the theory be true." |
| **the slogan "to be is to be the value of a *bound* variable"** | **CONTRADICTED — corrected** *(fixed)* | Quine writes "the semantical formula 'To be is to be the value of a variable'". The "bound variable" phrasing is Boolos's 1984 title, "To Be is To Be the Value of A Variable (or To Be Some Values of Some Variables)", quoted in the SEP entry. |
| regimenting into first-order logic | SUPPORTED | "first, regiment the competing theories in first-order predicate logic" — SEP |
| ontology as a property of language | SUPPORTED | "We look to bound variables in connection with ontology not in order to know what there is, but in order to know what a given remark or doctrine … says there is" |
| silence about truth | SUPPORTED, now quoted *(fixed)* | "how are we to adjudicate among rival ontologies? Certainly the answer is not provided by the semantical formula 'To be is to be the value of a variable'" |
| **"Guarino's formal treatment … is the direct descendant of this idea"** | **UNSUPPORTED — cut** *(fixed)* | `guarino-what-is-ontology.md` contains zero occurrences of "Quine". Replaced with a marked structural resemblance. |
| **"…and is what OWL's model-theoretic semantics implements"** | **UNSUPPORTED — cut** *(fixed)* | Guarino's only OWL mention is "languages from the family of description logics (DL) … e.g., OWL-DL … are strict subsets of first-order logic." Nothing about implementing ontological commitment. |
| Guarino's commitment as "a mapping from a vocabulary to an intended set of models" | PARTIAL — **re-worded** *(fixed)* | Def 3.2 maps to intensional relations: "a total function I : V → D ∪ ℑ that maps each vocabulary symbol of V to either an element of D or an intensional relation". Intended models are derived (Def 3.3). |
| "ontology alignment is a permanent engineering problem" | EDITORIAL — **marked** *(fixed)* | nearest span: "Disagreement in ontology involves basic disagreement in conceptual schemes; yet McX and I, despite these basic disagreements, find that our conceptual schemes converge" |

### notes/gruber-ontology-definition.md

| claim | verdict | span |
| --- | --- | --- |
| 1993 | SUPPORTED | "In 1993, Gruber originally defined the notion of an ontology as an 'explicit specification of a conceptualization'" — Guarino et al. |
| "an explicit specification of a conceptualization" | SUPPORTED | verbatim in both Gruber captures |
| the conceptualization wording | SUPPORTED, provenance corrected *(fixed)* | the note's "presumed to exist" is Gruber's 2009 restatement; Genesereth and Nilsson's original is "**assumed** to exist" |
| "the DARPA Knowledge Sharing Effort" | PARTIAL — **re-worded to "ARPA (later DARPA)"** *(fixed)* | Gruber's own acknowledgement says "ARPA Knowledge Sharing Effort"; the reference list carries "Patil, R. S., … (1992). The DARPA Knowledge Sharing Effort: Progress report." |
| Genesereth and Nilsson attribution | SUPPORTED | "A conceptualization is an abstract, simplified view of the world that we wish to represent for some purpose." |
| "every knowledge base is committed … whether or not it admits it" | SUPPORTED | "Every knowledge base, knowledge-based system, or knowledge-level agent is committed to some conceptualization, explicitly or implicitly." |
| Borst 1997 "shared", adds consensus | SUPPORTED | "In 1997, Borst defined an ontology as a 'formal specification of a shared conceptualization'… a consensus rather than an individual view." |
| interface, not internal encoding | SUPPORTED, now quoted *(fixed)* | "The agents sharing a vocabulary need not share a knowledge base; each knows things the other does not" |
| "Guarino wrote a paper" | PARTIAL — **three authors** *(fixed)* | the chapter is Guarino, Oberle and Staab (2009) |
| "the common failure where a team calls any schema an ontology" | PARTIAL — **re-framed as a contested objection** *(fixed)* | Gruber records and rejects it: "overly broad, allowing for a range of specifications from simple glossaries to logical theories couched in predicate calculus… But this holds true for data models of any complexity" |
| **"and every enterprise semantic layer makes [this move]"** | **UNSUPPORTED — cut** *(fixed)* | universal claim, no capture. Palantir half re-sourced: "The Ontology sits on top of the digital assets integrated into the Palantir platform … and connects them to their real-world counterparts" |

### notes/cyc-lenat-1995.md

| claim | verdict | span |
| --- | --- | --- |
| **"1995 CACM article"** | **UNSUPPORTED in the capture — re-sourced** *(fixed)* | the capture carries no date, volume or issue; the year came only from the filename `lenat95cyc.pdf`. DBLP: "CYC: A Large-Scale Investment in Knowledge Infrastructure. Commun. ACM 38 11 1995" |
| begun with Mary Shepherd in 1984, knowing the odds | SUPPORTED | "Mary Shepherd and I embarked on that task in 1984, knowing we had little chance of success, but seeing no alternative but to try." |
| "roughly a million hand-crafted commonsense axioms, and millions more inferred and cached" | SUPPORTED, now quoted *(fixed)* | "approximately 10⁶ commonsense axioms have been handcrafted for and entered into CYC's knowledge base, and millions more have been inferred and cached by CYC" |
| "a universal schema of general concepts" | SUPPORTED, figure restored *(fixed)* | "a universal schema of roughly 10⁵ general concepts spanning human reality" |
| "decades of specialist labour" | PARTIAL — **replaced with the paper's own figure** *(fixed)* | "Since 1984, a person-century of effort has gone into building CYC" |
| the peanut-butter/table example | PARTIAL, presented as the paper's wording but paraphrased — **now quoted verbatim** *(fixed)* | "if you cut a lump of peanut butter in half, each half is also a lump of peanut butter; but if you cut a table in half, neither half is a table" |
| "you cannot remember events that have not happened yet" | SUPPORTED verbatim | "• You cannot remember events that have not happened yet." |
| the representation list (causality, time, space…) | SUPPORTED | "handling causality, time, space, substances, intention, contradiction, uncertainty, belief, emotions, planning, and so on" |
| "microtheories for locally consistent contexts" | PARTIAL — **re-worded to the paper's language** *(fixed)* | "we sought to build a set of micro-theories… Each micro-theory inhabits its own context"; "Each of them is relatively small, solid, and flat" |
| critical mass | SUPPORTED | "That knowledge would serve as a critical mass, enabling further knowledge collection through NLU and ML" |
| LLM angle, first clause | SUPPORTED, now quoted *(fixed)* | "statistics, colocation, and frequency do not resolve such questions. But the task goes from impossible to trivial if one already knows a few things about boxes and pens" |
| LLM angle, "not inspectable, not consistent, cannot be audited" | UNSUPPORTED — **marked editorial and cross-linked** *(fixed)* | the paper is from 1995 and says nothing about language models |

### notes/semantic-web-2001-vision.md

| claim | verdict | span |
| --- | --- | --- |
| authorship, May 2001, *Scientific American* | SUPPORTED | masthead survives even in the stub: "May 1, 2001 … By Tim Berners-Lee, James Hendler and Ora Lassila" |
| Pete-and-Lucy scenario, physical therapy | SUPPORTED, **now against the article itself** *(fixed)* | "His sister, Lucy, was on the line from the doctor's office… a series of physical therapy sessions" — re-fetched full text |
| provider ratings, insurance, both calendars | SUPPORTED | "a rating of excellent or very good on trusted rating services"; "treatments covered by the user's insurance plan"; "Pete's and Lucy's busy schedules" |
| services never built to talk to each other | SUPPORTED | "Programs could exchange data across the Semantic Web without having to be explicitly engineered to talk to each other." |
| "Berners-Lee later **rebranded** the programme Web 3.0" | PARTIAL — **re-worded and attributed** *(fixed)* | "Berners-Lee began referring to the Semantic Web as Web 3.0." The word "rebranding" is applied in the source to *linked data*, not to Web 3.0. |
| RDF triples as the grammar | SUPPORTED | "RDF would be the grammar in which Semantic webpages expressed information." |
| RDFS and OWL as answers to the brief | SUPPORTED | "RDF Schema and another standard called OWL allows RDF authors to demarcate the boundary between valid and invalid RDF statements" |
| **SPARQL as an answer to the 2001 brief** | **UNSUPPORTED — marked as the author's reconstruction** *(fixed)* | SPARQL appears in zero occurrences of the cited history; the article predates it by five years |
| **"the URI as the identifier that lets independent parties talk about the same thing"** | UNSUPPORTED in the cited captures — **cut from Key concepts** *(fixed)* | zero URI mentions in `semweb-twobithistory.md` |
| open world | SUPPORTED, **re-sourced** *(fixed)* | "OWL currently adopts the standard logical model of an open world assumption… on the huge and only partially knowably World Wide Web this is the correct assumption." — Horrocks, Patel-Schneider and van Harmelen |
| "of anonymous publishers" | UNSUPPORTED — **cut** *(fixed)* | no capture characterises publishers as anonymous |
| the annotation-incentive pitfall | SUPPORTED, now quoted *(fixed)* | "most web users were likely to provide either no metadata at all or else lots of misleading metadata meant to draw clicks" |

### notes/semantic-web-retrospective.md

| claim | verdict | span |
| --- | --- | --- |
| "Sinclair Target's 2018 history" | date SUPPORTED; **byline was UNSUPPORTED — re-fetched** *(fixed)* | "*27 May 2018*"; and from the site's about page, "My name is Sinclair Target." |
| phase 1, 2001–2005, W3C standardisation | SUPPORTED | "The first phase, which lasted from 2001 to 2005, was the golden age of Semantic Web activity." |
| "RDF reached **recommendation status** in 2004" | PARTIAL — **re-worded** *(fixed)* | "The W3C issued the first version of the RDF standard in 2004" |
| **phase 3 as "enterprise and scientific deployments"** | **CONTRADICTED — rewritten** *(fixed)* | "The third phase … involved adapting the W3C's standards to fit the actual practices and preferences of web developers. By 2008, JSON had begun its meteoric rise" — that is JSON-LD and schema.org, not enterprise. Phase 4 is the W3C "under the heading of 'Data Activity'". The enterprise thread is Ontotext's, and is now attributed to Ontotext. |
| Swartz's unfinished book, "attacking a strawman" | SUPPORTED | "Aaron Swartz … wrote in an unfinished book about the Semantic Web published after his death that Doctorow was 'attacking a strawman.'" |
| "formalizing mindset of mathematics and the institutional structure of academics" | SUPPORTED verbatim | quoted exactly in the capture |
| standards before applications; standards too abstract | SUPPORTED | "a huge amount of effort and discussion went into creating standards before there were any applications out there to standardize"; "so abstract that few of them ever saw widespread adoption" |
| Guha's metadata work at Apple | SUPPORTED | "partly based on earlier attempts by Ramanathan Guha, an Apple engineer, to develop a metadata system for files stored on Apple computers" |
| "XML as an **adoption tax**" | PARTIAL — **re-worded to the source's framing** *(fixed)* | "whereas XML came packaged with a bunch of associated technologies of indeterminate purpose … JSON was just JSON. It was less verbose and more readable" |
| centralisation into Google, Yelp, Siri | SUPPORTED | "Today's physical therapists must enter information about their practice into Google or Yelp, because those are the only services that the smartphone agents know how to use" |
| **"Criticism written in 2003"** | **UNSUPPORTED — re-dated** *(fixed)* | the corpus's open-web criticism is Doctorow, "Version 1.3: 26 August 2001". No 2003-dated criticism is in scope. |
| **"survival … in finance"; FIBO as a named success** | **UNSUPPORTED — cut from the retrospective claim** *(fixed)* | "FIBO" has zero occurrences anywhere under `research/`. The corpus's own FIBO note is now cited instead of a retrospective. |
| **Gene Ontology / CIDOC CRM as retrospectively named successes** | PARTIAL — **re-attributed to corpus notes** *(fixed)* | the retrospectives name "schema.org, Knowledge Graphs, Wikidata, DBpedia, Biomedical Ontologies"; CIDOC-CRM appears only as a bare figure keyword |
| **Ontotext → "retrieval-augmented-generation and GraphRAG"** | **UNSUPPORTED — cut** *(fixed)* | `semweb-ontotext-20yr.md` contains no occurrence of RAG, GraphRAG, LLM, or large language model. The retrieval leg is now attributed to the VLDB survey. |
| schema.org's search-engine incentive | SUPPORTED, now quoted *(fixed)* | "schema.org was started by Google, Bing, and Yahoo with the express purpose of delivering better search results" |
| "kept the vocabulary shallow" | PARTIAL — **replaced with the source's own line** *(fixed)* | "The schema.org team are careful to state on their website that they are not attempting to create a 'universal ontology.'" |

### notes/knowledge-graph-turn.md

| claim | verdict | span |
| --- | --- | --- |
| Google Knowledge Graph, May 2012 | SUPPORTED, source now listed *(fixed)* | "What has been provided on google.com for the US-Market since May 2012, is now available also for most European countries." — Blumauer, in `research/exa/kg-revival.json` |
| Freebase via Metaweb | SUPPORTED | "Google's Knowledge Graph derives from Freebase, a proprietary graph database acquired by Google in 2010 when it bought Metaweb." |
| **"things, not strings" attributed only to "Google"** | attribution gap — **named** *(fixed)* | "Amit Singhal. 2012. Introducing the Knowledge Graph: Things, Not Strings. Google Official Blog." |
| Satori for Bing | SUPPORTED | "As of June 1, Satori had mapped over 400 million entities and Knowledge Graph had reached half a billion" |
| "the phrase spread … **whether or not it used RDF or OWL at all**" | PARTIAL and in tension with the paired example — **rewritten** *(fixed)* | Satori "uses the Resource Description Framework and the SPARQL query language". Replaced with the sourced definitional-contention span: "the definition of a 'knowledge graph' remains contentious" |
| **"graph databases with no formal semantics adopting the vocabulary of the field"** | **UNSUPPORTED — cut** *(fixed)* | no capture makes this claim |
| "entity resolution as the hard problem rather than logic" | PARTIAL — **replaced with the survey's own three-way heterogeneity framing** *(fixed)* | the survey lists entity, schema and value heterogeneity together and ranks none |
| the VLDB generations account | SUPPORTED | "we describe three generations of knowledge graphs: entity-based KGs, text-rich KGs, dual neural KGs"; "Generations of Knowledge Graphs: The Crazy Ideas and the Business Impact" |
| "Wikidata as the open **community-curated survivor**" | PARTIAL — **trimmed to what the survey states** *(fixed)* | it is listed among success stories; neither capture says "community-curated" or "survivor" |
| **"this corpus documents a concrete example …" (unnamed)** | attribution gap — **named** *(fixed)* | `notes/scigraph.md`: "The mapping is explicitly lossy and does not round-trip ontologies" |
| LLM angle, "**most often** justified as grounding" | PARTIAL — **marked as impression** *(fixed)* | the only frequency-free span is "at the current moment, LLMs clearly have not replaced knowledge graphs" |
| decentralisation as the casualty | SUPPORTED, now quoted *(fixed)* | "today we are stuck with giant, centralized repositories of information"; "no precedent exists in the Semantic Web setting for the type of decentralised infrastructure envisaged by Berners-Lee" |

### notes/doctorow-metacrap.md

| claim | verdict | span |
| --- | --- | --- |
| 2001 | SUPPORTED | "Version 1.3: 26 August 2001"; "Version 1.0, May 15 2001" |
| **"aimed directly at" the Scientific American article** | **UNSUPPORTED — cut** *(fixed)* | zero hits for "semantic web", "scientific american", or "berners" in the essay. His stated target: "Explicit, human-generated metadata has enjoyed recent trendiness, especially in the world of XML." |
| the thesis quote | SUPPORTED verbatim | "It's also a pipe-dream, founded on self-delusion, nerd hubris and hysterically inflated market opportunities." |
| "He lists seven obstacles" | PARTIAL — **restored his qualifiers** *(fixed)* | "There are at least seven insurmountable obstacles"; section title "seven straw-men" |
| obstacle 1, People lie; spam subject lines; keyword-stuffed press releases | SUPPORTED | "Press-releases have gargantuan lists of empty buzzwords attached to them." |
| obstacle 2, People are lazy; untitled files, subject-less mail, MP3s, CDDB button | SUPPORTED | "at least one will have no title, artist or track information … clicking the 'Fetch Track Info from CDDB' button" |
| obstacle 3, eBay "plam", **nine** listings | SUPPORTED, number correct | "Try searching for 'plam' on eBay. Right now, that turns up *nine* typoed listings for 'Plam Pilots.'" |
| **obstacle 4 title rendered "Know thyself is impossible"** | PARTIAL, presented as his title — **restored** *(fixed)* | his heading is "Mission: Impossible -- know thyself" |
| **"Nielsen's paper diaries"** | PARTIAL — **corrected to his word** *(fixed)* | "When Nielsen used log-books to gather information on the viewing habits of their sample families, the results were heavily skewed to *Masterpiece Theater* and *Sesame Street*." (the note also dropped *Sesame Street*; restored) |
| obstacle 5 heading | PARTIAL — **restored his spelling** *(fixed)* | "Schemas aren't neutral" |
| the washing-machine axes | SUPPORTED, both directions correct | "Energy consumption: Water consumption: Size:" vs "Color: Size: Programmability: Reliability" |
| obstacle 6, MTV/Nielsen | SUPPORTED; the note's hedge "partly" — **removed** *(fixed)* | "which is why MTV doesn't show videos any more -- Nielsen couldn't generate ratings for three-minute mini-programs" |
| obstacle 7, "denudes the cognitive landscape" | SUPPORTED verbatim | "Requiring everyone to use the same vocabulary to describe their material denudes the cognitive landscape" |
| the implicit-metadata concession | SUPPORTED, now quoted *(fixed)* | "Certain kinds of implicit metadata is awfully useful, in fact. Google exploits metadata about the structure of the World Wide Web" |

### notes/shirky-ontology-is-overrated.md

| claim | verdict | span |
| --- | --- | --- |
| "two 2005 talks" | SUPPORTED, now named *(fixed)* | "one at the O'Reilly ETech conference in March, entitled 'Ontology Is Overrated', and one at the IMCExpo in April entitled 'Folksonomies & Tags'… a heavily edited concatenation of those two talks" |
| the definition of ontological classification | SUPPORTED | "organizing a set of entities into groups, based on their essences and possible relations … its logical place already exists within the system, even before the book was published" |
| the periodic table / helium / noble gas / "frozen accident" | SUPPORTED | "noble gas is an odd category, because helium is no more a gas than mercury is a liquid"; "we've all just gotten used to that anomaly as a frozen accident" |
| **"Dewey's 200s give nine categories to Christianity and one to 'other religions'"** | **CONTRADICTED — corrected** *(fixed)* | the block lists nine subdivisions **in total** (210–290), of which one is "290 Other religions" |
| Library of Congress DA/DC/DS/DT | SUPPORTED but incomplete — **DR added** *(fixed)* | Shirky bolds "DR: Balkan Peninsula", "DS: Asia", "DT: Africa"; "These are all the top-level categories — all of these things are presented as being co-equal." |
| "What is being optimised is books on a shelf" | SUPPORTED | "What's being optimized is number of books on the shelf." |
| "The essence of a book isn't the ideas it contains…" | SUPPORTED verbatim | as quoted |
| "There is no shelf" | SUPPORTED | "the obvious truth: there is no shelf" |
| the Yahoo parable, the "@" marker | SUPPORTED | "That '@' sign is telling you that the category of Books and Literature isn't 'really' in the category Entertainment."; "*added the shelf back*" |
| **"Shirky's three preconditions"** | **CONTRADICTED — rewritten** *(fixed)* | he gives "a partial list of characteristics" in two groups: Domain — small corpus, formal categories, stable entities, restricted entities, clear edges; Participants — expert catalogers, an authoritative source of judgment, coordinated users, expert users. Nine items, explicitly partial, explicitly not a test. |
| **"Genomics, museum records, and financial instruments qualify"** | **UNSUPPORTED — cut** *(fixed)* | zero hits for "genomic", "museum", "financial instrument" in either Shirky capture. His worked example is DSM-IV: "a classic example of an classification scheme that works because of these characteristics." |
| "his **companion** essay on syllogism" | PARTIAL — **dated** *(fixed)* | "First published November 7, 2003 on the 'Networks, Economics, and Culture' mailing list" — two years earlier, different venue |
| Semantic Arts rebuttal | SUPPORTED, now named and dated *(fixed)* | "Shirky, Syllogism and the Semantic Web — by Dave McComb … Mar 25, 2015"; "The irony being of course, that this entire article is a syllogism." |
| **"the disagreement … is still live"** | **UNSUPPORTED — cut** *(fixed)* | replaced with McComb's sourced 2015 line, "we still have a long way to go to staunch the critics" |

### notes/bowker-star-sorting-things-out.md

| claim | verdict | span |
| --- | --- | --- |
| 1999 | SUPPORTED | "Pub date: September 29, 1999" |
| classification as an object of study | SUPPORTED, now attributed to Brooks *(fixed)* | "It is the accomplishment of this book to recognize classification itself as an object of study, as a vehicle for ethnography" |
| "values, policies, and modes of practice become embedded…" | SUPPORTED, but it is **Brooks's sentence**, not the authors' — now attributed *(fixed)* | "The effect of their sample critiques and examples is to illustrate how values, policies and modes of practice become embedded in large information systems and become expressed in classification systems." |
| **the definition of torque** | previously traced only to the 404 stub — **re-fetched** *(fixed)* | Bowker and Star "introduce the force metaphor of 'torque' to describe the process that unfolds when 'the "time" of the body and of [its] multiple identities cannot be aligned with the "time" of the classification system' (p. 190)"; "Individual biographies are twisted into tortured shapes"; "there is no experience of torque for those in power" — Helmreich |
| **ICD "took decades to negotiate"** | **CONTRADICTED — corrected** *(fixed)* | "developing this classification took many years and there are still many disagreements over it" — Nehrlich. Zero hits for "decades" in any Bowker capture. |
| tropical-disease under-representation | SUPPORTED verbatim | "tropical countries believe that tropical diseases are grossly underrepresented compared to 'rich-world' diseases like cancer and heart disease" |
| Japan, heart attack, stroke on the certificate | SUPPORTED verbatim | "In Japan, heart attacks are considered a low-status way of dying, so death certificates will often list a stroke as the cause of death" |
| apartheid reclassification and its consequences | SUPPORTED | "South African citizens who have been tossed back and forth between being classified as Whites, then Coloreds, then back again" (Brooks); "a government declaration of one's race forced one to change residences, jobs and families" (Nehrlich) |
| **"The category was not a description of a person. It was an instrument acting on one."** | UNSUPPORTED as reportage — **marked as the note's gloss** *(fixed)* | Helmreich's worked case (Asian at birth → African at majority) is now quoted in its place |
| tuberculosis patients | SUPPORTED verbatim | "tuberculosis patients who are completely dependent on their doctors to diagnose their status" |
| the Nursing Interventions Classification | SUPPORTED verbatim | "nurses were asked to describe what they do, so that it could be classified, standardized, and integrated into a billing system"; "Some nurses cheered … Others were aghast" |
| "the book's **recurring** finding" | PARTIAL — **scoped to the example** *(fixed)* | Nehrlich scopes it: "was made clearly evident in this example" |
| black-boxing | SUPPORTED, Latour now credited *(fixed)* | "Classification systems tend to get black-boxed, in the sense of Bruno Latour." |
| **"the residual-category test … every model needs an 'other' bucket"** | **UNSUPPORTED — cut** *(fixed)* | zero occurrences of "residual" anywhere under `research/`. Replaced with Nehrlich's platypus passage, which is sourced: "there will always be elements which do not slot neatly into a category… this is not a reflection of the element - it is a reflection of the inadequacy of the system" |
| "one reviewer notes…" | SUPPORTED, **reviewer now named** *(fixed)* | Terrence A. Brooks: "the survey treatment … leads to multiple examples that pile on and do not advance the argument"; "strangely disconnected from a large body of empircal, cognitive research in classification and categorization" |

### notes/palantir-ontology.md

Verified against Palantir's own documentation. Rows without a *(fixed)* marker were correct as written.

| claim | verdict | span |
| --- | --- | --- |
| "operational layer", sitting above datasets/virtual tables/models | SUPPORTED | "The Palantir Ontology is an operational layer for the organization. The Ontology sits on top of the digital assets integrated into the Palantir platform (datasets, virtual tables, and models) and connects them to their real-world counterparts" |
| "interconnected *decisions* of an enterprise rather than its data" | SUPPORTED | "The Ontology is designed to represent the complex, interconnected *decisions* of an enterprise, not simply the data." |
| explicitly "not a semantic layer" | SUPPORTED | "The Ontology is not a 'semantic layer'; the fourfold integration and operationalization of data, logic, action, and security cannot be accomplished with a thin semantic layer" |
| "digital twin of the organisation" | SUPPORTED | "In many settings, the Ontology serves as a digital twin of the organization" |
| the fourfold framing | SUPPORTED, Palantir's own | "The Ontology models decisions through the four-fold integration of **data**, **logic**, **action**, and **security**." |
| the seven data-source kinds | SUPPORTED, all seven present | "fragmented ERP estates, homegrown systems of record, CRMs, industrial databases, geospatial repositories, real-time sensors, document stores" |
| object type / object / object set | SUPPORTED | "An **object type** is the schema definition of a real-world entity or event. An **object or object instance** refers to a single instance… an **object set** refers to a collection" |
| link types bidirectional, two independently traversable sides | SUPPORTED | "A link type is bidirectional: it always has two **sides**… Each side of a link type can be traversed independently" |
| the dataset/row/filtered-rows/join analogy | SUPPORTED, Palantir's own | "analogous to that of a dataset… a row… a filtered set of rows"; "analogous to that of a join between two datasets" |
| action types, transactions, side effects | SUPPORTED | "An action is a single transaction that changes the properties of one or more objects"; "It also includes the side effect behaviors that occur with action submission." |
| "validation rules, submission criteria" | PARTIAL — **softened** *(fixed)* | "validation rules" as a compound never appears; "submission criteria" appears only in a further-reading link label, "learn about rules, parameters, and submission criteria" |
| **the business-rule/ML/LLM/orchestration list assigned to Functions** | **MISATTRIBUTED — corrected** *(fixed)* | the capture assigns that list to **logic**: "The logic underlying a given action … could be a simple business rule, a conventional machine learning model, an LLM-driven function, or a complex multi-step orchestration". Functions are defined separately: "functions provide a way to author and evolve business logic with arbitrary complexity." |
| interfaces / polymorphism | SUPPORTED verbatim | "Interfaces provide object type polymorphism" |
| writeback, writeback dataset, decisions become data | SUPPORTED | "will be captured in an object type's writeback dataset"; "The data asset grows in richness and value as user decisions and insights are captured" |
| security across data, logic, action; agents inherit scope | SUPPORTED | "enforcing granular controls across data, logic, and action simultaneously, whether the actor is a human or an agent"; "security scopes that either inherit from a human user, or from the permissions structure of a defined project" |
| Language / Engine / Toolchain | SUPPORTED, exact names | "can conceptually be grouped into a Language, an Engine, and Toolchain" |
| no cross-Ontology links | SUPPORTED verbatim | "Note that links between object types across different Ontologies is not supported." |
| **the entire OWL comparison** | **UNSUPPORTED as sourced — marked editorial** *(fixed)* | the seven `pltr-*` captures contain zero occurrences of OWL, RDF, W3C, semantic web, open-world, closed-world, reasoner, or subsumption |
| **"no reasoner deriving subsumption, no open-world assumption, no shared public vocabulary"** | argument from silence — **marked as the author's reading**, with the one real span added *(fixed)* | "Data types in Foundry are inspired by similar concepts in RDF, OWL and XSD" — Palantir's type reference (via `research/exa/palantir-ont.json`) |
| **LLM angle: "object queries provide retrieval context"** | PARTIAL and inverted — **corrected** *(fixed)* | Palantir positions the Ontology *against* the retrieval framing: it "enables LLMs to go beyond the data-centric limitations of retrieval-augmented generation" |
| agents as tools | SUPPORTED | "The Ontology is a 'tool factory' that lets your builders define tools for both humans and agents." |

### notes/palantir-ontology-critique.md

| claim | verdict | span |
| --- | --- | --- |
| Galis and Karlsson, 2024, *Information, Communication & Society* 27:13 | SUPPORTED | "Vasilis Galis & Björn Karlsson (2024) A world of Palantir – ontological politics in the Danish police's POL-INTEL, Information, Communication & Society, 27:13, 2438-2456" |
| POL-INTEL as a customisation of **Gotham** | SUPPORTED | "When Palantir Technologies customized the Gotham platform into POL-INTEL, a data integration and analysis platform purchased and used by the Danish police" |
| interviews with Palantir engineers and police officers | SUPPORTED verbatim | "Based on a series of interviews with Palantir engineers and police-officer users of POL-INTEL" |
| ontology in two senses | SUPPORTED, wording corrected *(fixed)* | "the concept of ontology should be understood in a twofold, albeit interconnected, way" |
| **"the two cannot be separated in practice"** | overstated — **corrected** *(fixed)* | the paper adopts Smith's R-ontology / E-ontology split; its "cannot be separated" line is about a different pairing: "The platform's E-ontology cannot be separated from Palantir's and/or the police." |
| the ontology is political | SUPPORTED verbatim | "POL-INTEL's ontology is inherently political, as it is articulated by an assemblage of data, ideological positions, and economic concerns that are translated into the Danish context." |
| **"not only describe the world but also enact it"** | SUPPORTED verbatim, but the paper **credits Leese (2023)** — now attributed *(fixed)* | "they not only describe the world but also enact it (Leese, 2023)" |
| the getaway-vehicle example | SUPPORTED verbatim | "the vehicle's information is mirrored from the Motor Vehicle registry into POL-INTEL. However, when it enters the world of the police … it is potentially seen as a getaway vehicle" |
| platformisation redistributes skill | SUPPORTED | "establishing new distributions of skills between the platform and police officers" |
| **the German ruling: "struck down Hamburg's law, and a similar Hesse law, as unconstitutional"** | **VERIFIED CORRECT after re-fetch, and sharpened** *(fixed)* | The secondary source (WIRED) said only "a top German court ruled the Hamburg law unconstitutional", which read as a contradiction. The court's own press release settles it: "§ 25a(1) first alternative of the … Land Hesse … and § 49(1) first alternative of the … Land Hamburg … are unconstitutional." The remedies differ, and the note now says so: the Hamburg provision "is void", while the Hesse provision "will continue to apply, subject to the restrictions set out below, until new provisions have been enacted, and in any case no later than 30 September 2023." |
| the date and the court | previously inferable only from a URL slug — **now primary** *(fixed)* | "Judgment of 16 February 2023 - 1 BvR 1547/19, 1 BvR 2634/20" |
| **"with just one click, create comprehensive profiles of persons"** | altered inside quotation marks — **restored verbatim** *(fixed)* | "They thus allow the police, with just one click, to create comprehensive profiles of persons, groups and circles." |
| "the first strict guidelines" | SUPPORTED | "issued strict guidelines for the first time about how automatic data analysis tools like Palantir's can be used by police" — WIRED |
| bystander data, witnesses, lawyers | SUPPORTED | "it warned against the inclusion of data belonging to bystanders, such as witnesses or lawyers like Eder" |
| eleven claimants; the Hamburg defence lawyer | SUPPORTED, now named *(fixed)* | "she decided to become one of 11 claimants"; "As a defense lawyer in Hamburg, her client list includes anti-fascists, people who campaign against nuclear power, and members of the PKK" |
| "pragmatically rather than agnostically" | SUPPORTED verbatim | "They *pragmatically* integrate, analyze, and visualize data … Pragmatically, not agnostically." |
| the note's softening gloss on that passage | PARTIAL — **the paper's blunter line restored** *(fixed)* | "Platforms such as POL-INTEL are not encoded with democratic values or other modernist sensibilities." |

### notes/llm-ontology-debate.md

| claim | verdict | span |
| --- | --- | --- |
| Sun and colleagues, VLDB | SUPPORTED | "Yushi Sun, Hao Xin, Kai Sun, Yifan Ethan Xu, Xiao Yang, Xin Luna Dong, Nan Tang, and Lei Chen. Are Large Language Models a Good Replacement of Taxonomies?. PVLDB, 17(11): 2919 - 2932, 2024." |
| **the finding reported on one axis only** | INCOMPLETE — **both axes and the positive half restored** *(fixed)* | "the QA accuracy of the best LLM drops by up to 30% as we go from common to specialized domains **and from root to leaf levels** of taxonomies"; and "The manually constructed and maintained taxonomies in these domains may not be needed shortly." |
| **"Maria Keet"** | first name UNSUPPORTED by any capture — **reduced to "Keet"** *(fixed)* | the capture never names the author; only `keet.wordpress.com` and "my ontology engineering textbook" |
| **Keet's lead argument omitted** | MATERIALLY INCOMPLETE — **added** *(fixed)* | "the LLMs do not store the (structured) facts, (axiomatised) sentences, and rules to make the inferences… technically, not knowledge bases"; "Two different runs then may lead to two different ontologies." |
| Keet's consistency objection | SUPPORTED | "an LLM may propose them to be fish, but that would make the ontology inconsistent… Inconsistent ontologies are bad computationally." |
| **"The replacement case"** | UNSUPPORTED as a sourced position — **marked as the note's reconstruction** *(fixed)* | the only sourced part is that the debate exists: "sparking a growing debate about whether traditional knowledge graphs will be replaced by LLMs in real applications" |
| the grounding case | SUPPORTED | "existing retrieval-augmented models, such as RAG… fail to account for structured domain knowledge… ontologies… offer a structured representation to address this gap"; "30% faster attribution of responses to context" |
| **"identifiers, and constraints"** | **UNSUPPORTED — cut** *(fixed)* | no capture attributes either to the ontology side |
| **"the division of labour that keeps recurring"** | EDITORIAL — **marked, and the VLDB's different split noted** *(fixed)* | the paper's own proposal is that root entities move into weights while leaf entities stay in the tree |
| **"weakest on the first, mixed on the second, strongest on the third"** | EDITORIAL — **marked** *(fixed)* | no capture ranks the three questions |
| **"hallucination and inconsistency survive good prompting"** | **CONTRADICTED in polarity — corrected** *(fixed)* | `notes/ontolearner.md`: "Clear prompts and structured output **reduce** hallucination and inconsistency; relationships and labels should be validated" |
| quadratic all-pairs matching | SUPPORTED | `notes/ontoaligner.md`: "Direct LLM matching has quadratic complexity and is documented as suitable for small ontologies (about 200 concepts or fewer)" |
| retrieval contexts cause memory problems | SUPPORTED | `notes/ontolearner.md`: "Large retrieval contexts can cause memory problems" |
| syntactic validity ≠ semantic correctness | SUPPORTED | `notes/elot.md`: "Automatic LLM mutation validation checks lint and OWL parsing, not semantic consistency" |
| the ELOT guarded design | SUPPORTED | `notes/elot.md`: "File writes are project-scoped, disabled by default, confirmation-gated, and revalidated with rollback" |
| **"permission-governed"** | UNSUPPORTED in this note's sources — **cross-linked instead** *(fixed)* | the corpus's permission argument lives in `notes/palantir-ontology.md` |

### Template compliance

**All thirteen notes were missing the `**Verdict**` field.** `NOTE_INDEX.json` had been hand-patched
with `"Verdict": "none stated"` for each, so the index did not mirror the notes and
`python3 scripts/check.py` failed with 39 errors. `uvx pytest tests -q` passed anyway, because
the test asserts against the index, not against the note files.

Fixed: a real, grounded `**Verdict**` line was written for each of the thirteen, and
`NOTE_INDEX.json` regenerated from the notes with `scripts/rebuild_index.py`. `check.py` now
passes.

Two broken relative links were also fixed: `[notes/cyc.md](notes/cyc.md)` inside
`notes/cyc-lenat-1995.md` resolved to `notes/notes/cyc.md`; same pattern in
`notes/llm-ontology-debate.md`.

---

## Part 3 — Claims cut

Every claim removed from a note in this run, with the reason. Nothing was softened in place of cutting.

1. **word-history** — "rather than because of what kind of thing it happens to be." No capture carries the contrast.
2. **word-history** — "is the direct ancestor of the split between upper ontologies such as BFO and domain ontologies such as GO." No capture asserts descent; BFO appears in zero captures; Gene Ontology in no cited capture.
3. **word-history** — "aimed to be the single true account of being." Only the deductive method is sourced.
4. **quine** — "…and is what OWL's model-theoretic semantics implements." No capture connects Guarino's construction to OWL's semantics.
5. **quine** — "is the direct descendant of this idea." Guarino's chapter never mentions Quine.
6. **gruber** — "and every enterprise semantic layer." Universal claim, no capture.
7. **semweb-2001** — "SPARQL because someone eventually has to query the result," as a claim about the 2001 brief. SPARQL postdates the article by five years and appears in none of the cited histories. Retained only as explicitly-marked reconstruction.
8. **semweb-2001** — "of anonymous publishers." No capture characterises publishers as anonymous.
9. **semweb-2001** — "the URI as the identifier that lets independent parties talk about the same thing," from Key concepts. Zero URI mentions in the cited captures.
10. **retrospective** — "finance" and "FIBO" as retrospectively named successes. Zero corpus-wide hits for FIBO in `research/`.
11. **retrospective** — "That is the position from which current retrieval-augmented-generation and GraphRAG work inherits," as an Ontotext claim. That post never mentions RAG, GraphRAG, or language models.
12. **kg-turn** — "graph databases with no formal semantics adopting the vocabulary of the field." No capture.
13. **kg-turn** — "whether or not it used RDF or OWL at all," as paired with Satori. Contradicted: Satori uses RDF and SPARQL.
14. **doctorow** — "aimed directly at it," of the Scientific American article. The essay never mentions it.
15. **shirky** — "Genomics, museum records, and financial instruments qualify." Zero hits in either Shirky capture.
16. **shirky** — "the disagreement about how much inference is worth doing is still live." No capture supports a present-tense liveness claim.
17. **bowker-star** — "Use the residual-category test as well: every model needs an 'other' bucket." Zero occurrences of "residual" anywhere under `research/`.
18. **llm-debate** — "identifiers, and constraints," from the grounding case. No capture attributes either to the ontology.
19. **llm-debate** — "permission-governed," from the closing sentence. Not in this note's sources.

---

## Part 4 — The 26 `CONCEPTS` glossary definitions

Grounding rule: each definition must be stated by a note in this repository, or be rewritten
from a note's own text, or be cut. Spans below are from `notes/`.

| term | verdict | supporting note and span | action |
| --- | --- | --- | --- |
| ABox | SUPPORTED | `description-logics-dls.md`: "A TBox states concept hierarchies; an ABox states facts about individuals." | keep |
| Alignment | SUPPORTED | `ontology-matching.md`: "methods for finding correspondences between semantically related entities in different ontologies"; "use the resulting correspondences to support merging, cross-ontology queries, translation, or navigation" | keep |
| Axiom | PARTIAL | `knowledge-graph-turn.md`: "a formal vocabulary with axioms whose consequences a reasoner can derive." No note says an axiom is "asserted to be true"; `tawny-owl.md` in fact separates asserted from inferred. | rewritten |
| Classification | SUPPORTED | `cel.md`: "its main task is computing the subsumption hierarchy induced by an ontology" | keep |
| Closed-world assumption | PARTIAL | `f-logic.md`: "its usual semantics use a closed-world assumption, unlike the open-world assumption described for description logics". **"Databases do this" is stated by no note.** The corpus's CWA exemplars are F-logic, SPIN constraints, and Palantir's Ontology. | rewritten |
| Conceptualization | SUPPORTED | `gruber-ontology-definition.md`: "a conceptualization is 'the objects, concepts, and other entities that are presumed to exist in some area of interest…'" | keep |
| Consistency checking | PARTIAL | `pellet-2.md`: "check whether an ontology is consistent and find unsatisfiable concepts"; `tawny-owl.md` distinguishes "satisfiability of classes, coherence of an ontology, and consistency when individuals are asserted". The dict welded consistency and unsatisfiability together. | rewritten |
| Description logic | PARTIAL | `description-logics-dls.md`: "generally more expressive than propositional logic and less expressive than first-order logic … many core reasoning problems are decidable". The note says *many*, not *the decidable fragments*, and frames the trade as complexity, not termination. | rewritten |
| Entailment | PARTIAL | `apache-jena-ontology-api.md`: "models may expose asserted plus entailed triples through the same model interface". No note defines the word. | rewritten |
| Individual | SUPPORTED | `description-logics-dls.md`: "Concepts correspond to classes or unary predicates, roles to properties or binary predicates, and individuals to constants." | keep |
| Instance checking | PARTIAL | `description-logics-dls.md`: "Common inference tasks include instance checking, relation checking, subsumption, and concept-consistency checking" — named, never defined | rewritten |
| Justification | **UNSUPPORTED** | the string "justification" occurs **zero times** in `notes/`. The corpus says *explanation*: `elk.md`: "it can show, step by step, how a logical consequence follows from ontology axioms". No note states minimality. | replaced by **Explanation** |
| Materialization | PARTIAL | `owl-rl.md`: "A narrowly scoped forward-chaining choice for materializing OWL 2 RL and RDFS inferences"; "A deductive closure expands a graph with inferred triples". "All entailments" overclaims; "instead of at query time" is in no note. | rewritten |
| Microtheory | PARTIAL | `cyc-lenat-1995.md` (as fixed): "micro-theories, each of which 'inhabits its own context'". The note does not say they quarantine contradictions. | rewritten |
| Object type | PARTIAL | `palantir-ontology.md`: "An **object type** is the schema definition of a real-world entity or event". "Given behaviour" is wrong by the note's own division — behaviour is kinetic (action types, functions). | rewritten |
| Ontological commitment | SUPPORTED | `quine-ontological-commitment.md`: "A theory's ontological commitments are whatever must be in the range of its quantified variables for its statements to come out true." | keep |
| Open-world assumption | SUPPORTED, one editorial clause | `description-logics-dls.md`: "lack of a fact does not imply its negation". "the source of most beginner surprise" is in no note. | trimmed |
| Punning | **UNSUPPORTED** | the only two corpus occurrences are in `yamlpyowl.md`, and both say it is *unavailable*: "`owlready2` and most OWL reasoners do not support metaclasses/punning, motivating the optional proxy-individual workaround." | rewritten to what the note says |
| Reification | PARTIAL | `nell-ontology-and-knowledge-base.md`: "provenance modeled through RDF reification, n-ary relations, named graphs, singleton properties, or NDFluents". The purpose is attested; the mechanism is not. | rewritten |
| Semantic layer | PARTIAL, with an invented clause | `palantir-ontology.md` reports the disclaimer and gives no reason for it. "because a semantic layer cannot act" was the dict's own inference. | rewritten |
| Subsumption | PARTIAL | `cel.md`: "computing the subsumption hierarchy induced by an ontology". "computed rather than declared" is contradicted by `rdf-schema-rdfs-1-1.md`, which lists `rdfs:subClassOf` as a declared term, and by `tawny-owl.md`'s asserted/inferred split. | rewritten |
| TBox | PARTIAL | `description-logics-dls.md`: "A TBox states concept hierarchies". "and property definitions" is contradicted by `sparql-dl.md`: "designed to combine TBox, RBox, and ABox queries" — property axioms are the RBox. | rewritten |
| Torque | PARTIAL | `bowker-star-sorting-things-out.md`: torque is a mismatch with "a person's own account of themselves", and "the system wins". The dict dropped both. | rewritten |
| Triple | SUPPORTED | `rdf-resource-description-framework-1-1.md`: "subject–predicate–object statements" | keep |
| Unique name assumption | PARTIAL | `description-logics-dls.md`: "different names need not denote different things". The `owl:sameAs` clause is supported by no note. | rewritten |
| Upper ontology | SUPPORTED | `bfo-basic-formal-ontology.md`: "a small upper-level ontology … it deliberately excludes physical, chemical, biological, and other terms belonging to specialized sciences"; `gist.md`: "minimalist, domain-independent upper ontology" | keep |

Nine kept as written, sixteen rewritten from a note's own text, one cut and replaced
(**Justification** → **Explanation**). The rewritten text is in `scripts/build_site.py`.
