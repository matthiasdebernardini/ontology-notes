#!/usr/bin/env python3
"""Deterministic, dependency-free retrieval for the ontology notes knowledge base."""

from __future__ import annotations

import argparse
import configparser
import difflib
import json
import math
import os
import re
import sys
import textwrap
from collections import Counter
from pathlib import Path
from typing import Any, Iterable, Sequence

EXIT_OK = 0
EXIT_USAGE = 2
EXIT_ROOT = 3
EXIT_NOT_FOUND = 4
EXIT_DATA = 5

INDEX_FILE = "NOTE_INDEX.json"
MANIFEST_FILE = "manifest.json"
FIELD_NAMES = (
    "What it is",
    "Key concepts",
    "How you'd use it",
    "LLM angle",
    "Pitfalls & lessons",
    "Verdict",
)
FIELD_WEIGHTS = {
    "name": 7.0,
    "section": 2.5,
    "What it is": 3.2,
    "Key concepts": 2.4,
    "How you'd use it": 1.8,
    "LLM angle": 1.6,
    "Pitfalls & lessons": 1.1,
    "Verdict": 1.5,
}
# These are only used to choose useful "related" query terms. Search itself does
# not remove stop words: every query token has ordinary BM25 semantics.
RELATED_STOP_WORDS = frozenset(
    "a an and are as at be been but by can for from has have how in into is it "
    "its of on or that the their this to tool tools use used using was were which "
    "with you your".split()
)
TOKEN_RE = re.compile(r"[^\W_]+(?:['’][^\W_]+)?", re.UNICODE)
SPACE_RE = re.compile(r"\s+")
SOURCE_HEADING_RE = re.compile(r"^##\s+Sources consulted\s*$", re.I | re.M)


class CliError(Exception):
    """A user-facing error with a stable process exit code."""

    def __init__(self, message: str, code: int, *, hint: str | None = None):
        super().__init__(message)
        self.message = message
        self.code = code
        self.hint = hint


class FriendlyParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        raise CliError(message, EXIT_USAGE, hint=f"Run '{self.prog} --help' for usage.")


def tokenize(text: str) -> list[str]:
    """Return Unicode-aware, case-insensitive word tokens."""
    return [m.group(0).replace("’", "'").casefold() for m in TOKEN_RE.finditer(text)]


def _candidate_config_paths(env: dict[str, str] | None = None) -> list[Path]:
    env = os.environ if env is None else env
    candidates: list[Path] = []
    if env.get("ONTOLOGY_KB_CONFIG"):
        candidates.append(Path(env["ONTOLOGY_KB_CONFIG"]).expanduser())
    xdg = Path(env.get("XDG_CONFIG_HOME", Path(env.get("HOME", "~")).expanduser() / ".config"))
    candidates.extend(
        [
            xdg / "ontology-chat" / "config.json",
            xdg / "ontology-chat" / "config.ini",
            Path(env.get("HOME", "~")).expanduser() / ".ontology-kb.json",
        ]
    )
    # Preserve precedence while removing duplicate paths.
    return list(dict.fromkeys(path.expanduser() for path in candidates))


def _read_config_root(path: Path) -> Path:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise CliError(f"Cannot read ontology KB config '{path}': {exc}", EXIT_ROOT) from exc
    try:
        if path.suffix.casefold() == ".ini":
            parser = configparser.ConfigParser()
            parser.read_string(text)
            value = parser.get("ontology-kb", "root", fallback="") or parser.get(
                "ontology_chat", "root", fallback=""
            )
        else:
            value_obj = json.loads(text)
            if isinstance(value_obj, str):
                value = value_obj
            elif isinstance(value_obj, dict):
                value = next(
                    (value_obj[key] for key in ("root", "kb_root", "ontology_kb_root") if value_obj.get(key)),
                    "",
                )
            else:
                value = ""
    except (json.JSONDecodeError, configparser.Error) as exc:
        raise CliError(f"Invalid ontology KB config '{path}': {exc}", EXIT_ROOT) from exc
    if not isinstance(value, str) or not value.strip():
        raise CliError(
            f"Ontology KB config '{path}' does not define a non-empty 'root'.",
            EXIT_ROOT,
        )
    root = Path(os.path.expandvars(value)).expanduser()
    if not root.is_absolute():
        root = path.parent / root
    return root


def _validate_root(path: Path, source: str) -> Path:
    try:
        root = path.expanduser().resolve()
    except OSError as exc:
        raise CliError(f"Cannot resolve ontology KB root from {source}: {exc}", EXIT_ROOT) from exc
    if not root.is_dir():
        raise CliError(f"Ontology KB root from {source} is not a directory: {root}", EXIT_ROOT)
    if not (root / INDEX_FILE).is_file():
        raise CliError(
            f"Ontology KB root from {source} has no {INDEX_FILE}: {root}",
            EXIT_ROOT,
            hint="Point --root or ONTOLOGY_KB_ROOT at the ontology-notes directory.",
        )
    return root


def discover_root(
    explicit: str | Path | None = None,
    *,
    cwd: Path | None = None,
    env: dict[str, str] | None = None,
) -> tuple[Path, str]:
    """Discover the KB root in documented precedence order.

    Precedence is explicit --root, ONTOLOGY_KB_ROOT, the first existing config,
    then the current directory and each of its ancestors.
    """
    env = os.environ if env is None else env
    if explicit:
        return _validate_root(Path(explicit), "--root"), "--root"
    if env.get("ONTOLOGY_KB_ROOT"):
        return _validate_root(Path(env["ONTOLOGY_KB_ROOT"]), "ONTOLOGY_KB_ROOT"), "ONTOLOGY_KB_ROOT"
    for path in _candidate_config_paths(env):
        if path.is_file():
            return _validate_root(_read_config_root(path), f"config {path}"), f"config:{path}"
    current = (Path.cwd() if cwd is None else cwd).resolve()
    for candidate in (current, *current.parents):
        if (candidate / INDEX_FILE).is_file():
            return _validate_root(candidate, "cwd ancestor"), "cwd-ancestor"
    checked = ", ".join(str(p) for p in _candidate_config_paths(env))
    raise CliError(
        "Could not find the ontology knowledge-base root.",
        EXIT_ROOT,
        hint=(
            f"Use --root PATH, set ONTOLOGY_KB_ROOT, create a config ({checked}), "
            f"or run inside a directory containing {INDEX_FILE}."
        ),
    )


def _load_json(path: Path, label: str) -> Any:
    try:
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError as exc:
        raise CliError(f"Missing {label}: {path}", EXIT_DATA) from exc
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise CliError(f"Cannot read {label} '{path}': {exc}", EXIT_DATA) from exc


def load_index(root: Path) -> list[dict[str, Any]]:
    data = _load_json(root / INDEX_FILE, "note index")
    if not isinstance(data, list):
        raise CliError(f"{INDEX_FILE} must contain a JSON array.", EXIT_DATA)
    slugs: set[str] = set()
    for number, entry in enumerate(data, 1):
        if not isinstance(entry, dict):
            raise CliError(f"{INDEX_FILE} entry {number} is not an object.", EXIT_DATA)
        missing = [key for key in ("slug", "name", "section", "kind", "note", "fields") if key not in entry]
        if missing:
            raise CliError(f"{INDEX_FILE} entry {number} lacks: {', '.join(missing)}.", EXIT_DATA)
        if not isinstance(entry["fields"], dict) or any(field not in entry["fields"] for field in FIELD_NAMES):
            raise CliError(f"{INDEX_FILE} entry '{entry.get('slug', number)}' lacks one or more six note fields.", EXIT_DATA)
        slug = entry["slug"]
        if not isinstance(slug, str) or not slug:
            raise CliError(f"{INDEX_FILE} entry {number} has an invalid slug.", EXIT_DATA)
        if slug in slugs:
            raise CliError(f"{INDEX_FILE} contains duplicate slug '{slug}'.", EXIT_DATA)
        slugs.add(slug)
    return data


def load_manifest(root: Path) -> list[dict[str, Any]]:
    data = _load_json(root / MANIFEST_FILE, "manifest")
    if not isinstance(data, list) or any(not isinstance(entry, dict) for entry in data):
        raise CliError(f"{MANIFEST_FILE} must contain a JSON array of objects.", EXIT_DATA)
    return data


def _entry_fields(entry: dict[str, Any]) -> dict[str, str]:
    fields = {"name": str(entry["name"]), "section": str(entry["section"])}
    fields.update({name: str(entry["fields"].get(name, "")) for name in FIELD_NAMES})
    return fields


class SearchIndex:
    """In-memory BM25F-style index over the fixed NOTE_INDEX fields."""

    def __init__(self, entries: list[dict[str, Any]]):
        self.entries = entries
        self.documents: list[dict[str, list[str]]] = []
        self.term_counts: list[dict[str, Counter[str]]] = []
        total_lengths = Counter()
        document_frequency = Counter()
        for entry in entries:
            token_fields = {field: tokenize(text) for field, text in _entry_fields(entry).items()}
            self.documents.append(token_fields)
            counts = {field: Counter(tokens) for field, tokens in token_fields.items()}
            self.term_counts.append(counts)
            for field, tokens in token_fields.items():
                total_lengths[field] += len(tokens)
            document_frequency.update(set().union(*(set(tokens) for tokens in token_fields.values())))
        count = max(len(entries), 1)
        self.average_lengths = {field: total_lengths[field] / count for field in FIELD_WEIGHTS}
        self.document_frequency = document_frequency

    def idf(self, term: str) -> float:
        n = len(self.entries)
        df = self.document_frequency.get(term, 0)
        return math.log(1.0 + (n - df + 0.5) / (df + 0.5))

    def score(self, doc_number: int, query_terms: Sequence[str]) -> tuple[float, dict[str, float]]:
        """Return a deterministic weighted sum of per-field BM25 scores."""
        k1 = 1.2
        b = 0.75
        unique_terms = list(dict.fromkeys(query_terms))
        contributions: dict[str, float] = {}
        for field, weight in FIELD_WEIGHTS.items():
            tokens = self.documents[doc_number][field]
            counts = self.term_counts[doc_number][field]
            avg_length = self.average_lengths[field] or 1.0
            normalization = k1 * (1.0 - b + b * len(tokens) / avg_length)
            subtotal = 0.0
            for term in unique_terms:
                tf = counts.get(term, 0)
                if tf:
                    subtotal += self.idf(term) * (tf * (k1 + 1.0)) / (tf + normalization)
            if subtotal:
                contributions[field] = weight * subtotal
        return sum(contributions.values()), contributions

    def search(
        self,
        query: str,
        *,
        limit: int = 10,
        section: str | None = None,
        kind: str | None = None,
        exclude_slug: str | None = None,
    ) -> list[dict[str, Any]]:
        terms = tokenize(query)
        if not terms:
            raise CliError("Search query must contain at least one word or number.", EXIT_USAGE)
        results: list[dict[str, Any]] = []
        section_key = section.casefold() if section else None
        kind_key = kind.casefold() if kind else None
        for number, entry in enumerate(self.entries):
            if entry["slug"] == exclude_slug:
                continue
            if section_key and str(entry["section"]).casefold() != section_key:
                continue
            if kind_key and str(entry["kind"]).casefold() != kind_key:
                continue
            score, contributions = self.score(number, terms)
            if score <= 0.0:
                continue
            matched_fields = sorted(contributions, key=lambda name: (-contributions[name], list(FIELD_WEIGHTS).index(name)))
            snippet_field = _choose_snippet_field(contributions)
            snippet = make_snippet(_entry_fields(entry)[snippet_field], terms)
            results.append(
                {
                    "slug": entry["slug"],
                    "name": entry["name"],
                    "section": entry["section"],
                    "kind": entry["kind"],
                    "note": entry["note"],
                    "score": round(score, 6),
                    "matched_fields": matched_fields,
                    "snippet_field": snippet_field,
                    "snippet": snippet,
                }
            )
        results.sort(key=lambda item: (-item["score"], item["slug"]))
        for rank, result in enumerate(results[:limit], 1):
            result["rank"] = rank
        return results[:limit]


def _choose_snippet_field(contributions: dict[str, float]) -> str:
    # Name/section are excellent ranking signals but rarely useful prose snippets.
    prose = [(score, field) for field, score in contributions.items() if field in FIELD_NAMES]
    if prose:
        return max(prose, key=lambda pair: (pair[0], -FIELD_NAMES.index(pair[1])))[1]
    return max(contributions, key=contributions.get)


def make_snippet(text: str, query_terms: Sequence[str], width: int = 240) -> str:
    clean = SPACE_RE.sub(" ", text).strip()
    if len(clean) <= width:
        return clean
    folded = clean.casefold()
    positions = [folded.find(term.casefold()) for term in query_terms]
    positions = [position for position in positions if position >= 0]
    center = min(positions) if positions else 0
    start = max(0, center - width // 3)
    end = min(len(clean), start + width)
    if start:
        boundary = clean.find(" ", start)
        start = boundary + 1 if boundary >= 0 and boundary < end else start
    if end < len(clean):
        boundary = clean.rfind(" ", start, end)
        end = boundary if boundary > start else end
    return ("…" if start else "") + clean[start:end].strip() + ("…" if end < len(clean) else "")


def resolve_entry(entries: list[dict[str, Any]], identifier: str) -> dict[str, Any]:
    key = identifier.strip().casefold()
    by_slug = [entry for entry in entries if entry["slug"].casefold() == key]
    if by_slug:
        return by_slug[0]
    by_name = [entry for entry in entries if str(entry["name"]).casefold() == key]
    if len(by_name) == 1:
        return by_name[0]
    slugified = re.sub(r"[^a-z0-9]+", "-", key).strip("-")
    by_slugified = [entry for entry in entries if entry["slug"].casefold() == slugified]
    if len(by_slugified) == 1:
        return by_slugified[0]
    choices = {entry["slug"]: entry["name"] for entry in entries}
    suggestions = difflib.get_close_matches(slugified, choices, n=5, cutoff=0.45)
    suggestion_text = ", ".join(f"{slug} ({choices[slug]})" for slug in suggestions)
    raise CliError(
        f"No note matches '{identifier}'.",
        EXIT_NOT_FOUND,
        hint=f"Closest slugs: {suggestion_text}" if suggestion_text else "Run search with words from the note name.",
    )


def _manifest_for(manifest: list[dict[str, Any]], slug: str) -> dict[str, Any] | None:
    return next((entry for entry in manifest if entry.get("slug") == slug), None)


def resolve_manifest_entry(manifest: list[dict[str, Any]], identifier: str) -> dict[str, Any]:
    """Resolve noted or skipped manifest entries for provenance inspection."""
    key = identifier.strip().casefold()
    slugified = re.sub(r"[^a-z0-9]+", "-", key).strip("-")
    matches = [entry for entry in manifest if str(entry.get("slug", "")).casefold() in {key, slugified}]
    if not matches:
        matches = [entry for entry in manifest if str(entry.get("name", "")).casefold() == key]
    if len(matches) == 1:
        metadata = matches[0]
        slug = str(metadata["slug"])
        return {
            "slug": slug,
            "name": metadata.get("name", slug),
            "section": metadata.get("section", ""),
            "kind": metadata.get("kind", ""),
            "note": f"notes/{slug}.md",
        }
    if len(matches) > 1:
        choices = ", ".join(str(entry.get("slug")) for entry in matches)
        raise CliError(f"Manifest entry '{identifier}' is ambiguous.", EXIT_NOT_FOUND, hint=f"Use one of: {choices}")
    choices = {str(entry.get("slug")): str(entry.get("name")) for entry in manifest}
    suggestions = difflib.get_close_matches(slugified, choices, n=5, cutoff=0.45)
    suggestion_text = ", ".join(f"{slug} ({choices[slug]})" for slug in suggestions)
    raise CliError(
        f"No manifest entry matches '{identifier}'.",
        EXIT_NOT_FOUND,
        hint=f"Closest slugs: {suggestion_text}" if suggestion_text else "Run status or inspect manifest.json.",
    )


def _consulted_sources(root: Path, entry: dict[str, Any]) -> list[str]:
    note_path = root / entry["note"]
    try:
        text = note_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return []
    match = SOURCE_HEADING_RE.search(text)
    if not match:
        return []
    sources: list[str] = []
    for line in text[match.end() :].splitlines():
        if line.startswith("## "):
            break
        item = re.match(r"\s*-\s+`?(.+?)`?\s*$", line)
        if item:
            sources.append(item.group(1))
    return sources


def show_payload(root: Path, entry: dict[str, Any], manifest: list[dict[str, Any]]) -> dict[str, Any]:
    metadata = _manifest_for(manifest, entry["slug"])
    return {
        "slug": entry["slug"],
        "name": entry["name"],
        "section": entry["section"],
        "kind": entry["kind"],
        "note": entry["note"],
        "fields": {field: entry["fields"][field] for field in FIELD_NAMES},
        "source_url": metadata.get("url") if metadata else None,
        "sources_consulted": _consulted_sources(root, entry),
    }


def related_terms(search_index: SearchIndex, doc_number: int, limit: int = 18) -> list[str]:
    weighted = Counter()
    for field, weight in FIELD_WEIGHTS.items():
        for term, frequency in search_index.term_counts[doc_number][field].items():
            if len(term) < 3 or term in RELATED_STOP_WORDS:
                continue
            weighted[term] += weight * min(frequency, 3) * search_index.idf(term)
    return [term for term, _ in sorted(weighted.items(), key=lambda pair: (-pair[1], pair[0]))[:limit]]


def related_payload(
    search_index: SearchIndex,
    entry: dict[str, Any],
    *,
    limit: int,
) -> tuple[list[str], list[dict[str, Any]]]:
    doc_number = next(number for number, item in enumerate(search_index.entries) if item["slug"] == entry["slug"])
    terms = related_terms(search_index, doc_number)
    results = search_index.search(" ".join(terms), limit=max(limit * 4, limit), exclude_slug=entry["slug"])
    for result in results:
        other_number = next(number for number, item in enumerate(search_index.entries) if item["slug"] == result["slug"])
        shared = [term for term in terms if any(term in field for field in search_index.documents[other_number].values())]
        result["shared_terms"] = shared[:8]
        if result["section"] == entry["section"]:
            result["score"] = round(result["score"] * 1.08, 6)
    results.sort(key=lambda item: (-item["score"], item["slug"]))
    results = results[:limit]
    for rank, result in enumerate(results, 1):
        result["rank"] = rank
    return terms, results


def sources_payload(root: Path, entry: dict[str, Any], manifest: list[dict[str, Any]]) -> dict[str, Any]:
    metadata = _manifest_for(manifest, entry["slug"])
    source_file = metadata.get("source_file") if metadata else None
    repo_path = f"repos/{entry['slug']}"
    local: list[dict[str, Any]] = [
        {"type": "note", "path": entry["note"], "exists": (root / entry["note"]).is_file()}
    ]
    if source_file:
        local.append({"type": "captured-source", "path": source_file, "exists": (root / source_file).is_file()})
    if (root / repo_path).is_dir() or entry["kind"] == "github-repo":
        local.append({"type": "repository", "path": repo_path, "exists": (root / repo_path).is_dir()})
    fetch_keys = ("http_status", "final_url", "fetch_method", "source_chars", "repo_size_mb", "default_branch", "archived")
    return {
        "slug": entry["slug"],
        "name": entry["name"],
        "kind": entry["kind"],
        "url": metadata.get("url") if metadata else None,
        "status": metadata.get("status") if metadata else None,
        "skip_reason": metadata.get("skip_reason") if metadata else None,
        "sources_consulted": _consulted_sources(root, entry),
        "local": local,
        "fetch": {key: metadata[key] for key in fetch_keys if metadata and key in metadata},
    }


def status_payload(root: Path, root_source: str, entries: list[dict[str, Any]], manifest: list[dict[str, Any]]) -> dict[str, Any]:
    status_counts = Counter(str(item.get("status", "unknown")) for item in manifest)
    kind_counts = Counter(str(item.get("kind", "unknown")) for item in entries)
    section_counts = Counter(str(item.get("section", "unknown")) for item in entries)
    missing_notes = sorted(entry["note"] for entry in entries if not (root / entry["note"]).is_file())
    noted_slugs = {item.get("slug") for item in manifest if item.get("status") == "noted"}
    indexed_slugs = {entry["slug"] for entry in entries}
    source_files = [item.get("source_file") for item in manifest if item.get("source_file")]
    missing_sources = sorted(path for path in source_files if not (root / path).is_file())
    present_sources = len(source_files) - len(missing_sources)
    return {
        # Raw captures are optional provenance artifacts and are deliberately
        # excluded from the public repository. Notes/index reconciliation is
        # the distributable health boundary; missing captures remain visible.
        "ok": not missing_notes and indexed_slugs == noted_slugs,
        "root": str(root),
        "root_source": root_source,
        "index_file": INDEX_FILE,
        "indexed_notes": len(entries),
        "manifest_entries": len(manifest),
        "manifest_status": dict(sorted(status_counts.items())),
        "sections": dict(sorted(section_counts.items())),
        "kinds": dict(sorted(kind_counts.items())),
        "source_files": len(source_files),
        "source_files_present": present_sources,
        "missing_notes": missing_notes,
        "missing_source_count": len(missing_sources),
        "missing_sources": missing_sources[:10],
        "missing_sources_truncated": len(missing_sources) > 10,
        "unindexed_noted_slugs": sorted(noted_slugs - indexed_slugs),
        "unmanifested_index_slugs": sorted(indexed_slugs - noted_slugs),
    }


def _human_search(payload: dict[str, Any]) -> str:
    lines = [f"Search: {payload['query']!r} — {payload['count']} result(s)"]
    if payload.get("filters"):
        lines.append("Filters: " + ", ".join(f"{key}={value}" for key, value in payload["filters"].items()))
    for item in payload["results"]:
        lines.extend(
            [
                "",
                f"{item['rank']}. {item['name']} [{item['slug']}]  score={item['score']:.6f}",
                f"   {item['section']} · {item['kind']} · {item['note']}",
                f"   {item['snippet_field']}: {item['snippet']}",
            ]
        )
    if not payload["results"]:
        lines.append("No matching notes. Try fewer or broader terms.")
    return "\n".join(lines)


def _human_show(payload: dict[str, Any]) -> str:
    lines = [f"# {payload['name']}", "", f"Slug: {payload['slug']}  |  Section: {payload['section']}  |  Kind: {payload['kind']}"]
    if payload["source_url"]:
        lines.append(f"Source: {payload['source_url']}")
    for field in FIELD_NAMES:
        lines.extend(["", f"## {field}", payload["fields"][field]])
    if payload["sources_consulted"]:
        lines.extend(["", "## Sources consulted", *(f"- {item}" for item in payload["sources_consulted"])])
    return "\n".join(lines)


def _human_related(payload: dict[str, Any]) -> str:
    lines = [f"Related to {payload['name']} [{payload['slug']}] — {payload['count']} result(s)"]
    for item in payload["results"]:
        reason = ", ".join(item["shared_terms"]) or "weighted note similarity"
        lines.extend(
            [
                "",
                f"{item['rank']}. {item['name']} [{item['slug']}]  score={item['score']:.6f}",
                f"   {item['section']} · {item['kind']}",
                f"   Shared terms: {reason}",
                f"   {item['snippet']}",
            ]
        )
    return "\n".join(lines)


def _human_sources(payload: dict[str, Any]) -> str:
    lines = [f"Sources for {payload['name']} [{payload['slug']}]", f"Canonical URL: {payload['url'] or '(not recorded)'}"]
    lines.append(f"Manifest status: {payload['status'] or '(not recorded)'}")
    if payload.get("skip_reason"):
        lines.append(f"Skip reason: {payload['skip_reason']}")
    if payload["sources_consulted"]:
        lines.extend(["", "Consulted:", *(f"- {item}" for item in payload["sources_consulted"])])
    lines.extend(["", "Local material:"])
    lines.extend(f"- {item['type']}: {item['path']} ({'present' if item['exists'] else 'missing'})" for item in payload["local"])
    if payload["fetch"]:
        lines.extend(["", "Fetch metadata:", *(f"- {key}: {value}" for key, value in payload["fetch"].items())])
    return "\n".join(lines)


def _human_status(payload: dict[str, Any]) -> str:
    state = "healthy" if payload["ok"] else "incomplete"
    lines = [
        f"Ontology KB: {state}",
        f"Root: {payload['root']} ({payload['root_source']})",
        f"Indexed notes: {payload['indexed_notes']}",
        f"Manifest entries: {payload['manifest_entries']} ({', '.join(f'{k}={v}' for k, v in payload['manifest_status'].items())})",
        f"Sections: {len(payload['sections'])}",
        f"Captured source files present: {payload['source_files_present']}/{payload['source_files']} (optional in public installs)",
    ]
    for key, label in (
        ("missing_notes", "Missing notes"),
        ("missing_sources", "Missing captured sources"),
        ("unindexed_noted_slugs", "Noted but unindexed"),
        ("unmanifested_index_slugs", "Indexed but not noted in manifest"),
    ):
        if payload[key]:
            lines.append(f"{label}: {', '.join(payload[key])}")
    return "\n".join(lines)


def build_parser() -> FriendlyParser:
    parser = FriendlyParser(
        prog="ontology_kb.py",
        description="Search and inspect the local ontology-notes knowledge base (no network or embeddings).",
    )
    parser.add_argument("--root", metavar="PATH", help="knowledge-base root (overrides environment and config)")
    parser.add_argument("--json", action="store_true", help="emit stable JSON instead of human-readable text")
    subparsers = parser.add_subparsers(dest="command", required=True)

    search = subparsers.add_parser("search", help="rank notes with deterministic weighted BM25")
    search.add_argument("query", nargs="+", metavar="QUERY", help="one or more search words")
    search.add_argument("-n", "--limit", type=_positive_int, default=10, help="maximum results (default: 10)")
    search.add_argument("--section", help="only this exact section (case-insensitive)")
    search.add_argument("--kind", help="only this exact manifest kind (case-insensitive)")

    show = subparsers.add_parser("show", help="show all six fields for one note")
    show.add_argument("identifier", metavar="SLUG_OR_NAME")

    related = subparsers.add_parser("related", help="find notes related to one note")
    related.add_argument("identifier", metavar="SLUG_OR_NAME")
    related.add_argument("-n", "--limit", type=_positive_int, default=8, help="maximum results (default: 8)")

    sources = subparsers.add_parser("sources", help="show provenance and local source material for one note")
    sources.add_argument("identifier", metavar="SLUG_OR_NAME")

    subparsers.add_parser("status", help="validate and summarize KB coverage")
    return parser


def _positive_int(value: str) -> int:
    try:
        integer = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("must be an integer") from exc
    if integer < 1 or integer > 100:
        raise argparse.ArgumentTypeError("must be between 1 and 100")
    return integer


def _normalize_global_options(argv: Sequence[str]) -> list[str]:
    """Make --json and --root work before or after a subcommand."""
    args = list(argv)
    globals_: list[str] = []
    rest: list[str] = []
    index = 0
    while index < len(args):
        arg = args[index]
        if arg == "--json":
            globals_.append(arg)
        elif arg == "--root":
            if index + 1 >= len(args):
                rest.append(arg)  # argparse will provide the standard missing-value error
            else:
                globals_.extend((arg, args[index + 1]))
                index += 1
        elif arg.startswith("--root="):
            globals_.append(arg)
        else:
            rest.append(arg)
        index += 1
    return globals_ + rest


def execute(args: argparse.Namespace) -> tuple[dict[str, Any], str]:
    root, root_source = discover_root(args.root)
    entries = load_index(root)
    manifest = load_manifest(root)
    if args.command == "status":
        payload = status_payload(root, root_source, entries, manifest)
        return payload, _human_status(payload)
    if args.command == "show":
        entry = resolve_entry(entries, args.identifier)
        payload = show_payload(root, entry, manifest)
        return payload, _human_show(payload)
    if args.command == "sources":
        entry = resolve_manifest_entry(manifest, args.identifier)
        payload = sources_payload(root, entry, manifest)
        return payload, _human_sources(payload)
    search_index = SearchIndex(entries)
    if args.command == "search":
        query = " ".join(args.query)
        results = search_index.search(query, limit=args.limit, section=args.section, kind=args.kind)
        filters = {key: value for key, value in (("section", args.section), ("kind", args.kind)) if value}
        payload = {"query": query, "count": len(results), "limit": args.limit, "filters": filters, "results": results}
        return payload, _human_search(payload)
    if args.command == "related":
        entry = resolve_entry(entries, args.identifier)
        terms, results = related_payload(search_index, entry, limit=args.limit)
        payload = {
            "slug": entry["slug"],
            "name": entry["name"],
            "query_terms": terms,
            "count": len(results),
            "limit": args.limit,
            "results": results,
        }
        return payload, _human_related(payload)
    raise CliError(f"Unsupported command '{args.command}'.", EXIT_USAGE)


def _emit_error(error: CliError, json_mode: bool) -> None:
    if json_mode:
        json.dump(
            {"ok": False, "error": error.message, "exit_code": error.code, "hint": error.hint},
            sys.stderr,
            ensure_ascii=False,
            sort_keys=True,
        )
        sys.stderr.write("\n")
    else:
        print(f"error: {error.message}", file=sys.stderr)
        if error.hint:
            print(f"hint: {error.hint}", file=sys.stderr)


def main(argv: Sequence[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else list(argv)
    json_mode = "--json" in argv
    parser = build_parser()
    try:
        args = parser.parse_args(_normalize_global_options(argv))
        payload, human = execute(args)
        if args.json:
            json.dump(payload, sys.stdout, ensure_ascii=False, indent=2, sort_keys=True)
            sys.stdout.write("\n")
        else:
            print(human)
        return EXIT_OK
    except CliError as error:
        _emit_error(error, json_mode)
        return error.code
    except BrokenPipeError:
        sys.stdout.close()
        return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
