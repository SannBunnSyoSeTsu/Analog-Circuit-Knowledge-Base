---
case_id: adb-v2-38
task_id: sky130-capless-ldo-1v0-20ma-pvt
category: 电源与驱动
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: true
derived_from:
  - ../sources/upstream/tasks/sky130-capless-ldo-1v0-20ma-pvt/instruction.md
  - ../sources/upstream/tasks/sky130-capless-ldo-1v0-20ma-pvt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-capless-ldo-1v0-20ma-pvt/tests/verify.py
  - ../sources/upstream/tasks/sky130-capless-ldo-1v0-20ma-pvt/results/reference.json
---

# 38 · 20 mA 无外部电容 LDO：片上储能仍可很大

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

目标 1.0 V、0–20 mA DC、0.5–20 mA 动态；30 点 PVT，理想内部电容合计预算 1 nF，参考源由外部理想提供。

## Reference 拓扑与尺寸线索（静态事实）

reference 的 PMOS pass 约 3000 µm，PMOS LVT 输入误差放大器，自偏置/启动，30k/20k 分压；输出 850 pF 配 150 Ω 阻尼另加 120 pF 直连，补偿等总计约 977 pF。

## 可复用的工程认识（推断，迁移时有条件）

“capless”在这里表示没有外部输出电容，不表示内部没有大储能。输出阻尼、反馈前馈与 pass 栅极驱动一起决定负载瞬态。应把 Iq 的稳态节省和阶跃时为大栅充放电的能力分开评估。

## 不能由 pass 推出的结论

没有直接 PM 分数；动态不包含真正 0 mA→20 mA 全跨度，VREF 的成本未计入。接近 1 nF 的内部理想电容也没有面积/寄生验证。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-capless-ldo-1v0-20ma-pvt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-capless-ldo-1v0-20ma-pvt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-capless-ldo-1v0-20ma-pvt)
- [Reference circuit](../sources/upstream/tasks/sky130-capless-ldo-1v0-20ma-pvt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-capless-ldo-1v0-20ma-pvt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-capless-ldo-1v0-20ma-pvt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-capless-ldo-1v0-20ma-pvt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-capless-ldo-1v0-20ma-pvt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-capless-ldo-1v0-20ma-pvt/circuit.spi) · [网站结果快照](../sources/astra/sky130-capless-ldo-1v0-20ma-pvt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-capless-ldo-1v0-20ma-pvt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 已做定向电路比较，见 [Astra 对照](../topics/08-astra-comparisons.md)。

Reference 结果生成时间：`2026-08-14T20:09:21+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `dc_regulation` | worst \|vout-1.0V\| over the 0-20mA DC sweep = 25.97mV at fs/1.5V/+85C/vmin_v (max 30mV) |
| `quiescent_current` | worst no-load VIN current = 92.51uA at fs/1.8V/+85C (max 100uA; ideal VREF current is free) |
| `psr_1khz` | 1kHz 1.5V: worst 34.32dB at sf/27C/1.5V (min 30dB); 1.8V: worst 40.86dB at fs/27C/1.8V (min 35dB) |
| `psr_100khz` | 100kHz: worst 28.44dB at fs/27C/1.5V (min 20dB) |
| `psr_1mhz` | 1MHz: worst 11.82dB at fs/27C/1.5V (min 10dB) |
| `load_step_excursion` | worst excursion from 1.0V = 130.7mV at fs/1.5V/+85C/droop_v (max 150mV) |
| `load_step_recovery` | worst tail-window deviation from 1.0V = 25.97mV at fs/1.5V/+85C/t1max_v (max 30mV, windows begin 20us after each edge completes) |
| `startup` | worst peak = 1.002V at ss/1.5V/+85C (max 1.05V); worst 200-400us deviation = 3.655mV at sf/1.5V/-40C (max 20mV) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/tb_dc_tt.spi](../sources/upstream/tasks/sky130-capless-ldo-1v0-20ma-pvt/environment/starter/testbench/tb_dc_tt.spi) — dc, op
- [environment/starter/testbench/tb_psr_tt.spi](../sources/upstream/tasks/sky130-capless-ldo-1v0-20ma-pvt/environment/starter/testbench/tb_psr_tt.spi) — ac
- [environment/starter/testbench/tb_start_tt.spi](../sources/upstream/tasks/sky130-capless-ldo-1v0-20ma-pvt/environment/starter/testbench/tb_start_tt.spi) — tran
- [environment/starter/testbench/tb_step_tt.spi](../sources/upstream/tasks/sky130-capless-ldo-1v0-20ma-pvt/environment/starter/testbench/tb_step_tt.spi) — tran
- [tests/benches/tb_matrix.spi](../sources/upstream/tasks/sky130-capless-ldo-1v0-20ma-pvt/tests/benches/tb_matrix.spi) — dc, op
- [tests/benches/tb_psr.spi](../sources/upstream/tasks/sky130-capless-ldo-1v0-20ma-pvt/tests/benches/tb_psr.spi) — ac
- [tests/benches/tb_start.spi](../sources/upstream/tasks/sky130-capless-ldo-1v0-20ma-pvt/tests/benches/tb_start.spi) — tran
- [tests/benches/tb_step.spi](../sources/upstream/tasks/sky130-capless-ldo-1v0-20ma-pvt/tests/benches/tb_step.spi) — tran

## 相邻案例

[07 5T 误差放大器 LDO：负载电容和 ESR 是环路参数](07-sky130-ldo-ota5-robust-pvt-mc.md) · [17 0.4 V NMOS LDO：低输出电压改变输入级和驱动极性](17-sky130-nmos-pass-ldo-0p4v-pvt-mc.md) · [18 受控升压泵：先确定控制变量和关断边界](18-sky130-regulated-charge-pump-10mhz-pvt.md)
