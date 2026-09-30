---
case_id: adb-v2-27
task_id: sky130-flash-adc-4bit-50msps
category: 采样与数据转换
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-flash-adc-4bit-50msps/instruction.md
  - ../sources/upstream/tasks/sky130-flash-adc-4bit-50msps/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-flash-adc-4bit-50msps/tests/verify.py
  - ../sources/upstream/tasks/sky130-flash-adc-4bit-50msps/results/reference.json
---

# 27 · 4 bit Flash ADC：前端采样与编码必须纳入转换链

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

仅 TT，50 MS/s，时钟后 9 ns 解码；16 个码中心、慢斜坡及 32 点 bin5 动态 FFT，功耗计参考供能但不含外部时钟。

## Reference 拓扑与尺寸线索（静态事实）

15 个 StrongARM 比较器配 SR 保持器，16×100 Ω 电阻梯、每侧 20 pF 共享 T/H；输入与阈值经 200 kΩ 网络组合，平衡 XOR 网络编码。

## 可复用的工程认识（推断，迁移时有条件）

采样保持隔离比较器再生和外部输入，SR 保持避免预充期污染编码。功耗、延迟与输入加载不只由比较器决定，电阻梯、前端和编码树都需要分配预算。

## 不能由 pass 推出的结论

约 90 点的有限分辨率斜坡出现 INL/DNL=0，只说明该提取网格未分辨到误差；不能宣称物理转换器理想线性。TT 短 FFT 也不覆盖失配或亚稳态概率。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-flash-adc-4bit-50msps/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-flash-adc-4bit-50msps/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-flash-adc-4bit-50msps)
- [Reference circuit](../sources/upstream/tasks/sky130-flash-adc-4bit-50msps/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-flash-adc-4bit-50msps/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-flash-adc-4bit-50msps/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-flash-adc-4bit-50msps/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-flash-adc-4bit-50msps/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-flash-adc-4bit-50msps/circuit.spi) · [网站结果快照](../sources/astra/sky130-flash-adc-4bit-50msps/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-flash-adc-4bit-50msps/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-13T10:39:54+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `transfer` | codes=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] errors=0 missing=0 |
| `sndr` | 25.483 dB |
| `sfdr` | 29.034 dB |
| `power` | 2.398 mW |
| `inl` | \|INL\|=0.000 LSB valid=True |
| `dnl` | \|DNL\|=0.000 LSB monotonic=True missing=0 |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/analyze_flash_adc.py](../sources/upstream/tasks/sky130-flash-adc-4bit-50msps/environment/starter/testbench/analyze_flash_adc.py) — noise
- [environment/starter/testbench/tb_dynamic_tt.spi](../sources/upstream/tasks/sky130-flash-adc-4bit-50msps/environment/starter/testbench/tb_dynamic_tt.spi) — tran
- [environment/starter/testbench/tb_linearity_tt.spi](../sources/upstream/tasks/sky130-flash-adc-4bit-50msps/environment/starter/testbench/tb_linearity_tt.spi) — tran
- [environment/starter/testbench/tb_transfer_tt.spi](../sources/upstream/tasks/sky130-flash-adc-4bit-50msps/environment/starter/testbench/tb_transfer_tt.spi) — tran
- [tests/benches/tb_dynamic.spi](../sources/upstream/tasks/sky130-flash-adc-4bit-50msps/tests/benches/tb_dynamic.spi) — tran
- [tests/benches/tb_inl_dnl.spi](../sources/upstream/tasks/sky130-flash-adc-4bit-50msps/tests/benches/tb_inl_dnl.spi) — tran
- [tests/benches/tb_transfer.spi](../sources/upstream/tasks/sky130-flash-adc-4bit-50msps/tests/benches/tb_transfer.spi) — tran

## 相邻案例

[23 5 bit 电阻 DAC：分母由固定支路决定](23-sky130-cmos-switched-resistor-dac-5bit-pvt.md) · [42 6 bit 异步 SAR：采集窗、握手与最终寄存都影响正确性](42-sky130-sar-adc-6bit-async.md) · [46 3 bit Flash：阈值绝对位置与编码尾部延迟都要检查](46-sky130-flash-adc-3bit-pvt.md)
