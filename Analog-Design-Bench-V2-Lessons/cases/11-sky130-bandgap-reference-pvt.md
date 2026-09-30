---
case_id: adb-v2-11
task_id: sky130-bandgap-reference-pvt
category: 偏置与基准
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-bandgap-reference-pvt/instruction.md
  - ../sources/upstream/tasks/sky130-bandgap-reference-pvt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-bandgap-reference-pvt/tests/verify.py
  - ../sources/upstream/tasks/sky130-bandgap-reference-pvt/results/reference.json
---

# 11 · 带隙基准：温度补偿、启动和噪声是三件事

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

高阻输出、5 pF 负载；多种 MOS/无源角落组合共 81 个 DC 点，另查温漂、噪声、电源扰动、启动与 30 个固定失配样本。

## Reference 拓扑与尺寸线索（静态事实）

NPN 发射结面积 1:8，VBE 与 2·RREF/RPTAT·ΔVBE 加权；物理多晶电阻，PMOS 1:1:2 镜与误差放大器，启动支路在建立后关断。

## 可复用的工程认识（推断，迁移时有条件）

先让 ΔVBE/R 形成 PTAT 电流，再用电阻比抵消 VBE 温度斜率；电阻绝对值同时影响电流和功耗，电阻比影响目标电压/温漂。对自偏置系统必须单独检查供电斜坡和启动能量，不能凭 DC 解认定能从零电流状态启动。

## 不能由 pass 推出的结论

输出未证明能直接带 ADC 脉冲负载。九种角落组合是声明的组合，不是所有器件角落的任意笛卡尔积；有限温度采样、种子数限制了外推。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-bandgap-reference-pvt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-bandgap-reference-pvt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-bandgap-reference-pvt)
- [Reference circuit](../sources/upstream/tasks/sky130-bandgap-reference-pvt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-bandgap-reference-pvt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-bandgap-reference-pvt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-bandgap-reference-pvt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-bandgap-reference-pvt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-bandgap-reference-pvt/circuit.spi) · [网站结果快照](../sources/astra/sky130-bandgap-reference-pvt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-bandgap-reference-pvt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-13T10:33:27+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `complete_signoff` | runs=189 groups={'pvt_op': 81, 'line': 27, 'temperature': 54, 'startup': 18, 'ac': 15, 'noise': 3, 'line_step': 15, 'monte_carlo': 30} |
| `pvt_reference_voltage` | VREF=1.222638..1.233071V |
| `pvt_power` | power_max=114.489uW |
| `temperature_coefficient` | per_corner_ppm_per_C={'tt': 16.223531496050665, 'ff': 15.756738920875723, 'ss': 16.899628380657383, 'fs': 15.907865863574072, 'sf': 16.52182252495599, 'll': 15.957648571412095, 'hh': 18.199499266917986, 'hl': 18.199499266917986, 'lh': 15.957648571412095} max=18.199 |
| `line_regulation` | per_corner_mV_per_V={tt: 11.949, ff: 11.939, ss: 11.961, fs: 11.802, sf: 12.196, ll: 12.106, hh: 11.871, hl: 11.871, lh: 12.106} max=12.196 |
| `multi_ramp_startup_settling` | continuous_window=1.222822..1.230723V after entry; endpoints=1.222822..1.230723V/1.222854..1.230723V |
| `startup_overshoot` | overshoot_max=17.276mV |
| `startup_inrush_and_energy` | peak_supply_current=0.879mA energy=1.760nJ |
| `supply_rejection` | VDD_to_VREF_gain_max=0.149045V/V |
| `integrated_output_noise` | noise_10Hz_to_1MHz=299.064uVrms |
| `supply_step_response` | excursion_max=56.959mV settling_max=5.236us within 1mV |
| `monte_carlo_reference_accuracy` | runs=30 mean=1.225834V sigma=14.067mV yield=1.000 in 1.15..1.28V |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/check_tb_op_tt.py](../sources/upstream/tasks/sky130-bandgap-reference-pvt/environment/starter/testbench/check_tb_op_tt.py) — 夹具、模板或数据处理辅助
- [environment/starter/testbench/tb_dc_sweep_ff.spi](../sources/upstream/tasks/sky130-bandgap-reference-pvt/environment/starter/testbench/tb_dc_sweep_ff.spi) — dc
- [environment/starter/testbench/tb_line_step_ff.spi](../sources/upstream/tasks/sky130-bandgap-reference-pvt/environment/starter/testbench/tb_line_step_ff.spi) — tran
- [environment/starter/testbench/tb_mc_61000.spi](../sources/upstream/tasks/sky130-bandgap-reference-pvt/environment/starter/testbench/tb_mc_61000.spi) — op
- [environment/starter/testbench/tb_noise_tt.spi](../sources/upstream/tasks/sky130-bandgap-reference-pvt/environment/starter/testbench/tb_noise_tt.spi) — noise
- [environment/starter/testbench/tb_op_tt.spi](../sources/upstream/tasks/sky130-bandgap-reference-pvt/environment/starter/testbench/tb_op_tt.spi) — op
- [environment/starter/testbench/tb_psrr_ff_cold.spi](../sources/upstream/tasks/sky130-bandgap-reference-pvt/environment/starter/testbench/tb_psrr_ff_cold.spi) — ac
- [environment/starter/testbench/tb_startup_ff_10us.spi](../sources/upstream/tasks/sky130-bandgap-reference-pvt/environment/starter/testbench/tb_startup_ff_10us.spi) — tran
- [environment/starter/testbench/tb_startup_ss.spi](../sources/upstream/tasks/sky130-bandgap-reference-pvt/environment/starter/testbench/tb_startup_ss.spi) — tran
- [tests/benches/tb_ac.spi](../sources/upstream/tasks/sky130-bandgap-reference-pvt/tests/benches/tb_ac.spi) — ac
- [tests/benches/tb_line_step.spi](../sources/upstream/tasks/sky130-bandgap-reference-pvt/tests/benches/tb_line_step.spi) — tran
- [tests/benches/tb_mc.spi](../sources/upstream/tasks/sky130-bandgap-reference-pvt/tests/benches/tb_mc.spi) — op
- [tests/benches/tb_noise.spi](../sources/upstream/tasks/sky130-bandgap-reference-pvt/tests/benches/tb_noise.spi) — noise
- [tests/benches/tb_op.spi](../sources/upstream/tasks/sky130-bandgap-reference-pvt/tests/benches/tb_op.spi) — op
- [tests/benches/tb_startup.spi](../sources/upstream/tasks/sky130-bandgap-reference-pvt/tests/benches/tb_startup.spi) — tran

## 相邻案例

[12 β 倍增偏置：恒 gm 条件来自器件比和电阻](12-sky130-beta-multiplier-reference-pvt-mc.md) · [21 高 PSRR 带隙：低频环路与高频滤波各有作用](21-sky130-high-psrr-bandgap-reference-pvt.md) · [38 20 mA 无外部电容 LDO：片上储能仍可很大](38-sky130-capless-ldo-1v0-20ma-pvt.md)
