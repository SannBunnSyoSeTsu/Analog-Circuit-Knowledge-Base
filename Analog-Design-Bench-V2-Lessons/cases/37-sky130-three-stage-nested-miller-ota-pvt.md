---
case_id: adb-v2-37
task_id: sky130-three-stage-nested-miller-ota-pvt
category: 放大器与滤波
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-three-stage-nested-miller-ota-pvt/instruction.md
  - ../sources/upstream/tasks/sky130-three-stage-nested-miller-ota-pvt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-three-stage-nested-miller-ota-pvt/tests/verify.py
  - ../sources/upstream/tasks/sky130-three-stage-nested-miller-ota-pvt/results/reference.json
---

# 37 · 三级 Nested Miller：增益乘积与速度预算要分开

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

45 点 PVT，CL=200 pF，增益≥110 dB、UGB≥0.4 MHz、PM≥70°、功耗≤300 µW，以及带宽-负载/功率 FOM、摆幅、压摆和建立。

## Reference 拓扑与尺寸线索（静态事实）

NMOS 差分镜像第一级、非反相镜像第二级、共源输出第三级；外层约 6 pF，内层约 3 pF 补偿。

## 可复用的工程认识（推断，迁移时有条件）

三级提供增益乘积，却增加内部模态；必须先标出每级反相关系，才能判断内外补偿形成的反馈符号。200 pF 大负载使输出电流/压摆率成为独立限制。FOM=UGB·CL/P 是任务定义的比较量，不代替噪声或面积预算。

## 不能由 pass 推出的结论

reference 建立约 2.61 µs，适用本题小带宽大负载条件，不能迁移到高速采样放大器。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-three-stage-nested-miller-ota-pvt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-three-stage-nested-miller-ota-pvt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-three-stage-nested-miller-ota-pvt)
- [Reference circuit](../sources/upstream/tasks/sky130-three-stage-nested-miller-ota-pvt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-three-stage-nested-miller-ota-pvt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-three-stage-nested-miller-ota-pvt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-three-stage-nested-miller-ota-pvt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-three-stage-nested-miller-ota-pvt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-three-stage-nested-miller-ota-pvt/circuit.spi) · [网站结果快照](../sources/astra/sky130-three-stage-nested-miller-ota-pvt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-three-stage-nested-miller-ota-pvt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-14T20:10:58+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `nominal_functional` | gain=124.23dB UGB=0.555MHz PM=79.99deg settling=2.237us |
| `complete_signoff` | 225 rows, five exact 45-point matrices |
| `pvt_gain` | gain_min=114.24dB |
| `pvt_large_load_drive` | UGB_min=0.446MHz drive_FOM_min=356.9kHz*pF/uW |
| `pvt_phase_margin` | PM_min=78.49deg |
| `pvt_output_bias` | output_error_max=4.73mV |
| `pvt_power` | power_max=253.1uW |
| `pvt_input_bias` | input_bias_max=0.00nA |
| `closed_loop_range` | range_min=0.870Vpp |
| `closed_loop_settling` | settling_max=2.61us final_error_max=0.946% |
| `slew_rate` | rise_min=0.236 fall_min=0.224V/us |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/measure.py](../sources/upstream/tasks/sky130-three-stage-nested-miller-ota-pvt/environment/starter/testbench/measure.py) — ac, dc
- [environment/starter/testbench/tb_ac_ss.spi](../sources/upstream/tasks/sky130-three-stage-nested-miller-ota-pvt/environment/starter/testbench/tb_ac_ss.spi) — ac, op
- [environment/starter/testbench/tb_ac_tt.spi](../sources/upstream/tasks/sky130-three-stage-nested-miller-ota-pvt/environment/starter/testbench/tb_ac_tt.spi) — ac, op
- [environment/starter/testbench/tb_input_bias_tt.spi](../sources/upstream/tasks/sky130-three-stage-nested-miller-ota-pvt/environment/starter/testbench/tb_input_bias_tt.spi) — op
- [environment/starter/testbench/tb_settling_ss.spi](../sources/upstream/tasks/sky130-three-stage-nested-miller-ota-pvt/environment/starter/testbench/tb_settling_ss.spi) — tran
- [environment/starter/testbench/tb_slew_ff.spi](../sources/upstream/tasks/sky130-three-stage-nested-miller-ota-pvt/environment/starter/testbench/tb_slew_ff.spi) — tran
- [environment/starter/testbench/tb_swing_fs.spi](../sources/upstream/tasks/sky130-three-stage-nested-miller-ota-pvt/environment/starter/testbench/tb_swing_fs.spi) — dc
- [tests/benches/tb_input_bias.spi](../sources/upstream/tasks/sky130-three-stage-nested-miller-ota-pvt/tests/benches/tb_input_bias.spi) — op
- [tests/benches/tb_pvt.spi](../sources/upstream/tasks/sky130-three-stage-nested-miller-ota-pvt/tests/benches/tb_pvt.spi) — ac, op
- [tests/benches/tb_settling.spi](../sources/upstream/tasks/sky130-three-stage-nested-miller-ota-pvt/tests/benches/tb_settling.spi) — tran
- [tests/benches/tb_slew.spi](../sources/upstream/tasks/sky130-three-stage-nested-miller-ota-pvt/tests/benches/tb_slew.spi) — tran
- [tests/benches/tb_swing.spi](../sources/upstream/tasks/sky130-three-stage-nested-miller-ota-pvt/tests/benches/tb_swing.spi) — dc

## 相邻案例

[16 200 MHz 两级 Miller：快环路与宽带积分噪声的代价](16-sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt.md) · [29 Ahuja 补偿：补偿接入点的阻抗决定物理作用](29-sky130-ahuja-compensated-two-stage-load-range-pvt.md) · [41 高 PSRR 中速 Miller：偏置供电路径决定抑制能力](41-sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt.md)
