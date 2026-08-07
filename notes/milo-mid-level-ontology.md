# MILO (Mid-Level Ontology)

**What it is**
MILO is a formal ontology intended to bridge SUMO’s abstract content and the richer detail of domain ontologies. Its KIF source combines natural-language documentation with subclass and instance declarations, relation signatures, functions, and logical rules across topics such as people, processes, communication, devices, substances, social relationships, and measurement.

**Key concepts**
- SUMO-to-domain bridge: mid-level vocabulary connects abstract categories to more specific concepts.
- Formal semantics: `subclass`, `instance`, `domain`, `range`, implication, equivalence, and temporal predicates constrain the represented terms.
- Time-sensitive modeling: rules use constructs such as `holdsDuring` and `WhenFn`; the organism-remains section explicitly treats a living organism and its post-death remains as temporally disjoint.
- Broad reusable vocabulary: documented terms include human life stages, starting and stopping processes, communication and social relations, devices, shapes, quantities, and biological classes.

**How you'd use it**
Use MILO as a shared mid-level vocabulary when a domain ontology needs more specificity than SUMO alone provides. Reuse its documented classes and relations, their argument constraints, and its implication rules to connect domain assertions to broader categories and derive explicitly encoded consequences.

**LLM angle**
none stated

**Pitfalls & lessons**
The file warns that its treatment of death and organism remains is awkward but deliberate: `Dead` should not be applied to an `Organism`, nor `Living` to `OrganismRemains`. It also labels adult legal personhood as a simplified, jurisdiction-dependent model, and its licensing notice requires GPL compliance plus credit to Teknowledge and Articulate Software and asks users to cite the named FOIS-2001 paper.

**Verdict**
A substantial, formally axiomatized bridge vocabulary with useful domain breadth, but adopters should inspect its modeling assumptions, temporal distinctions, and licensing/citation conditions rather than treating every rule as context-free.

## Sources consulted
- https://github.com/ontologyportal/sumo/blob/master/Mid-level-ontology.kif
- `sources/milo-mid-level-ontology.txt`
