---
case_id: adb-v2-41
task_id: sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt
category: 放大器与滤波
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt/instruction.md
  - ../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt/tests/verify.py
  - ../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt/results/reference.json
---

# 41 · 高 PSRR 中速 Miller：偏置供电路径决定抑制能力

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

27 点 PVT，CL=2 pF，增益≥70 dB、UGB≥20 MHz、PM≥60°、功耗≤600 µW；要求高低频 PSRR，噪声积分上限随 NG20 闭环带宽。

## Reference 拓扑与尺寸线索（静态事实）

NMOS 差分输入和宽摆幅级联 PMOS 镜，PMOS 第二级搭 NMOS 电流源；700 Ω/2 pF Miller 补偿。

## 可复用的工程认识（推断，迁移时有条件）

与任务 16 对照，可见较低跨频目标给偏置隔离、输出电阻和补偿更多空间。改变第二级极性后，供电前馈与偏置噪声路径也改变；不能从差模增益推断 PSRR。尺寸复用前先重画电源到输出的小信号路径。

## 不能由 pass 推出的结论

参考噪声积分带宽约 1.693 MHz，远小于任务 16 的对应带宽；同为 50 µV 上限并不代表同等噪声密度。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt)
- [Reference circuit](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt/circuit.spi) · [网站结果快照](../sources/astra/sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-14T20:10:37+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `nominal_functional` | gain=76.60dB UGB=38.14MHz PM=73.68deg |
| `pvt_gain_bandwidth` | worst=73.63dB at ff/1.62V/-40C (min 70dB); worst=31.3MHz at ss/1.62V/+125C (min 20MHz) |
| `pvt_phase_margin` | worst=70.68deg at ss/1.80V/+125C (min 60deg) |
| `pvt_output_bias` | worst=0.04558mV at ss/1.62V/-40C (max 25mV) |
| `pvt_power` | worst=517.4uW at ff/1.98V/+125C (max 600uW) |
| `pvt_input_noise` | worst=46.27uVrms integrated 10Hz-1.693MHz at ss/1.98V/+125C (max 50uVrms) |
| `pvt_supply_rejection` | worst=75.4dB at ss/1.62V/+125C (min 65dB); worst=30.44dB at ss/1.62V/+125C (min 20dB) |
| `pvt_common_mode_rejection` | worst=77.61dB at ss/1.62V/+125C (min 60dB) |
| `closed_loop_range` | worst=1.193Vpp at ss/1.62V/+125C (min 0.8Vpp) |
| `closed_loop_settling` | time_max=17.24ns at ss/1.62V/+125C (max 30ns); final_max=0.0364% at ss/1.62V/+125C; static_max=0.0364mV at ss/1.62V/+125C |
| `slew_rate` | worst=27.66V/us at ss/1.62V/+125C (min 10V/us); worst=24.85V/us at ff/1.98V/-40C (min 10V/us) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/tb_cmrr_tt_1p80v_28c.spi](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt/environment/starter/testbench/tb_cmrr_tt_1p80v_28c.spi) — ac
- [environment/starter/testbench/tb_noise_tt_1p80v_28c.spi](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt/environment/starter/testbench/tb_noise_tt_1p80v_28c.spi) — ac, noise
- [environment/starter/testbench/tb_op_ac_tt_1p80v_28c.spi](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt/environment/starter/testbench/tb_op_ac_tt_1p80v_28c.spi) — ac, op
- [environment/starter/testbench/tb_psrr_tt_1p80v_28c.spi](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt/environment/starter/testbench/tb_psrr_tt_1p80v_28c.spi) — ac
- [environment/starter/testbench/tb_settling_ss_1p80v_27c.spi](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt/environment/starter/testbench/tb_settling_ss_1p80v_27c.spi) — tran
- [environment/starter/testbench/tb_slew_tt_1p98v_m40c.spi](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt/environment/starter/testbench/tb_slew_tt_1p98v_m40c.spi) — tran
- [environment/starter/testbench/tb_swing_ff_1p62v_125c.spi](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt/environment/starter/testbench/tb_swing_ff_1p62v_125c.spi) — dc
- [tests/benches/tb_cmrr.spi](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt/tests/benches/tb_cmrr.spi) — ac
- [tests/benches/tb_noise.spi](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt/tests/benches/tb_noise.spi) — ac, noise
- [tests/benches/tb_op_ac.spi](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt/tests/benches/tb_op_ac.spi) — ac, op
- [tests/benches/tb_psrr.spi](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt/tests/benches/tb_psrr.spi) — ac
- [tests/benches/tb_settling.spi](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt/tests/benches/tb_settling.spi) — tran
- [tests/benches/tb_slew.spi](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt/tests/benches/tb_slew.spi) — tran
- [tests/benches/tb_swing.spi](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt/tests/benches/tb_swing.spi) — dc

## 相邻案例

[16 200 MHz 两级 Miller：快环路与宽带积分噪声的代价](16-sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt.md) · [21 高 PSRR 带隙：低频环路与高频滤波各有作用](21-sky130-high-psrr-bandgap-reference-pvt.md) · [37 三级 Nested Miller：增益乘积与速度预算要分开](37-sky130-three-stage-nested-miller-ota-pvt.md)
