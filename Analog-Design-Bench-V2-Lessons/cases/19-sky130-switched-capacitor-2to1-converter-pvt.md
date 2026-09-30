---
case_id: adb-v2-19
task_id: sky130-switched-capacitor-2to1-converter-pvt
category: 电源与驱动
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-switched-capacitor-2to1-converter-pvt/instruction.md
  - ../sources/upstream/tasks/sky130-switched-capacitor-2to1-converter-pvt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-switched-capacitor-2to1-converter-pvt/tests/verify.py
  - ../sources/upstream/tasks/sky130-switched-capacitor-2to1-converter-pvt/results/reference.json
---

# 19 · 2:1 开关电容降压：轻载效率揭示固定开关损耗

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

20 MHz，两种电阻负载 680/6800 Ω；45 主矩阵点加无源角落压力，共 47 点，全部储能电容在 DUT 内，0.3–0.7 µs 稳态窗口。

## Reference 拓扑与尺寸线索（静态事实）

两路交错飞跨电容串并联切换并加入非交叠；每路五个大 MIM 单元，输出另有多个 MIM 单元。

## 可复用的工程认识（推断，迁移时有条件）

转换比给出空载中心值，有限电荷转移产生 Rout≈ΔV/I。增加飞跨电容/频率可减小慢开关等效阻抗，但也提高栅驱和底板损耗。参考重载效率约 76–83%、轻载约 38–45%，说明固定时钟损耗会在轻载占主导。

## 不能由 pass 推出的结论

计分纳入各时钟源正向供能且不以回灌能量抵扣，效率口径不能偷换成净功率。没有电容版图或封装验证。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-switched-capacitor-2to1-converter-pvt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-switched-capacitor-2to1-converter-pvt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-switched-capacitor-2to1-converter-pvt)
- [Reference circuit](../sources/upstream/tasks/sky130-switched-capacitor-2to1-converter-pvt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-switched-capacitor-2to1-converter-pvt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-switched-capacitor-2to1-converter-pvt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-switched-capacitor-2to1-converter-pvt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-switched-capacitor-2to1-converter-pvt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-switched-capacitor-2to1-converter-pvt/circuit.spi) · [网站结果快照](../sources/astra/sky130-switched-capacitor-2to1-converter-pvt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-switched-capacitor-2to1-converter-pvt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-14T20:05:26+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `complete_signoff` | heavy=47/47 light=47/47 unique matched points |
| `pvt_loaded_conversion_ratio` | ratio=0.43087 at fs/1.62V/-40C..0.46589 at ff/1.98V/-40C |
| `pvt_efficiency` | efficiency=75.763% at fs/1.62V/-40C..83.447% at ff/1.80V/-40C |
| `pvt_output_ripple` | ripple_max=53.186mVpp at ff/1.98V/-40C |
| `pvt_startup` | startup_max=35.410ns at ss/1.62V/-40C; post_200ns_margin_min=80.241mV at fs/1.62V/-40C |
| `pvt_light_conversion_ratio` | ratio=0.47422 at fs/1.62V/-40C..0.49434 at ff/1.98V/-40C |
| `pvt_light_overhead_power` | input_power=208.101uW at ss/1.62V/-40C..367.013uW at ff/1.98V/+125C |
| `pvt_light_efficiency` | efficiency=38.338% at ff/1.98V/+125C..44.698% at ll/1.80V/+27C |
| `pvt_output_resistance` | Rout=46.451ohm at ff/1.98V/-40C..78.082ohm at ss/1.62V/-40C |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/tb_heavy_tt.spi](../sources/upstream/tasks/sky130-switched-capacitor-2to1-converter-pvt/environment/starter/testbench/tb_heavy_tt.spi) — tran
- [environment/starter/testbench/tb_light_tt.spi](../sources/upstream/tasks/sky130-switched-capacitor-2to1-converter-pvt/environment/starter/testbench/tb_light_tt.spi) — tran
- [tests/benches/tb_heavy.spi](../sources/upstream/tasks/sky130-switched-capacitor-2to1-converter-pvt/tests/benches/tb_heavy.spi) — tran
- [tests/benches/tb_light.spi](../sources/upstream/tasks/sky130-switched-capacitor-2to1-converter-pvt/tests/benches/tb_light.spi) — tran

## 相邻案例

[01 Class-D 半桥：导通损耗与驱动损耗必须一起算](01-sky130-class-d-halfbridge-eff95-tt.md) · [15 开环升压电荷泵：关断状态仍有时钟压力](15-sky130-unregulated-charge-pump-10mhz-pvt.md) · [18 受控升压泵：先确定控制变量和关断边界](18-sky130-regulated-charge-pump-10mhz-pvt.md)
