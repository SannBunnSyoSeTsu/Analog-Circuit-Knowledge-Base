---
case_id: adb-v2-04
task_id: sky130-gmr-degenerated-diff-amp-gain2-bw70m-power1p2mw-sdr60
category: 放大器与滤波
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-gmr-degenerated-diff-amp-gain2-bw70m-power1p2mw-sdr60/instruction.md
  - ../sources/upstream/tasks/sky130-gmr-degenerated-diff-amp-gain2-bw70m-power1p2mw-sdr60/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-gmr-degenerated-diff-amp-gain2-bw70m-power1p2mw-sdr60/tests/verify.py
  - ../sources/upstream/tasks/sky130-gmr-degenerated-diff-amp-gain2-bw70m-power1p2mw-sdr60/results/reference.json
---

# 04 · 简单退化差分对：有限 gm 是增益预算的一部分

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

五个 MOS 角落、固定 1.8 V/27 °C；增益约 2、BW≥70 MHz、功耗≤1.2 mW、SDR≥60 dB。

## Reference 拓扑与尺寸线索（静态事实）

大面积 LVT 差分对 w=10 µm、m=70、L=0.35 µm；每侧 630 Ω 退化，1.834 kΩ 电阻负载，尾电流镜用 L=1 µm 的 72:6 比例。

## 可复用的工程认识（推断，迁移时有条件）

每侧退化的简化差分模型为 Gm≈gm/(1+gm·Rs)，Av≈Gm·RL；不能把 RL/Rs≈2.91 直接当目标增益 2。参考依赖有限 gm 的贡献，故电阻比和偏置必须联立考虑。退化改善线性，但噪声、压降和高频极点仍需预算。

## 不能由 pass 推出的结论

只覆盖温度单点；“五角落通过”不能外推成全 PVT。当前只阅读既有结果，没有验证退化电阻温漂或寄生。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-gmr-degenerated-diff-amp-gain2-bw70m-power1p2mw-sdr60/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-gmr-degenerated-diff-amp-gain2-bw70m-power1p2mw-sdr60/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-gmr-degenerated-diff-amp-gain2-bw70m-power1p2mw-sdr60)
- [Reference circuit](../sources/upstream/tasks/sky130-gmr-degenerated-diff-amp-gain2-bw70m-power1p2mw-sdr60/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-gmr-degenerated-diff-amp-gain2-bw70m-power1p2mw-sdr60/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-gmr-degenerated-diff-amp-gain2-bw70m-power1p2mw-sdr60/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-gmr-degenerated-diff-amp-gain2-bw70m-power1p2mw-sdr60/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-gmr-degenerated-diff-amp-gain2-bw70m-power1p2mw-sdr60/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-gmr-degenerated-diff-amp-gain2-bw70m-power1p2mw-sdr60/circuit.spi) · [网站结果快照](../sources/astra/sky130-gmr-degenerated-diff-amp-gain2-bw70m-power1p2mw-sdr60/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-gmr-degenerated-diff-amp-gain2-bw70m-power1p2mw-sdr60/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-14T19:59:46+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `pvt_gain_1mhz` | min=1.99523 V/V at fs/+27C/1.80V; max=2.01436 V/V at sf/+27C/1.80V (requirement 1.98..2.02) |
| `pvt_bandwidth` | min=71.785 MHz at fs/+27C/1.80V (requirement >70 MHz) |
| `pvt_power` | max=1.100 mW at sf/+27C/1.80V (requirement <1.2 mW) |
| `pvt_dynamic_range` | SDR min=65.58 dB at fs/+27C/1.80V (>60 dB); fundamental gain=1.9905..2.0099 V/V (1.90..2.10 V/V) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/measure_sdr.py](../sources/upstream/tasks/sky130-gmr-degenerated-diff-amp-gain2-bw70m-power1p2mw-sdr60/environment/starter/testbench/measure_sdr.py) — 夹具、模板或数据处理辅助
- [environment/starter/testbench/tb_ac_tt.spi](../sources/upstream/tasks/sky130-gmr-degenerated-diff-amp-gain2-bw70m-power1p2mw-sdr60/environment/starter/testbench/tb_ac_tt.spi) — ac, op
- [environment/starter/testbench/tb_sdr_tt.spi](../sources/upstream/tasks/sky130-gmr-degenerated-diff-amp-gain2-bw70m-power1p2mw-sdr60/environment/starter/testbench/tb_sdr_tt.spi) — tran
- [tests/benches/tb_ac_power.spi](../sources/upstream/tasks/sky130-gmr-degenerated-diff-amp-gain2-bw70m-power1p2mw-sdr60/tests/benches/tb_ac_power.spi) — ac, op
- [tests/benches/tb_sdr.spi](../sources/upstream/tasks/sky130-gmr-degenerated-diff-amp-gain2-bw70m-power1p2mw-sdr60/tests/benches/tb_sdr.spi) — tran

## 相邻案例

[03 局部反馈恒 gm 放大器：用反馈压低有效跨导漂移](03-sky130-gmr-degen-amp-constant-gm-pvt.md) · [13 恒 gm 稳增益：偏置单元必须映射到输入电流密度](13-sky130-constant-gm-stable-gain-amplifier-pvt.md) · [30 Gilbert 混频器：线性指标需要幅度斜率自检](30-sky130-gilbert-cell-mixer-2p4ghz-pvt-mismatch.md)
