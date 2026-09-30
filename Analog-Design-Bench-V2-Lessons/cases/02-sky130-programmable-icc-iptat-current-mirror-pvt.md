---
case_id: adb-v2-02
task_id: sky130-programmable-icc-iptat-current-mirror-pvt
category: 偏置与基准
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: true
derived_from:
  - ../sources/upstream/tasks/sky130-programmable-icc-iptat-current-mirror-pvt/instruction.md
  - ../sources/upstream/tasks/sky130-programmable-icc-iptat-current-mirror-pvt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-programmable-icc-iptat-current-mirror-pvt/tests/verify.py
  - ../sources/upstream/tasks/sky130-programmable-icc-iptat-current-mirror-pvt/results/reference.json
---

# 02 · 可编程 ICC/IPTAT 镜：比例正确还不够

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

两个电流输入形成四组互补权重，额定各 50 µA 时保持总输出约 1 mA；判据还涉及 PVT、输出电压扫描、权重误差及输出电阻。完整矩阵以原说明和 verifier 为准。

## Reference 拓扑与尺寸线索（静态事实）

参考支路与输出电流镜统一 L=0.5 µm，ICC 权重 16/12/8/4，IPTAT 权重 4/8/12/16，分段开关后接输出共栅管。

## 可复用的工程认识（推断，迁移时有条件）

尺寸比例应建立在相同沟道长度与相近工作点上。reference 注释记载旧设计用 L=0.15 µm 的二极管对 L=0.5 µm 输出管，名义补偿后跨角落仍出现约 +51%/−38% 偏移；这属于作者历史记录。可复用的是同 L、控制 VDS 差及降低沟道长度调制敏感性，而不是只修正 TT 的 W 比。

## 不能由 pass 推出的结论

Astra R1 使用长 L 与另一种分段方式，见专文。静态四码通过不证明切码毛刺、局部失配或温度系数的系统精度。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-programmable-icc-iptat-current-mirror-pvt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-programmable-icc-iptat-current-mirror-pvt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-programmable-icc-iptat-current-mirror-pvt)
- [Reference circuit](../sources/upstream/tasks/sky130-programmable-icc-iptat-current-mirror-pvt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-programmable-icc-iptat-current-mirror-pvt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-programmable-icc-iptat-current-mirror-pvt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-programmable-icc-iptat-current-mirror-pvt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-programmable-icc-iptat-current-mirror-pvt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-programmable-icc-iptat-current-mirror-pvt/circuit.spi) · [网站结果快照](../sources/astra/sky130-programmable-icc-iptat-current-mirror-pvt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-programmable-icc-iptat-current-mirror-pvt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 已做定向电路比较，见 [Astra 对照](../topics/08-astra-comparisons.md)。

Reference 结果生成时间：`2026-08-14T19:59:44+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `output_current_error` | max=5.04% at ff/code11 (max 8%) |
| `output_current_positive` | min Iout=0.000732668A at ss/code11 (required >0A) |
| `weight_accuracy` | max=8.65% at ff/code11 (max 10%) |
| `ratio_accuracy` | max=0.78% at ff/code11 (max 10%) |
| `reference_pin_headroom` | icc_ref 0.705..0.815V; iptat_ref 0.736..0.798V (required 0.20..1.10V, nominal+perturbed) |
| `reference_pin_isolation_perturbation` | max=0.00mV at tt/code00 (max 25mV) |
| `reference_pin_isolation_code` | max=0.00mV at tt/code00 (max 50mV) |
| `static_vdd_current` | max=4.52uA at ff/code11 (max 100uA) |
| `digital_pin_current` | max=0.000uA at tt/code00 (max 1uA) |
| `compliance_flatness` | max=1.66% at ss/code11 (max 3%) |
| `output_resistance` | min=294.1kohm at ff/code11 (min 100kohm) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/tb_codes_tt.spi](../sources/upstream/tasks/sky130-programmable-icc-iptat-current-mirror-pvt/environment/starter/testbench/tb_codes_tt.spi) — dc, op
- [environment/starter/testbench/tb_compliance_tt.spi](../sources/upstream/tasks/sky130-programmable-icc-iptat-current-mirror-pvt/environment/starter/testbench/tb_compliance_tt.spi) — dc
- [environment/starter/testbench/tb_power_tt.spi](../sources/upstream/tasks/sky130-programmable-icc-iptat-current-mirror-pvt/environment/starter/testbench/tb_power_tt.spi) — op
- [environment/starter/testbench/tb_temperature_ff.spi](../sources/upstream/tasks/sky130-programmable-icc-iptat-current-mirror-pvt/environment/starter/testbench/tb_temperature_ff.spi) — op
- [environment/starter/testbench/tb_temperature_ss.spi](../sources/upstream/tasks/sky130-programmable-icc-iptat-current-mirror-pvt/environment/starter/testbench/tb_temperature_ss.spi) — op
- [environment/starter/testbench/tb_temperature_tt.spi](../sources/upstream/tasks/sky130-programmable-icc-iptat-current-mirror-pvt/environment/starter/testbench/tb_temperature_tt.spi) — op
- [tests/benches/tb_codes_weights.spi](../sources/upstream/tasks/sky130-programmable-icc-iptat-current-mirror-pvt/tests/benches/tb_codes_weights.spi) — dc, op
- [tests/benches/tb_compliance.spi](../sources/upstream/tasks/sky130-programmable-icc-iptat-current-mirror-pvt/tests/benches/tb_compliance.spi) — dc
- [tests/fixtures/iptat_series_r_headroom_violation.spi](../sources/upstream/tasks/sky130-programmable-icc-iptat-current-mirror-pvt/tests/fixtures/iptat_series_r_headroom_violation.spi) — 夹具、模板或数据处理辅助

## 相邻案例

[12 β 倍增偏置：恒 gm 条件来自器件比和电阻](12-sky130-beta-multiplier-reference-pvt-mc.md) · [13 恒 gm 稳增益：偏置单元必须映射到输入电流密度](13-sky130-constant-gm-stable-gain-amplifier-pvt.md) · [47 PLL 电荷泵：静态匹配与短脉冲电荷是两套预算](47-sky130-pll-charge-pump-pvt.md)
