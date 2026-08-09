# Narration setup

## Michael Caine

ElevenLabs launched an Iconic Marketplace with Sir Michael Caine as a
partner. His licensed voice is available **inside the ElevenReader app** to
narrate books, articles, PDFs, and uploaded text.

It is **not** in the shared voice library and not reachable through the
ElevenLabs API. So the route is the app, not a generated MP3:

1. Open ElevenReader on the iPhone.
2. Add each file from `transcripts/` as a document (they are plain `.txt`).
3. Pick Michael Caine from the Iconic voices.
4. Play in order, 01 through 10.

Ten files, one per walk, eighteen to twenty-four minutes each.

## Why the transcripts are shaped this way

Everything a narrator cannot say has been kept out: no headings, no bullets,
no markdown, no code, no URLs. Verified by grep — the files contain none of
these. Acronyms are expanded on first use in every lecture, because you may
start anywhere in the series.

Numbers, dates, and Latin phrases are written the way they should be spoken
(`1606`, `scientia entis in genere`). Text-to-speech handles both correctly.

## If you want MP3 files instead

The Caine voice cannot be generated through the API, so an offline render
needs a different narrator. A British male narration voice from the shared
library works; generate per file with the ElevenLabs `text_to_speech` tool at
`stability` around 0.4 and `speed` 1.0.

Cost check first: about 29,000 words, roughly 165,000 characters across the
ten files. Confirm the character allowance before rendering all ten.
