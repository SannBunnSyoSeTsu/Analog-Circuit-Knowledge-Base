---
case_id: adb-v2-34
task_id: sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc
category: 放大器与滤波
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: true
derived_from:
  - ../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc/instruction.md
  - ../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc/tests/verify.py
  - ../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc/results/reference.json
---

# 34 · 增益 8 采样反馈 OTA：β=1/9 决定环路速度

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

Cs=1 pF、Cf=125 fF、CL=250 fF；30 点含 fs/sf，温度 −25/27/85 °C。1% 静态/动态误差、10 ns 建立、输出噪声≤1 mV，另有失配抑制比和 CMFB 脉冲。

## Reference 拓扑与尺寸线索（静态事实）

reference 与任务 33 同族，但增加尾电流/输入尺寸，采用 LVT 输入，补偿约 450 Ω/0.64 pF。

## 可复用的工程认识（推断，迁移时有条件）

信号增益 8 与噪声增益约 9 不能混淆；β≈1/9 把输入级 gm、补偿和闭环带宽要求联系起来。仅按任务 33 的电容比修改而不重配电流，很容易无法在更短窗口建立。还要检查 fs/sf 造成的上拉下拉与共模失衡。

## 不能由 pass 推出的结论

reference 建立约 9.748 ns、共模误差约 24.499 mV，分别贴近 10 ns 和 25 mV 上限；这些余量不支持额外版图寄生。Astra 的另一种共模控制见专文。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc)
- [Reference circuit](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc/circuit.spi) · [网站结果快照](../sources/astra/sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc/runs/gpt-6-astra-thinking-max/run-1)

该 R1 已做定向电路比较，见 [Astra 对照](../topics/08-astra-comparisons.md)。

Reference 结果生成时间：`2026-08-14T20:09:58+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `pvt_phase_margin` | worst=69.3615deg at sf/1.80V/-25C; limit >=60deg |
| `pvt_output_common_mode` | worst=24.4989mV at fs/1.80V/+85C; limit <=25mV |
| `pvt_power` | worst=6.30723mW at ff/1.98V/+85C; limit <=10mW |
| `pvt_static_accuracy` | worst=0.0483111% at ss/1.80V/+85C; limit <=1% |
| `pvt_dynamic_accuracy` | worst=0.868767% at fs/1.98V/+85C; limit <=1% |
| `pvt_rise_settling` | worst=9.74834ns at fs/1.98V/+85C; limit <=10ns |
| `pvt_fall_settling` | worst=9.71326ns at fs/1.98V/+85C; limit <=10ns |
| `pvt_output_range` | 3dB-compression differential range=2.00686V at ss/1.80V/+85C; limit >=1.8V |
| `pvt_output_noise` | worst=860.775uVrms at fs/1.80V/+85C; limit <=1000uVrms |
| `mc_cmrr` | worst=54dB at tt/1.80V/+27C/seed-41002; limit >=50dB |
| `mc_psrr_plus` | worst=68.8817dB at tt/1.80V/+27C/seed-41002; limit >=60dB |
| `mc_psrr_minus` | worst=68.8817dB at tt/1.80V/+27C/seed-41002; limit >=60dB |
| `cmfb_peak_deviation` | worst=10.1375mV at ss/1.80V/+85C; limit <=100mV |
| `cmfb_residual_20ns` | worst=0.240609mV at tt/1.80V/+27C; limit <=5mV |
| `cmfb_residual_100ns` | worst=4.15598e-05mV at ff/1.98V/-25C; limit <=1mV |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/tb_cmfb_nominal.spi](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc/environment/starter/testbench/tb_cmfb_nominal.spi) — tran
- [environment/starter/testbench/tb_loop_nominal.spi](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc/environment/starter/testbench/tb_loop_nominal.spi) — ac, op
- [environment/starter/testbench/tb_mismatch_nominal.spi](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc/environment/starter/testbench/tb_mismatch_nominal.spi) — ac
- [environment/starter/testbench/tb_noise_nominal.spi](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc/environment/starter/testbench/tb_noise_nominal.spi) — noise
- [environment/starter/testbench/tb_nominal.spi](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc/environment/starter/testbench/tb_nominal.spi) — tran
- [environment/starter/testbench/tb_range_nominal.spi](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc/environment/starter/testbench/tb_range_nominal.spi) — dc
- [tests/benches/tb_cmfb_recovery.spi](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc/tests/benches/tb_cmfb_recovery.spi) — tran
- [tests/benches/tb_loop.spi](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc/tests/benches/tb_loop.spi) — ac, op
- [tests/benches/tb_mc.spi](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc/tests/benches/tb_mc.spi) — ac
- [tests/benches/tb_noise.spi](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc/tests/benches/tb_noise.spi) — noise
- [tests/benches/tb_ranges.spi](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc/tests/benches/tb_ranges.spi) — dc
- [tests/benches/tb_settling.spi](../sources/upstream/tasks/sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc/tests/benches/tb_settling.spi) — tran

## 相邻案例

[06 三级 Ring Amp：电容比、死区与动态终止共同定增益](06-sky130-ring-amp-3stage-gain8-400uw.md) · [28 FCT 残差放大器：保持稳定度不是目标建立误差](28-sky130-fct-residue-amplifier-900msps.md) · [33 增益 1 采样反馈 OTA：差模建立和 CMFB 要分开验收](33-sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc.md)
