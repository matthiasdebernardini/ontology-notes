# Gruber's Definition and Its Successors

**What it is**
The sentence that created the computer-science sense of the word. Tom Gruber's 1993 work, produced in the context of the DARPA Knowledge Sharing Effort, defined an ontology as "an explicit specification of a conceptualization," where a conceptualization is "the objects, concepts, and other entities that are presumed to exist in some area of interest and the relationships that hold among them." The conceptualization half is borrowed from Genesereth and Nilsson, who describe it as an abstract, simplified view of the world represented for some purpose, and who note that every knowledge base is committed to some conceptualization whether or not it admits it.

**Key concepts**
Explicit specification of a conceptualization; ontology as an interface specification rather than an internal encoding; ontological commitment as an agreement to use a vocabulary consistently; Borst's 1997 revision to "a formal specification of a shared conceptualization," which adds consensus; Guarino's formal reconstruction of conceptualization as an intensional relational structure.

**How you'd use it**
Read the definition as an engineering contract, not a metaphysical claim. Gruber's point is that an ontology is the language two agents use to talk to each other about a domain. An agent that supports the interface is not obliged to store its knowledge that way internally. That distinction is why an ontology can sit above heterogeneous systems that share nothing but the vocabulary, and it is exactly the architectural move Palantir's Ontology and every enterprise semantic layer makes.

**LLM angle**
none stated

**Pitfalls & lessons**
The words "specification" and "conceptualization" have caused decades of argument, and Guarino wrote a paper largely to repair the informality. Treating the definition as self-explanatory produces the common failure where a team calls any schema an ontology. The load-bearing words are *explicit* — the commitments are written down and machine-readable — and, after Borst, *shared* — more than one party agreed.

## Sources consulted
- https://tomgruber.org/writing/definition-of-ontology/
- https://tomgruber.org/writing/onto-design.pdf
- https://iaoa.org/isc2012/docs/Guarino2009_What_is_an_Ontology.pdf
- `research/firecrawl/gruber-definition.md`
- `research/firecrawl/guarino-what-is-ontology.md`
