# Stage Gates

状态：路径冻结；当前只执行 P0。

| 阶段 | 目标 | 必须证据 | 当前状态 |
|---|---|---|---|
| P0 | 开发基线 | Provider、GitHub 公开审计仓库、规范、测试、Secret、日志、双 Agent、独立审查 | BLOCKED |
| P1 | Mac Worker | 真机能力、任务隔离、队列、恢复和权限测试 | NOT_STARTED |
| P2 | Illustrator Bridge | 真实 Illustrator 会话、读写/保存/恢复验证 | NOT_STARTED |
| P3 | Photoshop Bridge | 真实 Photoshop 会话、资产与输出验证 | NOT_STARTED |
| P4 | Packaging Scene Graph | schema、fixture、版本化和拒绝测试 | NOT_STARTED |
| P5 | Structure + Layout Engine | 几何正确性、尺寸和可解释布局测试 | NOT_STARTED |
| P6 | Material + Process Engine | CMYK/专色/白墨/后加工规则和生产证据 | NOT_STARTED |
| P7 | Adobe Production Pipeline | 端到端真实 Adobe 产物和哈希 | NOT_STARTED |
| P8 | QA + Critic + Repair | 发现问题、修复、回归和人工复核闭环 | NOT_STARTED |
| P9 | 24/7 无人值守 | 长时间运行、告警、限流、恢复和人工接管 | NOT_STARTED |
| P10 | 真实包装压力测试 | 多类型真实任务、失败率、输出 QA 和人工验收 | NOT_STARTED |
| RC | 发布候选 | 全量回归、生产样本、变更冻结和用户终审 | NOT_STARTED |
| V1 | 正式版本 | RC 通过、关键 tag、回滚点和交付清单 | NOT_STARTED |

## P0 退出条件

P0 只有在以下条件全部满足时才允许 PASS：

1. Work 当前模型和思考设置已按用户最新决定记录；不隐瞒实际使用的模型。
2. TRAE Provider 的 Base URL、请求地址、模型 ID、协议、Key 存在性、超时/重试可见性和错误响应均有脱敏证据。
3. 在最后一次 Provider 修改后，连续 3 次最小请求成功，并完成 1 次正常代码任务；结果和时间可复核。
4. P0 GitHub 公开审计仓库、`dev` 分支和 `main` 保护规则已核验，且公开内容扫描确认没有业务代码、客户资料、真实 Adobe 文件或凭据。
5. 十份文档、Secret 忽略规则、测试入口和 JSONL 证据格式已进入 Git。
6. Developer 与 Reviewer 是两个独立上下文；Reviewer 默认只读/测试/审计，且有独立结果。
7. 本地测试、Secret 扫描、禁止路径检查和工作树检查均通过。
8. 用户/终审确认 P0 退出；在此之前不进入 P1。

任一项缺失、冲突或只依赖历史记录，P0 保持 BLOCKED。

## P1 进入前的仓库迁移门

P0 通过后、P1 开始前必须额外满足：

1. GitLab Free 私有项目已创建并完成基线迁移，迁移前后文件清单和提交哈希已核对。
2. GitLab `main` 已设置保护规则，直接推送、强制推送和删除均被禁止；合并门禁的实际状态已记录。
3. GitHub P0 审计仓库已冻结或归档；其公开内容仍按可能被复制处理。
4. 只有完成上述证据后，才允许创建 Mac Worker、Adobe Bridge 或包装业务代码。
