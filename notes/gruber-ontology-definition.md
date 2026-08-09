# Gruber's Definition and Its Successors

**What it is**
The sentence that created the computer-science sense of the word. Tom Gruber's 1993 work, written inside what his own acknowledgements call the ARPA (later DARPA) Knowledge Sharing Effort, defined an ontology as "an explicit specification of a conceptualization," where a conceptualization is "the objects, concepts, and other entities that are presumed to exist in some area of interest and the relationships that hold among them." That wording is Gruber's own 2009 restatement; Genesereth and Nilsson's original says "assumed to exist." The conceptualization half is borrowed from Genesereth and Nilsson, who describe it as an abstract, simplified view of the world represented for some purpose, and who note that every knowledge base is committed to some conceptualization whether or not it admits it.

**Key concepts**
Explicit specification of a conceptualization; ontology as an interface specification rather than an internal encoding; ontological commitment as an agreement to use a vocabulary consistently; Borst's 1997 revision to "a formal specification of a shared conceptualization," which adds consensus; Guarino's formal reconstruction of conceptualization as an intensional relational structure.

**How you'd use it**
Read the definition as an engineering contract, not a metaphysical claim. Gruber's point is that an ontology is the language two agents use to talk to each other about a domain. An agent that supports the interface is not obliged to store its knowledge that way internally. Gruber puts it plainly: "The agents sharing a vocabulary need not share a knowledge base; each knows things the other does not." That is why an ontology can sit above heterogeneous systems that share nothing but the vocabulary. Palantir describes its own Ontology in the same architectural terms — it "sits on top of the digital assets integrated into the Palantir platform … and connects them to their real-world counterparts" — though Palantir never invokes Gruber; see [palantir-ontology.md](palantir-ontology.md).

**LLM angle**
none stated

**Pitfalls & lessons**
Gruber concedes that "the terms specification and conceptualization have caused much debate," and Guarino, Oberle and Staab wrote their 2009 chapter largely to repair the informality, noting that all the earlier definitions "were assuming an informal notion of 'conceptualization'." One standing objection, which Gruber records and rejects, is that the definition "is overly broad, allowing for a range of specifications from simple glossaries to logical theories couched in predicate calculus." Whether that breadth is a defect is still argued; in practice it is what lets a team call any schema an ontology. The load-bearing words are *explicit* — the commitments are written down and machine-readable — and, after Borst, *shared* — more than one party agreed.

**Verdict**
Worth studying, and short enough to read in full. The definition is the hinge between the philosophical and engineering senses of the word, and knowing which two words carry the weight — *explicit*, and after Borst *shared* — settles most arguments about whether a given artifact qualifies.

## Sources consulted
- https://tomgruber.org/writing/definition-of-ontology/
- https://tomgruber.org/writing/onto-design.pdf
- https://iaoa.org/isc2012/docs/Guarino2009_What_is_an_Ontology.pdf
- `research/firecrawl/gruber-definition.md`
- `research/firecrawl/guarino-what-is-ontology.md`
- `research/firecrawl/gruber-onto-design.md`
- `research/firecrawl/pltr-ontology-overview.md`
