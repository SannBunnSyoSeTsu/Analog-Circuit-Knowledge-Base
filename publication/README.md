# 知识库发布记录

基础笔记沿用上游 `3dab7086bcfc26fd963ada29bd2aa2f9ffe02e58` 及其历史。`Analog-Design-Bench-V2-Lessons` 为静态案例学习，`SMIC18-Benchmark-Reproduction` 为 50 项 nominal 实测报告与证据。来源和许可见 [NOTICE](../NOTICE.md)。

本次公开副本包含已修正可读性的 50 份 Markdown。原 PDF、网表、合同与测量结果保留原值；19 个原厂 `hd_cells.scs` 副本未分发。机器配置与原始 PSF 波形不在此副本中。

- [当前内容校验](knowledge-audit.json)：211 份文档、374 张生成表格、3,429 个本地链接。
- [报告可读性校验](readability-audit.json)：50 份报告、217 张表、8,637 个单元格。
- [本地路径与配套工程映射](link-mapping.json)：历史本机链接映射到实际发布文件；未上传材料明确标注本地归档。
- [当前文件 SHA-256](files.sha256.json)：本次仓库文件，以此检查当前副本。

旧 JSON 中的机器路径、日期及文档哈希是历史记录，未改写成新的仿真或验收。当前报告哈希见各案例的 `markdown_readability.json`。本机原知识库按只读要求保留，此仓库在独立工作副本中整理。

在 Python 3.11 或更新版本运行：

```bash
python tools/verify_knowledge_base.py
```
