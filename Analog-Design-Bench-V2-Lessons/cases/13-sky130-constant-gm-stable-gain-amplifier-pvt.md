---
case_id: adb-v2-13
task_id: sky130-constant-gm-stable-gain-amplifier-pvt
category: 放大器与滤波
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: true
derived_from:
  - ../sources/upstream/tasks/sky130-constant-gm-stable-gain-amplifier-pvt/instruction.md
  - ../sources/upstream/tasks/sky130-constant-gm-stable-gain-amplifier-pvt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-constant-gm-stable-gain-amplifier-pvt/tests/verify.py
  - ../sources/upstream/tasks/sky130-constant-gm-stable-gain-amplifier-pvt/results/reference.json
---

# 13 · 恒 gm 稳增益：偏置单元必须映射到输入电流密度

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

27 点 PVT，增益 3–4、max/min≤1.15，负载压降 150–400 mV；500 fF 负载、±60 mV 差分线性检查及从零能量启动。

## Reference 拓扑与尺寸线索（静态事实）

参考 K=4 的 β 倍增环配 RB=2 kΩ、RL=8 kΩ；输入对电流密度与基准单元对应，尾电流约两倍单支路。

## 可复用的工程认识（推断，迁移时有条件）

理想电阻比给出增益 4，但网站参考结果约 3.408–3.637，说明体效应、有限输出电阻等非理想项不能忽略。把“输入对与 gm 基准的电流密度匹配”写入设计约束，比只要求尾电流稳定更直接。启动检查用绝对输出误差，不能先减去异常基线再宣称工作正常。

## 不能由 pass 推出的结论

理想电阻的温漂/失配没有自动纳入。Astra 用体源相连和不同电阻比例，仍需隔离阱及实际无源匹配条件才能迁移。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-constant-gm-stable-gain-amplifier-pvt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-constant-gm-stable-gain-amplifier-pvt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-constant-gm-stable-gain-amplifier-pvt)
- [Reference circuit](../sources/upstream/tasks/sky130-constant-gm-stable-gain-amplifier-pvt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-constant-gm-stable-gain-amplifier-pvt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-constant-gm-stable-gain-amplifier-pvt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-constant-gm-stable-gain-amplifier-pvt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-constant-gm-stable-gain-amplifier-pvt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-constant-gm-stable-gain-amplifier-pvt/circuit.spi) · [网站结果快照](../sources/astra/sky130-constant-gm-stable-gain-amplifier-pvt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-constant-gm-stable-gain-amplifier-pvt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 已做定向电路比较，见 [Astra 对照](../topics/08-astra-comparisons.md)。

Reference 结果生成时间：`2026-08-14T20:01:41+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `complete_signoff` | pvt=27/27 startup=27/27 linearity=27/27 |
| `absolute_gain_window` | gain=3.4084..3.6369 V/V |
| `bandwidth` | BW_min=40.00 MHz |
| `load_drop_window` | load_drop=195.81..333.48 mV |
| `deterministic_output_imbalance` | imbalance_max=0.0000 mV |
| `linearity` | linearity_error_max=5.99% |
| `pvt_power` | power_max=439.92 uW |
| `gain_spread` | gain_spread_ratio=1.06703 |
| `startup_power_on` | gain=3.3871..3.6295 V/V zero_imbalance_max=0.0000 mV load_drop=195.81..333.52 mV |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/tb_ac_ss.spi](../sources/upstream/tasks/sky130-constant-gm-stable-gain-amplifier-pvt/environment/starter/testbench/tb_ac_ss.spi) — ac, op
- [environment/starter/testbench/tb_ac_tt.spi](../sources/upstream/tasks/sky130-constant-gm-stable-gain-amplifier-pvt/environment/starter/testbench/tb_ac_tt.spi) — ac, op
- [environment/starter/testbench/tb_lin_tt.spi](../sources/upstream/tasks/sky130-constant-gm-stable-gain-amplifier-pvt/environment/starter/testbench/tb_lin_tt.spi) — dc
- [environment/starter/testbench/tb_startup_tt.spi](../sources/upstream/tasks/sky130-constant-gm-stable-gain-amplifier-pvt/environment/starter/testbench/tb_startup_tt.spi) — tran
- [tests/benches/tb_lin.spi](../sources/upstream/tasks/sky130-constant-gm-stable-gain-amplifier-pvt/tests/benches/tb_lin.spi) — dc
- [tests/benches/tb_pvt.spi](../sources/upstream/tasks/sky130-constant-gm-stable-gain-amplifier-pvt/tests/benches/tb_pvt.spi) — ac, op
- [tests/benches/tb_startup.spi](../sources/upstream/tasks/sky130-constant-gm-stable-gain-amplifier-pvt/tests/benches/tb_startup.spi) — tran

## 相邻案例

[03 局部反馈恒 gm 放大器：用反馈压低有效跨导漂移](03-sky130-gmr-degen-amp-constant-gm-pvt.md) · [04 简单退化差分对：有限 gm 是增益预算的一部分](04-sky130-gmr-degenerated-diff-amp-gain2-bw70m-power1p2mw-sdr60.md) · [12 β 倍增偏置：恒 gm 条件来自器件比和电阻](12-sky130-beta-multiplier-reference-pvt-mc.md)
