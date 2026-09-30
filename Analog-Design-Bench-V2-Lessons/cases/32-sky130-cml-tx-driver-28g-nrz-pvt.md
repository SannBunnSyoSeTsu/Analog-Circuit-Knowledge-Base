---
case_id: adb-v2-32
task_id: sky130-cml-tx-driver-28g-nrz-pvt
category: 时钟与射频
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-cml-tx-driver-28g-nrz-pvt/instruction.md
  - ../sources/upstream/tasks/sky130-cml-tx-driver-28g-nrz-pvt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-cml-tx-driver-28g-nrz-pvt/tests/verify.py
  - ../sources/upstream/tasks/sky130-cml-tx-driver-28g-nrz-pvt/results/reference.json
---

# 32 · 28 Gb/s CML 发射器：带宽还需眼图和群延迟约束

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

三个配对点：ss/1.62 V/−40 °C、tt/1.8 V/27 °C、ff/1.98 V/125 °C；输入每端 50 Ω/30 fF，输出每端 50 Ω 至 VDD 与 100 fF。

## Reference 拓扑与尺寸线索（静态事实）

直接 CML 差分对交叉输出实现正极性，尾管总宽约 850 µm；15 fF 交叉中和，输出 T-coil 每段 280 pH、k=0.4 和 15 fF 桥接。

## 可复用的工程认识（推断，迁移时有条件）

峰化网络提高带宽的同时会改变群延迟和过冲，所以需要 AC 平坦度、逐位符号正确性、PRBS7 眼高、过冲以及零交叉误差共同约束。功率必须包含外部终端从 VDD 取走的电流。

## 不能由 pass 推出的结论

理想 L/K 没有线圈损耗、耦合寄生或 EM 实现证据；约 1 ps 的发布抖动是去平均后的确定性图样抖动，不包含噪声、串扰和封装。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-cml-tx-driver-28g-nrz-pvt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-cml-tx-driver-28g-nrz-pvt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-cml-tx-driver-28g-nrz-pvt)
- [Reference circuit](../sources/upstream/tasks/sky130-cml-tx-driver-28g-nrz-pvt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-cml-tx-driver-28g-nrz-pvt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-cml-tx-driver-28g-nrz-pvt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-cml-tx-driver-28g-nrz-pvt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-cml-tx-driver-28g-nrz-pvt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-cml-tx-driver-28g-nrz-pvt/circuit.spi) · [网站结果快照](../sources/astra/sky130-cml-tx-driver-28g-nrz-pvt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-cml-tx-driver-28g-nrz-pvt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-14T20:06:35+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `differential_swing` | min=429.3mV at ff (need 400-900mV) |
| `output_common_mode` | worst range margin=181.212mV at ff/vocm0 (required >=0mV) |
| `common_mode_shift` | max=0.00mV (max 30mV) |
| `output_rail_range_static` | worst range margin=241.794mV at ss/vn0 (required >=0mV) |
| `static_offset` | max=0.00mV at ff (max 20mV) |
| `vdd_current_balance` | max=0.00% at tt (max 10%) |
| `gain_100mhz` | worst=1.441V/V at ff (need 1.3-4.0) |
| `bandwidth_22ghz` | worst=26.53GHz at ff (min 22GHz) |
| `passband_peaking` | worst=-0.000dB at ss (max 1.5dB) |
| `group_delay_variation` | worst=0.022ps at ss (max 8ps) |
| `eye_height` | worst=429.3mV at ff (min 320mV) |
| `eye_sign` | worst=0 errors at ss (need 0) |
| `rise_fall_time_28g` | worst=12.14ps at ff (max 15ps) |
| `overshoot_undershoot` | worst=6.89% at ss (max 12%) |
| `vocm_deviation_transient` | worst=3.56mV at ss (max 50mV) |
| `output_rail_range_transient` | worst range margin=222.761mV at ss (required >=0mV) |
| `jitter_pp` | worst=1.049ps at ss (max 5.0ps) |
| `jitter_rms` | worst=0.430ps at ss (max 1.5ps) |
| `dcd` | worst=0.011ps at ss (max 2.0ps) |
| `average_power` | worst=29.39mW at ff (max 45mW) |
| `sensitivity_swing` | worst=302.8mV at ff (min 250mV) |
| `sensitivity_sign` | worst=0 errors at ss (need 0) |
| `sensitivity_rise_fall` | worst=13.22ps at ss (max 17ps) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/analyze_ac.py](../sources/upstream/tasks/sky130-cml-tx-driver-28g-nrz-pvt/environment/starter/testbench/analyze_ac.py) — 夹具、模板或数据处理辅助
- [environment/starter/testbench/analyze_prbs7.py](../sources/upstream/tasks/sky130-cml-tx-driver-28g-nrz-pvt/environment/starter/testbench/analyze_prbs7.py) — 夹具、模板或数据处理辅助
- [environment/starter/testbench/analyze_sensitivity.py](../sources/upstream/tasks/sky130-cml-tx-driver-28g-nrz-pvt/environment/starter/testbench/analyze_sensitivity.py) — 夹具、模板或数据处理辅助
- [environment/starter/testbench/gen_prbs7.py](../sources/upstream/tasks/sky130-cml-tx-driver-28g-nrz-pvt/environment/starter/testbench/gen_prbs7.py) — 夹具、模板或数据处理辅助
- [environment/starter/testbench/gen_sensitivity.py](../sources/upstream/tasks/sky130-cml-tx-driver-28g-nrz-pvt/environment/starter/testbench/gen_sensitivity.py) — 夹具、模板或数据处理辅助
- [environment/starter/testbench/tb_ac_tt.spi](../sources/upstream/tasks/sky130-cml-tx-driver-28g-nrz-pvt/environment/starter/testbench/tb_ac_tt.spi) — ac
- [environment/starter/testbench/tb_prbs7_tt.spi](../sources/upstream/tasks/sky130-cml-tx-driver-28g-nrz-pvt/environment/starter/testbench/tb_prbs7_tt.spi) — tran
- [environment/starter/testbench/tb_sensitivity_tt.spi](../sources/upstream/tasks/sky130-cml-tx-driver-28g-nrz-pvt/environment/starter/testbench/tb_sensitivity_tt.spi) — tran
- [environment/starter/testbench/tb_static_tt.spi](../sources/upstream/tasks/sky130-cml-tx-driver-28g-nrz-pvt/environment/starter/testbench/tb_static_tt.spi) — op
- [tests/benches/tb_ac.spi](../sources/upstream/tasks/sky130-cml-tx-driver-28g-nrz-pvt/tests/benches/tb_ac.spi) — ac
- [tests/benches/tb_prbs7.spi](../sources/upstream/tasks/sky130-cml-tx-driver-28g-nrz-pvt/tests/benches/tb_prbs7.spi) — tran
- [tests/benches/tb_sensitivity.spi](../sources/upstream/tasks/sky130-cml-tx-driver-28g-nrz-pvt/tests/benches/tb_sensitivity.spi) — tran
- [tests/benches/tb_static.spi](../sources/upstream/tasks/sky130-cml-tx-driver-28g-nrz-pvt/tests/benches/tb_static.spi) — op

## 相邻案例

[09 宽频 CML 二分频：判定锁定需要周期级证据](09-sky130-cml-divider-div2-range1gto10g.md) · [43 2.4 GHz LNA：匹配、噪声与稳定性要使用同一端口定义](43-sky130-inductive-lna-2p4ghz-gain12-nf2-pvt.md) · [49 2 GHz LC VCO：调谐范围、pushing 与启动初值分开记录](49-sky130-lc-vco-2ghz-pvt.md)
