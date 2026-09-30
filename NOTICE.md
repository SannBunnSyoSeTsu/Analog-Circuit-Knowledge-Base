# 来源、署名与许可

## 原模拟电路知识库

基础笔记、`code/` 与 `figures/` 来自 [Arcadia-1/Analog-Circuit-Knowledge-Base](https://github.com/Arcadia-1/Analog-Circuit-Knowledge-Base)，原作者为 **Arcadia-1 / Token Zhang**。上游当前名称是 [circuits-and-systems-classroom](https://github.com/Arcadia-1/circuits-and-systems-classroom)。本仓库以本机冻结提交 `3dab7086bcfc26fd963ada29bd2aa2f9ffe02e58` 为基础，并保留该提交以前的 Git 历史；没有把这些笔记宣称为本项目原创。

上游当前 MIT 许可证原文保存在 [Arcadia-Classroom-MIT.txt](LICENSES/Arcadia-Classroom-MIT.txt)，复制自上游提交 `4bb0994d152baf6d0b3db1151c82b5f224c97c45` 的 LICENSE，保留 Copyright (c) 2026 Token Zhang。此文件用于记录基础知识库的上游许可，不作为整个聚合仓库的统一许可。

## Analog Design Bench V2

50 项任务、参考电路、验证脚本和基准数据来自 **[Arcadia-1/analog-design-bench](https://github.com/Arcadia-1/analog-design-bench)**，固定版本 `c23f124de1e461655d2e02ce6cfae2654ccea0d3`。上游署名为 Copyright 2026 Analog Design Bench contributors。

[原 LICENSE](Analog-Design-Bench-V2-Lessons/sources/upstream/LICENSE)、[Apache-2.0](Analog-Design-Bench-V2-Lessons/sources/upstream/LICENSES/Apache-2.0.txt)、[CC BY-NC 4.0](Analog-Design-Bench-V2-Lessons/sources/upstream/LICENSES/CC-BY-NC-4.0.txt) 均原样保留。软件与 benchmark 内容采用不同许可，商业使用等条件以各文件及原许可为准。来源说明和网站公开提交快照的边界见 [SOURCES](Analog-Design-Bench-V2-Lessons/SOURCES.md)。原 README 的 benchmark 语料声明与 canary 标识继续保留。

中文案例笔记是静态阅读和解释；SMIC18 部分是另行完成的工艺迁移与 nominal 仿真。二者的验证范围分别注明。第三方材料和相关改编保留来源与原有许可条件；未对其余新增材料另行授予统一开源许可。

## 工具与发布

复现使用 [Arcadia-1/virtuoso-bridge-lite](https://github.com/Arcadia-1/virtuoso-bridge-lite) 的 Spectre runner / PSF parser，感谢其工具支持。PDK、原厂标准单元和 Cadence 软件保留各自权利；本仓库未分发厂商模型、CDL、提取的 HD 单元库或许可证。

本次文档对应配套工程提交 [`6ae3e14`](https://github.com/SannBunnSyoSeTsu/smic18-benchmark-reproduction/tree/6ae3e1434914297c4ed12b93cb8d6a297ef8339a)。原始大体积 PSF 与机器环境保留在本机，GitHub 内的链接只指向实际发布的文件。
