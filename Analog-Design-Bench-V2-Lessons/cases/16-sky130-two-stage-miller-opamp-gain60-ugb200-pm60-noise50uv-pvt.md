---
case_id: adb-v2-16
task_id: sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt
category: 放大器与滤波
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt/instruction.md
  - ../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt/tests/verify.py
  - ../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt/results/reference.json
---

# 16 · 200 MHz 两级 Miller：快环路与宽带积分噪声的代价

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

27 点 PVT，CL=1 pF，增益≥60 dB、UGB≥200 MHz、PM≥60°。输入噪声按噪声增益 20 的闭环带宽积分，不是固定 10 MHz 上限。

## Reference 拓扑与尺寸线索（静态事实）

NMOS 输入对配 PMOS 镜负载、NMOS 第二级，Cc=0.45 pF、串联 Rc=1.8 kΩ。

## 可复用的工程认识（推断，迁移时有条件）

Cc 决定主极点与环路跨频，串联电阻用于控制补偿零点；第二级 gm 与输出负载决定非主极点。不能只减小 Cc 抬 UGB，必须同时留 PM、噪声和压摆率余量。与任务 41 对照时，先对齐噪声积分带宽和 PSRR 要求。

## 不能由 pass 推出的结论

本题低频 PSRR 门槛比任务 41 宽松。相同“50 µVrms”文字可能代表不同积分带宽，不能按数字直接排名。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt)
- [Reference circuit](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt/circuit.spi) · [网站结果快照](../sources/astra/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-14T20:03:33+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `nominal_functional` | gain=76.31dB UGB=294.68MHz PM=70.34deg |
| `pvt_gain_bandwidth` | worst=72.71dB at ff/1.62V/+125C (min 60dB); worst=213.4MHz at ss/1.62V/+125C (min 200MHz) |
| `pvt_phase_margin` | worst=63.72deg at ss/1.80V/-40C (min 60deg) |
| `pvt_output_bias` | worst=3.723mV at ss/1.62V/-40C (max 25mV) |
| `pvt_power` | worst=1861uW at ff/1.98V/+125C (max 2000uW) |
| `pvt_input_noise` | worst=47.75uVrms integrated 10Hz-14.94MHz at ss/1.98V/+125C (max 50uVrms) |
| `pvt_supply_rejection` | worst=39.2dB at ss/1.62V/+125C (min 35dB); worst=39.19dB at ss/1.62V/+125C (min 35dB) |
| `pvt_common_mode_rejection` | worst=58.09dB at ss/1.62V/+125C (min 55dB) |
| `closed_loop_range` | worst=0.9739Vpp at ss/1.62V/+125C (min 0.8Vpp) |
| `closed_loop_settling` | time_max=5.467ns at ss/1.62V/+125C (max 20ns); final_max=1.031% at ss/1.62V/+125C; static_max=1.031mV at ss/1.62V/+125C |
| `slew_rate` | worst=223.8V/us at ss/1.62V/+125C (min 50V/us); worst=387.6V/us at ff/1.98V/-40C (min 50V/us) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/tb_ac_ss.spi](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt/environment/starter/testbench/tb_ac_ss.spi) — ac, op
- [environment/starter/testbench/tb_ac_tt.spi](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt/environment/starter/testbench/tb_ac_tt.spi) — ac, op
- [environment/starter/testbench/tb_cmrr_tt.spi](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt/environment/starter/testbench/tb_cmrr_tt.spi) — ac
- [environment/starter/testbench/tb_noise_tt.spi](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt/environment/starter/testbench/tb_noise_tt.spi) — ac, noise
- [environment/starter/testbench/tb_psrr_tt.spi](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt/environment/starter/testbench/tb_psrr_tt.spi) — ac
- [environment/starter/testbench/tb_settling_tt.spi](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt/environment/starter/testbench/tb_settling_tt.spi) — tran
- [environment/starter/testbench/tb_slew_tt.spi](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt/environment/starter/testbench/tb_slew_tt.spi) — tran
- [environment/starter/testbench/tb_swing_tt.spi](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt/environment/starter/testbench/tb_swing_tt.spi) — dc
- [tests/benches/tb_cmrr.spi](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt/tests/benches/tb_cmrr.spi) — ac
- [tests/benches/tb_noise.spi](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt/tests/benches/tb_noise.spi) — ac, noise
- [tests/benches/tb_op_ac.spi](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt/tests/benches/tb_op_ac.spi) — ac, op
- [tests/benches/tb_psrr.spi](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt/tests/benches/tb_psrr.spi) — ac
- [tests/benches/tb_settling.spi](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt/tests/benches/tb_settling.spi) — tran
- [tests/benches/tb_slew.spi](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt/tests/benches/tb_slew.spi) — tran
- [tests/benches/tb_swing.spi](../sources/upstream/tasks/sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt/tests/benches/tb_swing.spi) — dc

## 相邻案例

[41 高 PSRR 中速 Miller：偏置供电路径决定抑制能力](41-sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt.md) · [44 5T OTA：最小拓扑也需要闭环噪声和环路定义](44-sky130-ota-5t-gain40-pm60-noise50uv-pvt.md) · [50 130 dB 高速 OTA：局部增益增强环与外环必须分层分析](50-sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt.md)
