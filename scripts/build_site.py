#!/usr/bin/env python3
"""Generate the mdBook source tree in site/src from the knowledge base.

Everything under site/src is generated. Edit this script, not the output.
Run: python3 scripts/build_site.py && ~/.local/bin/mdbook build site
"""
import json
import pathlib
import re
import shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "site" / "src"

# Section order for the sidebar: history first, then the engineering stack,
# then criticism, matching the reading order the lectures use.
SECTION_ORDER = [
    "History & Foundations",
    "Operational Ontologies",
    "Criticism",
    "Upper-level Ontologies",
    "Mid-level Ontologies",
    "Cross-domain Ontologies",
    "Domain Ontologies",
    "Ontologies and Vocabularies",
    "Vocabularies",
    "Languages",
    "Logics",
    "Querying",
    "Rule and Schema Definition",
    "Reasoners",
    "Ontology Editors",
    "Ontology Utilities",
    "OWL-aware libraries",
    "Alignment & Matching",
    "Machine Learning",
    "Datastore",
    "Communities",
    "Related",
]

# Concepts the lectures use that are not themselves tools or vocabularies.
CONCEPTS = {
    "ABox": "The assertional part of a knowledge base: the individuals and the facts about them, as opposed to the class definitions in the TBox.",
    "Alignment": "Finding correspondences between entities in two different ontologies so data described by one can be read through the other.",
    "Axiom": "A statement in an ontology's formal vocabulary whose consequences a reasoner can derive.",
    "Classification": "The reasoning task of computing the full subclass hierarchy implied by an ontology's axioms.",
    "Closed-world assumption": "Treating anything not stated as false. F-logic, SPIN constraints, and Palantir's Ontology work this way. OWL does not.",
    "Conceptualization": "The abstract model of a domain that an ontology is a specification of, in Gruber's 1993 definition.",
    "Consistency checking": "Asking a reasoner whether an ontology is consistent, which is a separate question from whether an individual class is satisfiable.",
    "Description logic": "A family of languages more expressive than propositional logic and less expressive than first-order logic, forming the logical foundation of OWL and trading expressive power against reasoning complexity.",
    "Entailment": "A triple a reasoner derives from an ontology's axioms rather than one anyone asserted.",
    "Individual": "A named instance in an ontology, as opposed to a class or a property.",
    "Explanation": "A reasoner's step-by-step account of how a logical consequence follows from an ontology's axioms.",
    "Instance checking": "The reasoning task of asking whether an individual belongs to a class, listed alongside relation checking, subsumption, and concept-consistency checking.",
    "Materialization": "Expanding a graph with inferred triples ahead of time by forward chaining, as OWL-RL does for RDFS and OWL 2 RL.",
    "Microtheory": "Cyc's device for scoping assertions into small local contexts, each of which inhabits its own context.",
    "Object type": "Palantir's term for the schema definition of a real-world entity or event; its own analogy is that an object type is like a dataset and an object like a row.",
    "Ontological commitment": "What a theory must say exists for it to be true. Quine's answer to what ontology means for a formal theory.",
    "Open-world assumption": "Treating anything not stated as unknown rather than false, so that lack of a fact does not imply its negation. OWL's default.",
    "Punning": "Treating one name as both a class and an individual. Most OWL reasoners do not support it, which is why tools such as yamlpyowl generate proxy individuals instead.",
    "Reification": "Modelling provenance about a statement, one option alongside n-ary relations, named graphs, singleton properties, and NDFluents.",
    "Semantic layer": "A label Palantir explicitly rejects for its Ontology, which its architecture documentation says represents an enterprise's interconnected decisions rather than its data.",
    "Subsumption": "The relation of one class being a subclass of another, either declared as an axiom or derived by a reasoner.",
    "TBox": "The terminological part of a knowledge base: the concept hierarchy, as opposed to the role axioms in the RBox and the facts in the ABox.",
    "Torque": "Bowker and Star's term for the twisting that happens when a classification system and a person's own account of themselves do not line up, and the system wins.",
    "Triple": "The atomic unit of RDF: subject, predicate, object.",
    "Unique name assumption": "Assuming two different names refer to two different things. Description logics do not generally assume it, so different names need not denote different things.",
    "Upper ontology": "A domain-neutral ontology of very general categories, meant as a shared spine that domain ontologies hang from.",
}

LECTURES = [
    ("01-three-things-people-mean", 'Three Things People Mean by "Ontology"'),
    ("02-aristotle-to-wolff", "From Aristotle to Wolff: Where the Word Came From"),
    ("03-quine-ontological-commitment", "Quine, and Ontology as a Property of Theories"),
    ("04-cyc-and-the-engineering-sense", "The Cathedral: Cyc, and the Birth of the Engineering Sense"),
    ("05-semantic-web-vision-and-stack", "The Semantic Web: A Vision and the Stack It Built"),
    ("06-how-the-machinery-works", "How the Machinery Actually Works"),
    ("07-building-one-for-real", "Building One for Real"),
    ("08-the-criticisms-that-landed", "The Criticisms That Landed"),
    ("09-palantir-operational-layer", "Palantir: The Ontology as an Operational Layer"),
    ("10-politics-and-what-comes-next", "The Politics of an Installed Ontology, and What Comes Next"),
]


def first_sentence(text, limit=260):
    text = " ".join(text.split())
    match = re.match(r"(.+?[.!?])(\s|$)", text)
    out = match.group(1) if match else text
    return out if len(out) <= limit else out[:limit].rsplit(" ", 1)[0] + "…"


def anchor(name):
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return slug


def write(rel, text):
    path = SRC / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def main():
    if SRC.exists():
        shutil.rmtree(SRC)
    SRC.mkdir(parents=True)

    index = json.loads((ROOT / "NOTE_INDEX.json").read_text())
    by_slug = {e["slug"]: e for e in index}
    sections = {}
    for entry in index:
        sections.setdefault(entry["section"], []).append(entry)
    for entries in sections.values():
        entries.sort(key=lambda e: e["name"].lower())

    ordered_sections = [s for s in SECTION_ORDER if s in sections]
    ordered_sections += sorted(s for s in sections if s not in SECTION_ORDER)

    # --- notes ---------------------------------------------------------
    for entry in index:
        body = (ROOT / entry["note"]).read_text()
        # Local capture paths are not published; the URLs above them are.
        body = re.sub(r"^- `sources/.*`$\n?", "", body, flags=re.M)
        write(f"notes/{entry['slug']}.md", body)

    note_index_lines = [
        "# All notes",
        "",
        f"{len(index)} notes across {len(sections)} sections. Every note follows the",
        "same shape: what it is, key concepts, how you would use it, the angle on",
        "large language models, pitfalls, and a verdict.",
        "",
    ]
    for section in ordered_sections:
        note_index_lines.append(f"## {section}")
        note_index_lines.append("")
        for entry in sections[section]:
            note_index_lines.append(
                f"- [{entry['name']}](notes/{entry['slug']}.md) — "
                f"{first_sentence(entry['fields']['What it is'], 160)}"
            )
        note_index_lines.append("")
    write("notes.md", "\n".join(note_index_lines))

    # --- glossary ------------------------------------------------------
    terms = {}
    for name, definition in CONCEPTS.items():
        terms[name] = (definition, None)
    for entry in index:
        name = entry["name"]
        if name in terms:
            name = f"{name} ({entry['section']})"
        terms[name] = (
            first_sentence(entry["fields"]["What it is"]),
            f"notes/{entry['slug']}.md",
        )

    glossary = [
        "# Glossary",
        "",
        "Every term the lectures and notes use, in one alphabetical list.",
        "Concepts are defined here. Tools, languages, and vocabularies link to",
        "their note.",
        "",
    ]
    letters = sorted({t[0].upper() if t[0].isalpha() else "#" for t in terms})
    glossary.append(" · ".join(f"[{c}](#{c.lower() if c != '#' else 'other'})" for c in letters))
    glossary.append("")
    for letter in letters:
        glossary.append(f"## {letter}" if letter != "#" else "## Other")
        glossary.append("")
        for name in sorted(
            (t for t in terms if (t[0].upper() if t[0].isalpha() else "#") == letter),
            key=str.lower,
        ):
            definition, link = terms[name]
            label = f"[{name}]({link})" if link else f"**{name}**"
            glossary.append(f"{label} — {definition}")
            glossary.append("")
    write("glossary.md", "\n".join(glossary))

    # --- lectures ------------------------------------------------------
    # Raw .txt files sit beside the lecture pages so mdBook copies them
    # through verbatim; a reader app can fetch one by URL.
    (SRC / "lectures" / "transcripts").mkdir(parents=True, exist_ok=True)
    for number, (slug, title) in enumerate(LECTURES, start=1):
        text = (ROOT / "lectures" / "transcripts" / f"{slug}.txt").read_text().strip()
        words = len(text.split())
        # Drop the spoken title line; the page heading carries it.
        lines = text.split("\n")
        if lines[0].startswith(f"Lecture "):
            text = "\n".join(lines[1:]).strip()
        page = [
            f"# {number}. {title}",
            "",
            f"About {round(words / 145)} minutes spoken, {words:,} words. ",
            f"Plain text for a reader app: [{slug}.txt](transcripts/{slug}.txt)",
            "",
            "---",
            "",
            text,
            "",
        ]
        write(f"lectures/{slug}.md", "\n".join(page))
        shutil.copy(
            ROOT / "lectures" / "transcripts" / f"{slug}.txt",
            SRC / "lectures" / "transcripts" / f"{slug}.txt",
        )

    shutil.copy(ROOT / "lectures" / "COURSE-PLAN.md", SRC / "lectures" / "plan.md")
    voice = (ROOT / "lectures" / "VOICE.md").read_text()
    write("lectures/voice.md", voice)

    total_words = sum(
        len((ROOT / "lectures" / "transcripts" / f"{s}.txt").read_text().split())
        for s, _ in LECTURES
    )
    lecture_index = [
        "# The lectures",
        "",
        f"Ten talks, {total_words:,} words, about {round(total_words / 145 / 60, 1)} hours.",
        "Written to be listened to, not read: no headings, no bullets, no code, no",
        "URLs spoken aloud. Each one opens by saying where it sits in the arc, and",
        "ends by stating the single claim it wants you to keep.",
        "",
        "## Listening on a phone",
        "",
        "Each lecture has a plain-text file. Paste its link into a reader app that",
        "fetches URLs, or open the lecture page and read it there.",
        "",
        "| # | Lecture | Plain text |",
        "| --- | --- | --- |",
    ]
    for number, (slug, title) in enumerate(LECTURES, start=1):
        lecture_index.append(
            f"| {number} | [{title}]({slug}.md) | [`{slug}.txt`](transcripts/{slug}.txt) |"
        )
    lecture_index += [
        "",
        "[The course plan](plan.md) gives the beats and the source notes behind each",
        "lecture. [Narration setup](voice.md) covers the voice.",
        "",
    ]
    write("lectures/index.md", "\n".join(lecture_index))

    # --- front matter --------------------------------------------------
    synthesis = (ROOT / "SYNTHESIS.md").read_text()
    write("synthesis.md", synthesis)

    write(
        "index.md",
        "\n".join(
            [
                "# Ontologies",
                "",
                "A ten-lecture audio course and a searchable knowledge base, built from",
                "the [awesome-ontology](https://github.com/ozekik/awesome-ontology) list",
                "and a research pass that filled the gaps it left.",
                "",
                "- **[The lectures](lectures/index.md)** — ten talks, about "
                f"{round(total_words / 145 / 60, 1)} hours, each with a plain-text file a reader app can fetch.",
                "- **[Synthesis](synthesis.md)** — the argument of the whole corpus in one essay.",
                f"- **[Notes](notes.md)** — {len(index)} notes on tools, languages, vocabularies, and arguments.",
                "- **[Glossary](glossary.md)** — every term in one alphabetical list.",
                "",
                "## What is here that is not in the source list",
                "",
                "The original list covers standards, tooling, reasoners, and vocabularies",
                "well. It has nothing on where the idea came from, the criticism of it, or",
                "the operational sense Palantir uses. Thirteen notes were added for that:",
                "the history from Aristotle to Wolff, Quine on ontological commitment,",
                "Gruber's definition, Cyc, the 2001 Semantic Web vision and what became of",
                "it, the knowledge graph turn, Doctorow, Shirky, Bowker and Star,",
                "Palantir's Ontology and the case against it, and the argument about",
                "whether large language models replace any of this.",
                "",
                "Search is in the top bar, or press `s`.",
                "",
                "## Source",
                "",
                "Notes, transcripts, and the generator for this site live in",
                "[matthiasdebernardini/ontology-notes](https://github.com/matthiasdebernardini/ontology-notes).",
                "Notes are CC BY 4.0, code is MIT.",
                "",
            ]
        ),
    )

    # --- SUMMARY -------------------------------------------------------
    summary = ["# Summary", "", "[Ontologies](index.md)", "", "---", "", "# Lectures", ""]
    summary.append("- [The lectures](lectures/index.md)")
    for number, (slug, title) in enumerate(LECTURES, start=1):
        summary.append(f"  - [{number}. {title}](lectures/{slug}.md)")
    summary += [
        "- [Course plan](lectures/plan.md)",
        "- [Narration setup](lectures/voice.md)",
        "",
        "---",
        "",
        "# Reference",
        "",
        "- [Synthesis](synthesis.md)",
        "- [Glossary](glossary.md)",
        "- [All notes](notes.md)",
    ]
    for section in ordered_sections:
        # Draft chapter: a heading in the sidebar with no page of its own.
        summary.append(f"  - [{section}]()")
        for entry in sections[section]:
            summary.append(f"    - [{entry['name']}](notes/{entry['slug']}.md)")
    write("SUMMARY.md", "\n".join(summary) + "\n")

    print(f"{len(index)} notes, {len(LECTURES)} lectures, {len(terms)} glossary terms")


if __name__ == "__main__":
    main()
