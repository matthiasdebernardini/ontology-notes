# The Palantir Ontology

**What it is**
Palantir's Ontology is the operational layer at the centre of Foundry's architecture. Palantir's own architecture documentation states that it is designed to represent the interconnected *decisions* of an enterprise rather than its data, and that it is explicitly "not a semantic layer." It sits above integrated datasets, virtual tables, and models, and connects them to real-world counterparts — plants, equipment, products, customer orders, financial transactions. Palantir describes it in many settings as a digital twin of the organisation.

**Key concepts**
- **The fourfold integration: data, logic, action, and security.** Data flows in from ERP estates, systems of record, CRMs, industrial databases, geospatial repositories, sensors, and document stores, and is unified into objects, properties, and links.
- **Semantic elements — the nouns.** An **object type** is the schema definition of a real-world entity or event; an **object** is one instance; an **object set** is a collection. A **link type** defines a relationship between two object types and is bidirectional, with two independently traversable sides. Palantir's own analogy: an object type is like a dataset, an object like a row, an object set like a filtered set of rows, and a link type like a join.
- **Kinetic elements — the verbs.** An **action type** is "the definition of a set of changes or edits to objects, property values, and links that a user can take at once"; an action is "a single transaction." It "includes the side effect behaviors that occur with action submission" — Palantir's worked example is a notification to the old and new manager on a role change. The action-types documentation points onward to "rules, parameters, and submission criteria." **Functions** "provide a way to author and evolve business logic with arbitrary complexity"; the logic behind a given action "could be a simple business rule, a conventional machine learning model, an LLM-driven function, or a complex multi-step orchestration that involves several compute engines." **Interfaces** "provide object type polymorphism, allowing for consistent modeling of and interaction with object types that share a common shape."
- **Writeback.** Edits commit to the Ontology, propagate to every application, and are captured in an object type's writeback dataset, so user decisions become data.
- **Security as a first-class element**, enforced across data, logic, and action simultaneously, with agents inheriting scope from a human user or a project's permission structure.
- **Language, Engine, and Toolchain** as the three component groups of the system.

**How you'd use it**
Compare it against the W3C stack rather than assuming it competes. The comparison that follows is mine: Palantir's documentation never mentions OWL, RDF, the W3C, reasoners, or world assumptions, so nothing below is a Palantir claim. Both aim at shared meaning across heterogeneous sources, and there the resemblance stops. OWL is a logic with model-theoretic semantics under an open-world assumption, designed for anonymous parties on a public web, with reasoners that derive consequences — see [owl-2-web-ontology-language.md](owl-2-web-ontology-language.md) and [description-logics-dls.md](description-logics-dls.md). Palantir's Ontology is a closed-world operational system for one organisation, whose distinguishing feature is that it models actions and permissions as first-class primitives. OWL cannot express "an HR employee may reassign this person's role, and doing so notifies both managers." That gap is the product.

**LLM angle**
Palantir positions the Ontology as the tool surface for AI agents, and explicitly against retrieval as the framing: it "enables LLMs to go beyond the data-centric limitations of retrieval-augmented generation, and instead interface with the interconnected data, logic, and action primitives … through an extensible tools paradigm." The Ontology is "a 'tool factory' that lets your builders define tools for both humans and agents," actions "can be automatically surfaced as tools for AI-driven copilots and automations," and the security system "has to reconcile all of these granular policies, at the time of interaction, across tens of thousands of humans and agents." The pitch, in my summary, is that an agent gets a governed set of nouns it can read and verbs it is permitted to invoke rather than the tables underneath.

**Pitfalls & lessons**
The vocabulary is borrowed from the formal tradition, and Palantir acknowledges some of that debt at the data-type level: its type reference says "data types in Foundry are inspired by similar concepts in RDF, OWL and XSD." The semantics are not borrowed. My reading, since the documentation neither asserts nor denies it: there is no reasoner deriving subsumption, no open-world assumption, and no shared public vocabulary, so reading Palantir's "ontology" as an OWL ontology, or as an implementation of the Semantic Web programme, misdescribes both. Palantir does state one hard boundary itself: "links between object types across different Ontologies is not supported."

**Verdict**
Worth studying, and the most useful counterexample in this corpus. It shows that the commercially successful sense of the word keeps the nouns, drops the logic, and adds verbs and permissions — which tells you what the market actually wanted from an ontology.

## Sources consulted
- https://palantir.com/docs/foundry/architecture-center/ontology-system/
- https://palantir.com/docs/foundry/ontology/overview/
- https://palantir.com/docs/foundry/object-link-types/object-types-overview/
- https://palantir.com/docs/foundry/object-link-types/link-types-overview/
- https://palantir.com/docs/foundry/action-types/overview/
- https://www.palantir.com/platforms/ontology/
- https://blog.palantir.com/connecting-ai-to-decisions-with-the-palantir-ontology-c73f7b0a1a72
- https://palantir.com/docs/foundry/object-link-types/type-reference/
- `research/firecrawl/pltr-ontology-system.md`
- `research/firecrawl/pltr-ontology-overview.md`
- `research/firecrawl/pltr-object-types.md`
- `research/firecrawl/pltr-link-types.md`
- `research/firecrawl/pltr-action-types.md`
- `research/firecrawl/pltr-platform-ontology.md`
- `research/firecrawl/pltr-blog-ai-decisions.md`
- `research/exa/palantir-ont.json`
