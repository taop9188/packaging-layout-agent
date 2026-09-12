# P0 证据记录

更新时间：2026-09-12
当前结论：`BLOCKED`

本文件只记录脱敏、可复核的事实。它不是 Stage PASS 声明。

## A. Work 模型记录

- 用户最新决定：不切换模型，沿用当前 Work。
- 当前 Work 主模型结构化状态：`gpt-5.6-luna`。
- 不能把当前状态写成 `gpt-5.6-terra`；此前 Terra 条件已被用户在本轮覆盖。
- 思考强度的当前值未从任务元数据独立读出，未作为已满足项。

## B. TRAE Provider 证据

### B1. 当前配置与连通性

- 2026-09-12 11:32-11:33，TRAE 当前模型管理界面仍显示 `deepseek-v4.1-flash`。
- Provider：`custom_openai_compatible`；协议：OpenAI Chat Completions。
- Base URL：`https://ai.comfly.org/v1`；TRAE 实际请求端点为 `/v1/chat/completions`。
- API Key：已保存/掩码状态；本记录不保存明文。
- 唯一配置修正：思考模式确认并保存为“关闭”；没有更换模型 ID、Base URL 或协议。
- TRAE 日志证据：`custom_model_connectivity_check` 在 `11:32:57.509` 发起，`11:33:15.361` 成功，耗时约 `17.852s`；`settings_custom_model_connect` 记录 `is_success:true`。
- 该连通性测试只证明 Provider 检查成功，不单独替代下面的完整请求序列。

### B2. 本轮新鲜请求验证

以下请求均在上述连通性测试之后，于同一个 TRAE 当前模型选择下完成；每次只在上一请求形成明确结果后才发送下一次。

| 时间 | 验证 | 实际结果 | 状态 |
|---|---|---|---|
| 11:36 | `Reply only OK-1` | 返回 `OK-1` | PASS |
| 11:37 | `Reply only OK-2` | 返回 `OK-2` | PASS |
| 11:38 | `Reply only OK-3` | 返回 `OK-3` | PASS |
| 11:39，任务耗时 42s | 创建并运行临时 `hello_timeout_check.py` | 输出 `TRAE_PROVIDER_OK`；退出码 `0`；确认未触碰项目文件或文档 | PASS |

### B3. 角色上下文

- Reviewer 独立任务于 11:42 返回 `REVIEWER_CONTEXT_READY`，确认 P0-only、只读、独立上下文、证据优先，并声明缺证据时返回 `BLOCKED`。
- 干净 Developer 独立任务于 11:44 返回 `DEVELOPER_CONTEXT_READY`，确认 P0-only、只有明确指派时才可写入、不得改 `SPEC`/降门禁/宣告 PASS、不得进入 P1 或包装业务代码、失败停止。
- 早期中文输入截断导致的旧 Developer 任务曾在其 TRAE 临时目录生成 3 个文档；这些文件不在本项目仓库内，不作为源码或基线证据。
- 早期 Reviewer 请求曾返回 HTTP 502；该失败发生在本轮配置连通性复测之前，保留为历史失败记录，不覆盖本轮成功验证。

## C. Codex 原生 DeepSeek 范围决策

- 用户最新决定：不需要 Codex 原生 DeepSeek 替代 TRAE。
- Codex 原生 DeepSeek 管理器不纳入本次 P0 验收范围，也不作为 TRAE 的替代或兜底依据。
- 不执行原生模型替换，不把原生管理器的状态写成 TRAE Provider 验收证据。

## D. GitHub 证据

- 账号：`taop9188`。
- 仓库：`taop9188/packaging-layout-agent`。
- 可见性：`private`。
- 默认分支：`main`。
- 远端分支：`main`、`dev`；通过远端分支查询确认两者存在。
- GitHub `main` 基线提交：`bb3ff40a3960bf793d43edd8b95065c630ec0ffe`；本轮范围修订同步前的 `dev` 提交：`6bad0d86b9d57b0f7102b311a0d790a88685b794`。
- 随后的 `records/P0_EVIDENCE.md` 内容同步操作由 GitHub API 返回新 `dev` 提交：`22859c0d934c668ae7c071c2ed6227f20e50507f`。
- 本地 `dev` 在完成范围修订时的提交：`2f57d896548f88af737e9e875e463c3de1bed1e6`；随后补充 transport 证据并重新提交，工作树保持干净。
- 本地 `origin` 已配置为 `https://github.com/taop9188/packaging-layout-agent.git`，未在 URL 中嵌入凭据。
- 只读 Git transport 验证未通过：`git ls-remote --heads origin` 返回 `could not read Username for 'https://github.com': Device not configured`；未执行 push、强制更新或覆盖远端历史。
- 远端抽样文件：`docs/STAGE_GATES.md`、`records/P0_EVIDENCE.md`、`tests/test_p0_baseline.py` 均可从 `dev` 读取。
- `main`/`dev` 当前 API 状态均为未保护；因此“main 只保留验收通过版本”目前是仓库协议与 CI 约束，尚未成为 GitHub 强制规则。
- GitHub rulesets 读取接口返回 `403: Upgrade to GitHub Pro or make this repository public to enable this feature`；本次保持仓库私有，未公开仓库或绕过该限制。

## E. 本地检查记录

以下栏目只在实际命令运行后填写：

| 时间 | 命令 | 退出码 | 结果 |
|---|---|---:|---|
| 2026-09-12 | `python3 -m unittest discover -s tests -p 'test_*.py' -v` | 0 | `5/5` 通过；含一次初版扫描规则修正后的新鲜结果 |
| 2026-09-12 | `python3 scripts/p0_gate.py` | 0 | 首次运行 `local_gate=true`；当时发现 `logs/README.md` 尚未纳入提交，已补正后重跑 |

## D2. 当前零费用路线状态（2026-09-12）

本节是对 D 节历史状态的当前修订，不删除历史证据。

- 用户已确认：不购买 GitHub Pro，不使用 Codex 原生 DeepSeek 替代 TRAE；采用“P0 GitHub Free 公开审计仓库，P1 起迁移 GitLab Free 私有项目”的路线。
- GitHub 仓库当前可见性已在设置页确认是 `public`。
- 公开仓库当前范围仍限于 P0 文档、测试、门禁脚本、日志说明和脱敏证据；未放入包装业务代码、客户资料、真实 Adobe 文件、私密算法或凭据。
- 已通过 GitHub 网页端同步的范围修订提交包括：`fdbf8a8`（README）、`c1945ba`（路线规范文档）、`e139977`（执行计划）。这些提交在远端提交页显示状态检查成功。
- 本文件上一版已通过 GitHub 网页端同步，远端 `dev` 提交为 `1b1087accb74f7079ccdc659333d5facb001d748`（短 SHA：`1b1087a`）。
- 随后补充的证据版本已同步为 `f5e26be8cdc207347b2e02572898abb47da93d37`（短 SHA：`f5e26be`）；对应 GitHub Actions `P0 local gate #18` 已完成且成功。
- GitHub ruleset：`P0 main protected`，规则集 ID `23008634`，状态为 Active；目标为默认分支 `main`。
- 已核实的规则：合并前必须提交拉取请求；必须通过状态检查 `P0 local gate`；限制删除；阻止强制推送；旁路列表为空。
- 规则集页面的状态检查来源显示为“任何来源”；本记录不声称其已限制为 GitHub Actions。当前 P0 仅要求检查名称与结果可追溯。
- P1 的 GitLab Free 私有项目尚未创建；这是 P0 用户/终审通过后的迁移入口，不在本轮提前执行。

## F. 当前阻断项

1. 本机 Git transport 仍没有可用 GitHub 凭据；本地提交与 GitHub 网页端内容提交的 SHA 不共用。远端文件和路径已抽样核验，但尚未建立同一 Git transport 的镜像关系。
2. P0 用户/终审尚未完成，不能创建 P0 PASS tag，也不能进入 P1。
3. 规则集的状态检查来源仍显示为“任何来源”；这不是当前 P0 的阻断项，但已明确记录，后续若需要收紧必须单独变更并留证。

## G. 零费用路径变更记录

- 用户已确认采用零额外费用路线：P0 使用 GitHub Free 公开审计仓库；P1 起迁移到 GitLab Free 私有项目。
- 当前本地仓库已更新 SPEC、架构、开发协议、Stage Gate、测试计划、README 和仓库策略，明确公开仓库禁止业务代码、客户资料、真实 Adobe 文件、私密算法和凭据。
- 2026-09-12 已完成公开设置并在 GitHub 设置页复核；随后创建并复核 Active ruleset `23008634`，将 `main` 的关键保护规则落到 GitHub。
- 此前公共证据记录同步提交为 `1b1087a`；随后远端提交页已核验 `f5e26be` 位于 `dev` 顶部。
- 未迁移到 GitLab、未删除或归档任何仓库；P1 及后续包装业务代码均未开始。
