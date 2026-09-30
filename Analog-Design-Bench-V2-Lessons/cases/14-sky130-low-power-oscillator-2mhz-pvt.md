---
case_id: adb-v2-14
task_id: sky130-low-power-oscillator-2mhz-pvt
category: 时钟与射频
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-low-power-oscillator-2mhz-pvt/instruction.md
  - ../sources/upstream/tasks/sky130-low-power-oscillator-2mhz-pvt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-low-power-oscillator-2mhz-pvt/tests/verify.py
  - ../sources/upstream/tasks/sky130-low-power-oscillator-2mhz-pvt/results/reference.json
---

# 14 · 低功耗 2 MHz 振荡器：缓冲与启动都占功率预算

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

五个代表性 PVT 点，10–20 µs 稳态计频，1.8–2.2 MHz；TT 总功耗≤20 µW，包括外部偏置供能，输出驱动 1 pF。

## Reference 拓扑与尺寸线索（静态事实）

三级限流环、2 µA 外部参考、弱 PMOS 增强及启动不对称，8×8 µm 物理 MIM 负载，施密特输出缓冲。

## 可复用的工程认识（推断，迁移时有条件）

低频功耗不仅是环内充放电，输出 1 pF 的轨到轨翻转、偏置镜及整形级也可能占主导。限流与电容共同设延迟，先检查频率裕量，再看缓冲是否把省下的电流耗掉。

## 不能由 pass 推出的结论

参考最高频率约 2.198 MHz，距离 2.2 MHz 上限很小。这里只支持五个代表点和确定性启动，不支持完整 PVT 或相噪/随机抖动结论。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-low-power-oscillator-2mhz-pvt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-low-power-oscillator-2mhz-pvt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-low-power-oscillator-2mhz-pvt)
- [Reference circuit](../sources/upstream/tasks/sky130-low-power-oscillator-2mhz-pvt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-low-power-oscillator-2mhz-pvt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-low-power-oscillator-2mhz-pvt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-low-power-oscillator-2mhz-pvt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-low-power-oscillator-2mhz-pvt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-low-power-oscillator-2mhz-pvt/circuit.spi) · [网站结果快照](../sources/astra/sky130-low-power-oscillator-2mhz-pvt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-low-power-oscillator-2mhz-pvt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-14T20:02:55+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `pvt_frequency` | range=1.83618MHz at ff/1.98V/-40C .. 2.19846MHz at ff/1.62V/+27C (required 1.8..2.2MHz) |
| `pvt_output_swing` | tightest Vpp=1.62046V at ss/1.62V/-40C; bounds=1.539..1.701V |
| `nominal_power` | 18.9772uW at tt/1.80V/+27C (required <=20uW, including 2uA bias and 1pF load drive) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/tb_osc_ss_hot.spi](../sources/upstream/tasks/sky130-low-power-oscillator-2mhz-pvt/environment/starter/testbench/tb_osc_ss_hot.spi) — tran
- [tests/benches/tb_osc.spi](../sources/upstream/tasks/sky130-low-power-oscillator-2mhz-pvt/tests/benches/tb_osc.spi) — tran

## 相邻案例

[09 宽频 CML 二分频：判定锁定需要周期级证据](09-sky130-cml-divider-div2-range1gto10g.md) · [24 限流环 VCO：调谐单调性与增益一致性需要独立约束](24-sky130-current-starved-ring-vco-pvt.md) · [49 2 GHz LC VCO：调谐范围、pushing 与启动初值分开记录](49-sky130-lc-vco-2ghz-pvt.md)
