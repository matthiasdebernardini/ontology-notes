# Loom

**What it is**
Loom is a knowledge-representation language and environment for constructing intelligent applications, developed at USC's Information Sciences Institute. Its deductive system supports declarative definitions, rules, facts, and default rules while integrating logic programming, production rules, and object-oriented programming.

**Key concepts**
- A classifier uses forward chaining, semantic unification, and object-oriented truth maintenance to compile declarative knowledge into a network for online deductive queries.
- A logic-based pattern matcher drives both production rules and pattern-directed object-oriented method dispatch.
- Loom can act as a deductive layer over an ordinary CLOS network.
- Ontosaurus provides a dynamically generated, hyperlinked browser for Loom and PowerLoom knowledge bases.

**How you'd use it**
Define domain concepts, facts, defaults, and rules, then rely on the classifier and query machinery to maintain and reason over the knowledge base. The source also describes using Loom as a common high-level vocabulary over heterogeneous information sources or as a domain-model layer above lower-level application data.

**LLM angle**
none stated

**Pitfalls & lessons**
The fetched project page's release news is historical, with Loom 4.0 dated July 1999 and its most recent listed news dated June 2006. The software is open-source licensed but explicitly remains USC intellectual property and is not in the public domain.

**Verdict**
A historically significant integrated reasoning environment with unusually close declarative/procedural coupling; evaluate its dated release context before adopting it for new work.

## Sources consulted
- https://www.isi.edu/isd/LOOM/
- `sources/loom.txt`
