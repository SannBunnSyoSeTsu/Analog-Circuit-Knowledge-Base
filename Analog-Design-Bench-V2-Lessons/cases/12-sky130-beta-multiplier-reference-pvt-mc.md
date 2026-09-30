---
case_id: adb-v2-12
task_id: sky130-beta-multiplier-reference-pvt-mc
category: 偏置与基准
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-beta-multiplier-reference-pvt-mc/instruction.md
  - ../sources/upstream/tasks/sky130-beta-multiplier-reference-pvt-mc/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-beta-multiplier-reference-pvt-mc/tests/verify.py
  - ../sources/upstream/tasks/sky130-beta-multiplier-reference-pvt-mc/results/reference.json
---

# 12 · β 倍增偏置：恒 gm 条件来自器件比和电阻

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

27 个 PVT 点，输出电流窗口、参考电压、输出顺从性与功耗；18 种供电斜坡及 50 个固定组合随机样本。输出测试电压也参与供能边界。

## Reference 拓扑与尺寸线索（静态事实）

NMOS 宽比 K=4、L=4 µm，PMOS 镜 L=2 µm，物理电阻建立电流，输出镜取更长 L=8 µm；弱启动支路在工作后关闭。

## 可复用的工程认识（推断，迁移时有条件）

忽略体效应、沟道长度调制并采用平方律时，gm,small=2(1−1/√K)/R；K=4 时约为 1/R。实际迁移必须检查体端、镜像 VDS 和工作区，不能把该关系当 PDK 全区间恒等式。自偏置的零电流平衡点与有效工作点都要在拓扑分析中明确。

## 不能由 pass 推出的结论

发布结果支持指定种子和斜坡；不构成任意电源时序下的启动证明。电阻实例的几何长度不是阻值，不能把 l=42.5 读成 42.5 Ω。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-beta-multiplier-reference-pvt-mc/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-beta-multiplier-reference-pvt-mc/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-beta-multiplier-reference-pvt-mc)
- [Reference circuit](../sources/upstream/tasks/sky130-beta-multiplier-reference-pvt-mc/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-beta-multiplier-reference-pvt-mc/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-beta-multiplier-reference-pvt-mc/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-beta-multiplier-reference-pvt-mc/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-beta-multiplier-reference-pvt-mc/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-beta-multiplier-reference-pvt-mc/circuit.spi) · [网站结果快照](../sources/astra/sky130-beta-multiplier-reference-pvt-mc/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-beta-multiplier-reference-pvt-mc/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-13T10:32:46+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `complete_signoff` | runs=95 PVT=27/27 compliance=27/27 startup=18/18 MC=50/50 |
| `pvt_output_current` | current=29.148..44.972uA |
| `nominal_current_accuracy` | TT/1.8V/27C current=36.109uA |
| `pvt_vref` | VREF=0.6334..0.7101V |
| `pvt_power` | power_max=64.97uW |
| `pvt_output_compliance` | current=28.477..45.679uA flatness_max=5.343% |
| `pvt_multi_ramp_startup_final` | final_current=30.267..43.892uA VREF=0.6334..0.7101V |
| `pvt_multi_ramp_startup_settling` | settling_time_max=5.812us |
| `startup_overshoot` | peak_to_final_current_ratio_max=1.2781 |
| `startup_inrush_and_energy` | peak_supply_current=0.012mA energy=0.180nJ |
| `mc_current_yield` | samples=50 yield=100.0% in 30..50uA |
| `mc_current_sigma` | samples=50 sigma=1.048uA |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/run_mc.py](../sources/upstream/tasks/sky130-beta-multiplier-reference-pvt-mc/environment/starter/testbench/run_mc.py) — 夹具、模板或数据处理辅助
- [environment/starter/testbench/sky130_mc_mm.lib.spice](../sources/upstream/tasks/sky130-beta-multiplier-reference-pvt-mc/environment/starter/testbench/sky130_mc_mm.lib.spice) — 夹具、模板或数据处理辅助
- [environment/starter/testbench/tb_compliance_ss.spi](../sources/upstream/tasks/sky130-beta-multiplier-reference-pvt-mc/environment/starter/testbench/tb_compliance_ss.spi) — dc
- [environment/starter/testbench/tb_mc.spi](../sources/upstream/tasks/sky130-beta-multiplier-reference-pvt-mc/environment/starter/testbench/tb_mc.spi) — op
- [environment/starter/testbench/tb_op_tt.spi](../sources/upstream/tasks/sky130-beta-multiplier-reference-pvt-mc/environment/starter/testbench/tb_op_tt.spi) — op
- [environment/starter/testbench/tb_startup_ff.spi](../sources/upstream/tasks/sky130-beta-multiplier-reference-pvt-mc/environment/starter/testbench/tb_startup_ff.spi) — tran
- [tests/benches/tb_compliance.spi](../sources/upstream/tasks/sky130-beta-multiplier-reference-pvt-mc/tests/benches/tb_compliance.spi) — dc
- [tests/benches/tb_mc.spi](../sources/upstream/tasks/sky130-beta-multiplier-reference-pvt-mc/tests/benches/tb_mc.spi) — op
- [tests/benches/tb_startup.spi](../sources/upstream/tasks/sky130-beta-multiplier-reference-pvt-mc/tests/benches/tb_startup.spi) — tran

## 相邻案例

[02 可编程 ICC/IPTAT 镜：比例正确还不够](02-sky130-programmable-icc-iptat-current-mirror-pvt.md) · [11 带隙基准：温度补偿、启动和噪声是三件事](11-sky130-bandgap-reference-pvt.md) · [13 恒 gm 稳增益：偏置单元必须映射到输入电流密度](13-sky130-constant-gm-stable-gain-amplifier-pvt.md)
