---
case_id: adb-v2-09
task_id: sky130-cml-divider-div2-range1gto10g
category: 时钟与射频
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-cml-divider-div2-range1gto10g/instruction.md
  - ../sources/upstream/tasks/sky130-cml-divider-div2-range1gto10g/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-cml-divider-div2-range1gto10g/tests/verify.py
  - ../sources/upstream/tasks/sky130-cml-divider-div2-range1gto10g/results/reference.json
---

# 09 · 宽频 CML 二分频：判定锁定需要周期级证据

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

五角落、1.8 V/27 °C，1/2/5/10 GHz 输入，300 mVpp 差分时钟经 50 Ω，输出每端 10 fF；5 ns 后检查至少 40 周期。

## Reference 拓扑与尺寸线索（静态事实）

主从 CML 锁存器以尾电流在透明/再生支路间转向，交相时钟及反相反馈形成二分频；负载电阻 2 kΩ/2.01 kΩ 带微小不对称。

## 可复用的工程认识（推断，迁移时有条件）

FFT 上有 f/2 峰并不等于稳定二分频：还要逐周期检查极性、频率、摆幅与连续性。微小不对称是确定性启动条件的一部分，不能替代失配统计或上电复位。跨输入频率检查能分开低频保持失败和高频带宽不足。

## 不能由 pass 推出的结论

功耗指标是静态 DUT 功耗，不包括外部高速时钟驱动；缺少复位语义与随机抖动保证。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-cml-divider-div2-range1gto10g/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-cml-divider-div2-range1gto10g/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-cml-divider-div2-range1gto10g)
- [Reference circuit](../sources/upstream/tasks/sky130-cml-divider-div2-range1gto10g/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-cml-divider-div2-range1gto10g/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-cml-divider-div2-range1gto10g/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-cml-divider-div2-range1gto10g/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-cml-divider-div2-range1gto10g/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-cml-divider-div2-range1gto10g/circuit.spi) · [网站结果快照](../sources/astra/sky130-cml-divider-div2-range1gto10g/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-cml-divider-div2-range1gto10g/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-14T20:00:17+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `divide_operating_points` | required_points=1.000,2.000,5.000,10.000GHz; highest_passing_frequency=10.000GHz; min_cycle_swing=251.1mVpp (require >=200mVpp); target_tone=454.7mVpp (require >=200mVpp); failed_points=none |
| `dc_power` | power_max=1.207mW (require <1.500mW) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/measure_divider.py](../sources/upstream/tasks/sky130-cml-divider-div2-range1gto10g/environment/starter/testbench/measure_divider.py) — 夹具、模板或数据处理辅助
- [environment/starter/testbench/tb_divider_10g.spi](../sources/upstream/tasks/sky130-cml-divider-div2-range1gto10g/environment/starter/testbench/tb_divider_10g.spi) — tran
- [environment/starter/testbench/tb_divider_1g.spi](../sources/upstream/tasks/sky130-cml-divider-div2-range1gto10g/environment/starter/testbench/tb_divider_1g.spi) — tran
- [environment/starter/testbench/tb_power.spi](../sources/upstream/tasks/sky130-cml-divider-div2-range1gto10g/environment/starter/testbench/tb_power.spi) — op
- [tests/benches/tb_divider.spi](../sources/upstream/tasks/sky130-cml-divider-div2-range1gto10g/tests/benches/tb_divider.spi) — tran
- [tests/benches/tb_power.spi](../sources/upstream/tasks/sky130-cml-divider-div2-range1gto10g/tests/benches/tb_power.spi) — op

## 相邻案例

[24 限流环 VCO：调谐单调性与增益一致性需要独立约束](24-sky130-current-starved-ring-vco-pvt.md) · [32 28 Gb/s CML 发射器：带宽还需眼图和群延迟约束](32-sky130-cml-tx-driver-28g-nrz-pvt.md) · [45 晶体管二分频：复位必须清除内部状态](45-sky130-transistor-divide-by-2.md)
