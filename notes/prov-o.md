# PROV-O

**What it is**
PROV-O is the W3C Recommendation that expresses the PROV Data Model in OWL 2, providing classes, properties, and restrictions for representing and exchanging provenance across systems and contexts. It is intentionally lightweight, directly usable, and designed to be specialized for domain-specific provenance models.

**Key concepts**
Its foundation is `prov:Entity`, `prov:Activity`, and `prov:Agent`: things with fixed aspects, processes that act on entities over time, and bearers of responsibility. Core relations describe generation, use, derivation, attribution, association, delegation, and timing; expanded terms add collections, bundles, agent types, versions/alternates, primary sources, locations, and invalidation. Qualified influence nodes such as `prov:Usage`, `prov:Generation`, and `prov:Association` let a model attach details such as time, role, or plan to an otherwise binary relation.

**How you'd use it**
Publish RDF provenance chains showing which activities used or generated entities and which agents were responsible, then add expanded or qualified terms only when the application needs more detail. Prefer an unqualified relation when it needs no attributes; when using the qualified form, also including its equivalent unqualified statement is encouraged to make consumption easier.

**LLM angle**
none stated

**Pitfalls & lessons**
Consumers should recognize both qualified and unqualified forms and treat the qualified form as implying the unqualified one. PROV-O defines few inverse properties because competing assertion directions force consumers to add reasoning, code, or larger queries; use the ontology's preferred property direction. It is based on OWL 2 RL but has five union-domain/range axioms outside that profile, and multiple RDFS domains/ranges denote intersections rather than alternatives.

**Verdict**
A compact, progressively adoptable provenance vocabulary with a simple core and an explicit path to richer, domain-specific detail. Its interoperability guidance is practical, but implementers need to handle the two relationship forms and its small OWL 2 RL exception set deliberately.

## Sources consulted

- https://www.w3.org/TR/prov-o/
- `sources/prov-o.txt`
