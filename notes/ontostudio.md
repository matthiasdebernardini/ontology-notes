# OntoStudio

**What it is**
OntoStudio X is a lightweight, Excel-based IDE for building explainable knowledge systems with OntoBroker's Java API and ObjectLogic capabilities. It lets engineers and domain experts model, run, query, debug, and audit active ontologies within macro-free `.xlsx` workbooks.

**Key concepts**
- ObjectLogic queries return cell values or spill into Excel dynamic arrays.
- Named intermediate objects can be reused across formulas, and a workbook can connect to multiple OntoBroker servers and ontologies.
- The bundled Java and Python bridges avoid VBA macros.
- ObjectLogic supports higher-order rules, expressive frames, parametrized relations, and built-ins; an F2 workflow opens cell content in VS Code with syntax coloring.

**How you'd use it**
Create a manager connection to one or more OntoBroker servers, bind named ontology objects in the workbook, declare axioms and rules with worksheet functions, and run spilling queries for automatically sized result tables. Use Java or Python helpers where needed while keeping ontology artifacts and results addressable from spreadsheet cells.

**LLM angle**
none stated

**Pitfalls & lessons**
The described workflow depends on OntoBroker servers and targets OntoBroker 6.x for its full ObjectLogic rule support. The fetched page is a product overview rather than a compatibility, deployment, or licensing specification.

**Verdict**
A distinctive spreadsheet-native ontology IDE for teams that want live reasoning and auditability inside Excel, provided their stack is centered on OntoBroker and ObjectLogic.

## Sources consulted
- https://semafora-systems.com/technology/ontostudio-x/
- `sources/ontostudio.txt`
