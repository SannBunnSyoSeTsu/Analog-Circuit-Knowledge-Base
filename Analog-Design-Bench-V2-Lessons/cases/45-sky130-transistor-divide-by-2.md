---
case_id: adb-v2-45
task_id: sky130-transistor-divide-by-2
category: 时钟与射频
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-transistor-divide-by-2/instruction.md
  - ../sources/upstream/tasks/sky130-transistor-divide-by-2/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-transistor-divide-by-2/tests/verify.py
  - ../sources/upstream/tasks/sky130-transistor-divide-by-2/results/reference.json
---

# 45 · 晶体管二分频：复位必须清除内部状态

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

TT、1 GHz、20 fF；异步高有效复位≤100 ps，释放后等下一有效时钟才翻转，输出 500 MHz、占空比 49–51%、传播≤400 ps。

## Reference 拓扑与尺寸线索（静态事实）

TG 主从触发器，复位 NOR 放入从锁存器回路；Qbar 经三级缓冲反馈，时钟反相器加大驱动。

## 可复用的工程认识（推断，迁移时有条件）

只在输出端加钳位不能保证内部锁存状态被清除，释放时会泄漏旧状态或立即翻转。先从主从透明窗口与复位路径验证逻辑，再看门尺寸对竞争和时钟偏斜的影响。

## 不能由 pass 推出的结论

该题复位语义比 CML 分频题明确，但只测 TT；没有 setup/hold 全扫描、亚稳态统计或全 PVT 保证。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-transistor-divide-by-2/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-transistor-divide-by-2/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-transistor-divide-by-2)
- [Reference circuit](../sources/upstream/tasks/sky130-transistor-divide-by-2/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-transistor-divide-by-2/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-transistor-divide-by-2/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-transistor-divide-by-2/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-transistor-divide-by-2/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-transistor-divide-by-2/circuit.spi) · [网站结果快照](../sources/astra/sky130-transistor-divide-by-2/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-transistor-divide-by-2/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-15T13:43:09Z`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `reset` | delay=0.0773ns; pre/asserted/release/next=1.8/0.004928/0.002661/1.8V |
| `frequency` | input=1GHz; output=500MHz; ratio=2.00013 |
| `duty_cycle` | high duty=49.901/49.891/49.891%; low duty=50.099/50.109/50.109%; levels passed |
| `clock_to_output_delay` | delays=251.992/252.386/252.386/252.386ps |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/tb_reset_tt.spi](../sources/upstream/tasks/sky130-transistor-divide-by-2/environment/starter/testbench/tb_reset_tt.spi) — tran
- [environment/starter/testbench/tb_toggle_tt.spi](../sources/upstream/tasks/sky130-transistor-divide-by-2/environment/starter/testbench/tb_toggle_tt.spi) — tran
- [tests/benches/tb_divide.spi](../sources/upstream/tasks/sky130-transistor-divide-by-2/tests/benches/tb_divide.spi) — tran
- [tests/benches/tb_reset.spi](../sources/upstream/tasks/sky130-transistor-divide-by-2/tests/benches/tb_reset.spi) — tran

## 相邻案例

[09 宽频 CML 二分频：判定锁定需要周期级证据](09-sky130-cml-divider-div2-range1gto10g.md) · [42 6 bit 异步 SAR：采集窗、握手与最终寄存都影响正确性](42-sky130-sar-adc-6bit-async.md) · [48 4 bit 异步 SAR：采样率与输出延迟不能互相代替](48-sky130-sar-adc-4bit-async.md)
