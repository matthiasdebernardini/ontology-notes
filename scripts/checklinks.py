#!/usr/bin/env python3
"""Check every local link in a directory of built HTML. mdBook does not do this.

    python3 scripts/checklinks.py site/book

Checks `href` and `src`, relative and root-relative, URL-encoded or not, including
links to non-HTML files such as the raw `.txt` transcripts. `#fragment` targets are
checked against the anchors of the destination page. External `http(s)` links,
`mailto:`, `data:` and `javascript:` are skipped. Prints every broken link with the
file it came from and exits nonzero if there are any.
"""
from __future__ import annotations

import html.parser
import pathlib
import sys
import urllib.parse

SKIP_SCHEMES = ("http:", "https:", "mailto:", "data:", "javascript:", "tel:", "//")


class Page(html.parser.HTMLParser):
    """Collect outbound links and the anchors this page offers."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[str] = []
        self.anchors: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = {k: (v or "") for k, v in attrs}
        for key in ("href", "src"):
            if key in a:
                self.links.append(a[key])
        for key in ("id", "name"):
            if a.get(key):
                self.anchors.add(a[key])


def parse(path: pathlib.Path) -> Page:
    page = Page()
    page.feed(path.read_text(encoding="utf-8", errors="replace"))
    return page


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(f"usage: {argv[0]} DIRECTORY", file=sys.stderr)
        return 2
    root = pathlib.Path(argv[1]).resolve()
    if not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        return 2

    pages = sorted(root.rglob("*.html"))
    if not pages:
        print(f"no HTML found under {root}", file=sys.stderr)
        return 2

    parsed = {p: parse(p) for p in pages}
    broken: list[str] = []
    checked = 0

    for source, page in parsed.items():
        for raw in page.links:
            link = raw.strip()
            if not link or link.startswith(SKIP_SCHEMES):
                continue
            path_part, _, fragment = link.partition("#")
            path_part = urllib.parse.unquote(path_part.partition("?")[0])
            fragment = urllib.parse.unquote(fragment)

            if not path_part:
                target = source  # same-page fragment
            elif path_part.startswith("/"):
                target = root / path_part.lstrip("/")
            else:
                target = (source.parent / path_part).resolve()

            if target.is_dir():
                target = target / "index.html"

            checked += 1
            if not target.is_file():
                broken.append(f"{source.relative_to(root)}: missing target {raw}")
                continue
            if fragment and target.suffix in (".html", ".htm"):
                anchors = parsed.get(target)
                if anchors is None:
                    anchors = parse(target)
                    parsed[target] = anchors
                if fragment not in anchors.anchors:
                    broken.append(f"{source.relative_to(root)}: missing anchor {raw}")

    for line in broken:
        print(line)
    print(
        f"{len(pages)} pages, {checked} local links checked, {len(broken)} broken",
        file=sys.stderr,
    )
    return 1 if broken else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
