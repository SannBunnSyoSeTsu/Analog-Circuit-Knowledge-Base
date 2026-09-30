---
case_id: adb-v2-46
task_id: sky130-flash-adc-3bit-pvt
category: 采样与数据转换
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-flash-adc-3bit-pvt/instruction.md
  - ../sources/upstream/tasks/sky130-flash-adc-3bit-pvt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-flash-adc-3bit-pvt/tests/verify.py
  - ../sources/upstream/tasks/sky130-flash-adc-3bit-pvt/results/reference.json
---

# 46 · 3 bit Flash：阈值绝对位置与编码尾部延迟都要检查

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

0.6–1.4 V 量程、0.1 V/LSB；三个静态代表点、两个 16 样本 FFT 点、三个动态点。时钟到稳定码≤9.5 ns，并检查后续保持。

## Reference 拓扑与尺寸线索（静态事实）

七个 StrongARM 与 SR 保持、8×500 Ω 电阻梯和 300 fF 阈值滤波，温度码转二进制逻辑。

## 可复用的工程认识（推断，迁移时有条件）

端点拟合 INL 可以掩盖全量程平移，必须同时限制绝对阈值偏差。转换延迟应计到比较器、锁存与编码链最后一次越阈值，不是只量比较器第一跳。动态波形避开阈值的策略也属于测量定义。

## 不能由 pass 推出的结论

输入为零输出阻抗理想源，可能钳住 kickback；不能据此认定真实前端容易驱动。FFT 点少且无失配统计，不支持亚稳态失败率结论。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-flash-adc-3bit-pvt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-flash-adc-3bit-pvt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-flash-adc-3bit-pvt)
- [Reference circuit](../sources/upstream/tasks/sky130-flash-adc-3bit-pvt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-flash-adc-3bit-pvt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-flash-adc-3bit-pvt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-flash-adc-3bit-pvt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-flash-adc-3bit-pvt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-flash-adc-3bit-pvt/circuit.spi) · [网站结果快照](../sources/astra/sky130-flash-adc-3bit-pvt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-flash-adc-3bit-pvt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-15T18:00:00Z`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `valid_output_levels` | all sampled outputs were finite, rail-valid, and stable in the published window |
| `pvt_code_progression` | 8/8 codes and 7/7 thresholds passed |
| `pvt_dnl` | worst=0.100 LSB (<= 0.30) |
| `pvt_inl` | worst=0.120 LSB (<= 0.30) |
| `pvt_absolute_threshold_error` | worst=0.200 LSB (<= 0.30) |
| `hidden_transition_sequence` | code_errors=0; missing_expected_transitions=0; stable_level_violations=0 |
| `pvt_clock_to_output_delay` | last_crossing=1.752 ns; late_crossings=0 (<= 9.5 ns) |
| `pvt_core_reference_power` | worst=0.476 mW (<= 1.0 mW) |
| `pvt_clock_delivery_power` | worst=0.070 mW (<= 0.25 mW) |
| `low_frequency_sndr` | SNDR=18.458 dB (>= 17.0 dB) |
| `high_frequency_sndr` | SNDR=22.415 dB (>= 17.0 dB) |
| `dynamic_sfdr` | worst=22.012 dB (>= 21.0 dB) |
| `dynamic_normalized_enob` | worst=2.846 bit (>= 2.50 bit) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/analyze_adc.py](../sources/upstream/tasks/sky130-flash-adc-3bit-pvt/environment/starter/testbench/analyze_adc.py) — noise
- [environment/starter/testbench/tb_dynamic_high_tt.spi](../sources/upstream/tasks/sky130-flash-adc-3bit-pvt/environment/starter/testbench/tb_dynamic_high_tt.spi) — tran
- [environment/starter/testbench/tb_dynamic_tt.spi](../sources/upstream/tasks/sky130-flash-adc-3bit-pvt/environment/starter/testbench/tb_dynamic_tt.spi) — tran
- [environment/starter/testbench/tb_ramp_tt.spi](../sources/upstream/tasks/sky130-flash-adc-3bit-pvt/environment/starter/testbench/tb_ramp_tt.spi) — tran
- [environment/starter/testbench/tb_transition_tt.spi](../sources/upstream/tasks/sky130-flash-adc-3bit-pvt/environment/starter/testbench/tb_transition_tt.spi) — tran
- [tests/benches/tb_dynamic.spi](../sources/upstream/tasks/sky130-flash-adc-3bit-pvt/tests/benches/tb_dynamic.spi) — tran
- [tests/benches/tb_ramp.spi](../sources/upstream/tasks/sky130-flash-adc-3bit-pvt/tests/benches/tb_ramp.spi) — tran
- [tests/benches/tb_sine.spi](../sources/upstream/tasks/sky130-flash-adc-3bit-pvt/tests/benches/tb_sine.spi) — tran

## 相邻案例

[23 5 bit 电阻 DAC：分母由固定支路决定](23-sky130-cmos-switched-resistor-dac-5bit-pvt.md) · [27 4 bit Flash ADC：前端采样与编码必须纳入转换链](27-sky130-flash-adc-4bit-50msps.md) · [42 6 bit 异步 SAR：采集窗、握手与最终寄存都影响正确性](42-sky130-sar-adc-6bit-async.md)
