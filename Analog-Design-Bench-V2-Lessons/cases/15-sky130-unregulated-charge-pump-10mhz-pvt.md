---
case_id: adb-v2-15
task_id: sky130-unregulated-charge-pump-10mhz-pvt
category: 电源与驱动
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-unregulated-charge-pump-10mhz-pvt/instruction.md
  - ../sources/upstream/tasks/sky130-unregulated-charge-pump-10mhz-pvt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-unregulated-charge-pump-10mhz-pvt/tests/verify.py
  - ../sources/upstream/tasks/sky130-unregulated-charge-pump-10mhz-pvt/results/reference.json
---

# 15 · 开环升压电荷泵：关断状态仍有时钟压力

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

固定 1.8 V、八个工艺/温度点，10 MHz 时钟，1 nF 外部输出、50 µA 负载；190–200 µs 取稳态，输出 2.2–2.8 V、纹波≤5 mV。

## Reference 拓扑与尺寸线索（静态事实）

交叉耦合的 5 V/native NMOS 及 MIM 飞跨电容，两相驱动并带 enable 门控。

## 可复用的工程认识（推断，迁移时有条件）

输出电压由理想升压值扣除开关压降与等效电阻压降，不能仅用电容比推断。启用功耗与“时钟继续运行但 enable 关闭”的漏电是两种约束；门控位置决定关断后哪些节点仍翻转。

## 不能由 pass 推出的结论

这里的时钟源边沿是 1 ps，与受控泵任务不同；不能直接把功耗差归因于调节环路。原网表出现不同乘数拼写，迁移时要遵守具体 wrapper，勿当通用 SPICE 别名。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-unregulated-charge-pump-10mhz-pvt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-unregulated-charge-pump-10mhz-pvt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-unregulated-charge-pump-10mhz-pvt)
- [Reference circuit](../sources/upstream/tasks/sky130-unregulated-charge-pump-10mhz-pvt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-unregulated-charge-pump-10mhz-pvt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-unregulated-charge-pump-10mhz-pvt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-unregulated-charge-pump-10mhz-pvt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-unregulated-charge-pump-10mhz-pvt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-unregulated-charge-pump-10mhz-pvt/circuit.spi) · [网站结果快照](../sources/astra/sky130-unregulated-charge-pump-10mhz-pvt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-unregulated-charge-pump-10mhz-pvt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-14T20:03:58+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `pvt_loaded_output_voltage` | range=2.35616V at ss/1.8V/-10C .. 2.68624V at ff/1.8V/+125C (required 2.2..2.8V) |
| `pvt_output_ripple` | worst=3.26mVpp at sf/1.8V/-10C (required <=5mVpp) |
| `pvt_enabled_current` | worst=136.114uA at ss/1.8V/-10C (required <=200uA) |
| `pvt_disabled_current` | worst=9.02651nA at ff/1.8V/+125C (required <=100nA) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/tb_charge_pump_ff_hot.spi](../sources/upstream/tasks/sky130-unregulated-charge-pump-10mhz-pvt/environment/starter/testbench/tb_charge_pump_ff_hot.spi) — tran
- [environment/starter/testbench/tb_charge_pump_pd_ff_hot.spi](../sources/upstream/tasks/sky130-unregulated-charge-pump-10mhz-pvt/environment/starter/testbench/tb_charge_pump_pd_ff_hot.spi) — tran
- [tests/benches/tb_charge_pump.spi](../sources/upstream/tasks/sky130-unregulated-charge-pump-10mhz-pvt/tests/benches/tb_charge_pump.spi) — tran
- [tests/benches/tb_charge_pump_pd.spi](../sources/upstream/tasks/sky130-unregulated-charge-pump-10mhz-pvt/tests/benches/tb_charge_pump_pd.spi) — tran

## 相邻案例

[18 受控升压泵：先确定控制变量和关断边界](18-sky130-regulated-charge-pump-10mhz-pvt.md) · [19 2:1 开关电容降压：轻载效率揭示固定开关损耗](19-sky130-switched-capacitor-2to1-converter-pvt.md) · [05 高侧自举驱动：以源极为参考检查 VGS](05-sky130-bootstrap-driver-pt.md)
