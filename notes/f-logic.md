# F-Logic

**What it is**

F-Logic (frame logic) is a knowledge-representation and ontology language combining conceptual modeling and object/frame-oriented features with declarative syntax and logic-programming semantics. It was originally developed for deductive databases and is now used chiefly in semantic technologies.

**Key concepts**

Object identity, complex objects, inheritance, polymorphism, query methods, and encapsulation are core features. Its syntax represents classes, individuals, properties, relations, and rules; its usual semantics use a closed-world assumption, unlike the open-world assumption described for description logics.

**How you'd use it**

Use it to model classes and individuals, state object properties and relations, and write inference axioms for information integration, question answering, semantic search, or other rule-oriented semantic applications.

**LLM angle**

none stated

**Pitfalls & lessons**

Description logic and OWL are described as more popular and accepted. F-Logic is generally undecidable, while the source says OWL DL's underlying SHOIN description logic is decidable; the source also warns through an example that a syntactically expressible inference need not be factually sound.

**Verdict**

An expressive ontology and rule language when object/frame modeling and closed-world reasoning matter, but its lower adoption and general undecidability are important tradeoffs.

## Sources consulted

- https://en.wikipedia.org/wiki/F-logic
- `sources/f-logic.txt`
