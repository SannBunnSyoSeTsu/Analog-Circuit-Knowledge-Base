---
case_id: adb-v2-42
task_id: sky130-sar-adc-6bit-async
category: 采样与数据转换
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-sar-adc-6bit-async/instruction.md
  - ../sources/upstream/tasks/sky130-sar-adc-6bit-async/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-sar-adc-6bit-async/tests/verify.py
  - ../sources/upstream/tasks/sky130-sar-adc-6bit-async/results/reference.json
---

# 42 · 6 bit 异步 SAR：采集窗、握手与最终寄存都影响正确性

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

TT、100 MS/s、2 ns 采集，在本周期 9 ns 解码；全 64 码中心两种排列，2.25 ns 后改变输入以检查保持。64 点 bin31 FFT，同时规定原始 SNDR 与归一化 ENOB。

## Reference 拓扑与尺寸线索（静态事实）

差分 CDAC 每侧约 640 fF；二进制电容以 20.578125 fF 为单位，额外 dummy 为 2.078125 fF。自举采样、VALID 驱动比较器握手、逐位状态和 EOC 输出寄存器。

## 可复用的工程认识（推断，迁移时有条件）

异步 SAR 的时序预算包括获取、DAC 更新、比较器再生、有效检测、状态推进和输出保持。码中心测试与输入诱饵一起排除持续跟踪；EOC 寄存避免下一转换预充污染输出。参考非整数 dummy 是这份原理图寄生条件下的补偿线索。

## 不能由 pass 推出的结论

不能把名义 dummy 修正照抄到另一版图。无 PVT/失配/随机噪声验收；短 FFT 归一化 ENOB 不是 ADC 的普适分辨率。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-sar-adc-6bit-async/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-sar-adc-6bit-async/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-sar-adc-6bit-async)
- [Reference circuit](../sources/upstream/tasks/sky130-sar-adc-6bit-async/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-sar-adc-6bit-async/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-sar-adc-6bit-async/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-sar-adc-6bit-async/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-sar-adc-6bit-async/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-sar-adc-6bit-async/circuit.spi) · [网站结果快照](../sources/astra/sky130-sar-adc-6bit-async/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-sar-adc-6bit-async/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-14T20:13:00+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `sample_hold_64_codes` | transfer=[11, 48, 21, 58, 31, 4, 41, 14, 51, 24, 61, 34, 7, 44, 17, 54, 27, 0, 37, 10, 47, 20, 57, 30, 3, 40, 13, 50, 23, 60, 33, 6, 43, 16, 53, 26, 63, 36, 9, 46, 19, 56, 29, 2, 39, 12, 49, 22, 59, 32, 5, 42, 15, 52, 25, 62, 35, 8, 45, 18, 55, 28, 1, 38]; transfer_alt=[47, 4, 25, 46, 3, 24, 45, 2, 23, 44, 1, 22, 43, 0, 21, 42, 63, 20, 41, 62, 19, 40, 61, 18, 39, 60, 17, 38, 59, 16, 37, 58, 15, 36, 57, 14, 35, 56, 13, 34, 55, 12, 33, 54, 11, 32, 53, 10, 31, 52, 9, 30, 51, 8, 29, 50, 7, 28, 49, 6, 27, 48, 5, 26] |
| `sndr` | worst=37.35dB at tt_1p80v_27c_bin31 (min 35dB) |
| `normalized_enob` | worst=5.999 bit at tt_1p80v_27c_bin31 (> 5.9 bit) |
| `power` | worst=2.004mW at tt_1p80v_27c_bin31 (< 3mW) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/analyze_dynamic.py](../sources/upstream/tasks/sky130-sar-adc-6bit-async/environment/starter/testbench/analyze_dynamic.py) — noise
- [environment/starter/testbench/analyze_transfer.py](../sources/upstream/tasks/sky130-sar-adc-6bit-async/environment/starter/testbench/analyze_transfer.py) — 夹具、模板或数据处理辅助
- [environment/starter/testbench/tb_dynamic_64sample_tt.spi](../sources/upstream/tasks/sky130-sar-adc-6bit-async/environment/starter/testbench/tb_dynamic_64sample_tt.spi) — tran
- [environment/starter/testbench/tb_smoke_100msps_3code_tt.spi](../sources/upstream/tasks/sky130-sar-adc-6bit-async/environment/starter/testbench/tb_smoke_100msps_3code_tt.spi) — tran
- [environment/starter/testbench/tb_transfer_64code_tt.spi](../sources/upstream/tasks/sky130-sar-adc-6bit-async/environment/starter/testbench/tb_transfer_64code_tt.spi) — tran
- [tests/benches/tb_dynamic.spi](../sources/upstream/tasks/sky130-sar-adc-6bit-async/tests/benches/tb_dynamic.spi) — tran
- [tests/benches/tb_transfer.spi](../sources/upstream/tasks/sky130-sar-adc-6bit-async/tests/benches/tb_transfer.spi) — tran
- [tests/benches/tb_transfer_alt.spi](../sources/upstream/tasks/sky130-sar-adc-6bit-async/tests/benches/tb_transfer_alt.spi) — tran

## 相邻案例

[27 4 bit Flash ADC：前端采样与编码必须纳入转换链](27-sky130-flash-adc-4bit-50msps.md) · [40 一阶 ΔΣ：先划清 DUT 与外部模拟核心](40-sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40.md) · [48 4 bit 异步 SAR：采样率与输出延迟不能互相代替](48-sky130-sar-adc-4bit-async.md)
