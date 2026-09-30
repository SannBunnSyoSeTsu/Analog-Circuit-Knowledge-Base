---
case_id: adb-v2-22
task_id: sky130-bootstrap-sampler-fft
category: 采样与数据转换
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-bootstrap-sampler-fft/instruction.md
  - ../sources/upstream/tasks/sky130-bootstrap-sampler-fft/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-bootstrap-sampler-fft/tests/verify.py
  - ../sources/upstream/tasks/sky130-bootstrap-sampler-fft/results/reference.json
---

# 22 · 自举采样驱动：VGS 平坦要与采样失真一起看

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

设计对象只有驱动器；bench 提供 w/l=64/0.15 的采样管、1 pF 保持电容，100 MHz、低相跟踪。11 个 PVT 点，32 点相干 FFT 的 bin15，即 46.875 MHz。

## Reference 拓扑与尺寸线索（静态事实）

两组自举单元，约 950 fF 储能，预充、钳位和输出传递支路构成浮动栅驱动。

## 可复用的工程认识（推断，迁移时有条件）

自举目的是降低输入相关的导通电阻变化；检查中点 VGS/VDD 下限之外，还要保留信号增益和高频 SDR。驱动器和采样管归属必须分开，否则会误算总器件数、功率与噪声。

## 不能由 pass 推出的结论

功耗未覆盖所有外部时钟缓冲；有限长无随机噪声 FFT 不能证明热噪声或 kT/C。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-bootstrap-sampler-fft/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-bootstrap-sampler-fft/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-bootstrap-sampler-fft)
- [Reference circuit](../sources/upstream/tasks/sky130-bootstrap-sampler-fft/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-bootstrap-sampler-fft/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-bootstrap-sampler-fft/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-bootstrap-sampler-fft/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-bootstrap-sampler-fft/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-bootstrap-sampler-fft/circuit.spi) · [网站结果快照](../sources/astra/sky130-bootstrap-sampler-fft/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-bootstrap-sampler-fft/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-14T20:05:07+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `complete_signoff` | 22/22 serial analyses complete |
| `pvt_sdr` | worst=75.50dB at ss_1p98v_125c (min 72dB) |
| `pvt_midtrack_vgs` | worst=0.8162*VDD at ff_1p62v_125c (min 0.8*VDD) |
| `acquisition_and_hold` | worst retained gain=0.9841 at ff_1p98v_m40c negative_retained_gain (min 0.9) |
| `pvt_power` | max=303.1uW at ff_1p98v_125c (max 500uW) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/check_nominal.py](../sources/upstream/tasks/sky130-bootstrap-sampler-fft/environment/starter/testbench/check_nominal.py) — 夹具、模板或数据处理辅助
- [environment/starter/testbench/tb_fft_tt.spi](../sources/upstream/tasks/sky130-bootstrap-sampler-fft/environment/starter/testbench/tb_fft_tt.spi) — tran
- [environment/starter/testbench/tb_static_tt.spi](../sources/upstream/tasks/sky130-bootstrap-sampler-fft/environment/starter/testbench/tb_static_tt.spi) — tran
- [tests/benches/tb_fft.spi](../sources/upstream/tasks/sky130-bootstrap-sampler-fft/tests/benches/tb_fft.spi) — tran
- [tests/benches/tb_static.spi](../sources/upstream/tasks/sky130-bootstrap-sampler-fft/tests/benches/tb_static.spi) — tran

## 相邻案例

[05 高侧自举驱动：以源极为参考检查 VGS](05-sky130-bootstrap-driver-pt.md) · [20 8:1 模拟 MUX：Ron、关断耦合与输入源阻抗相互牵制](20-sky130-analog-input-mux-8to1-pvt.md) · [31 底板采样：存储电压必须按两端差计算](31-sky130-bottom-plate-sampler-pvt.md)
