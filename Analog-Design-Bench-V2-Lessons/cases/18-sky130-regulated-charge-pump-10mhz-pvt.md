---
case_id: adb-v2-18
task_id: sky130-regulated-charge-pump-10mhz-pvt
category: 电源与驱动
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-regulated-charge-pump-10mhz-pvt/instruction.md
  - ../sources/upstream/tasks/sky130-regulated-charge-pump-10mhz-pvt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-regulated-charge-pump-10mhz-pvt/tests/verify.py
  - ../sources/upstream/tasks/sky130-regulated-charge-pump-10mhz-pvt/results/reference.json
---

# 18 · 受控升压泵：先确定控制变量和关断边界

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

10 MHz、1 ns 时钟边沿及 50 Ω 源，1 nF 输出，1/25/50 µA 负载；八个代表性启用点与五个关闭 DC 点。

## Reference 拓扑与尺寸线索（静态事实）

误差放大器比较 VDD/2 和输出电阻分压，通过 PMOS 改变泵时钟的驱动幅度；电阻几何比对应输出约 1.3·VDD，enable 同时关闭相关偏置。

## 可复用的工程认识（推断，迁移时有条件）

调节电荷泵可以控制时钟摆幅，而不一定改变频率。应把稳态压差、轻重载纹波与关断偏置路径分别读清。参考输出跟随供电比例，不能误认为绝对电压基准。

## 不能由 pass 推出的结论

1 µA 外部偏置未计入 AVDD 指标；没有完整效率或动态负载规范。因此“123 µW 通过”只能按本题定义使用。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-regulated-charge-pump-10mhz-pvt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-regulated-charge-pump-10mhz-pvt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-regulated-charge-pump-10mhz-pvt)
- [Reference circuit](../sources/upstream/tasks/sky130-regulated-charge-pump-10mhz-pvt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-regulated-charge-pump-10mhz-pvt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-regulated-charge-pump-10mhz-pvt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-regulated-charge-pump-10mhz-pvt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-regulated-charge-pump-10mhz-pvt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-regulated-charge-pump-10mhz-pvt/circuit.spi) · [网站结果快照](../sources/astra/sky130-regulated-charge-pump-10mhz-pvt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-regulated-charge-pump-10mhz-pvt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-14T20:04:21+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `pvt_load_regulation` | worst VOUT=2.11424V at ff/1.62V/+125C/1uA; bounds=2.0007..2.2113V |
| `pvt_output_ripple` | worst=0.09mVpp at ff/1.98V/-10C/50uA (required <=5mVpp) |
| `pvt_enabled_current` | worst=123.417uA at ff/1.98V/-10C/50uA (required <=200uA) |
| `pvt_disabled_current` | worst=14.8632nA at ff/1.98V/+125C/powerdown (required <=100nA) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/tb_charge_pump_regulated_ff_hot.spi](../sources/upstream/tasks/sky130-regulated-charge-pump-10mhz-pvt/environment/starter/testbench/tb_charge_pump_regulated_ff_hot.spi) — tran
- [tests/benches/tb_charge_pump_regulated.spi](../sources/upstream/tasks/sky130-regulated-charge-pump-10mhz-pvt/tests/benches/tb_charge_pump_regulated.spi) — tran
- [tests/benches/tb_charge_pump_regulated_pd.spi](../sources/upstream/tasks/sky130-regulated-charge-pump-10mhz-pvt/tests/benches/tb_charge_pump_regulated_pd.spi) — op

## 相邻案例

[15 开环升压电荷泵：关断状态仍有时钟压力](15-sky130-unregulated-charge-pump-10mhz-pvt.md) · [19 2:1 开关电容降压：轻载效率揭示固定开关损耗](19-sky130-switched-capacitor-2to1-converter-pvt.md) · [11 带隙基准：温度补偿、启动和噪声是三件事](11-sky130-bandgap-reference-pvt.md)
