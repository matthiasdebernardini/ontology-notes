# Racer

**What it is**

Racer is a freely available knowledge-representation system implementing an optimized tableau calculus for the description logic SHIQ(D). It succeeds RacerPro and supports standard reasoning over T-boxes and A-boxes as well as non-standard services such as logical abduction.

**Key concepts**

Its nRQL conjunctive query language supports features including negation as failure, numeric constraints across individuals’ attribute values, and substring relations between string attributes. Racer exposes reasoning services through Common Lisp and Java APIs and is also available as open source on GitHub.

**How you'd use it**

Install it through Quicklisp with `(ql:quickload "racer")`, then use its reasoning and nRQL query facilities from Lisp or Java. The page recommends Portacle as a host environment and describes a Portacle-based setup.

**LLM angle**

none stated

**Pitfalls & lessons**

The page says Racer requires ASDF 2.32 and gives an additional encoding setting for LispWorks. Its Portacle setup also includes platform-specific configuration, including a macOS quarantine command and memory-related Lisp settings.

**Verdict**

A feature-rich description-logic reasoner for T-box/A-box inference and expressive querying, especially suited to users comfortable with its Lisp-centered installation path.

## Sources consulted

- https://www.ifis.uni-luebeck.de/~moeller/racer/
- `sources/racer.txt`
