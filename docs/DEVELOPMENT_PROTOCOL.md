# 开发协议

## 1. 分支与提交

- `main` 只保存已通过当前 Stage 终审的版本。
- `dev` 承载开发、测试和 Reviewer 审计。
- 每次提交只做一个可说明的变更，提交消息使用 `type: scope: summary` 形式，例如 `docs: p0: freeze stage gates`。
- 未通过本地检查的提交不得推送到 `main`。
- 关键 tag 只能指向已有证据的提交；当前 P0 未通过前不创建 PASS tag。

## 2. 自动 commit/push 约束

自动化只能调用只读检查和显式授权的提交包装流程。包装流程必须在 commit 前依次确认：

1. 当前分支不是 `main`，除非这是已批准的验收合并。
2. 工作树中没有被忽略规则之外的 Secret、数据库、缓存或原始日志。
3. 本地测试与 P0 gate 均返回 0。
4. 提交内容和提交消息与任务范围一致。
5. 推送目标是已确认的 `taop9188/packaging-layout-agent`。

自动化不得：

- 读取、回显或写入 API Key。
- 强制推送、重写历史、删除远端分支或覆盖他人提交。
- 直接把未审查变更推到 `main`。
- 在失败后无限重试、自动改模型或自动放宽超时。

## 3. Developer 规则

Developer 只在当前任务声明的路径内工作；遇到缺失凭据、未知 Provider 状态、冲突修改、测试失败或外部服务超时，记录并停止。Developer 不能编辑 `docs/SPEC.md` 的产品边界，也不能自报 Stage PASS。

## 4. Reviewer 规则

Reviewer 必须使用与 Developer 不同的会话上下文。输入只包括事实文件与输出，不包括 Developer 的私下解释。Reviewer 可以运行本地测试，但默认不写文件、不提交、不推送；如发现问题，返回带路径和证据的 BLOCKED/REQUEST_CHANGES。

## 5. 失败停止条件

以下任一情况立即停止当前阶段：

- Provider 返回 4xx/5xx、响应格式不完整或身份状态不明。
- API Key 进入输出、日志、Git diff 或 URL。
- 当前分支、远端或文件来源无法确认。
- 结果与已有事实冲突且没有人工裁决。
- 发生文件损坏、并发写入、非预期删除或权限异常。
