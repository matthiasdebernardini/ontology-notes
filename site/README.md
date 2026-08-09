# site

The published book: https://ontology-course.pages.dev

Built with [mdBook](https://github.com/rust-lang/mdBook), the same generator
the Cargo book uses. `src/` and `book/` are both generated — edit the notes,
the transcripts, or `scripts/build_site.py`, never the output.

    python3 scripts/build_site.py
    mdbook build site
    wrangler pages deploy site/book --project-name ontology-course --branch main --commit-dirty=true

`src/lectures/transcripts/*.txt` are copied through untouched, so each lecture
has a plain-text URL a reader app can fetch.
