---
case_id: adb-v2-43
task_id: sky130-inductive-lna-2p4ghz-gain12-nf2-pvt
category: 时钟与射频
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-inductive-lna-2p4ghz-gain12-nf2-pvt/instruction.md
  - ../sources/upstream/tasks/sky130-inductive-lna-2p4ghz-gain12-nf2-pvt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-inductive-lna-2p4ghz-gain12-nf2-pvt/tests/verify.py
  - ../sources/upstream/tasks/sky130-inductive-lna-2p4ghz-gain12-nf2-pvt/results/reference.json
---

# 43 · 2.4 GHz LNA：匹配、噪声与稳定性要使用同一端口定义

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

27 点 PVT，在 2.35–2.45 GHz 检查 transducer gain≥12 dB、NF≤2 dB、S11/S22/S12；0.1–10 GHz 另查 K 与 |Δ|。

## Reference 拓扑与尺寸线索（静态事实）

官方有限 Q 电感，栅/漏约 5.79 nH，源用中心抽头半绕组；NMOS 输入总宽 480 µm/nf32、cascode 320 µm/nf64，物理 MIM 匹配及复制偏置。

## 可复用的工程认识（推断，迁移时有条件）

源退化电感能产生输入实部，栅电感配谐振消除虚部；cascode 抑制反向传输。电压增益不能代替含源/负载失配的功率增益，低 NF 也不能替代带外稳定性条件。半绕组的接法与完整器件参数不可混用。

## 不能由 pass 推出的结论

已使用 PDK 有限 Q 模型，但仍不是提取/EM 结果。reference NF≈1.98 dB、S12≈−30.4 dB 余量很小，不宜直接承担额外版图损耗。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-inductive-lna-2p4ghz-gain12-nf2-pvt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-inductive-lna-2p4ghz-gain12-nf2-pvt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-inductive-lna-2p4ghz-gain12-nf2-pvt)
- [Reference circuit](../sources/upstream/tasks/sky130-inductive-lna-2p4ghz-gain12-nf2-pvt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-inductive-lna-2p4ghz-gain12-nf2-pvt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-inductive-lna-2p4ghz-gain12-nf2-pvt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-inductive-lna-2p4ghz-gain12-nf2-pvt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-inductive-lna-2p4ghz-gain12-nf2-pvt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-inductive-lna-2p4ghz-gain12-nf2-pvt/circuit.spi) · [网站结果快照](../sources/astra/sky130-inductive-lna-2p4ghz-gain12-nf2-pvt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-inductive-lna-2p4ghz-gain12-nf2-pvt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-14T20:10:55+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `band_transducer_gain` | gain_min=15.8dB at ff/1.62V/+125C; gain_max=19.1dB; ripple_max=0.458dB at tt/1.62V/-40C |
| `input_match` | S11_worst=-12.2dB at ff/1.62V/+125C |
| `output_match` | S22_worst=-12.4dB at ss/1.98V/+125C |
| `noise_figure` | NF_worst=1.98dB at ff/1.62V/+125C |
| `reverse_isolation` | S12_worst=-30.4dB at ff/1.62V/+125C |
| `unconditional_stability` | K_min=2.166 at ff/1.62V/-40C; delta_max=0.9847 at ff/1.62V/+27C |
| `power_and_bias_compliance` | power_max=6.003mW at ss/1.98V/+125C; iref_min=0.6338V; headroom_min=0.8215V |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/tb_rf_tt.spi](../sources/upstream/tasks/sky130-inductive-lna-2p4ghz-gain12-nf2-pvt/environment/starter/testbench/tb_rf_tt.spi) — ac, noise, op
- [tests/benches/tb_rf.spi](../sources/upstream/tasks/sky130-inductive-lna-2p4ghz-gain12-nf2-pvt/tests/benches/tb_rf.spi) — ac, noise, op

## 相邻案例

[30 Gilbert 混频器：线性指标需要幅度斜率自检](30-sky130-gilbert-cell-mixer-2p4ghz-pvt-mismatch.md) · [32 28 Gb/s CML 发射器：带宽还需眼图和群延迟约束](32-sky130-cml-tx-driver-28g-nrz-pvt.md) · [49 2 GHz LC VCO：调谐范围、pushing 与启动初值分开记录](49-sky130-lc-vco-2ghz-pvt.md)
