# P0 证据记录

更新时间：2026-09-12
当前结论：`BLOCKED`

本文件只记录脱敏、可复核的事实。它不是 Stage PASS 声明。

## A. Work 模型记录

- 用户最新决定：不切换模型，沿用当前 Work。
- 当前 Work 主模型结构化状态：`gpt-5.6-luna`。
- 不能把当前状态写成 `gpt-5.6-terra`；此前 Terra 条件已被用户在本轮覆盖。
- 思考强度的当前值未从任务元数据独立读出，未作为已满足项。

## B. TRAE Provider 历史证据

- 来源：同日独立 TRAE 排障任务，任务标题为“修复 TRAE DeepSeek 超时错误”。
- Provider：`custom_openai_compatible`；显示模型：`deepseek-v4.1-flash`。
- Base URL 与协议在报告中已记录，API Key 只记录为已保存/掩码状态，未记录明文。
- 修复动作：思考模式从“跟随模型默认配置”改为“关闭”；没有更换模型 ID、Base URL 或协议。
- 结果：修复后连续最小请求 `3/3` 成功，随后 1 次正常代码任务退出码为 0，输出为 `TRAE_PROVIDER_OK`。
- 限制：这是历史任务证据；若 Provider 在本记录之后发生变化，必须重新执行验证。

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
- 远端分支：`main`、`dev`，当前 `dev` HEAD 为 `d8938b9e06d78c4546e707dd9f4145a95114fc3e`。
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
4. Developer/Reviewer 的独立上下文已创建，但首条确认响应仍未形成可复核的完成证据。
5. P0 用户/终审尚未完成。
