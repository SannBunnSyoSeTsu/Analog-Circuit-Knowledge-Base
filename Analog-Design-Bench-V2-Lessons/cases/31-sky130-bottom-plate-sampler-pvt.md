---
case_id: adb-v2-31
task_id: sky130-bottom-plate-sampler-pvt
category: 采样与数据转换
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-bottom-plate-sampler-pvt/instruction.md
  - ../sources/upstream/tasks/sky130-bottom-plate-sampler-pvt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-bottom-plate-sampler-pvt/tests/verify.py
  - ../sources/upstream/tasks/sky130-bottom-plate-sampler-pvt/results/reference.json
---

# 31 · 底板采样：存储电压必须按两端差计算

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

九个代表点，100 MS/s、5 MHz 输入、80 样本 FFT；同时检查增益误差、共模、全端口功耗及保持期间输入反向扰动。

## Reference 拓扑与尺寸线索（静态事实）

输入双路及共模开关自举，反馈 NAND/延迟网络使共模底板先断，1 pF 存储电容的顶底板分别作为节点暴露。

## 可复用的工程认识（推断，迁移时有条件）

实际存储差分为 (vsp−vtopp)−(vsn−vtopn)，不能用两顶板对地电压代替；存储共模接近零也是合理的，并非必须等于 VDD/2。底板先断使关键关断电荷对输入的依赖减小，但仍须与其他开关的时序联合判断。

## 不能由 pass 推出的结论

网表内部有字面节点 0，移植到非零参考地系统需修改。高 SFDR 并不证明 kT/C 或 SNDR；保持扰动测试是防止透明直通的独立证据。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-bottom-plate-sampler-pvt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-bottom-plate-sampler-pvt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-bottom-plate-sampler-pvt)
- [Reference circuit](../sources/upstream/tasks/sky130-bottom-plate-sampler-pvt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-bottom-plate-sampler-pvt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-bottom-plate-sampler-pvt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-bottom-plate-sampler-pvt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-bottom-plate-sampler-pvt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-bottom-plate-sampler-pvt/circuit.spi) · [网站结果快照](../sources/astra/sky130-bottom-plate-sampler-pvt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-bottom-plate-sampler-pvt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-14T20:09:30+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `bipolar_acquisition_5mv` | +0.8V=2.938mV, -0.8V=2.937mV |
| `hold_isolation_and_reacquisition_5mv` | capture=2.992mV at ss/1.62V/+125C, shift=0.0082mV at ss/1.62V/+125C, reacquire=2.988mV at ss/1.62V/+125C (max 5mV each) |
| `representative_sfdr_80db` | worst=88.283dB at ff/1.98V/-40C (min 80dB) |
| `representative_gain_error_0p5pct` | worst=0.3846% at fs/1.80V/+27C (max 0.5%) |
| `representative_stored_common_mode_25mv` | worst=21.3041mV at ff/1.98V/-40C (max 25mV) |
| `representative_total_source_power_0p6mw` | worst=0.4975mW at ff/1.98V/-40C (max 0.6mW) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/run_fft_tt.py](../sources/upstream/tasks/sky130-bottom-plate-sampler-pvt/environment/starter/testbench/run_fft_tt.py) — 夹具、模板或数据处理辅助
- [environment/starter/testbench/tb_acquisition_tt.spi](../sources/upstream/tasks/sky130-bottom-plate-sampler-pvt/environment/starter/testbench/tb_acquisition_tt.spi) — tran
- [environment/starter/testbench/tb_fft_tt.spi](../sources/upstream/tasks/sky130-bottom-plate-sampler-pvt/environment/starter/testbench/tb_fft_tt.spi) — tran
- [environment/starter/testbench/tb_hold_tt.spi](../sources/upstream/tasks/sky130-bottom-plate-sampler-pvt/environment/starter/testbench/tb_hold_tt.spi) — tran
- [tests/benches/tb_fft.spi](../sources/upstream/tasks/sky130-bottom-plate-sampler-pvt/tests/benches/tb_fft.spi) — tran
- [tests/benches/tb_hold.spi](../sources/upstream/tasks/sky130-bottom-plate-sampler-pvt/tests/benches/tb_hold.spi) — tran
- [tests/benches/tb_static.spi](../sources/upstream/tasks/sky130-bottom-plate-sampler-pvt/tests/benches/tb_static.spi) — tran

## 相邻案例

[20 8:1 模拟 MUX：Ron、关断耦合与输入源阻抗相互牵制](20-sky130-analog-input-mux-8to1-pvt.md) · [22 自举采样驱动：VGS 平坦要与采样失真一起看](22-sky130-bootstrap-sampler-fft.md) · [28 FCT 残差放大器：保持稳定度不是目标建立误差](28-sky130-fct-residue-amplifier-900msps.md)
