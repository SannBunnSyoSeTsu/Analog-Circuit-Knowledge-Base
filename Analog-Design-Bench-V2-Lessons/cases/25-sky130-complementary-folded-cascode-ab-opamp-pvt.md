---
case_id: adb-v2-25
task_id: sky130-complementary-folded-cascode-ab-opamp-pvt
category: 放大器与滤波
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: true
derived_from:
  - ../sources/upstream/tasks/sky130-complementary-folded-cascode-ab-opamp-pvt/instruction.md
  - ../sources/upstream/tasks/sky130-complementary-folded-cascode-ab-opamp-pvt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-complementary-folded-cascode-ab-opamp-pvt/tests/verify.py
  - ../sources/upstream/tasks/sky130-complementary-folded-cascode-ab-opamp-pvt/results/reference.json
---

# 25 · 轨到轨 Class-AB 运放：输入 gm 平整和内部模态同样重要

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

五角落 × 五个供电/温度组合，25 点；AC 再扫五个输入共模，输出通过 DC 反馈独立保持中点。4 pF 与 10 kΩ 负载，另查 THD、噪声、跟踪与三个固定失调种子。

## Reference 拓扑与尺寸线索（静态事实）

reference 使用互补 LVT 输入、尾电流转向、退化电阻、折叠求和、Monticelli 浮动控制的 AB 输出；双 6 pF/5 kΩ 补偿，并在内部栅节点加 0.5 pF 阻尼。

## 可复用的工程认识（推断，迁移时有条件）

互补输入交接改变 gm；尾电流转向必须同时照顾折叠支路电流，否则共模扫描可能破坏工作点。内部栅节点的慢振荡未必在单次差模 PM 数字中显现，阶跃尾段和失真检查能补充证据。

## 不能由 pass 推出的结论

标题拓扑不是硬性结构约束。Astra R1 用电阻把输入抬高后接单 NMOS 对及 Class-A 输出，也被接受；不能据其 pass 宣称实现了互补输入/AB。reference PM、THD 余量也很小。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-complementary-folded-cascode-ab-opamp-pvt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-complementary-folded-cascode-ab-opamp-pvt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-complementary-folded-cascode-ab-opamp-pvt)
- [Reference circuit](../sources/upstream/tasks/sky130-complementary-folded-cascode-ab-opamp-pvt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-complementary-folded-cascode-ab-opamp-pvt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-complementary-folded-cascode-ab-opamp-pvt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-complementary-folded-cascode-ab-opamp-pvt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-complementary-folded-cascode-ab-opamp-pvt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-complementary-folded-cascode-ab-opamp-pvt/circuit.spi) · [网站结果快照](../sources/astra/sky130-complementary-folded-cascode-ab-opamp-pvt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-complementary-folded-cascode-ab-opamp-pvt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 已做定向电路比较，见 [Astra 对照](../topics/08-astra-comparisons.md)。

Reference 结果生成时间：`2026-08-14T20:07:47+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `complete_signoff` | 212/212 serial analyses complete |
| `pvt_gain_10hz` | core worst=92.23dB at fs/1.62V/+125C, VCM=1.420V (min 90dB); near-rail worst=92.08dB at fs/1.62V/+125C, VCM=1.520V (min 80dB) |
| `pvt_ugbw` | worst=2.851MHz at fs/1.62V/+125C (min 1MHz) |
| `pvt_phase_margin` | core worst=60.08deg at fs/1.62V/+125C, VCM=0.810V (min 60deg); near-rail worst=62.99deg at fs/1.62V/+125C, VCM=1.520V (min 55deg) |
| `pvt_ugbw_pvt_flatness` | complete PVT/VCM max/min=1.955; maximum at sf/1.98V/-40C (max 2) |
| `pvt_input_common_mode_range` | worst low edge=0.040V at fs/1.98V/+125C (max 0.1V); worst high headroom=0.005V at tt/1.80V/+27C (max 0.1V); worst span=1.583V at fs/1.62V/+125C (min 1.5V) |
| `pvt_rail_tracking` | core=0.589mV at sf/1.98V/+125C (max 5mV); full=1.298mV at fs/1.98V/+125C (max 20mV) |
| `pvt_static_power` | max=1298.3uW at fs/1.98V/-40C during 0..VDD tracking sweep (max 1500uW) |
| `pvt_slew_rate` | slew_worst=2.053V/us slew_up_v_per_us at ss/1.62V/+125C (min 2V/us); tail_error_worst=0.583mV at sf/1.98V/+125C (max 5mV) |
| `pvt_input_noise` | worst=66.70uVrms at fs/1.98V/+125C (max 70uVrms) |
| `representative_cmrr` | 1kHz worst=94.38dB at ss/1.62V/+125C; 1MHz worst=57.08dB at ss/1.62V/+125C |
| `representative_psrr` | 10Hz worst=62.83dB at ss/1.62V/+125C; 1MHz worst=15.49dB at ss/1.62V/+125C |
| `representative_thd` | Fourier THD worst=0.00961% at ff/1.98V/-40C (max 0.01%); bounded residual=0.1081% at ff/1.98V/-40C (max 0.5%) |
| `mismatch_offset` | worst \|offset\|=1.038mV at seed 31000 (max 5mV) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/tb_ac_tt.spi](../sources/upstream/tasks/sky130-complementary-folded-cascode-ab-opamp-pvt/environment/starter/testbench/tb_ac_tt.spi) — ac, op
- [environment/starter/testbench/tb_cmrr_tt.spi](../sources/upstream/tasks/sky130-complementary-folded-cascode-ab-opamp-pvt/environment/starter/testbench/tb_cmrr_tt.spi) — ac
- [environment/starter/testbench/tb_noise_tt.spi](../sources/upstream/tasks/sky130-complementary-folded-cascode-ab-opamp-pvt/environment/starter/testbench/tb_noise_tt.spi) — noise
- [environment/starter/testbench/tb_offset_tt_mm.spi](../sources/upstream/tasks/sky130-complementary-folded-cascode-ab-opamp-pvt/environment/starter/testbench/tb_offset_tt_mm.spi) — op
- [environment/starter/testbench/tb_psrr_tt.spi](../sources/upstream/tasks/sky130-complementary-folded-cascode-ab-opamp-pvt/environment/starter/testbench/tb_psrr_tt.spi) — ac
- [environment/starter/testbench/tb_step_ff.spi](../sources/upstream/tasks/sky130-complementary-folded-cascode-ab-opamp-pvt/environment/starter/testbench/tb_step_ff.spi) — tran
- [environment/starter/testbench/tb_thd_tt.spi](../sources/upstream/tasks/sky130-complementary-folded-cascode-ab-opamp-pvt/environment/starter/testbench/tb_thd_tt.spi) — tran
- [environment/starter/testbench/tb_track_ss.spi](../sources/upstream/tasks/sky130-complementary-folded-cascode-ab-opamp-pvt/environment/starter/testbench/tb_track_ss.spi) — dc, op
- [tests/benches/tb_ac.spi](../sources/upstream/tasks/sky130-complementary-folded-cascode-ab-opamp-pvt/tests/benches/tb_ac.spi) — ac, op
- [tests/benches/tb_cmrr.spi](../sources/upstream/tasks/sky130-complementary-folded-cascode-ab-opamp-pvt/tests/benches/tb_cmrr.spi) — ac
- [tests/benches/tb_noise.spi](../sources/upstream/tasks/sky130-complementary-folded-cascode-ab-opamp-pvt/tests/benches/tb_noise.spi) — noise
- [tests/benches/tb_offset.spi](../sources/upstream/tasks/sky130-complementary-folded-cascode-ab-opamp-pvt/tests/benches/tb_offset.spi) — op
- [tests/benches/tb_psrr.spi](../sources/upstream/tasks/sky130-complementary-folded-cascode-ab-opamp-pvt/tests/benches/tb_psrr.spi) — ac
- [tests/benches/tb_step.spi](../sources/upstream/tasks/sky130-complementary-folded-cascode-ab-opamp-pvt/tests/benches/tb_step.spi) — tran
- [tests/benches/tb_thd.spi](../sources/upstream/tasks/sky130-complementary-folded-cascode-ab-opamp-pvt/tests/benches/tb_thd.spi) — tran
- [tests/benches/tb_track.spi](../sources/upstream/tasks/sky130-complementary-folded-cascode-ab-opamp-pvt/tests/benches/tb_track.spi) — dc, op

## 相邻案例

[17 0.4 V NMOS LDO：低输出电压改变输入级和驱动极性](17-sky130-nmos-pass-ldo-0p4v-pvt-mc.md) · [29 Ahuja 补偿：补偿接入点的阻抗决定物理作用](29-sky130-ahuja-compensated-two-stage-load-range-pvt.md) · [39 低功耗线路驱动：Class-AB 的价值是峰值/静态电流比](39-sky130-low-power-line-driver-pvt.md)
