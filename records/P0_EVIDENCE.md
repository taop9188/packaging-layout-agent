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

## C. Codex 原生 DeepSeek 证据

- 管理脚本静态状态：`configured`；Keychain 中存在凭据状态，但没有输出 Key 内容。
- 管理脚本固定模型：`deepseek-v4-flash`，不是项目要求的 `deepseek-v4.1-flash`。
- `setup --json` 返回官方安装脚本格式已变化，未执行远程脚本。
- `test --json` 未返回可接受的 `NATIVE_DEEPSEEK_OK` 与子线程数据库元数据双证据。
- 结论：Codex 原生 Developer/Reviewer 的 exact v4.1-flash 验收未完成，不能用其替代 TRAE 证据。

## D. GitHub 证据

- 账号：`taop9188`。
- 仓库：`taop9188/packaging-layout-agent`。
- 可见性：`private`。
- 默认分支：`main`。
- 远端分支：`main`、`dev`，本记录更新后的 `dev` HEAD 为 `bbc7a997f14a4490167a7486fda7bb2064a6880e`。
- 远端抽样文件：`docs/STAGE_GATES.md`、`records/P0_EVIDENCE.md`、`tests/test_p0_baseline.py` 均可从 `dev` 读取。
- `main`/`dev` 当前 API 状态均为未保护；因此“main 只保留验收通过版本”目前是仓库协议与 CI 约束，尚未成为 GitHub 强制规则。

## E. 本地检查记录

以下栏目只在实际命令运行后填写：

| 时间 | 命令 | 退出码 | 结果 |
|---|---|---:|---|
| 2026-09-12 | `python3 -m unittest discover -s tests -p 'test_*.py' -v` | 0 | `5/5` 通过；含一次初版扫描规则修正后的新鲜结果 |
| 2026-09-12 | `python3 scripts/p0_gate.py` | 0 | 首次运行 `local_gate=true`；当时发现 `logs/README.md` 尚未纳入提交，已补正后重跑 |

## F. 当前阻断项

1. Codex 原生管理器的模型与项目 exact `deepseek-v4.1-flash` 不一致，且没有实时验收双证据。
2. GitHub 的 `main`/`dev` 尚未配置强制保护；当前只完成协议文件和 CI 约束。
3. 本地 Git 提交与 GitHub 内容 API 的提交历史不共用 SHA；内容和路径已抽样核验，但尚未建立同一 Git transport 的镜像关系。
4. 本轮 TRAE Provider、3 次最小请求、正常代码任务及 Developer/Reviewer 上下文均已形成可复核证据；不再作为当前阻断项。
5. P0 用户/终审尚未完成。
