---
case_id: adb-v2-26
task_id: sky130-fully-differential-ota-c-biquad-pvt
category: 放大器与滤波
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-fully-differential-ota-c-biquad-pvt/instruction.md
  - ../sources/upstream/tasks/sky130-fully-differential-ota-c-biquad-pvt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-fully-differential-ota-c-biquad-pvt/tests/verify.py
  - ../sources/upstream/tasks/sky130-fully-differential-ota-c-biquad-pvt/results/reference.json
---

# 26 · OTA-C 双二阶滤波器：状态节点的共模预算不能合并

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

25 个代表性 PVT 点及三个动态压力点；同时检查低通与带通响应、二阶拟合残差、Q、噪声、近 2 MHz THD 和两个状态的共模阶跃。

## Reference 拓扑与尺寸线索（静态事实）

三个信号跨导及额外阻尼跨导，退化桥接约 19.1/8 kΩ；两个积分状态分别用 8/4 pF，另有 250 fF 外部负载。每个状态独立 CMFB，额外阻尼级共享部分负载。

## 可复用的工程认识（推断，迁移时有条件）

理想 f0≈gm/(2π√(C1C2))，Q 还依赖电容比和阻尼 gm；实际应把测量负载也计入状态电容。带通节点存在三路下拉却只有两路上拉，偏置复制比例要按真实支路计数，不能照抄对称单 OTA 的 CMFB。

## 不能由 pass 推出的结论

参考共模误差约 9.09 mV，接近 10 mV 上限。单看 −3 dB 点不能证实二阶函数正确，完整 LP/BP 形状与拟合残差才是本题证据。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-fully-differential-ota-c-biquad-pvt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-fully-differential-ota-c-biquad-pvt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-fully-differential-ota-c-biquad-pvt)
- [Reference circuit](../sources/upstream/tasks/sky130-fully-differential-ota-c-biquad-pvt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-fully-differential-ota-c-biquad-pvt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-fully-differential-ota-c-biquad-pvt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-fully-differential-ota-c-biquad-pvt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-fully-differential-ota-c-biquad-pvt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-fully-differential-ota-c-biquad-pvt/circuit.spi) · [网站结果快照](../sources/astra/sky130-fully-differential-ota-c-biquad-pvt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-fully-differential-ota-c-biquad-pvt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-13T10:36:28+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `complete_signoff` | runs=62/62 failed=0 |
| `pvt_center_frequency` | fitted f0 1.971..2.124 MHz (band 1.8..2.2) |
| `pvt_quality_factor` | fitted Q 0.677..0.711 (band 0.65..0.75) |
| `pvt_passband_gain` | passband gain -0.689..-0.605 dB (band -1..1) |
| `pvt_second_order_fit` | second-order fit RMS error 0.002 dB (max 0.5) |
| `pvt_stopband_attenuation` | attenuation at 20 MHz 38.91 dB (min 35) |
| `pvt_bandpass_output` | BP peak 1.950..2.138 MHz, gain -6.58..-6.13 dB, worst decade-edge attenuation 15.77 dB |
| `pvt_bandpass_low_frequency_rejection` | 1 kHz rejection from BP peak 22.02 dB (min 18) |
| `pvt_output_common_mode` | output common-mode error 9.09 mV on both node pairs (max 10 mV) |
| `pvt_power` | supply power 430.0 uW (max 500) |
| `stress_thd_nominal` | THD -51.07 dB, fundamental gain 0.920 at 0.6 Vpp diff |
| `stress_thd_large_signal` | THD -40.85 dB, fundamental gain 0.911 at 0.9 Vpp diff |
| `stress_thd_near_f0` | at 2 MHz and 0.9 Vpp: LP THD -57.99 dB / gain 0.647, BP THD -52.62 dB / gain 0.476 |
| `pvt_output_noise` | integrated output noise 433.3 uVrms over 1 kHz..4 MHz (max 500) |
| `stress_cmfb_settling` | common-mode step settling 0.432 us on both loops (max 1) |
| `stress_cmfb_damping` | late common-mode excursion 8.66 mV (max 10 mV) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/tb_ac_tt.spi](../sources/upstream/tasks/sky130-fully-differential-ota-c-biquad-pvt/environment/starter/testbench/tb_ac_tt.spi) — ac, op
- [environment/starter/testbench/tb_cmstep_tt.spi](../sources/upstream/tasks/sky130-fully-differential-ota-c-biquad-pvt/environment/starter/testbench/tb_cmstep_tt.spi) — tran
- [environment/starter/testbench/tb_noise_tt.spi](../sources/upstream/tasks/sky130-fully-differential-ota-c-biquad-pvt/environment/starter/testbench/tb_noise_tt.spi) — noise
- [environment/starter/testbench/tb_thd_f0_sf_hot.spi](../sources/upstream/tasks/sky130-fully-differential-ota-c-biquad-pvt/environment/starter/testbench/tb_thd_f0_sf_hot.spi) — tran
- [environment/starter/testbench/tb_thd_large_sf_hot.spi](../sources/upstream/tasks/sky130-fully-differential-ota-c-biquad-pvt/environment/starter/testbench/tb_thd_large_sf_hot.spi) — tran
- [environment/starter/testbench/tb_thd_sf_hot.spi](../sources/upstream/tasks/sky130-fully-differential-ota-c-biquad-pvt/environment/starter/testbench/tb_thd_sf_hot.spi) — tran
- [tests/benches/tb_ac.spi](../sources/upstream/tasks/sky130-fully-differential-ota-c-biquad-pvt/tests/benches/tb_ac.spi) — ac, op
- [tests/benches/tb_cmstep.spi](../sources/upstream/tasks/sky130-fully-differential-ota-c-biquad-pvt/tests/benches/tb_cmstep.spi) — tran
- [tests/benches/tb_noise.spi](../sources/upstream/tasks/sky130-fully-differential-ota-c-biquad-pvt/tests/benches/tb_noise.spi) — noise
- [tests/benches/tb_thd.spi](../sources/upstream/tasks/sky130-fully-differential-ota-c-biquad-pvt/tests/benches/tb_thd.spi) — tran
- [tests/benches/tb_thd2.spi](../sources/upstream/tasks/sky130-fully-differential-ota-c-biquad-pvt/tests/benches/tb_thd2.spi) — tran
- [tests/benches/tb_thd_f0.spi](../sources/upstream/tasks/sky130-fully-differential-ota-c-biquad-pvt/tests/benches/tb_thd_f0.spi) — tran

## 相邻案例

[03 局部反馈恒 gm 放大器：用反馈压低有效跨导漂移](03-sky130-gmr-degen-amp-constant-gm-pvt.md) · [13 恒 gm 稳增益：偏置单元必须映射到输入电流密度](13-sky130-constant-gm-stable-gain-amplifier-pvt.md) · [35 全差分两级 Miller：高差模增益不能替代电源抑制](35-sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt.md)
