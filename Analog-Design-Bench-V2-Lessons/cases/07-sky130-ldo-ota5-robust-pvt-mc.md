---
case_id: adb-v2-07
task_id: sky130-ldo-ota5-robust-pvt-mc
category: 电源与驱动
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-ldo-ota5-robust-pvt-mc/instruction.md
  - ../sources/upstream/tasks/sky130-ldo-ota5-robust-pvt-mc/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-ldo-ota5-robust-pvt-mc/tests/verify.py
  - ../sources/upstream/tasks/sky130-ldo-ota5-robust-pvt-mc/results/reference.json
---

# 07 · 5T 误差放大器 LDO：负载电容和 ESR 是环路参数

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

目标 1.2 V，外部 0.8 V 参考和 300k/600k 分压，1/10/30 mA 负载。135 个 DC 点及额外电容/ESR 动态压力，另有 30 个固定组合 Monte Carlo 样本。

## Reference 拓扑与尺寸线索（静态事实）

NMOS 输入 5T 放大器控制大 PMOS pass；额定外部 1 µF、50 mΩ ESR，并检查 0.8/1.2 µF 与 20/100 mΩ 组合。

## 可复用的工程认识（推断，迁移时有条件）

对 LDO，“输出负载”至少包含电流、电容和 ESR 三个维度；轻载极点与重载驱动能力可能由不同工况主导。把 DC 精度、dropout、静态电流、环路裕量与命令端点 last-entry 分成独立验收项，比用单一阶跃波形判断可靠。

## 不能由 pass 推出的结论

这里依赖 µF 级外部电容，不能与片上电容 LDO 直接比较瞬态。固定 30 样本的全部通过只说明该种子集合，不能称为量产 100% 良率。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-ldo-ota5-robust-pvt-mc/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-ldo-ota5-robust-pvt-mc/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-ldo-ota5-robust-pvt-mc)
- [Reference circuit](../sources/upstream/tasks/sky130-ldo-ota5-robust-pvt-mc/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-ldo-ota5-robust-pvt-mc/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-ldo-ota5-robust-pvt-mc/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-ldo-ota5-robust-pvt-mc/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-ldo-ota5-robust-pvt-mc/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-ldo-ota5-robust-pvt-mc/circuit.spi) · [网站结果快照](../sources/astra/sky130-ldo-ota5-robust-pvt-mc/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-ldo-ota5-robust-pvt-mc/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-13T10:31:15+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `complete_signoff` | runs=161 PVT=15/15 DC-points=135 |
| `pvt_dc_regulation_and_iq` | error=14.201mV Iq=130.918uA..143.211uA |
| `dropout` | dropout=221.155mV |
| `loop_stability` | gain_min=47.254dB PM_min=64.694deg UGB_min=55.194kHz |
| `psrr_and_output_noise` | PSRR_min(100Hz/1kHz/100kHz/1MHz)=48.064dB/48.064dB/46.485dB/26.539dB noise=97.571uVrms |
| `startup` | sustained_t90=20.965us settling_after_ramp=0.675us overshoot=13.479mV |
| `load_transient` | excursion=9.194mV settling=0.000us |
| `line_transient` | excursion=9.966mV settling=0.000us |
| `monte_carlo_output` | samples=30/30 yield=100.000% |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/check_load_tran_tt.py](../sources/upstream/tasks/sky130-ldo-ota5-robust-pvt-mc/environment/starter/testbench/check_load_tran_tt.py) — 夹具、模板或数据处理辅助
- [environment/starter/testbench/tb_line_dc_tt.spi](../sources/upstream/tasks/sky130-ldo-ota5-robust-pvt-mc/environment/starter/testbench/tb_line_dc_tt.spi) — dc
- [environment/starter/testbench/tb_load_tran_tt.spi](../sources/upstream/tasks/sky130-ldo-ota5-robust-pvt-mc/environment/starter/testbench/tb_load_tran_tt.spi) — tran
- [tests/benches/tb_dropout.spi](../sources/upstream/tasks/sky130-ldo-ota5-robust-pvt-mc/tests/benches/tb_dropout.spi) — dc
- [tests/benches/tb_line_tran.spi](../sources/upstream/tasks/sky130-ldo-ota5-robust-pvt-mc/tests/benches/tb_line_tran.spi) — tran
- [tests/benches/tb_load_tran.spi](../sources/upstream/tasks/sky130-ldo-ota5-robust-pvt-mc/tests/benches/tb_load_tran.spi) — tran
- [tests/benches/tb_loop.spi](../sources/upstream/tasks/sky130-ldo-ota5-robust-pvt-mc/tests/benches/tb_loop.spi) — ac
- [tests/benches/tb_noise.spi](../sources/upstream/tasks/sky130-ldo-ota5-robust-pvt-mc/tests/benches/tb_noise.spi) — noise
- [tests/benches/tb_op.spi](../sources/upstream/tasks/sky130-ldo-ota5-robust-pvt-mc/tests/benches/tb_op.spi) — op
- [tests/benches/tb_psrr.spi](../sources/upstream/tasks/sky130-ldo-ota5-robust-pvt-mc/tests/benches/tb_psrr.spi) — ac
- [tests/benches/tb_pvt_dc.spi](../sources/upstream/tasks/sky130-ldo-ota5-robust-pvt-mc/tests/benches/tb_pvt_dc.spi) — dc
- [tests/benches/tb_startup.spi](../sources/upstream/tasks/sky130-ldo-ota5-robust-pvt-mc/tests/benches/tb_startup.spi) — tran

## 相邻案例

[17 0.4 V NMOS LDO：低输出电压改变输入级和驱动极性](17-sky130-nmos-pass-ldo-0p4v-pvt-mc.md) · [38 20 mA 无外部电容 LDO：片上储能仍可很大](38-sky130-capless-ldo-1v0-20ma-pvt.md) · [44 5T OTA：最小拓扑也需要闭环噪声和环路定义](44-sky130-ota-5t-gain40-pm60-noise50uv-pvt.md)
