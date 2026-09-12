import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_DOCS = (
    "SPEC.md",
    "ARCHITECTURE.md",
    "DEVELOPMENT_PROTOCOL.md",
    "PACKAGING_SCHEMA.md",
    "PROCESS_RULES.md",
    "ADOBE_AUTOMATION.md",
    "QA_STANDARD.md",
    "STAGE_GATES.md",
    "TEST_PLAN.md",
    "RECOVERY.md",
)
FORBIDDEN_RUNTIME_DIRS = ("src", "worker", "adobe-bridge", "scene_graph")
SECRET_PATTERNS = (
    re.compile(r"sk-[A-Za-z0-9]{16,}"),
    re.compile(r"(?i)bearer[ \t]+[A-Za-z0-9._-]{20,}"),
    re.compile(r"(?i)(?:api[_ -]?key|token|password)[ \t]*[:=][ \t]*[A-Za-z0-9+/=_-]{20,}"),
)
IGNORED_GENERATED_PARTS = {".git", "__pycache__", ".pytest_cache", ".venv", "venv", "build", "dist"}


class P0BaselineTests(unittest.TestCase):
    def test_required_documents_exist(self):
        for name in REQUIRED_DOCS:
            path = ROOT / "docs" / name
            with self.subTest(name=name):
                self.assertTrue(path.is_file(), f"missing required document: {path}")
                self.assertGreater(path.stat().st_size, 200)

    def test_no_post_p0_runtime_directories_exist(self):
        for name in FORBIDDEN_RUNTIME_DIRS:
            with self.subTest(name=name):
                self.assertFalse((ROOT / name).exists(), f"P1+ runtime path exists: {name}")

    def test_secret_patterns_are_absent_from_candidate_files(self):
        candidates = [
            path
            for path in ROOT.rglob("*")
            if path.is_file()
            and not any(part in IGNORED_GENERATED_PARTS for part in path.parts)
            and path.name != ".env"
            and path.suffix not in {".pyc", ".db", ".sqlite", ".sqlite3"}
        ]
        for path in candidates:
            text = path.read_text(encoding="utf-8")
            for pattern in SECRET_PATTERNS:
                with self.subTest(path=path.relative_to(ROOT), pattern=pattern.pattern):
                    self.assertIsNone(pattern.search(text), f"possible secret in {path}")

    def test_stage_gate_covers_all_stages(self):
        text = (ROOT / "docs" / "STAGE_GATES.md").read_text(encoding="utf-8")
        for marker in ("P0", "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10", "RC", "V1"):
            with self.subTest(marker=marker):
                self.assertIn(marker, text)

    def test_p0_boundary_is_explicit(self):
        spec = (ROOT / "docs" / "SPEC.md").read_text(encoding="utf-8")
        gates = (ROOT / "docs" / "STAGE_GATES.md").read_text(encoding="utf-8")
        self.assertIn("P0 不包含", spec)
        self.assertIn("P0 = BLOCKED", (ROOT / "README.md").read_text(encoding="utf-8"))
        self.assertIn("连续 3 次最小请求", gates)
        self.assertIn("deepseek-v4.1-flash", spec)
        self.assertIn("deepseek-v4-flash", spec)


if __name__ == "__main__":
    unittest.main()
