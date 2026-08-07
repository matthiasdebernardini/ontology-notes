# Digital Buildings Ontology (DBO)

**What it is**

Digital Buildings is an Apache-licensed schema and toolset for representing structured information about buildings and installed equipment. Its ontology defines semantic primitives and concrete constructions for physical spaces, equipment, telemetry, and relationships; Google says a version is used to manage its own building portfolio.

**Key concepts**

- An **entity** is a modeled thing such as a building, floor, or equipment item. An **entity type** places it in a composable taxonomy and declares its expected fields; directed, named **connections** relate entities.
- **Subfields** are the basic units of meaning. Categorized subfields compose semantically precise **fields**, while units, states/multi-state groups, inheritance, abstract types, canonical types, and namespaces provide further structure.
- The ontology allows a global namespace plus exactly one child level; hierarchical namespacing is disallowed. Definitions may be elevated to the global namespace when safe.
- A building configuration is the instance or “Assertion box”: it maps real assets and raw data to ontology types using GUID-keyed entities, translations, links, and connections. The docs distinguish logical, reporting, and virtual entities.
- The supplied abstract model favors minimal atomic functional field sets composed into equipment types. Its stated target is portable high-level analysis and control—not a full cloud BMS.

**How you'd use it**

- Use the YAML ontology as the primary configuration source, or generate RDF/OWL from it. Extend entity types, fields, states, or subfields in YAML and validate extensions for consistency and backward compatibility.
- Describe one building (or another logical division) in a YAML building configuration, mapping device-native point names to standard fields with translations and linking reporting data into virtual devices where needed.
- Use ABEL to move between templated Google Sheets and building configurations, Explorer to compare ontology types, the Instance Validator for configurations and optional telemetry, the Ontology Validator for YAML extensions, and the RDF/OWL Generator for RDF output.
- The documented workflow is: reuse existing types where possible; otherwise propose and validate an ontology extension, then construct a GUID-based building configuration and validate both its type mapping and telemetry.

**LLM angle**

No LLM or RAG use is stated. The ontology docs do state that implicit inheritance forms a graph of related field concepts which can support navigation and search expansion—for example, fanning a search for `zone_air_temperature` across fields containing that subfield set.

**Pitfalls & lessons**

- Equipment boundaries are subjective: a flatter graph yields fewer, more complex entities, while deeper composition yields simpler comparable components but harder retrieval. DBO generally chooses the flatter approach because equipment is usually analyzed as a unit.
- Field names should use the smallest subfield set that is unambiguous in context; overly strict construction can create redundant or unwieldy names, yet arbitrary device scope means there is not always one correct name.
- The abstract model is intentionally reductionist, so low-level configuration, most interpreted alarms, and full BMS behavior are outside its normal focus unless explicitly needed.
- Some useful concrete-model conventions are not yet encoded in the ontology structure, detailed explanations are primarily HVAC-focused, and the ontology’s versioning process and constraints are still TBD.
- Building-configuration documentation includes details specific to Google’s campus implementation and warns that they may not transfer directly to other deployments.

**Verdict**

A practical, validation-centered building ontology for portable operational analytics and control, strongest when its deliberately minimal, flatter equipment model matches the deployment’s scope.

## Sources consulted

- `README.md`
- `ontology/README.md`
- `ontology/docs/overview.md`
- `ontology/docs/ontology.md`
- `ontology/docs/model.md`
- `ontology/docs/building_config.md`
- `ontology/docs/ontology_config.md`
- `ontology/docs/faq.md`
- `ontology/yaml/README.md`
- `ontology/rdf/README.md`
