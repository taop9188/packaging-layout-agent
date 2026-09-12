# 总架构

状态：P0 只冻结边界，不实现运行时。

## 1. 责任链

```text
用户：产品方向 / 审美决策 / 最终终审
  ↓
主控 Agent：架构 / 证据 / Stage Gate / 交付验收
  ↓
GitHub 私有仓库：唯一源码与阶段状态基线
  ↓
TRAE Developer：受范围约束的编码、测试、提交和推送
TRAE Reviewer：独立上下文的只读审计与测试
  ↓
未来 Mac Worker：受控执行节点（P1，当前未开始）
  ↓
未来 Adobe Bridge：Illustrator / Photoshop 生产接口（P2/P3，当前未开始）
  ↓
未来包装流水线：Scene Graph、布局、材料、QA、修复（P4-P8，当前未开始）
```

## 2. 事实与执行分离

规划文档描述意图；Git 提交描述已落地文件；测试日志描述可重复命令；TRAE/Adobe 结果描述外部运行事实。任何一层都不能替代另一层。

## 3. P0 组件

P0 只包含：

- 规范层：`docs/` 下十份冻结文档。
- 验证层：`scripts/p0_gate.py` 与 `tests/`。
- 证据层：`records/P0_EVIDENCE.md` 与脱敏 JSONL 约定。
- 版本层：Git `dev`/`main` 规则和 GitHub 私有仓库。
- Agent 层：TRAE 的 Developer/Reviewer 会话定义及验收清单。

P0 不产生任何 Worker、Adobe、Scene Graph 或包装生产运行时模块。

## 4. 后续接口原则

后续每个执行节点都必须：

- 接收带版本号的输入和可追溯任务 ID。
- 输出结构化结果、文件哈希、日志位置和失败原因。
- 在超时、未知状态或文件校验失败时停止，不自动猜测或覆盖原件。
- 由下一阶段的 Gate 消费，而不是依赖聊天上下文中的隐含状态。
