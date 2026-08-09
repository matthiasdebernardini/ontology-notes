"""Focused tests for the dependency-free ontology knowledge-base CLI.

These tests exercise the distributable NOTE_INDEX, notes, and manifest. Raw web
captures and cloned upstream repositories are optional local provenance artifacts.
"""

from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "ontology-chat" / "scripts" / "ontology_kb.py"
SPEC = importlib.util.spec_from_file_location("ontology_kb", SCRIPT)
assert SPEC and SPEC.loader
kb = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(kb)


class ActualKnowledgeBaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.entries = kb.load_index(ROOT)
        cls.manifest = kb.load_manifest(ROOT)
        cls.search_index = kb.SearchIndex(cls.entries)

    def test_actual_index_has_fixed_six_field_schema(self) -> None:
        self.assertEqual(181, len(self.entries))
        for entry in self.entries:
            self.assertEqual(set(kb.FIELD_NAMES), set(entry["fields"]))

    def test_search_title_weight_puts_exact_tool_first(self) -> None:
        results = self.search_index.search("Protégé", limit=5)
        self.assertEqual("protege", results[0]["slug"])
        self.assertIn("name", results[0]["matched_fields"])

    def test_search_is_deterministic(self) -> None:
        first = self.search_index.search("SHACL validation", limit=10)
        second = kb.SearchIndex(self.entries).search("SHACL validation", limit=10)
        self.assertEqual(first, second)
        self.assertEqual("shacl-shapes-constraint-language", first[0]["slug"])

    def test_search_filters_section_and_kind_case_insensitively(self) -> None:
        results = self.search_index.search(
            "editor ontology", limit=100, section="ontology editors", kind="SITE"
        )
        self.assertTrue(results)
        self.assertTrue(all(item["section"] == "Ontology Editors" for item in results))
        self.assertTrue(all(item["kind"] == "site" for item in results))

    def test_search_snippet_contains_query_context(self) -> None:
        result = self.search_index.search("SHACL validation", limit=1)[0]
        snippet = result["snippet"].casefold()
        self.assertTrue("shacl" in snippet or "validation" in snippet)
        self.assertLessEqual(len(result["snippet"]), 242)

    def test_no_match_is_an_empty_successful_result(self) -> None:
        self.assertEqual([], self.search_index.search("zzzzunfindablezzzz", limit=5))

    def test_empty_punctuation_query_is_usage_error(self) -> None:
        with self.assertRaises(kb.CliError) as raised:
            self.search_index.search("---", limit=5)
        self.assertEqual(kb.EXIT_USAGE, raised.exception.code)

    def test_show_resolves_slug_name_and_slugified_name(self) -> None:
        expected = kb.resolve_entry(self.entries, "protege")
        self.assertEqual(expected, kb.resolve_entry(self.entries, "Protégé"))
        self.assertEqual(
            "owl-2-web-ontology-language",
            kb.resolve_entry(self.entries, "OWL 2 Web Ontology Language")["slug"],
        )

    def test_unknown_note_has_suggestions_and_not_found_code(self) -> None:
        with self.assertRaises(kb.CliError) as raised:
            kb.resolve_entry(self.entries, "protegee")
        self.assertEqual(kb.EXIT_NOT_FOUND, raised.exception.code)
        self.assertIn("protege", raised.exception.hint or "")

    def test_related_excludes_origin_and_is_deterministic(self) -> None:
        entry = kb.resolve_entry(self.entries, "protege")
        terms_a, results_a = kb.related_payload(self.search_index, entry, limit=5)
        terms_b, results_b = kb.related_payload(self.search_index, entry, limit=5)
        self.assertEqual(terms_a, terms_b)
        self.assertEqual(results_a, results_b)
        self.assertNotIn("protege", {item["slug"] for item in results_a})
        self.assertTrue(all(item["shared_terms"] for item in results_a))

    def test_sources_describe_optional_web_capture_and_github_checkout(self) -> None:
        web = kb.sources_payload(
            ROOT, kb.resolve_entry(self.entries, "ontology-matching"), self.manifest
        )
        self.assertTrue(any(item["type"] == "note" and item["exists"] for item in web["local"]))
        self.assertTrue(any(item["type"] == "captured-source" for item in web["local"]))
        repo = kb.sources_payload(ROOT, kb.resolve_entry(self.entries, "eddy"), self.manifest)
        self.assertEqual("https://github.com/obdasystems/eddy", repo["url"])
        self.assertTrue(any(item["type"] == "repository" for item in repo["local"]))
        self.assertIn("README.md", repo["sources_consulted"])

    def test_sources_resolves_skipped_manifest_entry(self) -> None:
        entry = kb.resolve_manifest_entry(self.manifest, "WordNet")
        payload = kb.sources_payload(ROOT, entry, self.manifest)
        self.assertEqual("wordnet", payload["slug"])
        self.assertEqual("skipped", payload["status"])
        self.assertIn("Cloudflare", payload["skip_reason"])
        self.assertFalse(next(item for item in payload["local"] if item["type"] == "note")["exists"])

    def test_actual_status_is_healthy_and_reconciled(self) -> None:
        payload = kb.status_payload(ROOT, "test", self.entries, self.manifest)
        self.assertTrue(payload["ok"])
        self.assertEqual(181, payload["indexed_notes"])
        self.assertEqual({"noted": 181, "skipped": 20}, payload["manifest_status"])
        self.assertEqual([], payload["missing_notes"])
        self.assertEqual([], payload["unindexed_noted_slugs"])


class RootDiscoveryTests(unittest.TestCase):
    def test_explicit_root_has_precedence_over_bad_environment(self) -> None:
        root, source = kb.discover_root(ROOT, env={"ONTOLOGY_KB_ROOT": "/definitely/missing"})
        self.assertEqual(ROOT.resolve(), root)
        self.assertEqual("--root", source)

    def test_environment_root_has_precedence_over_config(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            temp_path = Path(temp)
            config = temp_path / "ontology-chat" / "config.json"
            config.parent.mkdir()
            config.write_text(json.dumps({"root": "/definitely/missing"}))
            root, source = kb.discover_root(
                env={
                    "ONTOLOGY_KB_ROOT": str(ROOT),
                    "XDG_CONFIG_HOME": str(temp_path),
                    "HOME": temp,
                }
            )
        self.assertEqual(ROOT.resolve(), root)
        self.assertEqual("ONTOLOGY_KB_ROOT", source)

    def test_json_config_is_used_before_cwd(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            temp_path = Path(temp)
            xdg = temp_path / "config"
            config = xdg / "ontology-chat" / "config.json"
            config.parent.mkdir(parents=True)
            config.write_text(json.dumps({"root": str(ROOT)}))
            cwd = temp_path / "elsewhere"
            cwd.mkdir()
            root, source = kb.discover_root(
                cwd=cwd,
                env={"XDG_CONFIG_HOME": str(xdg), "HOME": temp},
            )
        self.assertEqual(ROOT.resolve(), root)
        self.assertTrue(source.startswith("config:"))

    def test_cwd_ancestor_discovery(self) -> None:
        root, source = kb.discover_root(
            cwd=ROOT / "notes", env={"HOME": "/definitely/missing", "XDG_CONFIG_HOME": "/also/missing"}
        )
        self.assertEqual(ROOT.resolve(), root)
        self.assertEqual("cwd-ancestor", source)

    def test_invalid_explicit_root_does_not_fall_back(self) -> None:
        with self.assertRaises(kb.CliError) as raised:
            kb.discover_root("/definitely/missing", cwd=ROOT)
        self.assertEqual(kb.EXIT_ROOT, raised.exception.code)


class CommandLineContractTests(unittest.TestCase):
    def run_cli(self, *arguments: str, cwd: Path = ROOT, env: dict[str, str] | None = None):
        process_env = os.environ.copy()
        if env:
            process_env.update(env)
        return subprocess.run(
            [sys.executable, str(SCRIPT), *arguments],
            cwd=cwd,
            env=process_env,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_global_json_works_before_subcommand(self) -> None:
        completed = self.run_cli("--json", "search", "ELK", "reasoner", "--limit", "1")
        self.assertEqual(0, completed.returncode, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertEqual("elk", payload["results"][0]["slug"])
        self.assertEqual(1, payload["limit"])

    def test_global_json_and_root_work_after_subcommand(self) -> None:
        completed = self.run_cli("show", "--json", "--root", str(ROOT), "protege")
        self.assertEqual(0, completed.returncode, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertEqual("protege", payload["slug"])
        self.assertEqual(set(kb.FIELD_NAMES), set(payload["fields"]))

    def test_status_human_output_is_compact_and_clear(self) -> None:
        completed = self.run_cli("status")
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertIn("Ontology KB: healthy", completed.stdout)
        self.assertIn("Indexed notes: 181", completed.stdout)

    def test_sources_command_reports_skipped_entry(self) -> None:
        completed = self.run_cli("sources", "--json", "wordnet")
        self.assertEqual(0, completed.returncode, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertEqual("skipped", payload["status"])
        self.assertIn("Cloudflare", payload["skip_reason"])

    def test_unknown_note_returns_json_error_and_exit_four(self) -> None:
        completed = self.run_cli("--json", "show", "does-not-exist")
        self.assertEqual(kb.EXIT_NOT_FOUND, completed.returncode)
        payload = json.loads(completed.stderr)
        self.assertFalse(payload["ok"])
        self.assertEqual(kb.EXIT_NOT_FOUND, payload["exit_code"])
        self.assertIn("No note matches", payload["error"])

    def test_bad_limit_is_usage_exit_two(self) -> None:
        completed = self.run_cli("search", "owl", "--limit", "0")
        self.assertEqual(kb.EXIT_USAGE, completed.returncode)
        self.assertIn("between 1 and 100", completed.stderr)

    def test_missing_root_has_actionable_exit_three(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            empty = Path(temp)
            completed = self.run_cli(
                "status",
                cwd=empty,
                env={
                    "HOME": temp,
                    "XDG_CONFIG_HOME": str(empty / "config"),
                    "ONTOLOGY_KB_ROOT": "",
                    "ONTOLOGY_KB_CONFIG": "",
                },
            )
        self.assertEqual(kb.EXIT_ROOT, completed.returncode)
        self.assertIn("Use --root PATH", completed.stderr)


if __name__ == "__main__":
    unittest.main()
