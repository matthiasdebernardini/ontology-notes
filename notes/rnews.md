# rNews

**What it is**
rNews is an IPTC-approved standard for embedding news-specific metadata in HTML documents. It provides the terminology and data model needed to give article regions machine-readable meaning through RDFa or HTML5 Microdata rather than relying on visual styling.

**Key concepts**
- The page covers production rNews 1.x and says version 1.2 was approved on 23 October 2013.
- Its classes include concepts, places, geographic coordinates, people, organizations, storylines, news items, articles, media objects, and user comments.
- RDFa and HTML5 Microdata are the embedding frameworks described for applying rNews metadata in HTML.
- The standard is published under the Creative Commons Attribution 3.0 license.

**How you'd use it**
Mark up an online news page so machines can reliably identify the headline and other news entities and relationships independent of site-specific presentation. Follow the implementation guides for the chosen RDFa or Microdata syntax and use the class documentation or quick reference to select terms.

**LLM angle**
none stated

**Pitfalls & lessons**
Visual HTML styling alone is not reliable machine-readable semantics because publishers use inconsistent styles and may reuse the same style for multiple regions. The page describes an OWL ontology only as a third draft available for review, so that artifact should not be confused with the approved production status stated for rNews 1.x.

**Verdict**
A domain-specific semantic-markup model for making online news understandable to machines, with clear RDFa and Microdata implementation paths.

## Sources consulted
- http://dev.iptc.org/rNews
- `sources/rnews.txt`
