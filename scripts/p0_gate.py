#!/usr/bin/env python3
"""只读 P0 本地门禁；不访问网络、不读取 Secret、不修改文件。"""

from __future__ import annotations

import json
import re
import subprocess
import sys
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
SECRET_PATTERNS = (
    re.compile(r"sk-[A-Za-z0-9]{16,}"),
    re.compile(r"(?i)bearer[ \t]+[A-Za-z0-9._-]{20,}"),
    re.compile(r"(?i)(?:api[_ -]?key|token|password)[ \t]*[:=][ \t]*[A-Za-z0-9+/=_-]{20,}"),
)
IGNORED_GENERATED_PARTS = {".git", "__pycache__", ".pytest_cache", ".venv", "venv", "build", "dist"}


def check_required_docs() -> tuple[bool, list[str]]:
    missing = [name for name in REQUIRED_DOCS if not (ROOT / "docs" / name).is_file()]
    return not missing, missing


def check_forbidden_paths() -> tuple[bool, list[str]]:
    forbidden = [name for name in ("src", "worker", "adobe-bridge", "scene_graph") if (ROOT / name).exists()]
    return not forbidden, forbidden


def candidate_files():
    return (
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and not any(part in IGNORED_GENERATED_PARTS for part in path.parts)
        and path.name != ".env"
        and path.suffix not in {".pyc", ".db", ".sqlite", ".sqlite3"}
    )


def check_secrets() -> tuple[bool, list[str]]:
    hits: list[str] = []
    for path in candidate_files():
        text = path.read_text(encoding="utf-8")
        if any(pattern.search(text) for pattern in SECRET_PATTERNS):
            hits.append(str(path.relative_to(ROOT)))
    return not hits, hits


def check_stage_markers() -> tuple[bool, list[str]]:
    text = (ROOT / "docs" / "STAGE_GATES.md").read_text(encoding="utf-8")
    markers = ("P0", "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10", "RC", "V1")
    missing = [marker for marker in markers if marker not in text]
    return not missing, missing


def run_tests() -> dict[str, object]:
    proc = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py", "-v"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    return {
        "passed": proc.returncode == 0,
        "exit_code": proc.returncode,
        "stdout": proc.stdout[-4000:],
        "stderr": proc.stderr[-2000:],
    }


def git_state() -> dict[str, object]:
    proc = subprocess.run(["git", "status", "--short", "--branch"], cwd=ROOT, capture_output=True, text=True)
    return {"available": proc.returncode == 0, "exit_code": proc.returncode, "status": proc.stdout.strip()}


def main() -> int:
    docs_ok, missing_docs = check_required_docs()
    forbidden_ok, forbidden = check_forbidden_paths()
    secrets_ok, secret_hits = check_secrets()
    stages_ok, missing_stages = check_stage_markers()
    tests = run_tests()
    result = {
        "stage": "P0",
        "local_gate": all((docs_ok, forbidden_ok, secrets_ok, stages_ok, bool(tests["passed"]))),
        "checks": {
            "required_docs": {"passed": docs_ok, "missing": missing_docs},
            "forbidden_post_p0_paths": {"passed": forbidden_ok, "present": forbidden},
            "secret_scan": {"passed": secrets_ok, "hits": secret_hits},
            "stage_markers": {"passed": stages_ok, "missing": missing_stages},
            "tests": tests,
            "git": git_state(),
        },
        "note": "local_gate is not the same as external Provider, GitHub, Agent or user acceptance",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["local_gate"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
