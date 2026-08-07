# Dublin Core Metadata Element Set

**What it is**

The Dublin Core Metadata Element Set 1.1 is a vocabulary of fifteen broad, generic properties for describing many kinds of resources. The fetched 2012 reference is explicitly a historical snapshot; current documentation for these terms is part of the larger DCMI Metadata Terms specification.

**Key concepts**

- The fifteen elements are contributor, coverage, creator, date, description, format, identifier, language, publisher, relation, rights, source, subject, title, and type.
- The legacy `dc:` properties have no formal domains or ranges so existing “simple Dublin Core” RDF implementations remain conformant.
- Correspondingly named `dcterms:` properties are subproperties of the legacy terms and add formal domains and ranges for machine-processable inference.
- DCMI terms are designed to be combined with compatible vocabularies in application profiles.

**How you'd use it**

Attach a small, interoperable metadata record to a resource using the fifteen generic properties, applying controlled vocabularies or formal identifiers where the term guidance recommends them. Choose between the legacy `dc:` and `dcterms:` variants according to application requirements, while following DCMI’s encouragement to prefer the more semantically precise `dcterms:` properties over time.

**LLM angle**

none stated

**Pitfalls & lessons**

The page warns that this version is somewhat out of date and directs implementers to DCMI Metadata Terms for current documentation. The two namespaces are not interchangeable in semantics: `dcterms:` adds domains and ranges that the legacy `dc:` properties intentionally omit.

**Verdict**

A compact historical reference for the original fifteen Dublin Core properties; useful for legacy interpretation, while new work should consult the current DCMI terms and favor their more precise variants where appropriate.

## Sources consulted

- http://dublincore.org/documents/dces/
- `sources/dublin-core-metadata-element-set.txt`
