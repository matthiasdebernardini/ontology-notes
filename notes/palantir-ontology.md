# The Palantir Ontology

**What it is**
Palantir's Ontology is the operational layer at the centre of Foundry's architecture. Palantir's own architecture documentation states that it is designed to represent the interconnected *decisions* of an enterprise rather than its data, and that it is explicitly "not a semantic layer." It sits above integrated datasets, virtual tables, and models, and connects them to real-world counterparts — plants, equipment, products, customer orders, financial transactions. Palantir describes it in many settings as a digital twin of the organisation.

**Key concepts**
- **The fourfold integration: data, logic, action, and security.** Data flows in from ERP estates, systems of record, CRMs, industrial databases, geospatial repositories, sensors, and document stores, and is unified into objects, properties, and links.
- **Semantic elements — the nouns.** An **object type** is the schema definition of a real-world entity or event; an **object** is one instance; an **object set** is a collection. A **link type** defines a relationship between two object types and is bidirectional, with two independently traversable sides. Palantir's own analogy: an object type is like a dataset, an object like a row, an object set like a filtered set of rows, and a link type like a join.
- **Kinetic elements — the verbs.** An **action type** defines a set of edits to objects, properties, and links that a user can take as a single transaction, with parameters, validation rules, submission criteria, and side effects such as notifications. **Functions** carry the logic behind an action, which may be a business rule, a machine-learning model, a language-model function, or a multi-step orchestration. **Interfaces** give object-type polymorphism.
- **Writeback.** Edits commit to the Ontology, propagate to every application, and are captured in an object type's writeback dataset, so user decisions become data.
- **Security as a first-class element**, enforced across data, logic, and action simultaneously, with agents inheriting scope from a human user or a project's permission structure.
- **Language, Engine, and Toolchain** as the three component groups of the system.

**How you'd use it**
Compare it against the W3C stack rather than assuming it competes. Palantir's Ontology and OWL both aim at shared meaning across heterogeneous sources, and there the resemblance stops. OWL is a logic with model-theoretic semantics under an open-world assumption, designed for anonymous parties on a public web, with reasoners that derive consequences. Palantir's Ontology is a closed-world operational system for one organisation, whose distinguishing feature is that it models actions and permissions as first-class primitives. OWL cannot express "an HR employee may reassign this person's role, and doing so notifies both managers." That gap is the product.

**LLM angle**
Palantir positions the Ontology as the tool surface for AI agents: object queries provide retrieval context, functions and action types provide tools, and the security layer governs a workforce of humans and agents together. The pitch is that an agent should not be given raw table access, but a governed set of nouns it can read and verbs it is permitted to invoke.

**Pitfalls & lessons**
The vocabulary is borrowed from the formal tradition, but the semantics are not. There is no reasoner deriving subsumption, no open-world assumption, and no shared public vocabulary. Reading Palantir's "ontology" as an OWL ontology, or as an implementation of the Semantic Web programme, misdescribes both. Note also that links between object types across different Ontologies are not supported, which puts a hard boundary on federation.

## Sources consulted
- https://palantir.com/docs/foundry/architecture-center/ontology-system/
- https://palantir.com/docs/foundry/ontology/overview/
- https://palantir.com/docs/foundry/object-link-types/object-types-overview/
- https://palantir.com/docs/foundry/object-link-types/link-types-overview/
- https://palantir.com/docs/foundry/action-types/overview/
- https://www.palantir.com/platforms/ontology/
- `research/firecrawl/pltr-ontology-system.md`
- `research/firecrawl/pltr-ontology-overview.md`
- `research/firecrawl/pltr-object-types.md`
- `research/firecrawl/pltr-link-types.md`
- `research/firecrawl/pltr-action-types.md`
