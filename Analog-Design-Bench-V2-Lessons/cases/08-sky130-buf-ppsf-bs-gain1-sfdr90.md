---
case_id: adb-v2-08
task_id: sky130-buf-ppsf-bs-gain1-sfdr90
category: 放大器与滤波
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-buf-ppsf-bs-gain1-sfdr90/instruction.md
  - ../sources/upstream/tasks/sky130-buf-ppsf-bs-gain1-sfdr90/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-buf-ppsf-bs-gain1-sfdr90/tests/verify.py
  - ../sources/upstream/tasks/sky130-buf-ppsf-bs-gain1-sfdr90/results/reference.json
---

# 08 · 自举互补源跟随器：小输入电流不等于小物理电容

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

五角落、1.8 V/27 °C，差分每端 1 pF；0.8 V 差分峰值，1/11/41 MHz SFDR 门槛分别 90/80/70 dB，40 MHz 输入电流也受限。

## Reference 拓扑与尺寸线索（静态事实）

LVT 推挽源跟随器，大量 5 pF / 1 MΩ 自举网络，若干体端随源极。

## 可复用的工程认识（推断，迁移时有条件）

自举让电容两端共同运动，可减小信号源所见交流电流；40 MHz、0.8 V 峰值、20 µA 相当于约 100 fF 的纯容性输入量级，但这不是实际电容总面积。bench 另外约束基波增益，避免靠衰减信号获得高 SFDR。

## 不能由 pass 推出的结论

体源连接能减弱体效应，但隔离阱和版图可实现性未由原理图测试证明。未覆盖供电、温度和局部失配；不能将 SFDR 当作包含随机噪声的 SNDR。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-buf-ppsf-bs-gain1-sfdr90/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-buf-ppsf-bs-gain1-sfdr90/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-buf-ppsf-bs-gain1-sfdr90)
- [Reference circuit](../sources/upstream/tasks/sky130-buf-ppsf-bs-gain1-sfdr90/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-buf-ppsf-bs-gain1-sfdr90/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-buf-ppsf-bs-gain1-sfdr90/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-buf-ppsf-bs-gain1-sfdr90/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-buf-ppsf-bs-gain1-sfdr90/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-buf-ppsf-bs-gain1-sfdr90/circuit.spi) · [网站结果快照](../sources/astra/sky130-buf-ppsf-bs-gain1-sfdr90/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-buf-ppsf-bs-gain1-sfdr90/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-14T20:00:58+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `input_current_gate` | max 40 MHz differential input current=17.454 uA, equivalent capacitance=86.811 fF (requirement <20 uA) |
| `gain_1m_to_40m` | min gain=0.99531 V/V (requirement >0.99) |
| `sfdr_1m_11m_41m` | worst SFDR=92.102 dB (requirement >90 dB); minimum transient fundamental gain=0.99640 V/V (requirement >0.95); worst SFDR=87.507 dB (requirement >80 dB); minimum transient fundamental gain=0.99636 V/V (requirement >0.95); worst SFDR=72.576 dB (requirement >70 dB); minimum transient fundamental gain=0.99057 V/V (requirement >0.95) |
| `dc_power` | max power=0.78191 mW (requirement <1.0 mW) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/measure_sfdr.py](../sources/upstream/tasks/sky130-buf-ppsf-bs-gain1-sfdr90/environment/starter/testbench/measure_sfdr.py) — 夹具、模板或数据处理辅助
- [environment/starter/testbench/run_ac_process_sweep.py](../sources/upstream/tasks/sky130-buf-ppsf-bs-gain1-sfdr90/environment/starter/testbench/run_ac_process_sweep.py) — 夹具、模板或数据处理辅助
- [environment/starter/testbench/run_ac_pvt_sweep.py](../sources/upstream/tasks/sky130-buf-ppsf-bs-gain1-sfdr90/environment/starter/testbench/run_ac_pvt_sweep.py) — 夹具、模板或数据处理辅助
- [environment/starter/testbench/run_sfdr_process_sweep.py](../sources/upstream/tasks/sky130-buf-ppsf-bs-gain1-sfdr90/environment/starter/testbench/run_sfdr_process_sweep.py) — 夹具、模板或数据处理辅助
- [environment/starter/testbench/tb_ac_power.spi](../sources/upstream/tasks/sky130-buf-ppsf-bs-gain1-sfdr90/environment/starter/testbench/tb_ac_power.spi) — ac, op
- [environment/starter/testbench/tb_sfdr.spi](../sources/upstream/tasks/sky130-buf-ppsf-bs-gain1-sfdr90/environment/starter/testbench/tb_sfdr.spi) — tran
- [tests/benches/tb_ac_power.spi](../sources/upstream/tasks/sky130-buf-ppsf-bs-gain1-sfdr90/tests/benches/tb_ac_power.spi) — ac, op
- [tests/benches/tb_sfdr.spi](../sources/upstream/tasks/sky130-buf-ppsf-bs-gain1-sfdr90/tests/benches/tb_sfdr.spi) — tran

## 相邻案例

[10 宽带 TIA：跨阻、输入噪声与大信号不能分开定规格](10-sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt.md) · [22 自举采样驱动：VGS 平坦要与采样失真一起看](22-sky130-bootstrap-sampler-fft.md) · [31 底板采样：存储电压必须按两端差计算](31-sky130-bottom-plate-sampler-pvt.md)
