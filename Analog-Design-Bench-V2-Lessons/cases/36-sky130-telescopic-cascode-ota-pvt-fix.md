---
case_id: adb-v2-36
task_id: sky130-telescopic-cascode-ota-pvt-fix
category: 放大器与滤波
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-telescopic-cascode-ota-pvt-fix/instruction.md
  - ../sources/upstream/tasks/sky130-telescopic-cascode-ota-pvt-fix/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-telescopic-cascode-ota-pvt-fix/tests/verify.py
  - ../sources/upstream/tasks/sky130-telescopic-cascode-ota-pvt-fix/results/reference.json
---

# 36 · 套筒 OTA：堆叠余量与共模感测极点

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

27 点 PVT，增益≥60 dB、UGB≥50 MHz、PM≥60°、功耗≤1 mW；约束单次跨频至 10 GHz、标称摆幅/10 ns 建立和 40 ns 共模恢复。

## Reference 拓扑与尺寸线索（静态事实）

单级 telescopic 堆叠，复制偏置配 20/24 kΩ 电平移位；共模以 4.7 MΩ 并 150 fF 感测，另有双 390 fF/3 kΩ 补偿。

## 可复用的工程认识（推断，迁移时有条件）

套筒结构通过堆叠提高增益，需要同时分配输入共模、上下 cascode 和尾源余量。高阻共模采样几乎不加载 DC 输出，但会引入慢时间常数，并联电容用于改变动态感测路径，仍须检查 CMFB 模态。

## 不能由 pass 推出的结论

此题没有输入噪声、PSRR 或 fs/sf 验收，不能把“套筒通过”外推为这些指标也合格。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-telescopic-cascode-ota-pvt-fix/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-telescopic-cascode-ota-pvt-fix/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-telescopic-cascode-ota-pvt-fix)
- [Reference circuit](../sources/upstream/tasks/sky130-telescopic-cascode-ota-pvt-fix/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-telescopic-cascode-ota-pvt-fix/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-telescopic-cascode-ota-pvt-fix/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-telescopic-cascode-ota-pvt-fix/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-telescopic-cascode-ota-pvt-fix/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-telescopic-cascode-ota-pvt-fix/circuit.spi) · [网站结果快照](../sources/astra/sky130-telescopic-cascode-ota-pvt-fix/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-telescopic-cascode-ota-pvt-fix/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-13T10:40:49+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `complete_signoff` | rows=30/30 PVT=27/27 executed=30 blocked=0 |
| `pvt_gain_bandwidth` | gain_min=62.58dB at ff/1.62V/+125C; UGB_min=77.54MHz at ss/1.62V/+125C |
| `pvt_phase_margin` | PM_min=87.95deg at ss/1.62V/+125C; falling_crossings=1 post_first_max=-0.000dB |
| `pvt_output_common_mode` | CM_error_max=0.145mV at ss/1.62V/-40C |
| `pvt_power` | power_min=394.1uW; power_max=516.1uW at ff/1.98V/+125C |
| `closed_loop_range` | range=0.900Vpp points=181/181 tracking_max=0.214mV CM_error_max=0.104mV |
| `closed_loop_settling` | last_entry=8.120ns final_10ns_error=0.0228mV (0.0228% of step) |
| `common_mode_recovery` | last_entry=19.275ns final_20ns_error=1.2433mV |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/public_checks.py](../sources/upstream/tasks/sky130-telescopic-cascode-ota-pvt-fix/environment/starter/testbench/public_checks.py) — ac, tran
- [environment/starter/testbench/tb_ac_ff.spi](../sources/upstream/tasks/sky130-telescopic-cascode-ota-pvt-fix/environment/starter/testbench/tb_ac_ff.spi) — ac, op
- [environment/starter/testbench/tb_ac_ss.spi](../sources/upstream/tasks/sky130-telescopic-cascode-ota-pvt-fix/environment/starter/testbench/tb_ac_ss.spi) — ac, op
- [environment/starter/testbench/tb_ac_tt.spi](../sources/upstream/tasks/sky130-telescopic-cascode-ota-pvt-fix/environment/starter/testbench/tb_ac_tt.spi) — ac, op
- [environment/starter/testbench/tb_cm_recovery_tt.spi](../sources/upstream/tasks/sky130-telescopic-cascode-ota-pvt-fix/environment/starter/testbench/tb_cm_recovery_tt.spi) — tran
- [environment/starter/testbench/tb_range_public.spi](../sources/upstream/tasks/sky130-telescopic-cascode-ota-pvt-fix/environment/starter/testbench/tb_range_public.spi) — dc
- [environment/starter/testbench/tb_settling_public.spi](../sources/upstream/tasks/sky130-telescopic-cascode-ota-pvt-fix/environment/starter/testbench/tb_settling_public.spi) — tran
- [tests/benches/tb_cm_recovery.spi](../sources/upstream/tasks/sky130-telescopic-cascode-ota-pvt-fix/tests/benches/tb_cm_recovery.spi) — tran
- [tests/benches/tb_pvt.spi](../sources/upstream/tasks/sky130-telescopic-cascode-ota-pvt-fix/tests/benches/tb_pvt.spi) — ac, op
- [tests/benches/tb_settling.spi](../sources/upstream/tasks/sky130-telescopic-cascode-ota-pvt-fix/tests/benches/tb_settling.spi) — tran
- [tests/benches/tb_swing.spi](../sources/upstream/tasks/sky130-telescopic-cascode-ota-pvt-fix/tests/benches/tb_swing.spi) — dc
- [tests/fixtures/controlled_source.spi](../sources/upstream/tasks/sky130-telescopic-cascode-ota-pvt-fix/tests/fixtures/controlled_source.spi) — 夹具、模板或数据处理辅助
- [tests/fixtures/nonfunctional.spi](../sources/upstream/tasks/sky130-telescopic-cascode-ota-pvt-fix/tests/fixtures/nonfunctional.spi) — 夹具、模板或数据处理辅助

## 相邻案例

[33 增益 1 采样反馈 OTA：差模建立和 CMFB 要分开验收](33-sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc.md) · [35 全差分两级 Miller：高差模增益不能替代电源抑制](35-sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt.md) · [50 130 dB 高速 OTA：局部增益增强环与外环必须分层分析](50-sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt.md)
