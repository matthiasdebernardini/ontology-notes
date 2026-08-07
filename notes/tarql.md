# Tarql

**What it is**

Tarql is a Java command-line tool, based on Apache ARQ, that converts CSV files to RDF using SPARQL 1.1 syntax. It treats CSV contents as a table of variable bindings and commonly generates RDF with `CONSTRUCT` queries.

**Key concepts**

Header names become SPARQL variables by default, while headerless input uses `?a`, `?b`, and so on; `?ROWNUM` exposes the non-empty input-row number. Mappings may be `SELECT`, `ASK`, or one or more consecutive `CONSTRUCT` queries, and the CLI supports CSV/TSV parsing controls, Turtle or N-Triples output, testing, and duplicate removal.

**How you'd use it**

Write a SPARQL mapping that binds tabular columns, computes IRIs or tagged literals with SPARQL expressions, and constructs the desired RDF, then run `tarql mapping.sparql input.csv`. Use `--test` to inspect the template, variables, and a few rows while developing the mapping.

**LLM angle**

none stated

**Pitfalls & lessons**

CSV and TSV inputs vary in headers, delimiters, quote/escape characters, and encodings, so configure parsing explicitly when defaults do not fit. In multi-`CONSTRUCT` mappings, generated triples can feed later queries, and the source warns that `OPTIONAL`/`BIND` order is significant.

**Verdict**

A focused bridge from tables to RDF that lets existing SPARQL skills define both transformation logic and output structure.

## Sources consulted

- https://tarql.github.io/
- `sources/tarql.txt`
