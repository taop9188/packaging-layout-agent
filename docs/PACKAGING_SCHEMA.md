# Packaging Scene Graph 数据规范（冻结契约，P0 不实现）

## 1. 目的

为后续包装结构、版面和工艺处理提供可版本化的中间表示。本文只规定边界与校验原则，不定义当前可执行的布局业务。

## 2. 顶层对象

后续输入必须包含：

```json
{
  "schema_version": "1.0",
  "job_id": "stable-id",
  "package_type": "declared-type",
  "units": "mm",
  "panels": [],
  "layers": [],
  "processes": [],
  "assets": [],
  "constraints": []
}
```

`schema_version`、`job_id`、单位、尺寸、来源和输入哈希必须存在；缺失时拒绝进入布局或 Adobe 阶段。

## 3. 几何与层

每个 panel 必须有明确闭合边界、坐标系、折线/切线定义和容差。每个 layer 必须声明语义、颜色空间、工艺角色、可见性和来源。刀线、折线、出血、图文、白墨、专色、烫金、UV 和击凸不能只靠图层名字猜测。

## 4. 不可变输入

原始资产、用户确认尺寸和已批准工艺参数只读保存；派生对象通过新版本产生。任何修复都要记录输入哈希、变更原因、操作者和输出哈希，不覆盖原件。

## 5. P0 边界

P0 只冻结字段和拒绝条件；没有 parser、layout engine、renderer 或 Adobe 导出实现。后续 P4/P5 必须先通过 schema fixture 和几何测试才能使用本契约。
