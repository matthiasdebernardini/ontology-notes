# Food Ontology

**What it is**

This is an RDF/XML OWL ontology for foods, drinks, meals, and meal courses, derived from and substantially modifying a DAML wine ontology. It imports the companion wine ontology and connects local food concepts to wine classes, properties, and named values.

**Key concepts**

- A hierarchy rooted in `ConsumableThing`, including `EdibleThing`, `PotableLiquid`, `Meal`, `MealCourse`, fruits, meats, seafood, desserts, and pasta dishes.
- Four object properties: `madeFromFruit`, `course`, `hasFood`, and `hasDrink`, each with stated domains and ranges.
- OWL constructions including subclassing, disjointness, union and intersection classes, cardinality constraints, value restrictions, enumerations, `equivalentClass`, and `sameAs`.
- Course classes encode drink constraints: for example, a spicy red-sauce pasta course restricts its drink to red, full-bodied, strong, dry wine characteristics.

**How you'd use it**

Use it as an OWL example for modeling meals and food categories, then classify course descriptions or check their restrictions against imported wine characteristics. Its course axioms also demonstrate how a food category can constrain the properties of a paired drink.

**LLM angle**

none stated

**Pitfalls & lessons**

The source comment says the food and wine ontologies mutually import one another because they share many wine properties, so the model is intentionally coupled to its companion ontology rather than self-contained. Its scope is selective: the file concentrates on a small set of meal, food, and pairing categories rather than presenting a general inventory of food knowledge.

**Verdict**

A useful, compact OWL modeling example—especially for restrictions, class expressions, and cross-ontology links—but too selective and wine-dependent to serve as a standalone broad food ontology.

## Sources consulted

- https://www.w3.org/TR/2004/REC-owl-guide-20040210/food.rdf
- Local fetched source: `sources/food-ontology.txt`
