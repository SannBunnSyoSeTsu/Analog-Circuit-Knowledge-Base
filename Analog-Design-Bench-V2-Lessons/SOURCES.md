# 来源、版本与证据链

## 固定版本

- 原始入口：[Analog Design Bench V2](https://analog-design-bench.tokenzhang.com/task/v2)。
- 公开仓库：[Arcadia-1/analog-design-bench](https://github.com/Arcadia-1/analog-design-bench)。
- 本次固定 commit：`c23f124de1e461655d2e02ce6cfae2654ccea0d3`，获取日期 2026-09-20。
- [冻结任务清单](sources/upstream/tasks/benchmark.toml) 声明 `analog-design-bench-v2`、`state=frozen`，包含 50 个 slot。
- [Git tree 快照](sources/upstream-git-tree.json) 与 [逐文件 SHA-256](sources/sha256-manifest.json) 用于检查本地资料一致性。

`sources/upstream/` 是该固定版本的 996 个文件的原样副本，包含每题 instruction、task.toml、solution/circuit.spi、results/reference.json、公开诊断材料、正式 benches、verifier、夹具和许可证。保留脚本是为了读取测量定义；本次没有执行它们。

## Reference 结果的归属

每题 `results/reference.json` 提供检查消息、指标、生成时间及 provenance。已逐题核对：电路、任务说明、任务配置三个 SHA-256 与记录一致，共 150/150 项。另将所有原始文件与固定版本 Git blob 核对；这属于资料完整性，不是电路复验。

原记录包含 ngspice 版本、Sky130 commit、verifier tree 与容器 digest，各题详情留在 [case-manifest.json](case-manifest.json)。本次未下载/构建这些运行环境，也未独立重建容器以核对 image digest。不得把上游 `runtime.ngspice_runs`、stdout 或通过状态解读为本次运行产生的日志。

## 网站与 Astra 结果

- [任务列表 API 快照](sources/website-tasks.json)：`GET /api/v2/tasks`。
- [榜单 API 快照](sources/website-leaderboard.json)：`GET /api/v2/leaderboard`。
- 逐题详情来源：`GET /api/v2/tasks/{task_id}`；其中 referenceResult 另存为每题 `website-reference.json`。
- Astra 最终提交来源：`GET /api/v2/tasks/{task_id}/runs/gpt-6-astra-thinking-max/run-1`。

每个 `sources/astra/{task_id}/` 目录保存三个文件：`circuit.spi`（API 中的最终电路文本）、`result.json`（其余字段，加来源 URL、获取日期和模型分轮摘要）、`website-reference.json`（网站参考结果）。因此这是一份可追溯的提取快照，不能称为完整原始 HTTP 响应。50 个 R1 均有网站 pass 和 gates 记录；仅 8 个已做定向结构比较，其余归档供以后查阅。

没有读取或保存模型 trajectory，没有向 Astra、DeepSeek 或其他外部模型发送设计材料。不能从最终电路推断模型具体迭代步骤。网站快照的最终电路不附带与 reference 同等的三文件 provenance，所以它与固定仓库测试环境之间的关系以网站公开声明为限。

## 记录方式

每个案例的 `derived_from` 指向原说明、参考电路、verifier 与发布结果。bench 索引列出 392 个诊断/正式 deck、夹具或处理脚本入口；自动提取的分析名只帮助定位，不表示执行过这些分析，也不意味着这是 392 个独立电路。

中文知识内容由本次静态阅读综合形成。连接、元件和边界属于源码事实；简化公式与“为什么有效”的解释属于有条件推断；发布数值原文保留在检查摘要。案例间的理论链接表示关联，不表示已有知识库笔记获得了新的仿真验证。

## 署名与许可证

上游署名：Copyright 2026 Analog Design Bench contributors。原样保存 [LICENSE](sources/upstream/LICENSE)、[Apache-2.0](sources/upstream/LICENSES/Apache-2.0.txt) 与 [CC BY-NC 4.0](sources/upstream/LICENSES/CC-BY-NC-4.0.txt)。

按上游 LICENSE，Python/shell/Dockerfile 等软件适用 Apache-2.0；任务、网表、reference 数据、文档及网站内容适用 CC BY-NC 4.0，商业使用需另有书面许可；第三方 PDK/工具保留各自许可证。本次没有给这些材料重新授权，中文笔记明确标识为整理/解释，不能把附带源材料当成无条件可再许可内容。网站 Astra 提交也保留来源；未取得单独额外的使用授权。

上游 [README](sources/upstream/README.md) 还声明 benchmark 数据不应进入训练语料，并附 canary 标识；该声明和标识在原始副本中保留。本次用途是用户要求的知识库案例学习与查阅，不是模型训练数据制作。
