---
case_id: adb-v2-44
task_id: sky130-ota-5t-gain40-pm60-noise50uv-pvt
category: 放大器与滤波
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-ota-5t-gain40-pm60-noise50uv-pvt/instruction.md
  - ../sources/upstream/tasks/sky130-ota-5t-gain40-pm60-noise50uv-pvt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-ota-5t-gain40-pm60-noise50uv-pvt/tests/verify.py
  - ../sources/upstream/tasks/sky130-ota-5t-gain40-pm60-noise50uv-pvt/results/reference.json
---

# 44 · 5T OTA：最小拓扑也需要闭环噪声和环路定义

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

27 点 PVT，CL=1 pF，VCM=VDD/2，40 dB/100 MHz/60°、功耗≤0.5 mW，10 Hz–10 MHz 输入噪声≤50 µVrms。

## Reference 拓扑与尺寸线索（静态事实）

核心五管加一偏置管；NMOS 输入 96/1，PMOS 负载 64/1，尾源 L=3 µm，200:60 的镜比对应约 167 µA 标称尾流。

## 可复用的工程认识（推断，迁移时有条件）

gm/ID、ro 和输出电容共同决定这类单级 OTA 的增益带宽折中。此处只能记录已有尺寸和测量，不把尺寸比误称为 gm/ID 查表结果。双注入 Middlebrook 返回比、自然开环 DC 的 CMRR/PSRR、反馈噪声台各有偏置定义，不能混为同一测量。

## 不能由 pass 推出的结论

参考增益约 41.42 dB，余量有限；不要仅按标称 gm/CL 估算就宣称跨 PVT 满足。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-ota-5t-gain40-pm60-noise50uv-pvt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-ota-5t-gain40-pm60-noise50uv-pvt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-ota-5t-gain40-pm60-noise50uv-pvt)
- [Reference circuit](../sources/upstream/tasks/sky130-ota-5t-gain40-pm60-noise50uv-pvt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-ota-5t-gain40-pm60-noise50uv-pvt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-ota-5t-gain40-pm60-noise50uv-pvt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-ota-5t-gain40-pm60-noise50uv-pvt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-ota-5t-gain40-pm60-noise50uv-pvt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-ota-5t-gain40-pm60-noise50uv-pvt/circuit.spi) · [网站结果快照](../sources/astra/sky130-ota-5t-gain40-pm60-noise50uv-pvt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-ota-5t-gain40-pm60-noise50uv-pvt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-16T20:44:28+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `gain_40db` | worst=41.42dB at ff/1.62V/+125C (min 40dB) |
| `ugb_100mhz` | worst=111.3MHz at ss/1.62V/+125C (min 100MHz) |
| `phase_margin_60deg` | worst=66.52deg at ff/1.98V/-40C (min 60deg) |
| `power_0p5mw` | worst=0.4223mW at ff/1.98V/+125C (max 0.5mW) |
| `noise_50uvrms` | worst=38.6uVrms at ss/1.62V/+125C (max 50uVrms) |
| `cmrr_50db` | worst=56.85dB at ss/1.62V/+125C (min 50dB) |
| `psrr_30db` | worst=40dB at ss/1.62V/+125C (min 30dB) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/tb_cmrr_tt_1p80v_125c.spi](../sources/upstream/tasks/sky130-ota-5t-gain40-pm60-noise50uv-pvt/environment/starter/testbench/tb_cmrr_tt_1p80v_125c.spi) — ac
- [environment/starter/testbench/tb_op_ac_noise_ff_1p80v_125c.spi](../sources/upstream/tasks/sky130-ota-5t-gain40-pm60-noise50uv-pvt/environment/starter/testbench/tb_op_ac_noise_ff_1p80v_125c.spi) — ac, noise, op
- [environment/starter/testbench/tb_psrr_minus_ff_1p62v_m40c.spi](../sources/upstream/tasks/sky130-ota-5t-gain40-pm60-noise50uv-pvt/environment/starter/testbench/tb_psrr_minus_ff_1p62v_m40c.spi) — ac
- [environment/starter/testbench/tb_psrr_plus_ss_1p80v_27c.spi](../sources/upstream/tasks/sky130-ota-5t-gain40-pm60-noise50uv-pvt/environment/starter/testbench/tb_psrr_plus_ss_1p80v_27c.spi) — ac
- [tests/benches/tb_cmrr.spi](../sources/upstream/tasks/sky130-ota-5t-gain40-pm60-noise50uv-pvt/tests/benches/tb_cmrr.spi) — ac
- [tests/benches/tb_op_ac_noise.spi](../sources/upstream/tasks/sky130-ota-5t-gain40-pm60-noise50uv-pvt/tests/benches/tb_op_ac_noise.spi) — ac, noise, op
- [tests/benches/tb_psrr_minus.spi](../sources/upstream/tasks/sky130-ota-5t-gain40-pm60-noise50uv-pvt/tests/benches/tb_psrr_minus.spi) — ac
- [tests/benches/tb_psrr_plus.spi](../sources/upstream/tasks/sky130-ota-5t-gain40-pm60-noise50uv-pvt/tests/benches/tb_psrr_plus.spi) — ac

## 相邻案例

[07 5T 误差放大器 LDO：负载电容和 ESR 是环路参数](07-sky130-ldo-ota5-robust-pvt-mc.md) · [16 200 MHz 两级 Miller：快环路与宽带积分噪声的代价](16-sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt.md) · [36 套筒 OTA：堆叠余量与共模感测极点](36-sky130-telescopic-cascode-ota-pvt-fix.md)
