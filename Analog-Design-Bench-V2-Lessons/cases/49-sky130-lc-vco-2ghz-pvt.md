---
case_id: adb-v2-49
task_id: sky130-lc-vco-2ghz-pvt
category: 时钟与射频
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-lc-vco-2ghz-pvt/instruction.md
  - ../sources/upstream/tasks/sky130-lc-vco-2ghz-pvt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-lc-vco-2ghz-pvt/tests/verify.py
  - ../sources/upstream/tasks/sky130-lc-vco-2ghz-pvt/results/reference.json
---

# 49 · 2 GHz LC VCO：调谐范围、pushing 与启动初值分开记录

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

27 点 PVT、四档控制电压 0/0.6/1.2/1.8 V，调谐频率下降并覆盖 2 GHz；另限启动、功率、摆幅和供电 pushing。

## Reference 拓扑与尺寸线索（静态事实）

官方中心抽头有限 Q 电感、交叉耦合 NMOS 负阻、PMOS 电流镜、物理 MIM 和 LVT MOS varactor；外部 50 µA 参考。

## 可复用的工程认识（推断，迁移时有条件）

频率由总差分等效 L/C 决定，变容范围需与寄生、电感连接方式同时解释。供电 pushing 反映幅度/工作点改变耦合到频率，不能用 KVCO 替代。启动测量所用初始能量必须作为条件记录。

## 不能由 pass 推出的结论

bench 预设两端约 0.61/0.59 V 的不对称初值，所以通过的是有扰动种子的启动；没有从物理噪声自启动或相位噪声证据。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-lc-vco-2ghz-pvt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-lc-vco-2ghz-pvt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-lc-vco-2ghz-pvt)
- [Reference circuit](../sources/upstream/tasks/sky130-lc-vco-2ghz-pvt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-lc-vco-2ghz-pvt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-lc-vco-2ghz-pvt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-lc-vco-2ghz-pvt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-lc-vco-2ghz-pvt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-lc-vco-2ghz-pvt/circuit.spi) · [网站结果快照](../sources/astra/sky130-lc-vco-2ghz-pvt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-lc-vco-2ghz-pvt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-15T18:00:00Z`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `complete_signoff` | 27/27 unique finite PVT points passed |
| `pvt_2ghz_coverage` | f(0V)_min=2.1128 GHz; f(1.8V) maximum passed 1.72 GHz limit |
| `pvt_tuning` | ratio_min=1.291; segment_drop_min=10.55 MHz |
| `pvt_differential_swing` | Vdiff_pp_min=0.356 V |
| `pvt_startup` | startup_max=13.01 ns |
| `pvt_output_operating_range` | output rail and common-mode windows passed |
| `pvt_supply_pushing` | pushing_max=0.471 %/V |
| `pvt_reference_compliance` | reference-pin voltage and headroom passed |
| `pvt_power` | power_max=2.125 mW |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/check_supply_pushing_benches.py](../sources/upstream/tasks/sky130-lc-vco-2ghz-pvt/environment/starter/testbench/check_supply_pushing_benches.py) — 夹具、模板或数据处理辅助
- [environment/starter/testbench/tb_supply_pushing_tt_1p62v_27c.spi](../sources/upstream/tasks/sky130-lc-vco-2ghz-pvt/environment/starter/testbench/tb_supply_pushing_tt_1p62v_27c.spi) — tran
- [environment/starter/testbench/tb_supply_pushing_tt_1p98v_27c.spi](../sources/upstream/tasks/sky130-lc-vco-2ghz-pvt/environment/starter/testbench/tb_supply_pushing_tt_1p98v_27c.spi) — tran
- [environment/starter/testbench/tb_tune_ss_1p62v_125c.spi](../sources/upstream/tasks/sky130-lc-vco-2ghz-pvt/environment/starter/testbench/tb_tune_ss_1p62v_125c.spi) — tran
- [environment/starter/testbench/tb_tune_tt_1p8v_27c.spi](../sources/upstream/tasks/sky130-lc-vco-2ghz-pvt/environment/starter/testbench/tb_tune_tt_1p8v_27c.spi) — tran
- [tests/benches/tb_tune.spi](../sources/upstream/tasks/sky130-lc-vco-2ghz-pvt/tests/benches/tb_tune.spi) — tran

## 相邻案例

[14 低功耗 2 MHz 振荡器：缓冲与启动都占功率预算](14-sky130-low-power-oscillator-2mhz-pvt.md) · [24 限流环 VCO：调谐单调性与增益一致性需要独立约束](24-sky130-current-starved-ring-vco-pvt.md) · [43 2.4 GHz LNA：匹配、噪声与稳定性要使用同一端口定义](43-sky130-inductive-lna-2p4ghz-gain12-nf2-pvt.md)
