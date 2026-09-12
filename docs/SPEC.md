# Packaging Production Agent：项目规格与事实边界

版本：P0 baseline v0.1
状态：冻结候审，不代表 P0 已通过

## 1. 产品方向

Packaging Production Agent 的目标是把包装结构、版面、工艺、Adobe 生产和质量审查组织成可追溯的生产流水线。产品最终要服务于真实包装文件，而不是只生成概念图或聊天建议。

## 2. 当前范围

本次只完成 P0 开发基线：

- 稳定并记录 TRAE 中 `deepseek-v4.1-flash` Provider 的最小请求和正常代码任务。
- 固定 Developer 与独立 Reviewer 的职责、会话隔离和权限边界。
- 建立私有 GitHub 仓库、`dev` 分支和 `main` 验收规则。
- 冻结架构、Scene Graph、印前工艺、Adobe 自动化、QA、Stage Gate、测试与恢复规范。
- 建立脱敏证据、日志格式、Secret 管理和确定性检查入口。

P0 不包含：

- Mac Worker、24/7 调度、队列、远程执行或无人值守运行。
- Illustrator/Photoshop Bridge、AppleScript、插件安装或真实 Adobe 文件操作。
- 包装业务算法、Scene Graph 解析器、布局引擎、材料引擎或自动修复器。
- 任何声称完成真实印前生产的模拟输出。

## 3. 事实源

任何 AI 都不是项目事实源。事实源按以下优先级排列：

1. GitHub 中审查过的规范、源代码、测试和提交记录。
2. 实际 Provider/TRAE 运行结果、命令退出码和脱敏 JSONL 日志。
3. 实际 Adobe 产物、尺寸、颜色、专色和输出 QA 记录。
4. 计划、截图、模型自述、搜索结果和历史报告只能作为辅助材料。

如果来源冲突，保留冲突记录并暂停 Stage，不用模型回复覆盖事实源。

## 4. 角色边界

### 用户

负责产品方向、最终审美选择和正式 Stage 终审。

### 主控 Agent

负责架构、Stage Gate、证据检查和最终交付验收；不能把子 Agent 的自述当作通过证据。

### TRAE Developer

可以在明确范围内读取代码、编辑文件、执行测试、提交和推送。不能修改本规格的核心边界，不能降低门禁，不能自行宣布 Stage PASS。

### TRAE Reviewer

使用独立的新上下文，只读取 SPEC、Stage Gate、Git Diff、测试输出、运行结果和实际产物。默认只读、可运行测试和审计；不得编辑、提交或推送。

## 5. 不可擅自降低的要求

- 没有真实请求结果，不能把 Provider 状态写成稳定。
- 没有连续 3 次最小请求和 1 次正常代码任务，不能通过 Provider 验收。
- 没有独立 Reviewer 证据，不能把 P0 标为 PASS。
- 没有真实颜色、几何和生产证据，不能声称包装文件已达到印前交付标准。
- 不得把 `deepseek-v4-flash` 作为 `deepseek-v4.1-flash` 的静默替代。
- P0 未通过前不得进入 P1 或写包装业务代码。
