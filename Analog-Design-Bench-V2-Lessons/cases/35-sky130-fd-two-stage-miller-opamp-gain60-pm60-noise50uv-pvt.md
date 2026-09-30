---
case_id: adb-v2-35
task_id: sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt
category: 放大器与滤波
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt/instruction.md
  - ../sources/upstream/tasks/sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt/tests/verify.py
  - ../sources/upstream/tasks/sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt/results/reference.json
---

# 35 · 全差分两级 Miller：高差模增益不能替代电源抑制

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

27 点 PVT，UGB≥100 MHz，输入噪声固定 10 Hz–15 MHz；另有 20 个失配样本下 10 Hz CMRR/PSRR 及共模动态恢复。

## Reference 拓扑与尺寸线索（静态事实）

第一级负载/尾源延长沟道并匹配复制偏置，第二级电流比约 16；CMFB 的尺寸与电流同步放大，补偿 600 Ω/1.2 pF。

## 可复用的工程认识（推断，迁移时有条件）

长沟道能提升 ro 与 DC 增益，但电源扰动还会沿偏置、负载和共模环路传播。CMFB 增强要配合它驱动的栅电容，不能只增加感测放大器 gm。检查差模 CMRR 和共模阶跃恢复，得到的是不同方向的系统行为。

## 不能由 pass 推出的结论

reference 增益约 101.5 dB 很高，但功耗约 4.932 mW 接近 5 mW，PSRR 约 40.38 dB 接近 40 dB；不能把 DC 增益富余当所有指标都有余量。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt)
- [Reference circuit](../sources/upstream/tasks/sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt/circuit.spi) · [网站结果快照](../sources/astra/sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-14T20:08:39+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `pvt_gain` | worst=101.5dB at ss/1.62V/+125C (min 60dB) |
| `pvt_bandwidth` | worst=151.2MHz at ss/1.62V/+125C (min 100MHz) |
| `pvt_phase_margin` | worst=65.85deg at ss/1.62V/-40C (min 60deg) |
| `pvt_input_noise` | worst=44.14uVrms at ss/1.62V/+125C (max 50uVrms) |
| `pvt_output_bias` | worst=6.597mV at ff/1.98V/+125C (max 15mV); worst=9.375e-05mV at tt/1.98V/-40C (max 0.1mV) |
| `pvt_power` | worst=4.932mW at ff/1.98V/+125C (max 5mW) |
| `common_mode_rejection` | worst=55.9dB at tt/1.80V/+27C/seed-41002 (min 50dB) |
| `supply_rejection` | worst=40.38dB at tt/1.80V/+27C/seed-41002 (min 40dB); worst=40.38dB at tt/1.80V/+27C/seed-41002 (min 40dB) |
| `closed_loop_range` | worst=1.6Vpp at tt/1.80V/+27C (min 0.8Vpp); worst=0.007558mV at ss/1.62V/+125C (max 5mV) |
| `precision_settling` | worst=11.78ns at ss/1.62V/+125C (max 15ns); worst=0.00085% at ss/1.62V/+125C (max 1%) |
| `common_mode_recovery` | worst=30.12ns at ss/1.62V/+125C (max 100ns); worst=3.902mV at ff/1.98V/-40C (max 10mV) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/tb_ac_ss.spi](../sources/upstream/tasks/sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt/environment/starter/testbench/tb_ac_ss.spi) — ac, op
- [environment/starter/testbench/tb_ac_tt.spi](../sources/upstream/tasks/sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt/environment/starter/testbench/tb_ac_tt.spi) — ac, op
- [environment/starter/testbench/tb_cm_recovery_ff.spi](../sources/upstream/tasks/sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt/environment/starter/testbench/tb_cm_recovery_ff.spi) — tran
- [environment/starter/testbench/tb_mismatch_tt.spi](../sources/upstream/tasks/sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt/environment/starter/testbench/tb_mismatch_tt.spi) — ac
- [environment/starter/testbench/tb_noise_ff.spi](../sources/upstream/tasks/sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt/environment/starter/testbench/tb_noise_ff.spi) — noise
- [environment/starter/testbench/tb_settling_ss.spi](../sources/upstream/tasks/sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt/environment/starter/testbench/tb_settling_ss.spi) — tran
- [environment/starter/testbench/tb_swing_tt.spi](../sources/upstream/tasks/sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt/environment/starter/testbench/tb_swing_tt.spi) — dc
- [tests/benches/tb_cm_recovery.spi](../sources/upstream/tasks/sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt/tests/benches/tb_cm_recovery.spi) — tran
- [tests/benches/tb_mc.spi](../sources/upstream/tasks/sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt/tests/benches/tb_mc.spi) — ac
- [tests/benches/tb_noise.spi](../sources/upstream/tasks/sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt/tests/benches/tb_noise.spi) — noise
- [tests/benches/tb_op_ac.spi](../sources/upstream/tasks/sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt/tests/benches/tb_op_ac.spi) — ac, op
- [tests/benches/tb_settling.spi](../sources/upstream/tasks/sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt/tests/benches/tb_settling.spi) — tran
- [tests/benches/tb_swing.spi](../sources/upstream/tasks/sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt/tests/benches/tb_swing.spi) — dc

## 相邻案例

[26 OTA-C 双二阶滤波器：状态节点的共模预算不能合并](26-sky130-fully-differential-ota-c-biquad-pvt.md) · [33 增益 1 采样反馈 OTA：差模建立和 CMFB 要分开验收](33-sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc.md) · [34 增益 8 采样反馈 OTA：β=1/9 决定环路速度](34-sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc.md)
