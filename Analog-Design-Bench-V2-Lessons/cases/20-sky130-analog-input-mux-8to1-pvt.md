---
case_id: adb-v2-20
task_id: sky130-analog-input-mux-8to1-pvt
category: 采样与数据转换
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-analog-input-mux-8to1-pvt/instruction.md
  - ../sources/upstream/tasks/sky130-analog-input-mux-8to1-pvt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-analog-input-mux-8to1-pvt/tests/verify.py
  - ../sources/upstream/tasks/sky130-analog-input-mux-8to1-pvt/results/reference.json
---

# 20 · 8:1 模拟 MUX：Ron、关断耦合与输入源阻抗相互牵制

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

五个代表性 PVT × 三个共模 × 八个选码，120 状态；每状态测八路传输，要求低频插损、1 MHz 隔离、带宽与静态电流。

## Reference 拓扑与尺寸线索（静态事实）

三级传输门树，共 14 个 TG 和三个反相控制，NMOS/PMOS 尺寸按导通能力配比。

## 可复用的工程认识（推断，迁移时有条件）

做大开关降低 Ron，但关断通道的结电容和栅漏耦合也增加。每个选码检查所有未选输入，比只测相邻一路更能发现树形路径泄漏。输入源与电源串联 50 Ω 避免理想源钳位掩盖耦合。

## 不能由 pass 推出的结论

AC 隔离不能代表切码电荷注入或大信号失真；本任务未给出这些动态验收。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-analog-input-mux-8to1-pvt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-analog-input-mux-8to1-pvt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-analog-input-mux-8to1-pvt)
- [Reference circuit](../sources/upstream/tasks/sky130-analog-input-mux-8to1-pvt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-analog-input-mux-8to1-pvt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-analog-input-mux-8to1-pvt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-analog-input-mux-8to1-pvt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-analog-input-mux-8to1-pvt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-analog-input-mux-8to1-pvt/circuit.spi) · [网站结果快照](../sources/astra/sky130-analog-input-mux-8to1-pvt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-analog-input-mux-8to1-pvt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-15T08:17:11+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `pvt_selected_gain` | range=-0.000286639dB at ss/1.62V/+125C/VCM=0.81V/S=0 .. 0dB at tt/1.80V/+40C/VCM=0.9V/S=2 (required -0.001..0.001dB) |
| `pvt_crosstalk_dc` | worst=-112.059dB at ss/1.62V/+125C/VCM=0V/S=4 from VIN0 (required <=-80dB at 1mHz) |
| `pvt_crosstalk_1mhz` | worst=-81.8418dB at ss/1.62V/+125C/VCM=0V/S=0 from VIN4 (required <=-80dB at 1MHz) |
| `pvt_selected_bandwidth` | worst 3dB bandwidth=17.3061MHz at ss/1.62V/+125C/VCM=0.81V/S=0 (required >=5MHz) |
| `pvt_supply_current` | worst=0.722615uA at fs/1.98V/+125C/VCM=0V/S=7 (required <=5uA) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/analyze_mux.py](../sources/upstream/tasks/sky130-analog-input-mux-8to1-pvt/environment/starter/testbench/analyze_mux.py) — ac
- [environment/starter/testbench/tb_mux.spi](../sources/upstream/tasks/sky130-analog-input-mux-8to1-pvt/environment/starter/testbench/tb_mux.spi) — ac, op
- [tests/benches/tb_mux.spi](../sources/upstream/tasks/sky130-analog-input-mux-8to1-pvt/tests/benches/tb_mux.spi) — ac, op
- [tests/fixtures/stuck_output.spi](../sources/upstream/tasks/sky130-analog-input-mux-8to1-pvt/tests/fixtures/stuck_output.spi) — 夹具、模板或数据处理辅助
- [tests/fixtures/wrong_select.spi](../sources/upstream/tasks/sky130-analog-input-mux-8to1-pvt/tests/fixtures/wrong_select.spi) — 夹具、模板或数据处理辅助

## 相邻案例

[22 自举采样驱动：VGS 平坦要与采样失真一起看](22-sky130-bootstrap-sampler-fft.md) · [23 5 bit 电阻 DAC：分母由固定支路决定](23-sky130-cmos-switched-resistor-dac-5bit-pvt.md) · [31 底板采样：存储电压必须按两端差计算](31-sky130-bottom-plate-sampler-pvt.md)
