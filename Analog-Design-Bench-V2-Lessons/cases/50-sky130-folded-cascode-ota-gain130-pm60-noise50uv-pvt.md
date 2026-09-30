---
case_id: adb-v2-50
task_id: sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt
category: 放大器与滤波
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: true
derived_from:
  - ../sources/upstream/tasks/sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt/instruction.md
  - ../sources/upstream/tasks/sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt/tests/verify.py
  - ../sources/upstream/tasks/sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt/results/reference.json
---

# 50 · 130 dB 高速 OTA：局部增益增强环与外环必须分层分析

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

27 点 PVT，CL=1 pF，130 dB/200 MHz/60°，10 Hz–100 GHz 返回比只能一次下降穿越；固定 10 Hz–10 MHz 噪声、三个范围点和三个 last-entry 建立点。

## Reference 拓扑与尺寸线索（静态事实）

reference 是增益增强折叠级加第二级，NMOS/PMOS 局部辅助环、复制电平移位，局部约 3/9 pF 补偿，主环 1.37 pF/700 Ω。

## 可复用的工程认识（推断，迁移时有条件）

局部辅助放大器提高等效 ro，但新增极点/零点；应把局部环路稳定与整体跨频分开，不能用“总 DC 增益更高”掩盖再穿越。参考最小 UGB≈202.85 MHz、PM≈60.91°，迁移时寄生余量很小。

## 不能由 pass 推出的结论

Astra R1 用三级低频增益单元和 140 nF/1.4 nF/14 pF 前馈路径，满足拓扑中立的任务但没有面积/失配/PSRR 保证。必须按专文解释，不能直接称为可流片的低功耗替代。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt)
- [Reference circuit](../sources/upstream/tasks/sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt/circuit.spi) · [网站结果快照](../sources/astra/sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 已做定向电路比较，见 [Astra 对照](../topics/08-astra-comparisons.md)。

Reference 结果生成时间：`2026-08-15T18:00:00Z`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `complete_signoff` | rows=60/60; OP/AC=27/27 noise=27/27 range=3/3 settling=3/3 |
| `pvt_gain_bandwidth` | gain_min=132.90 dB; UGB_min=202.85 MHz |
| `pvt_phase_margin` | PM_min=60.91 deg; 27/27 single crossing with no recross |
| `pvt_input_noise` | max=46.60 uVrms (<= 50 uVrms) |
| `pvt_output_bias` | error_max=0.401 mV (<= 0.8 mV) |
| `pvt_power` | max=5.217 mW (<= 5.4 mW) |
| `closed_loop_range` | range_min=0.9363 Vpp; tracking_max=17.748 mV |
| `closed_loop_settling` | last_entry_max=6.975 ns; final error=0.4190 mV |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/public_checks.py](../sources/upstream/tasks/sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt/environment/starter/testbench/public_checks.py) — noise
- [environment/starter/testbench/tb_ac_ss.spi](../sources/upstream/tasks/sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt/environment/starter/testbench/tb_ac_ss.spi) — ac, op
- [environment/starter/testbench/tb_ac_tt.spi](../sources/upstream/tasks/sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt/environment/starter/testbench/tb_ac_tt.spi) — ac, op
- [environment/starter/testbench/tb_noise_tt.spi](../sources/upstream/tasks/sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt/environment/starter/testbench/tb_noise_tt.spi) — noise
- [environment/starter/testbench/tb_range_ss.spi](../sources/upstream/tasks/sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt/environment/starter/testbench/tb_range_ss.spi) — dc
- [environment/starter/testbench/tb_settling_ff.spi](../sources/upstream/tasks/sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt/environment/starter/testbench/tb_settling_ff.spi) — tran
- [tests/benches/tb_closed_loop_range.spi](../sources/upstream/tasks/sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt/tests/benches/tb_closed_loop_range.spi) — dc
- [tests/benches/tb_noise.spi](../sources/upstream/tasks/sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt/tests/benches/tb_noise.spi) — noise
- [tests/benches/tb_op_ac.spi](../sources/upstream/tasks/sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt/tests/benches/tb_op_ac.spi) — ac, op
- [tests/benches/tb_settling.spi](../sources/upstream/tasks/sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt/tests/benches/tb_settling.spi) — tran
- [tests/reviewer_benches/tb_gnc.spi](../sources/upstream/tasks/sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt/tests/reviewer_benches/tb_gnc.spi) — ac
- [tests/reviewer_benches/tb_gpc.spi](../sources/upstream/tasks/sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt/tests/reviewer_benches/tb_gpc.spi) — ac

## 相邻案例

[16 200 MHz 两级 Miller：快环路与宽带积分噪声的代价](16-sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt.md) · [35 全差分两级 Miller：高差模增益不能替代电源抑制](35-sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt.md) · [36 套筒 OTA：堆叠余量与共模感测极点](36-sky130-telescopic-cascode-ota-pvt-fix.md)
