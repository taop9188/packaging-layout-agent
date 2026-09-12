# Packaging Production Agent

这是包装生产 Agent 的阶段门禁仓库。当前只建立 P0 开发基线，不包含包装业务逻辑、Mac Worker、Illustrator Bridge、Photoshop Bridge 或 Scene Graph 运行时。

## 当前状态

`P0 = BLOCKED`

本地规范与确定性检查可以通过，但 P0 还需要外部证据：TRAE Provider 的当前验收记录、Developer/Reviewer 两个独立上下文的实际元数据与结果，以及 GitHub 公开审计仓库 `dev` 分支和 `main` 保护规则的可复核状态。静态配置、历史报告和 AI 自述都不会被当作 PASS。

## 零费用仓库策略

- P0：GitHub Free 公开审计仓库，只放规范、测试、门禁脚本和脱敏证据。
- P1 起：迁移到 GitLab Free 私有项目，作为唯一源码基线。
- 公开仓库不得出现包装业务代码、客户资料、真实 Adobe 文件、私密算法或凭据；P0 通过后冻结/归档，不依赖删除清除公开副本。

## 事实源优先级

1. 当前阶段指定仓库中的规范、代码、提交和分支状态。
2. 实际命令输出、TRAE 运行结果和脱敏日志。
3. 实际 Adobe 产物及其 QA 记录。
4. 计划、模型回复和口头结论只作为工作材料。

## 本地检查

```text
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 scripts/p0_gate.py
```

检查脚本只读本地文件和 Git 状态，不发起模型请求、不修改 Provider、不写入凭据、不执行 Adobe 操作。

## 分支规则

- `dev`：开发与审查分支。
- `main`：只接收证据完整、通过独立审查的版本。
- `P0-*` tag：只有 P0 全部条件满足后才能创建；当前没有 PASS tag。

完整边界见 [`docs/SPEC.md`](docs/SPEC.md)、[`docs/STAGE_GATES.md`](docs/STAGE_GATES.md) 和 [`records/P0_EVIDENCE.md`](records/P0_EVIDENCE.md)。
