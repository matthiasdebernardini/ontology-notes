# Open Graph protocol

**What it is**

The Open Graph protocol is a metadata vocabulary that lets a web page be represented as a rich object in a social graph. Its initial design is based on RDFa and uses `<meta>` elements in the page’s `<head>`, with developer simplicity as an explicit goal.

**Key concepts**

- Every page requires `og:title`, `og:type`, `og:image`, and `og:url`; the URL is the object’s canonical permanent identifier in the graph.
- Recommended optional metadata includes audio, description, determiner, locale and alternate locales, site name, and video.
- Structured properties add details such as a media item’s secure URL, MIME type, dimensions, and image alternative text.
- Repeating a meta property forms an array, while global and custom namespaced object types extend the type system.

**How you'd use it**

Add the four required properties to a page’s `<head>`, then supply optional and type-specific properties for the preview or graph object you need. Add structured media metadata after its root property, and provide `og:image:alt` when an Open Graph image is present.

**LLM angle**

none stated

**Pitfalls & lessons**

Some `og:type` values impose additional required properties. For repeated values, the first tag wins conflicts; structured properties must immediately follow the root value they describe, because a new root starts a new grouping. The protocol also says an Open Graph image should have alternative text.

**Verdict**

A deliberately small implementation target for turning ordinary pages into graph objects, with enough extension points for richer media and domain-specific types.

## Sources consulted

- http://ogp.me/
- `sources/open-graph-protocol.txt`
