# SKOS (Simple Knowledge Organization System)

**What it is**

SKOS is a W3C Recommendation defining a common data model for sharing and linking knowledge organization systems such as thesauri, classification schemes, subject-heading systems, and taxonomies on the Web. It represents those systems as RDF triples under a model formally defined as an OWL Full ontology, while explicitly distinguishing a knowledge organization system from a formal knowledge-representation ontology.

**Key concepts**

- URI-identified `skos:Concept` resources grouped into concept schemes.
- Preferred, alternative, and hidden multilingual labels; notations for scheme-specific codes; and extensible documentation notes.
- Hierarchical and associative semantic relations, labeled or ordered collections, and mappings between schemes using hierarchical, associative, close-equivalence, or exact-equivalence links.
- An optional SKOS-XL extension for identifying, describing, and linking lexical entities.

**How you'd use it**

Publish an existing thesaurus, taxonomy, or classification scheme as machine-readable RDF without first re-engineering it into formal domain axioms. Use labels, notes, relations, collections, and cross-scheme mappings to support exchange, linking, navigation, and discovery across applications.

**LLM angle**

none stated

**Pitfalls & lessons**

SKOS concepts model the ideas in a thesaurus as individuals and the scheme's descriptions as facts about those individuals; they are not OWL classes or formal facts about how the domain itself is arranged. The OWL Full/open-world basis is also important: missing data supports no conclusion, the specification defines relatively few integrity conditions, and its RDF/XML schema captures only a normative subset of the full specification.

**Verdict**

A strong fit for interoperable, Web-published controlled vocabularies when preserving their informal or semi-formal character matters; use OWL alongside it when the application instead needs formal domain axioms.

## Sources consulted

- https://www.w3.org/TR/skos-reference/
- Local fetched source: `sources/skos-simple-knowledge-organization-system.txt`
