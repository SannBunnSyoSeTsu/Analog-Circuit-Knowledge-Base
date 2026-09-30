---
case_id: adb-v2-30
task_id: sky130-gilbert-cell-mixer-2p4ghz-pvt-mismatch
category: 时钟与射频
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-gilbert-cell-mixer-2p4ghz-pvt-mismatch/instruction.md
  - ../sources/upstream/tasks/sky130-gilbert-cell-mixer-2p4ghz-pvt-mismatch/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-gilbert-cell-mixer-2p4ghz-pvt-mismatch/tests/verify.py
  - ../sources/upstream/tasks/sky130-gilbert-cell-mixer-2p4ghz-pvt-mismatch/results/reference.json
---

# 30 · Gilbert 混频器：线性指标需要幅度斜率自检

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

2.4 GHz，十个代表性 PVT 点、四个 LO 幅相失衡点及十个 tt_mm 样本；同时检查增益、端口隔离、IF 杂散、压缩与两幅度 IIP3。

## Reference 拓扑与尺寸线索（静态事实）

LVT 输入 gm 对采用分立尾支路和 650 Ω 跨源退化，短沟道 LO 换向四管，3.3 kΩ 负载和 75 fF 内部补偿/负载，外部再加 200 fF。

## 可复用的工程认识（推断，迁移时有条件）

源退化提高输入线性但消耗增益与电压余量；换向级则受 LO 驱动强度和时序影响。用 10/20 mV 两档输入核对基波/三阶斜率，可避免在噪底或压缩区用一次测量硬外推 IIP3。电压转输入功率要用声明的差分 100 Ω 口径。

## 不能由 pass 推出的结论

理想无源不会自动经历 MOS mismatch；十个种子也不是隔离或线性良率。端口隔离与 IF 谱纯净必须分别记录。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-gilbert-cell-mixer-2p4ghz-pvt-mismatch/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-gilbert-cell-mixer-2p4ghz-pvt-mismatch/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-gilbert-cell-mixer-2p4ghz-pvt-mismatch)
- [Reference circuit](../sources/upstream/tasks/sky130-gilbert-cell-mixer-2p4ghz-pvt-mismatch/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-gilbert-cell-mixer-2p4ghz-pvt-mismatch/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-gilbert-cell-mixer-2p4ghz-pvt-mismatch/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-gilbert-cell-mixer-2p4ghz-pvt-mismatch/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-gilbert-cell-mixer-2p4ghz-pvt-mismatch/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-gilbert-cell-mixer-2p4ghz-pvt-mismatch/circuit.spi) · [网站结果快照](../sources/astra/sky130-gilbert-cell-mixer-2p4ghz-pvt-mismatch/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-gilbert-cell-mixer-2p4ghz-pvt-mismatch/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-14T20:06:21+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `conversion_gain` | min=4.22dB at tt/1.62V/+125C/2.4GHz |
| `robust_port_isolation` | LO-IF=-51.4dB at tt_mm/1.80V/+27C/seed43010; RF-IF=-53.3dB at tt/1.98V/+125C/2.5GHz/imbalance; LO-RF=-56.7dB at ff/1.98V/-40C/2.5GHz/imbalance |
| `output_operating_point` | offset_max=4.49mV at tt_mm/1.80V/+27C/seed43003; VCM_min=0.607V at tt/1.62V/+125C/2.4GHz; headroom_min=0.982V at ss/1.80V/-40C/2.4GHz |
| `two_tone_iip3` | IIP3_min=-2.69dBm at tt/1.80V/+27C; two_tone_gain_difference_max=1.14dB; slopes=fund 0.989..0.994, IM3 1.89..2.08 |
| `large_signal_linearity` | compression_max=0.484dB at ss/1.62V/+125C |
| `if_spectral_purity` | worst=-32.7dBc at tt_mm/1.80V/+27C/seed43010 |
| `average_power` | max=1.31mW at tt/1.98V/+125C/2.5GHz/imbalance |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/tb_linearity_ss_example.spi](../sources/upstream/tasks/sky130-gilbert-cell-mixer-2p4ghz-pvt-mismatch/environment/starter/testbench/tb_linearity_ss_example.spi) — tran
- [environment/starter/testbench/tb_mismatch_tt_mm.spi](../sources/upstream/tasks/sky130-gilbert-cell-mixer-2p4ghz-pvt-mismatch/environment/starter/testbench/tb_mismatch_tt_mm.spi) — tran
- [environment/starter/testbench/tb_rf_tt_2p4ghz.spi](../sources/upstream/tasks/sky130-gilbert-cell-mixer-2p4ghz-pvt-mismatch/environment/starter/testbench/tb_rf_tt_2p4ghz.spi) — tran
- [tests/benches/tb_linearity.spi](../sources/upstream/tasks/sky130-gilbert-cell-mixer-2p4ghz-pvt-mismatch/tests/benches/tb_linearity.spi) — tran
- [tests/benches/tb_rf.spi](../sources/upstream/tasks/sky130-gilbert-cell-mixer-2p4ghz-pvt-mismatch/tests/benches/tb_rf.spi) — tran

## 相邻案例

[04 简单退化差分对：有限 gm 是增益预算的一部分](04-sky130-gmr-degenerated-diff-amp-gain2-bw70m-power1p2mw-sdr60.md) · [10 宽带 TIA：跨阻、输入噪声与大信号不能分开定规格](10-sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt.md) · [43 2.4 GHz LNA：匹配、噪声与稳定性要使用同一端口定义](43-sky130-inductive-lna-2p4ghz-gain12-nf2-pvt.md)
