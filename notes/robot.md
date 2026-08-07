# ROBOT

**What it is**
ROBOT is a tool for working with Open Biomedical Ontologies, available as a command-line program or as a library for JVM languages. Its Java code is divided into `robot-core` ontology operations and the `robot-command` command-line interface.

**Key concepts**
Its documented commands cover tasks such as annotation, conversion, diffing, extraction, filtering, materialization, merging, querying, reasoning, repair, reporting, templating, profile validation, and verification. The library exposes operation classes plus `IOHelper` methods for loading and saving ontologies and sets of term IRIs.

**How you'd use it**
Install Java 11 or later and run the packaged JAR through the supplied shell or batch script, or use the OBO Library Docker image. For embedded use, add the Maven artifacts or standalone JAR and compose `robot-core` operations—for example, loading an ontology and term list, extracting a core subset, and saving the result.

**LLM angle**
none stated

**Pitfalls & lessons**
The command-line installation requires both the JAR and the correct platform script on `PATH`. The source specifically warns that PowerShell versions before 6 write a byte-order mark that breaks the generated Windows batch file.

**Verdict**
A broad automation surface for ontology workflows, usable both from scripts and directly inside JVM applications.

## Sources consulted
- http://robot.obolibrary.org/
- `sources/robot.txt`
