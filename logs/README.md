# 日志约定

运行日志采用一行一个 JSON 对象的 JSONL 格式。允许字段：`timestamp`、`run_id`、`stage`、`component`、`event`、`status`、`duration_ms`、`exit_code`、`model_id`、`request_id`、`artifact_sha256`、`error_code`、`redaction`。

禁止字段和值：API Key、Bearer token、Cookie、完整 Authorization header、密码、原始响应中的敏感字段、用户文件内容和未脱敏截图路径。

仓库只保存格式说明和脱敏摘要；本地运行日志默认被 `.gitignore` 忽略。需要进入证据包的内容必须先脱敏，并在 `records/P0_EVIDENCE.md` 中写明来源和哈希。
