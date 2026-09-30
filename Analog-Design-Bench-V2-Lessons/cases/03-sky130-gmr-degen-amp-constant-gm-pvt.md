---
case_id: adb-v2-03
task_id: sky130-gmr-degen-amp-constant-gm-pvt
category: 放大器与滤波
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-gmr-degen-amp-constant-gm-pvt/instruction.md
  - ../sources/upstream/tasks/sky130-gmr-degen-amp-constant-gm-pvt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-gmr-degen-amp-constant-gm-pvt/tests/verify.py
  - ../sources/upstream/tasks/sky130-gmr-degen-amp-constant-gm-pvt/results/reference.json
---

# 03 · 局部反馈恒 gm 放大器：用反馈压低有效跨导漂移

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

五个 MOS 角落 × −40/27/85 °C，共 15 点，固定 1.8 V；每端 1 pF，目标增益约 2、带宽至少 60 MHz。SDR 用 3 MHz、100 mV 差分峰值的正弦拟合残差定义。

## Reference 拓扑与尺寸线索（静态事实）

参考以局部反馈控制跨导，配每侧 140 Ω 退化、1.2 kΩ 桥接电阻和到 VCM 的 2.3034 kΩ 负载。IREF 端经 1 Ω 终接，实际偏置来自 VCM 相关网络。

## 可复用的工程认识（推断，迁移时有条件）

接口存在 IREF 不等于电路真的使用该参考建立偏置；要沿直流电流路径辨认偏置来源。闭环局部退化可使有效 gm 与电阻更相关，但输出增益仍包含有限环路增益及负载效应。功耗中纳入 VCM/输入源，避免把偏置能量转移到辅助端口。

## 不能由 pass 推出的结论

无电源扫描、局部失配及真实电阻工艺偏差。SDR 的拟合残差定义不能与另一任务的 FFT SFDR 混用。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-gmr-degen-amp-constant-gm-pvt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-gmr-degen-amp-constant-gm-pvt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-gmr-degen-amp-constant-gm-pvt)
- [Reference circuit](../sources/upstream/tasks/sky130-gmr-degen-amp-constant-gm-pvt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-gmr-degen-amp-constant-gm-pvt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-gmr-degen-amp-constant-gm-pvt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-gmr-degen-amp-constant-gm-pvt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-gmr-degen-amp-constant-gm-pvt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-gmr-degen-amp-constant-gm-pvt/circuit.spi) · [网站结果快照](../sources/astra/sky130-gmr-degen-amp-constant-gm-pvt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-gmr-degen-amp-constant-gm-pvt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-14T19:59:57+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `pvt_gain_1mhz` | min=1.98510 V/V at tt/-40C/1.80V; max=2.01577 V/V at fs/+85C/1.80V (requirement 1.98..2.02) |
| `pvt_bandwidth` | min=65.902 MHz at ss/-40C/1.80V (requirement >60 MHz) |
| `pvt_power` | max=1.329 mW at ss/+85C/1.80V (requirement <1.5 mW) |
| `pvt_dynamic_range` | SDR min=60.98 dB at ff/-40C/1.80V (>60 dB); fundamental gain=1.9781..2.0117 V/V (1.90..2.10 V/V) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/measure_sdr.py](../sources/upstream/tasks/sky130-gmr-degen-amp-constant-gm-pvt/environment/starter/testbench/measure_sdr.py) — 夹具、模板或数据处理辅助
- [environment/starter/testbench/tb_ac_tt.spi](../sources/upstream/tasks/sky130-gmr-degen-amp-constant-gm-pvt/environment/starter/testbench/tb_ac_tt.spi) — ac, op
- [environment/starter/testbench/tb_sdr_tt.spi](../sources/upstream/tasks/sky130-gmr-degen-amp-constant-gm-pvt/environment/starter/testbench/tb_sdr_tt.spi) — tran
- [tests/benches/tb_ac_power.spi](../sources/upstream/tasks/sky130-gmr-degen-amp-constant-gm-pvt/tests/benches/tb_ac_power.spi) — ac, op
- [tests/benches/tb_sdr.spi](../sources/upstream/tasks/sky130-gmr-degen-amp-constant-gm-pvt/tests/benches/tb_sdr.spi) — tran

## 相邻案例

[04 简单退化差分对：有限 gm 是增益预算的一部分](04-sky130-gmr-degenerated-diff-amp-gain2-bw70m-power1p2mw-sdr60.md) · [13 恒 gm 稳增益：偏置单元必须映射到输入电流密度](13-sky130-constant-gm-stable-gain-amplifier-pvt.md) · [26 OTA-C 双二阶滤波器：状态节点的共模预算不能合并](26-sky130-fully-differential-ota-c-biquad-pvt.md)
