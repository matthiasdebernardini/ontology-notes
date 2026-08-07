# cwm

**What it is**
cwm is a general-purpose Semantic Web data processor and forward-chaining reasoner for querying, checking, transforming, and filtering information. Its core language is RDF extended with rules, using RDF/XML or RDF/N3 serializations, and it is written in Python as part of SWAP.

**Key concepts**
It can load and emit RDF/XML or N3, apply N3 rules, filter query results, pretty-print data, and generate arbitrary formats. Built-ins cover math, strings, web document access, command-line and environment inputs, cryptographic operations, and some database access.

**How you'd use it**
Use the command-line tool to combine RDF data and N3 rules, derive results by forward chaining, filter them to a query, and serialize the output. The page positions it primarily for prototyping Semantic Web applications.

**LLM angle**
none stated

**Pitfalls & lessons**
Untrusted rules can read web or confidential data, leak information through URIs, and consume processor time or memory. The software is explicitly not guaranteed or made for production use, and its main RDF/XML parser omits some obscure syntax cases.

**Verdict**
A flexible rule-driven RDF/N3 processing workbench for prototypes, with unusually clear warnings against trusting rules or treating it as production-grade.

## Sources consulted
- https://www.w3.org/2000/10/swap/doc/cwm.html
- `sources/cwm.txt`
