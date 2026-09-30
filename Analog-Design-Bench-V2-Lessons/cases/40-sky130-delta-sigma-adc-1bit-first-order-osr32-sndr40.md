---
case_id: adb-v2-40
task_id: sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40
category: 采样与数据转换
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40/instruction.md
  - ../sources/upstream/tasks/sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40/tests/verify.py
  - ../sources/upstream/tasks/sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40/results/reference.json
---

# 40 · 一阶 ΔΣ：先划清 DUT 与外部模拟核心

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

TT、10 MHz、OSR32；580 周期取末 512 点，带内使用 bins1–8，并有不同幅度/相位/DC 刺激。OTA 与 StrongARM 比较器由 bench 固定提供。

## Reference 拓扑与尺寸线索（静态事实）

交付的是 200 fF 采样/400 fF 积分电容、开关、一位反馈 DAC 与 50 fF 决策保持；外部 OTA 有有限增益/带宽，比较器含 1 mV 设定偏移。

## 可复用的工程认识（推断，迁移时有条件）

从开关相位写离散时间关系 u[n]≈ρu[n−1]+0.5·(x−Dprev)，先确认反馈符号和上一拍判决，再讨论噪声整形。有限增益让 ρ 偏离 1；不同刺激用来排除非线性或固定码模式碰巧得到好 FFT。

## 不能由 pass 推出的结论

功耗包含提供的模拟核心 VDD，但排除外部时钟；不能称为独立设计出整个 ADC。确定性 FFT 未注入完整热噪声，测得的 OSR 改善也不能当普适理论斜率。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40)
- [Reference circuit](../sources/upstream/tasks/sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40/circuit.spi) · [网站结果快照](../sources/astra/sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-14T20:10:11+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `nominal_function` | gain=1.243 density=0.531 transitions=53% complementary=100.0% invalid=0 |
| `stimulus_transfer` | AC gains=1.243,1.247,1.247 streams_valid=True (gain target [0.70,1.35]) |
| `dc_tracking` | worst mean-code error=0.0125 (target <=0.035) |
| `polarity_tracking` | magnitude_ratio=1.000 phase_error=0.0deg |
| `bounded_state` | worst max\|integrator differential\|=0.396 V (target <2) |
| `noise_shaping` | shaping dB=41.4,38.0,38.0 (min >=10) |
| `first_order_gain` | nominal SNDR32-SNDR16=18.25 dB/oct (target >=6) |
| `power` | worst total VDD power=1.236 mW (target <=2.0) |
| `sndr_suite` | SNDR32 dB=53.04,48.47,48.47 (targets 40/40/40) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/fd_ota_5t_cmfb.spi](../sources/upstream/tasks/sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40/environment/starter/testbench/fd_ota_5t_cmfb.spi) — 夹具、模板或数据处理辅助
- [environment/starter/testbench/run_dev.py](../sources/upstream/tasks/sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40/environment/starter/testbench/run_dev.py) — noise
- [environment/starter/testbench/strongarm.spi](../sources/upstream/tasks/sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40/environment/starter/testbench/strongarm.spi) — 夹具、模板或数据处理辅助
- [environment/starter/testbench/tb_ns_dev.spi](../sources/upstream/tasks/sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40/environment/starter/testbench/tb_ns_dev.spi) — tran
- [tests/benches/fd_ota_5t_cmfb.spi](../sources/upstream/tasks/sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40/tests/benches/fd_ota_5t_cmfb.spi) — 夹具、模板或数据处理辅助
- [tests/benches/strongarm.spi](../sources/upstream/tasks/sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40/tests/benches/strongarm.spi) — 夹具、模板或数据处理辅助
- [tests/benches/tb_ns_adc.spi](../sources/upstream/tasks/sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40/tests/benches/tb_ns_adc.spi) — tran

## 相邻案例

[27 4 bit Flash ADC：前端采样与编码必须纳入转换链](27-sky130-flash-adc-4bit-50msps.md) · [42 6 bit 异步 SAR：采集窗、握手与最终寄存都影响正确性](42-sky130-sar-adc-6bit-async.md) · [48 4 bit 异步 SAR：采样率与输出延迟不能互相代替](48-sky130-sar-adc-4bit-async.md)
