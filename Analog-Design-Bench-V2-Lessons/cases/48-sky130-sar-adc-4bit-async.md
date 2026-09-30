---
case_id: adb-v2-48
task_id: sky130-sar-adc-4bit-async
category: 采样与数据转换
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-sar-adc-4bit-async/instruction.md
  - ../sources/upstream/tasks/sky130-sar-adc-4bit-async/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-sar-adc-4bit-async/tests/verify.py
  - ../sources/upstream/tasks/sky130-sar-adc-4bit-async/results/reference.json
---

# 48 · 4 bit 异步 SAR：采样率与输出延迟不能互相代替

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

100 MS/s，所有 16 码保持验证在 TT，三个代表 PVT 做动态；判码在下一周期 4.5 ns，而不是当前周期内完成输出。32 点近 Nyquist FFT。

## Reference 拓扑与尺寸线索（静态事实）

每侧 400 fF CDAC，50 fF dummy 与 50/100/200 fF 二进制阵列；VALID 握手推进，EOC 后寄存输出。

## 可复用的工程认识（推断，迁移时有条件）

流水接口可能每 10 ns 接收一个新样本，但前一结果更晚可用，故必须分别保存采样率、吞吐率、延迟和码对应关系。对照 6 bit SAR 的本周期 9 ns 解码，不能仅凭 bit 数或 fs 判断哪一个时序更紧。

## 不能由 pass 推出的结论

网站归一化 ENOB 约 4.313，大于 4 不能解释成超出位数的真实有效分辨率；短记录与归一化公式下同时看 raw SNDR 才能理解。功耗约 4.287 mW 含多端口供能。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-sar-adc-4bit-async/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-sar-adc-4bit-async/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-sar-adc-4bit-async)
- [Reference circuit](../sources/upstream/tasks/sky130-sar-adc-4bit-async/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-sar-adc-4bit-async/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-sar-adc-4bit-async/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-sar-adc-4bit-async/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-sar-adc-4bit-async/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-sar-adc-4bit-async/circuit.spi) · [网站结果快照](../sources/astra/sky130-sar-adc-4bit-async/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-sar-adc-4bit-async/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-15T18:00:00Z`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `sample_hold_16_codes` | two complete 16-code sampled transfer sequences matched exactly |
| `sndr` | worst=27.14 dB (strictly > 24 dB) |
| `normalized_enob` | worst=4.313 bit (strictly > 3.90 bit) |
| `power` | worst=4.287 mW (<= 5 mW) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/analyze_dynamic.py](../sources/upstream/tasks/sky130-sar-adc-4bit-async/environment/starter/testbench/analyze_dynamic.py) — noise
- [environment/starter/testbench/analyze_transfer.py](../sources/upstream/tasks/sky130-sar-adc-4bit-async/environment/starter/testbench/analyze_transfer.py) — 夹具、模板或数据处理辅助
- [environment/starter/testbench/tb_dynamic_32sample_tt.spi](../sources/upstream/tasks/sky130-sar-adc-4bit-async/environment/starter/testbench/tb_dynamic_32sample_tt.spi) — tran
- [environment/starter/testbench/tb_smoke_100msps_3code_tt.spi](../sources/upstream/tasks/sky130-sar-adc-4bit-async/environment/starter/testbench/tb_smoke_100msps_3code_tt.spi) — tran
- [environment/starter/testbench/tb_transfer_16code_tt.spi](../sources/upstream/tasks/sky130-sar-adc-4bit-async/environment/starter/testbench/tb_transfer_16code_tt.spi) — tran
- [tests/benches/tb_dynamic.spi](../sources/upstream/tasks/sky130-sar-adc-4bit-async/tests/benches/tb_dynamic.spi) — tran
- [tests/benches/tb_transfer.spi](../sources/upstream/tasks/sky130-sar-adc-4bit-async/tests/benches/tb_transfer.spi) — tran
- [tests/benches/tb_transfer_alt.spi](../sources/upstream/tasks/sky130-sar-adc-4bit-async/tests/benches/tb_transfer_alt.spi) — tran

## 相邻案例

[40 一阶 ΔΣ：先划清 DUT 与外部模拟核心](40-sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40.md) · [42 6 bit 异步 SAR：采集窗、握手与最终寄存都影响正确性](42-sky130-sar-adc-6bit-async.md) · [45 晶体管二分频：复位必须清除内部状态](45-sky130-transistor-divide-by-2.md)
