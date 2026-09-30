---
case_id: adb-v2-21
task_id: sky130-high-psrr-bandgap-reference-pvt
category: 偏置与基准
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-high-psrr-bandgap-reference-pvt/instruction.md
  - ../sources/upstream/tasks/sky130-high-psrr-bandgap-reference-pvt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-high-psrr-bandgap-reference-pvt/tests/verify.py
  - ../sources/upstream/tasks/sky130-high-psrr-bandgap-reference-pvt/results/reference.json
---

# 21 · 高 PSRR 带隙：低频环路与高频滤波各有作用

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

四个代表点，−40…85 °C 温度扫描，同时规定低频和 1 MHz 电源传递抑制。

## Reference 拓扑与尺寸线索（静态事实）

PNP 面积 36:1，物理电阻，级联/退化的 PMOS 偏置路径，以及输出 RC 滤波和补偿。

## 可复用的工程认识（推断，迁移时有条件）

低频电源抑制依赖偏置电流的供电敏感度、输出电阻和反馈；高频则还需要处理寄生前馈路径及滤波。结果若写供电增益 −57 dB，通常对应正定义 PSRR≈57 dB，不能把负值当失败方向。

## 不能由 pass 推出的结论

温漂参考约 47.63 ppm/°C，贴近 50 上限；没有完整噪声、失配、功耗验收。输出滤波提高 PSRR 并不自动保留负载阶跃性能。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-high-psrr-bandgap-reference-pvt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-high-psrr-bandgap-reference-pvt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-high-psrr-bandgap-reference-pvt)
- [Reference circuit](../sources/upstream/tasks/sky130-high-psrr-bandgap-reference-pvt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-high-psrr-bandgap-reference-pvt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-high-psrr-bandgap-reference-pvt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-high-psrr-bandgap-reference-pvt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-high-psrr-bandgap-reference-pvt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-high-psrr-bandgap-reference-pvt/circuit.spi) · [网站结果快照](../sources/astra/sky130-high-psrr-bandgap-reference-pvt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-high-psrr-bandgap-reference-pvt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-14T20:04:37+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `pvt_reference_voltage` | range=1.14539V at ss/1.7V/+85C .. 1.15289V at fs/1.7V/-40C (required 1.05..1.35V) |
| `pvt_temperature_drift` | worst=47.6307ppm/C at ff/1.9V/-40C (required <=50ppm/C) |
| `pvt_low_frequency_supply_gain` | worst=-57.2829dB at ff/1.9V/-40C (required <=-50dB); nominal=-69.5703dB (required <=-60dB) |
| `pvt_one_megahertz_supply_gain` | worst=-33.5361dB at fs/1.7V/-40C (required <=-30dB) |
| `pvt_startup_accuracy` | worst=0.0200749% at tt/1.8V/+27C (required <=1%) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/tb_bandgap_ac.spi](../sources/upstream/tasks/sky130-high-psrr-bandgap-reference-pvt/environment/starter/testbench/tb_bandgap_ac.spi) — ac
- [environment/starter/testbench/tb_bandgap_dc_temp.spi](../sources/upstream/tasks/sky130-high-psrr-bandgap-reference-pvt/environment/starter/testbench/tb_bandgap_dc_temp.spi) — dc
- [environment/starter/testbench/tb_bandgap_startup.spi](../sources/upstream/tasks/sky130-high-psrr-bandgap-reference-pvt/environment/starter/testbench/tb_bandgap_startup.spi) — op, tran
- [tests/benches/tb_bandgap_ac.spi](../sources/upstream/tasks/sky130-high-psrr-bandgap-reference-pvt/tests/benches/tb_bandgap_ac.spi) — ac
- [tests/benches/tb_bandgap_dc_temp.spi](../sources/upstream/tasks/sky130-high-psrr-bandgap-reference-pvt/tests/benches/tb_bandgap_dc_temp.spi) — dc
- [tests/benches/tb_bandgap_startup.spi](../sources/upstream/tasks/sky130-high-psrr-bandgap-reference-pvt/tests/benches/tb_bandgap_startup.spi) — tran

## 相邻案例

[11 带隙基准：温度补偿、启动和噪声是三件事](11-sky130-bandgap-reference-pvt.md) · [41 高 PSRR 中速 Miller：偏置供电路径决定抑制能力](41-sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt.md) · [47 PLL 电荷泵：静态匹配与短脉冲电荷是两套预算](47-sky130-pll-charge-pump-pvt.md)
