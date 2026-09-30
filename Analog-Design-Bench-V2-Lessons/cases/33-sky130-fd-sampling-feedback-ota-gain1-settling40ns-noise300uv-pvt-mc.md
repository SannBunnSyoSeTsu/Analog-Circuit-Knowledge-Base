---
case_id: adb-v2-33
task_id: sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc
category: 放大器与滤波
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc/instruction.md
  - ../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc/tests/verify.py
  - ../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc/results/reference.json
---

# 33 · 增益 1 采样反馈 OTA：差模建立和 CMFB 要分开验收

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

五角落 × 1.8/1.98 V × −20/27/80 °C，共 30 点；Cs=Cf=1 pF、CL=1 pF，0.9 V 输出阶跃，0.1% 动态误差 40 ns，20 个 tt_mm 样本。

## Reference 拓扑与尺寸线索（静态事实）

折叠第一级加第二级，复制管生成 cascode 偏置，300 Ω/1.8 pF 补偿；100 kΩ 并 100 fF 的共模感测及独立 CMFB 放大器。

## 可复用的工程认识（推断，迁移时有条件）

闭环信号增益 1 不代表反馈系数 1；忽略寄生时 β=Cf/(Cs+Cf)=1/2。输出噪声积分到 10 GHz，是本题固定定义。差模环路、输出共模静态误差、共模电流脉冲恢复以及失配下 CMRR/PSRR 各是独立证据。

## 不能由 pass 推出的结论

理想电容反馈网络与其保持条件属于夹具，不能直接外推真实开关网络的注入、采样热噪声。reference 建立约 34.26 ns，仅在该步幅/误差定义下成立。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc)
- [Reference circuit](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc/circuit.spi) · [网站结果快照](../sources/astra/sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-14T20:08:22+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `pvt_phase_margin` | worst=74.9205deg at ss/1.80V/+80C; limit >=60deg |
| `pvt_output_common_mode` | worst=4.07273mV at ss/1.80V/+80C; limit <=25mV |
| `pvt_power` | worst=3.07349mW at ff/1.98V/+80C; limit <=5mW |
| `pvt_static_accuracy` | worst=0.00516667% at ff/1.80V/+80C; limit <=0.01% |
| `pvt_dynamic_accuracy` | worst=0.0114556% at ff/1.80V/+80C; limit <=0.1% |
| `pvt_rise_settling` | worst=34.2647ns at sf/1.80V/+80C; limit <=40ns |
| `pvt_fall_settling` | worst=33.9096ns at sf/1.80V/+80C; limit <=40ns |
| `pvt_output_range` | 3dB-compression differential range=2.16716V at tt/1.80V/+27C; limit >=1.8V |
| `pvt_output_noise` | worst=274.886uVrms at fs/1.80V/+80C; limit <=300uVrms |
| `mc_cmrr` | worst=66.3223dB at tt/1.80V/+27C/seed-41003; limit >=60dB |
| `mc_psrr_plus` | worst=74.4195dB at tt/1.80V/+27C/seed-41007; limit >=70dB |
| `mc_psrr_minus` | worst=74.4195dB at tt/1.80V/+27C/seed-41007; limit >=70dB |
| `cmfb_peak_deviation` | worst=8.33004mV at ss/1.80V/+80C; limit <=150mV |
| `cmfb_residual_20ns` | worst=0.0858042mV at ss/1.80V/+80C; limit <=50mV |
| `cmfb_residual_100ns` | worst=1.09021e-05mV at ss/1.80V/+80C; limit <=20mV |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/tb_cmfb_nominal.spi](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc/environment/starter/testbench/tb_cmfb_nominal.spi) — tran
- [environment/starter/testbench/tb_loop_nominal.spi](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc/environment/starter/testbench/tb_loop_nominal.spi) — ac, op
- [environment/starter/testbench/tb_mismatch_nominal.spi](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc/environment/starter/testbench/tb_mismatch_nominal.spi) — ac
- [environment/starter/testbench/tb_noise_nominal.spi](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc/environment/starter/testbench/tb_noise_nominal.spi) — noise
- [environment/starter/testbench/tb_nominal.spi](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc/environment/starter/testbench/tb_nominal.spi) — tran
- [environment/starter/testbench/tb_range_nominal.spi](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc/environment/starter/testbench/tb_range_nominal.spi) — dc
- [tests/benches/tb_cmfb_recovery.spi](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc/tests/benches/tb_cmfb_recovery.spi) — tran
- [tests/benches/tb_loop.spi](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc/tests/benches/tb_loop.spi) — ac, op
- [tests/benches/tb_mc.spi](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc/tests/benches/tb_mc.spi) — ac
- [tests/benches/tb_noise.spi](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc/tests/benches/tb_noise.spi) — noise
- [tests/benches/tb_ranges.spi](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc/tests/benches/tb_ranges.spi) — dc
- [tests/benches/tb_settling.spi](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc/tests/benches/tb_settling.spi) — tran

## 相邻案例

[34 增益 8 采样反馈 OTA：β=1/9 决定环路速度](34-sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc.md) · [35 全差分两级 Miller：高差模增益不能替代电源抑制](35-sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt.md) · [36 套筒 OTA：堆叠余量与共模感测极点](36-sky130-telescopic-cascode-ota-pvt-fix.md)
