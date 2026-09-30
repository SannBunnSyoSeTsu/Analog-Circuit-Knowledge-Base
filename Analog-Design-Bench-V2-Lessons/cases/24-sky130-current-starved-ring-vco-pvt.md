---
case_id: adb-v2-24
task_id: sky130-current-starved-ring-vco-pvt
category: 时钟与射频
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-current-starved-ring-vco-pvt/instruction.md
  - ../sources/upstream/tasks/sky130-current-starved-ring-vco-pvt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-current-starved-ring-vco-pvt/tests/verify.py
  - ../sources/upstream/tasks/sky130-current-starved-ring-vco-pvt/results/reference.json
---

# 24 · 限流环 VCO：调谐单调性与增益一致性需要独立约束

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

27 点 PVT；控制电压 0.9–1.2 V 必须覆盖 25 MHz，限制 KVCO 最小值、变化比、占空比、启动及供电 pushing。

## Reference 拓扑与尺寸线索（静态事实）

五级限流环，47 kΩ 源退化的 V-to-I 控制与电流镜，每级约 30 fF，后接两级缓冲。

## 可复用的工程认识（推断，迁移时有条件）

“频率范围覆盖”不足以保证 PLL 可用：还要每步单调、有界 KVCO、频率平台内稳定且有足够有效周期。将控制压到频率的非线性主要交给退化 V-to-I，有利于限制 KVCO 变化。

## 不能由 pass 推出的结论

确定性周期漂移不是随机抖动，相噪未测。供电 pushing 使用另一套声明的供电扫描，不能从主调谐表推断。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-current-starved-ring-vco-pvt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-current-starved-ring-vco-pvt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-current-starved-ring-vco-pvt)
- [Reference circuit](../sources/upstream/tasks/sky130-current-starved-ring-vco-pvt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-current-starved-ring-vco-pvt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-current-starved-ring-vco-pvt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-current-starved-ring-vco-pvt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-current-starved-ring-vco-pvt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-current-starved-ring-vco-pvt/circuit.spi) · [网站结果快照](../sources/astra/sky130-current-starved-ring-vco-pvt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-current-starved-ring-vco-pvt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-15T03:46:10+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `pvt_frequency_coverage` | f(0.9V)_range=12.55..20.68MHz; f(1.2V)_min=26.42MHz at ff/1.98V/+125C |
| `pvt_tuning_ratio` | worst=1.791 at ff/1.98V/+125C |
| `pvt_kvco_monotonic_linear` | KVCO_min=37.26MHz/V at ff/1.98V/+125C; linearity_max=1.095 at ss/1.98V/+125C |
| `pvt_frequency_settling` | worst=0.004786% at tt/1.62V/-40C |
| `pvt_duty_cycle` | range=0.486..0.4999 |
| `pvt_startup` | worst=47.61ns at ss/1.62V/-40C |
| `pvt_output_swing` | low_max=0.0001658 at ff/1.98V/+125C; high_min=1.001 at ff/1.98V/+125C |
| `pvt_power` | worst=151.6uW at ff/1.98V/+125C |
| `supply_pushing` | worst=88.9%/V at ff/27C |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/tb_push_high_tt.spi](../sources/upstream/tasks/sky130-current-starved-ring-vco-pvt/environment/starter/testbench/tb_push_high_tt.spi) — tran
- [environment/starter/testbench/tb_push_low_tt.spi](../sources/upstream/tasks/sky130-current-starved-ring-vco-pvt/environment/starter/testbench/tb_push_low_tt.spi) — tran
- [environment/starter/testbench/tb_push_tt.spi](../sources/upstream/tasks/sky130-current-starved-ring-vco-pvt/environment/starter/testbench/tb_push_tt.spi) — tran
- [environment/starter/testbench/tb_tune_tt.spi](../sources/upstream/tasks/sky130-current-starved-ring-vco-pvt/environment/starter/testbench/tb_tune_tt.spi) — tran
- [tests/benches/tb_push.spi](../sources/upstream/tasks/sky130-current-starved-ring-vco-pvt/tests/benches/tb_push.spi) — tran
- [tests/benches/tb_tune.spi](../sources/upstream/tasks/sky130-current-starved-ring-vco-pvt/tests/benches/tb_tune.spi) — tran

## 相邻案例

[09 宽频 CML 二分频：判定锁定需要周期级证据](09-sky130-cml-divider-div2-range1gto10g.md) · [14 低功耗 2 MHz 振荡器：缓冲与启动都占功率预算](14-sky130-low-power-oscillator-2mhz-pvt.md) · [49 2 GHz LC VCO：调谐范围、pushing 与启动初值分开记录](49-sky130-lc-vco-2ghz-pvt.md)
