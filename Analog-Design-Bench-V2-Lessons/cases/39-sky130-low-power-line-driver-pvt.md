---
case_id: adb-v2-39
task_id: sky130-low-power-line-driver-pvt
category: 放大器与滤波
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-low-power-line-driver-pvt/instruction.md
  - ../sources/upstream/tasks/sky130-low-power-line-driver-pvt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-low-power-line-driver-pvt/tests/verify.py
  - ../sources/upstream/tasks/sky130-low-power-line-driver-pvt/results/reference.json
---

# 39 · 低功耗线路驱动：Class-AB 的价值是峰值/静态电流比

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

45 点 PVT，闭环反相增益 −1、10 kΩ 反馈，输出经 1 µF 耦合到 300 Ω 线路并带 200 pF；静态≤400 µW，峰值电流≥2 mA 且≥10 倍静态。

## Reference 拓扑与尺寸线索（静态事实）

两级 Monticelli AB，输出 PMOS/NMOS 宽约 252/48 µm、L=0.3 µm；双 1.5 pF/680 Ω 补偿。

## 可复用的工程认识（推断，迁移时有条件）

低静态电流与高动态驱动并不矛盾，关键在交越区域控制和两支路动态偏置。必须同时检查静态、峰值、THD、摆幅和大电容负载下稳定性。耦合电容改变低频负载，不能用纯 300 Ω DC 负载代替原测试。

## 不能由 pass 推出的结论

参考 20 kHz、0.6 V 峰值的 THD 与驱动倍数仅对应声明输入；并非全音频功率放大器认证。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-low-power-line-driver-pvt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-low-power-line-driver-pvt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-low-power-line-driver-pvt)
- [Reference circuit](../sources/upstream/tasks/sky130-low-power-line-driver-pvt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-low-power-line-driver-pvt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-low-power-line-driver-pvt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-low-power-line-driver-pvt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-low-power-line-driver-pvt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-low-power-line-driver-pvt/circuit.spi) · [网站结果快照](../sources/astra/sky130-low-power-line-driver-pvt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-low-power-line-driver-pvt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-14T20:10:52+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `pvt_loop_gain` | worst=52.32dB at ss/1.62V/-40C (min 40dB) |
| `pvt_bandwidth` | worst=0.5381MHz at ss/1.62V/-40C (min 0.5MHz) |
| `pvt_phase_margin` | worst=65.13deg at fs/1.98V/-40C (min 60deg) |
| `pvt_output_bias` | worst=4.48mV at fs/1.98V/+125C (max 20mV) |
| `pvt_quiescent_power` | worst=347.8uW at fs/1.98V/+125C (max 400uW) |
| `line_distortion` | THD_max=0.572% at sf/1.62V/-40C (max 3%); fundamental_min=0.591V at sf/1.62V/-40C (min 0.55V) |
| `line_drive` | ipeak_min=2.16mA at ss/1.62V/-40C (min 2mA); drive_ratio_min=12.8 at fs/1.98V/+125C (min 10) |
| `closed_loop_range` | worst=1.536Vpp at tt/1.62V/-40C (min 1.5Vpp) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/measure_thd.py](../sources/upstream/tasks/sky130-low-power-line-driver-pvt/environment/starter/testbench/measure_thd.py) — 夹具、模板或数据处理辅助
- [environment/starter/testbench/tb_loopgain_ss_1p71v_125c.spi](../sources/upstream/tasks/sky130-low-power-line-driver-pvt/environment/starter/testbench/tb_loopgain_ss_1p71v_125c.spi) — ac, op
- [environment/starter/testbench/tb_loopgain_tt_1p80v_85c.spi](../sources/upstream/tasks/sky130-low-power-line-driver-pvt/environment/starter/testbench/tb_loopgain_tt_1p80v_85c.spi) — ac, op
- [environment/starter/testbench/tb_swing_tt_1p80v_85c.spi](../sources/upstream/tasks/sky130-low-power-line-driver-pvt/environment/starter/testbench/tb_swing_tt_1p80v_85c.spi) — dc
- [environment/starter/testbench/tb_thd_tt_1p80v_85c.spi](../sources/upstream/tasks/sky130-low-power-line-driver-pvt/environment/starter/testbench/tb_thd_tt_1p80v_85c.spi) — tran
- [tests/benches/tb_loopgain.spi](../sources/upstream/tasks/sky130-low-power-line-driver-pvt/tests/benches/tb_loopgain.spi) — ac, op
- [tests/benches/tb_swing.spi](../sources/upstream/tasks/sky130-low-power-line-driver-pvt/tests/benches/tb_swing.spi) — dc
- [tests/benches/tb_thd.spi](../sources/upstream/tasks/sky130-low-power-line-driver-pvt/tests/benches/tb_thd.spi) — tran

## 相邻案例

[01 Class-D 半桥：导通损耗与驱动损耗必须一起算](01-sky130-class-d-halfbridge-eff95-tt.md) · [25 轨到轨 Class-AB 运放：输入 gm 平整和内部模态同样重要](25-sky130-complementary-folded-cascode-ab-opamp-pvt.md) · [29 Ahuja 补偿：补偿接入点的阻抗决定物理作用](29-sky130-ahuja-compensated-two-stage-load-range-pvt.md)
