---
case_id: adb-v2-06
task_id: sky130-ring-amp-3stage-gain8-400uw
category: 采样与数据转换
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: true
derived_from:
  - ../sources/upstream/tasks/sky130-ring-amp-3stage-gain8-400uw/instruction.md
  - ../sources/upstream/tasks/sky130-ring-amp-3stage-gain8-400uw/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-ring-amp-3stage-gain8-400uw/tests/verify.py
  - ../sources/upstream/tasks/sky130-ring-amp-3stage-gain8-400uw/results/reference.json
---

# 06 · 三级 Ring Amp：电容比、死区与动态终止共同定增益

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

TT/1.8 V/27 °C；13 引脚包含外部复位/偏置接口，每端 10 pF，500 ns 周期含 50 ns 自动调零，在第三周期测量。目标增益 8、放大相功耗≤400 µW、10% 误差带建立≤50 ns。

## Reference 拓扑与尺寸线索（静态事实）

参考采样/反馈电容 800/100 fF；三级放大路径配独立上下拉控制。输入处的 1 GH 理想电感提供直流通路，在信号动态频段呈高阻，交流信号经并联的 800 fF 电容耦合。注释记录一次不合适的 PDK 几何分指被改为并联 nf=1 器件。

## 可复用的工程认识（推断，迁移时有条件）

Cs/Cf 是起点；实际闭环增益还受有限增益、死区和测量时刻影响。bench 同时用两种输入差值求斜率并检查零输入残留，防止把固定输出跳变当增益。建立时间、静态误差及输出共模必须分别满足。

## 不能由 pass 推出的结论

外部自动调零与复位、超大理想电感均属于抽象条件；不是独立工作的完整 ADC 放大器。reference 扁平 metrics 中 static_error 的单位标注有歧义，应按检查消息/计算式理解为相对误差。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-ring-amp-3stage-gain8-400uw/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-ring-amp-3stage-gain8-400uw/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-ring-amp-3stage-gain8-400uw)
- [Reference circuit](../sources/upstream/tasks/sky130-ring-amp-3stage-gain8-400uw/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-ring-amp-3stage-gain8-400uw/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-ring-amp-3stage-gain8-400uw/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-ring-amp-3stage-gain8-400uw/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-ring-amp-3stage-gain8-400uw/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-ring-amp-3stage-gain8-400uw/circuit.spi) · [网站结果快照](../sources/astra/sky130-ring-amp-3stage-gain8-400uw/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-ring-amp-3stage-gain8-400uw/runs/gpt-6-astra-thinking-max/run-1)

该 R1 已做定向电路比较，见 [Astra 对照](../topics/08-astra-comparisons.md)。

Reference 结果生成时间：`2026-08-14T19:59:51+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `gain_transfer` | gain_positive=8.037 gain_bipolar=8.027 (each target [7.2, 8.8]) |
| `gain_zero_input` | zero_input_residual=0.000857 (<= 0.005) |
| `static_error` | worst_static_error=0.004537 (<= 0.01) |
| `vout_cm` | worst_vout_cm_error=0.03914 (<= 0.05) |
| `power` | worst_power_w=0.0002881 (<= 0.0004) |
| `settle_ns` | worst_settle_ns=43.3 ns (<= 50 ns) |
| `ripple` | worst_ripple=7.414e-06 (<= 0.005) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/tb_sc_dev.spi](../sources/upstream/tasks/sky130-ring-amp-3stage-gain8-400uw/environment/starter/testbench/tb_sc_dev.spi) — tran
- [tests/benches/tb_sc_tran.spi](../sources/upstream/tasks/sky130-ring-amp-3stage-gain8-400uw/tests/benches/tb_sc_tran.spi) — tran
- [tests/benches/tb_sc_tran_b.spi](../sources/upstream/tasks/sky130-ring-amp-3stage-gain8-400uw/tests/benches/tb_sc_tran_b.spi) — tran
- [tests/benches/tb_sc_tran_c.spi](../sources/upstream/tasks/sky130-ring-amp-3stage-gain8-400uw/tests/benches/tb_sc_tran_c.spi) — tran
- [tests/benches/tb_sc_tran_d.spi](../sources/upstream/tasks/sky130-ring-amp-3stage-gain8-400uw/tests/benches/tb_sc_tran_d.spi) — tran

## 相邻案例

[28 FCT 残差放大器：保持稳定度不是目标建立误差](28-sky130-fct-residue-amplifier-900msps.md) · [33 增益 1 采样反馈 OTA：差模建立和 CMFB 要分开验收](33-sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc.md) · [34 增益 8 采样反馈 OTA：β=1/9 决定环路速度](34-sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc.md)
