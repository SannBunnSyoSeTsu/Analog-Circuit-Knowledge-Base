---
case_id: adb-v2-28
task_id: sky130-fct-residue-amplifier-900msps
category: 采样与数据转换
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-fct-residue-amplifier-900msps/instruction.md
  - ../sources/upstream/tasks/sky130-fct-residue-amplifier-900msps/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-fct-residue-amplifier-900msps/tests/verify.py
  - ../sources/upstream/tasks/sky130-fct-residue-amplifier-900msps/results/reference.json
---

# 28 · FCT 残差放大器：保持稳定度不是目标建立误差

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

900 MS/s，五角落、1.8 V/27 °C；DUT 只交付 TEST_FCT 核心，bench 提供理想采样/转移/复位开关、400 fF 飞跨与 50 fF 负载。64 次预热后 32 点 FFT。

## Reference 拓扑与尺寸线索（静态事实）

浮动储能电容 2 pF、输入耦合 1 pF、大跨导输入器件及交叉体连接，配时钟缓冲和偏置。

## 可复用的工程认识（推断，迁移时有条件）

评估必须画清能量来自浮动储能还是输入/时钟端。0.78 ns 与 0.88 ns 的两次采样用于衡量保持期残差移动，其 RMS 比值上限 1.5%；它不等价于“达到理想增益终值的 1.5% 建立误差”。分别保留增益、FFT 线性和保持漂移定义。

## 不能由 pass 推出的结论

功耗计入 DUT 多端口但排除理想外部开关等夹具；性能属于这套采样环境。不能直接作为全晶体管 900 MS/s ADC 的功耗或噪声证明。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-fct-residue-amplifier-900msps/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-fct-residue-amplifier-900msps/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-fct-residue-amplifier-900msps)
- [Reference circuit](../sources/upstream/tasks/sky130-fct-residue-amplifier-900msps/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-fct-residue-amplifier-900msps/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-fct-residue-amplifier-900msps/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-fct-residue-amplifier-900msps/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-fct-residue-amplifier-900msps/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-fct-residue-amplifier-900msps/circuit.spi) · [网站结果快照](../sources/astra/sky130-fct-residue-amplifier-900msps/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-fct-residue-amplifier-900msps/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-14T20:08:02+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `sampled_gain_pvt_10mv` | 10 mV range=5.7250..6.1577V/V (5.5..6.5) |
| `sfdr_pvt_10mv` | 10 mV min=61.368dB at tt (min 60dB) |
| `output_common_mode_pvt_10mv` | 10 mV mean range=0.7909..1.1891V (0.3..1.2V) |
| `output_headroom_pvt_10mv` | 10 mV sample range=0.7595..1.2281V (0.2..1.6V) |
| `hold_transition_movement_pvt_10mv` | 10 mV max=1.1510% at fs (max 1.5%) |
| `power_pvt_10mv` | 10 mV total delivered range=3.8711..4.1171mW (0..5mW) |
| `sampled_gain_pvt_20mv` | 20 mV range=5.7514..6.2025V/V (5.5..6.5) |
| `sfdr_pvt_20mv` | 20 mV min=61.593dB at tt (min 60dB) |
| `output_common_mode_pvt_20mv` | 20 mV mean range=0.7908..1.1886V (0.3..1.2V) |
| `output_headroom_pvt_20mv` | 20 mV sample range=0.7282..1.2565V (0.2..1.6V) |
| `hold_transition_movement_pvt_20mv` | 20 mV max=1.1343% at fs (max 1.5%) |
| `power_pvt_20mv` | 20 mV total delivered range=3.8717..4.1170mW (0..5mW) |
| `complete_signoff` | 10/10 unique finite transients: tt/ss/ff/fs/sf at 10mV and 20mV |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/analyze_fct.py](../sources/upstream/tasks/sky130-fct-residue-amplifier-900msps/environment/starter/testbench/analyze_fct.py) — 夹具、模板或数据处理辅助
- [environment/starter/testbench/fct_fixture.spi](../sources/upstream/tasks/sky130-fct-residue-amplifier-900msps/environment/starter/testbench/fct_fixture.spi) — 夹具、模板或数据处理辅助
- [environment/starter/testbench/tb_dynamic_tt.spi](../sources/upstream/tasks/sky130-fct-residue-amplifier-900msps/environment/starter/testbench/tb_dynamic_tt.spi) — tran
- [environment/starter/testbench/tb_dynamic_tt_20mv.spi](../sources/upstream/tasks/sky130-fct-residue-amplifier-900msps/environment/starter/testbench/tb_dynamic_tt_20mv.spi) — tran
- [tests/benches/fct_fixture.spi](../sources/upstream/tasks/sky130-fct-residue-amplifier-900msps/tests/benches/fct_fixture.spi) — 夹具、模板或数据处理辅助
- [tests/benches/tb_dynamic_pvt.spi](../sources/upstream/tasks/sky130-fct-residue-amplifier-900msps/tests/benches/tb_dynamic_pvt.spi) — tran
- [tests/benches/tb_large_signal_tt.spi](../sources/upstream/tasks/sky130-fct-residue-amplifier-900msps/tests/benches/tb_large_signal_tt.spi) — tran

## 相邻案例

[06 三级 Ring Amp：电容比、死区与动态终止共同定增益](06-sky130-ring-amp-3stage-gain8-400uw.md) · [31 底板采样：存储电压必须按两端差计算](31-sky130-bottom-plate-sampler-pvt.md) · [34 增益 8 采样反馈 OTA：β=1/9 决定环路速度](34-sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc.md)
