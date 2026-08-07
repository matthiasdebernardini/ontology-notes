# Description Logic Complexity Navigator

**What it is** — A web navigator maintained by Evgeny Zolin for complexity results about reasoning in Description Logics. It starts from ALC and lets a selected logic vary by concept constructors, role constructors, TBox/RBox features, and whether complex roles are allowed in number restrictions.

**Key concepts** —
- The selectable concept features include functionality, unqualified and qualified number restrictions, nominals, and a least-fixpoint operator.
- Role features include inverse, intersection, union, complement, composition, reflexive-transitive closure, and concept identity; axiom choices include empty, acyclic, or general TBoxes plus transitivity, role hierarchies, and complex role inclusions.
- Results cover concept satisfiability, ABox consistency, and finite- and tree-model properties.
- The page distinguishes upper bounds (“in C”), lower bounds (“C-hard”), and matching bounds (“C-complete”).

**How you'd use it** — Select the constructors and axiom features of a Description Logic, then consult the reported reasoning complexity and model properties. When a target combination has no result, the page suggests adding or removing ingredients to inspect known neighboring logics, while warning that this does not fill every intermediate gap.

**LLM angle** — none stated

**Pitfalls & lessons** — The author says the navigator is always incomplete and frequently updated; a missing result means the page author found none in the literature, not that no result exists. Logic names can also hide whether complex roles are allowed in number restrictions, and the navigator cannot display every independent combination of role use in value versus number restrictions.

**Verdict** — A focused comparison tool for navigating how Description Logic features relate to reasoning complexity, best treated as an incomplete literature map rather than an exhaustive authority.

## Sources consulted

- http://www.cs.man.ac.uk/~ezolin/dl/
- `sources/description-logic-complexity-navigator.txt`
