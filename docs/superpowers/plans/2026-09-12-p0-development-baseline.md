# Packaging Production Agent P0 Development Baseline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 建立 Packaging Production Agent 的可追溯 P0 开发基线，让 GitHub、规范、测试、凭据边界、日志、双 Agent 角色和 Stage Gate 在进入任何包装业务代码前先固定下来。

**Architecture:** 本地仓库只承载可审计的规范、验证脚本和测试骨架；GitHub 私有仓库作为源码与阶段状态的唯一基线。TRAE 负责实际执行，Developer 与 Reviewer 使用不同会话；Reviewer 只读取证据并给出审计结论，P0 通过必须同时满足文件、测试、配置、分支和外部验证证据。

**Tech Stack:** Git 2.x；Python 3.11+ 标准库 `unittest`；TRAE Work `deepseek-v4.1-flash`；GitHub 私有仓库；macOS Keychain；JSONL 审计日志。

**Spec:** `docs/SPEC.md`、`docs/STAGE_GATES.md` 和本计划。

## Global Constraints

- 当前 Work 沿用用户最新决定的 `gpt-5.6-luna`，不自动切换模型；此项不宣称满足此前的 Terra 条件。
- TRAE Provider 的目标模型固定为 `deepseek-v4.1-flash`；不使用其他模型替代验收。
- 只完成 P0；在 P0 通过用户/终审前，不创建 P1 Mac Worker、Adobe Bridge 或包装业务代码。
- API Key 只允许进入 macOS Keychain 或运行时环境；禁止进入 Git、日志、Markdown、截图、URL、命令行参数和测试夹具。
- `dev` 是工作分支；`main` 只接收带验收证据的版本；没有证据不得把分支或 tag 宣称为通过。
- 任何 Stage PASS 都必须由独立证据支持，AI 自述、绿色测试或一次 UI 点击都不能单独构成通过。
- 失败、超时、证据缺失或发现泄密时立即停止当前阶段，并保留可回滚的提交和备份。

---

## File Map

- `docs/SPEC.md`: 产品边界、事实源、P0/P1 边界和禁止降级项。
- `docs/ARCHITECTURE.md`: 人、GitHub、TRAE、Agent、后续 Adobe/Worker 的责任边界。
- `docs/DEVELOPMENT_PROTOCOL.md`: 开发、审查、提交、推送和停止规则。
- `docs/PACKAGING_SCHEMA.md`: 未来 Scene Graph 的数据边界；P0 只冻结契约，不实现业务。
- `docs/PROCESS_RULES.md`: CMYK、专色、白墨、烫金、UV、击凸等印前约束。
- `docs/ADOBE_AUTOMATION.md`: 后续 Adobe 控制的安全边界；P0 只冻结接口原则。
- `docs/QA_STANDARD.md`: Geometry、Visual、Production QA 的证据要求。
- `docs/STAGE_GATES.md`: P0-P10、RC、V1 的进入/退出条件。
- `docs/TEST_PLAN.md`: P0 测试矩阵与后续真机测试边界。
- `docs/RECOVERY.md`: 504、Worker/Adobe 中断、损坏文件和回滚处理。
- `.gitignore`, `.env.example`, `pyproject.toml`: 版本库边界、密钥示例和测试入口。
- `scripts/p0_gate.py`: 只读检查 P0 文件、秘密扫描、测试命令和当前 Git 状态。
- `tests/test_p0_baseline.py`: 不依赖网络、Key 或 Adobe 的确定性基线测试。
- `records/P0_EVIDENCE.md`: 只记录脱敏、可复核的当前证据与阻断项。
- `logs/README.md`: JSONL 日志格式、保留策略和禁止字段。

## Tasks

### Task 1: Create the local repository skeleton

**Files:**

- Create: `.gitignore`, `.env.example`, `pyproject.toml`, `README.md`
- Create: `docs/superpowers/plans/2026-09-12-p0-development-baseline.md`

- [ ] **Step 1: Create only the repository directories and metadata files.** Keep `src/`, Adobe bridge, worker, scene graph implementation, and production fixtures absent.
- [ ] **Step 2: Add the secret and artifact boundaries.** Ignore `.env`, Keychain exports, runtime logs, caches, virtual environments, databases, build output, and Adobe temporary files.
- [ ] **Step 3: Add the standard-library test entry.** `python3 -m unittest discover -s tests -p 'test_*.py' -v` must be the baseline command on macOS; CI uses the equivalent `python` command.
- [ ] **Step 4: Run the baseline test command and inspect the working tree.** Record the exact result in `records/P0_EVIDENCE.md`.

### Task 2: Freeze the ten project documents

**Files:**

- Create: `docs/SPEC.md`, `docs/ARCHITECTURE.md`, `docs/DEVELOPMENT_PROTOCOL.md`
- Create: `docs/PACKAGING_SCHEMA.md`, `docs/PROCESS_RULES.md`, `docs/ADOBE_AUTOMATION.md`
- Create: `docs/QA_STANDARD.md`, `docs/STAGE_GATES.md`, `docs/TEST_PLAN.md`, `docs/RECOVERY.md`

- [ ] **Step 1: Write the authority and scope rules.** State that GitHub files, test output, runtime evidence and actual Adobe artifacts outrank AI claims and planning text.
- [ ] **Step 2: Write the P0 gate.** Require Provider evidence, three consecutive TRAE minimum requests, one normal code task, repository visibility, branch policy, secret scan, deterministic tests, and independent Reviewer evidence.
- [ ] **Step 3: Write the P0-P10 path and later-stage contracts.** Mark all post-P0 stages as not started and forbid their implementation in this baseline.
- [ ] **Step 4: Write production constraints without pretending they are implemented.** CMYK, spot colors, white ink, foil, UV and embossing are acceptance rules for future production artifacts, not runtime features in P0.
- [ ] **Step 5: Cross-check all ten documents for conflicting model names, stage names, permissions, or secret handling.**

### Task 3: Add deterministic P0 verification

**Files:**

- Create: `scripts/p0_gate.py`, `tests/test_p0_baseline.py`, `logs/README.md`
- Create: `records/P0_EVIDENCE.md`

- [ ] **Step 1: Test required files and forbidden implementation paths.** The test must fail if a required document is absent or if P1/Adobe/scene-graph runtime code appears.
- [ ] **Step 2: Test secret hygiene.** Scan tracked candidate files for API-key patterns and forbidden fields; permit only redacted words in evidence documentation.
- [ ] **Step 3: Test stage and branch rules.** Check that the stage table contains P0 through P10, RC and V1, and that `main`/`dev` rules are present.
- [ ] **Step 4: Implement `scripts/p0_gate.py` as a read-only wrapper.** It runs the deterministic checks, the test command, and emits a compact JSON result without network calls or configuration writes.
- [ ] **Step 5: Run both the unit tests and the gate script.** Save exit codes and counts; a missing external credential remains a blocked check, never a fabricated pass.

### Task 4: Establish Git and GitHub history

**Files:**

- Modify: local Git metadata only
- Create: GitHub private repository `taop9188/packaging-layout-agent`

- [ ] **Step 1: Initialize local `main` and commit the repository bootstrap.** The bootstrap contains no business code and is safe to audit.
- [ ] **Step 2: Create local `dev` from the bootstrap.** Commit the P0 documents and verification tooling there.
- [ ] **Step 3: Push or write the same commits to the private GitHub repository.** Use a credentialed GitHub connector or an existing authenticated Git transport; never embed a token in a remote URL.
- [ ] **Step 4: Verify the remote repository is private, the default branch is `main`, and `dev` contains the P0 commit.** Record commit IDs and repository metadata.
- [ ] **Step 5: Create a key P0 baseline tag only after the gate result is supported by current evidence.** If any external check is blocked, use no PASS tag.

### Task 5: Configure and verify the two TRAE contexts

**Files:**

- Modify: TRAE Work sessions only; no project business files
- Record: `records/P0_EVIDENCE.md`

- [ ] **Step 1: Preserve the existing Provider configuration before any change.** Record only masked Key state and non-secret fields: Base URL, model ID, protocol, timeout/retry visibility, and error code.
- [ ] **Step 2: Confirm the actual TRAE model is `deepseek-v4.1-flash`.** Codex-native DeepSeek is outside this P0 acceptance scope and is not used as a replacement.
- [ ] **Step 3: Use one new Developer session and one separate Reviewer session.** Developer may edit only the scoped repository; Reviewer is read-only/test/audit and must not write or commit.
- [ ] **Step 4: Verify three minimum requests and one normal code task after the last Provider change.** Do not repeat requests after a missing or contradictory result without first recording the cause.
- [ ] **Step 5: Record the earlier same-day TRAE evidence as historical evidence and distinguish it from current-session verification.** The historical result is not a substitute for a new result when the Provider changed.

### Task 6: Independent P0 review and handoff

**Files:**

- Modify: `records/P0_EVIDENCE.md`
- Modify: `docs/STAGE_GATES.md` only if a factual correction is needed

- [ ] **Step 1: Run the full local verification command and inspect the complete output.** Check exit code, test count, secret scan result, and forbidden-path result.
- [ ] **Step 2: Compare the working tree and GitHub `dev` state.** Confirm no untracked secret, cache, runtime database, or generated output is present.
- [ ] **Step 3: Obtain independent Reviewer evidence.** It must cite the exact files and outputs inspected. Native-agent evidence is outside this P0 scope.
- [ ] **Step 4: Decide P0 status from evidence.** Mark `PASS` only when every P0 criterion is true; otherwise mark `BLOCKED` with the exact missing evidence and stop before P1.
- [ ] **Step 5: Prepare user handoff.** Report actual model/provider, repository visibility, commit/tag IDs, test counts, historical versus current evidence, and the next required user action.

## Self-Review Checklist

- [ ] The plan covers all ten required documents, the P0-P10 path, branch rules, secret boundaries, logging, test framework, backup/recovery, TRAE verification, and independent review.
- [ ] No plan step instructs an agent to invent output, bypass a missing credential, or silently replace `deepseek-v4.1-flash`.
- [ ] No task creates P1 Worker, Adobe Bridge, scene-graph runtime, or packaging business code.
- [ ] The plan distinguishes static configuration from real-time Provider and sub-agent acceptance.
