---
case_id: adb-v2-01
task_id: sky130-class-d-halfbridge-eff95-tt
category: 电源与驱动
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-class-d-halfbridge-eff95-tt/instruction.md
  - ../sources/upstream/tasks/sky130-class-d-halfbridge-eff95-tt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-class-d-halfbridge-eff95-tt/tests/verify.py
  - ../sources/upstream/tasks/sky130-class-d-halfbridge-eff95-tt/results/reference.json
---

# 01 · Class-D 半桥：导通损耗与驱动损耗必须一起算

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

5 MHz、50% 占空比、50 Ω 时钟源；外部 3 µH / 345 pF 滤波及七档 1–16 Ω 负载。检查 TT 的 27/125 °C，功率取 18–20 µs 稳态窗口，效率计入时钟供能。

## Reference 拓扑与尺寸线索（静态事实）

交叉耦合 NAND 产生互锁，延迟链设死区，四级渐大缓冲驱动功率管。PMOS w=50 µm、m=4096，NMOS LVT w=50 µm、m=1024，所用总宽非常大。

## 可复用的工程认识（推断，迁移时有条件）

减小导通电阻会增加栅电荷和驱动损耗，不能只按 I²R 选宽度。死区同时影响交叠电流与体二极管导通；必须把负载扫描、温度与驱动链放进同一个损耗预算。七档负载使单个最优效率点不足以代表可用范围。

## 不能由 pass 推出的结论

没有面积、布线、电迁移或音频 THD 结论。如此大的并联倍数只是原理图模型下的可行解，不能直接变成版图尺寸。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-class-d-halfbridge-eff95-tt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-class-d-halfbridge-eff95-tt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-class-d-halfbridge-eff95-tt)
- [Reference circuit](../sources/upstream/tasks/sky130-class-d-halfbridge-eff95-tt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-class-d-halfbridge-eff95-tt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-class-d-halfbridge-eff95-tt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-class-d-halfbridge-eff95-tt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-class-d-halfbridge-eff95-tt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-class-d-halfbridge-eff95-tt/circuit.spi) · [网站结果快照](../sources/astra/sky130-class-d-halfbridge-eff95-tt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-class-d-halfbridge-eff95-tt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-14T20:03:17+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `e1_peak_eff_27c_95pct` | peak_27c=95.20% (limit > 95%) |
| `e2_all_eff_27c_85pct` | min_27c=85.37% at 1ohm (limit > 85%) |
| `e3_peak_eff_125c_90pct` | peak_125c=93.44% (limit > 90%) |
| `e4_all_eff_125c_80pct` | min_125c=82.78% at 16ohm (limit > 80%) |
| `e5_min_output_power_30mw` | min_p_out=40.26mW (limit > 30mW) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/tb_class_d_tt_1p80v_27c.spi](../sources/upstream/tasks/sky130-class-d-halfbridge-eff95-tt/environment/starter/testbench/tb_class_d_tt_1p80v_27c.spi) — tran
- [tests/benches/tb_efficiency.spi](../sources/upstream/tasks/sky130-class-d-halfbridge-eff95-tt/tests/benches/tb_efficiency.spi) — tran

## 相邻案例

[05 高侧自举驱动：以源极为参考检查 VGS](05-sky130-bootstrap-driver-pt.md) · [19 2:1 开关电容降压：轻载效率揭示固定开关损耗](19-sky130-switched-capacitor-2to1-converter-pvt.md) · [39 低功耗线路驱动：Class-AB 的价值是峰值/静态电流比](39-sky130-low-power-line-driver-pvt.md)
