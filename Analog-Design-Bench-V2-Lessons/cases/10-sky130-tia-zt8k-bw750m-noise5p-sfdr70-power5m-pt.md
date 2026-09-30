---
case_id: adb-v2-10
task_id: sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt
category: 放大器与滤波
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: true
derived_from:
  - ../sources/upstream/tasks/sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt/instruction.md
  - ../sources/upstream/tasks/sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt/tests/verify.py
  - ../sources/upstream/tasks/sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt/results/reference.json
---

# 10 · 宽带 TIA：跨阻、输入噪声与大信号不能分开定规格

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

五工艺角落 × 三温度、固定 1.8 V；输入 0.3 pF、输出 0.2 pF、20 µA IREF。ZT≥8 kΩ、BW≥750 MHz，10–500 MHz 输入电流噪声密度/积分双限制。

## Reference 拓扑与尺寸线索（静态事实）

参考先用互补反相器电阻反馈跨阻级 RF=5.55 kΩ，再接约 13.2/5.5 的电压增益级，直流回路另含 1 MΩ 偏置电阻。

## 可复用的工程认识（推断，迁移时有条件）

分配跨阻与电压增益可以缓解单个大反馈电阻的带宽压力，但第二级噪声和失真需要折算到输入。最终 SFDR 的 100 MHz 输入电流峰值是 10 µA；公开诊断中的 5 µA 测试不能代替这个更强压力。功耗纳入 VDD 与 VCM 供能。

## 不能由 pass 推出的结论

Astra 替代解用了大面积 PDK MIM，实现上与 reference 很不同；没有面积指标时，低功耗并非成本更低的充分证据。见 Astra 专文。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt)
- [Reference circuit](../sources/upstream/tasks/sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt/circuit.spi) · [网站结果快照](../sources/astra/sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 已做定向电路比较，见 [Astra 对照](../topics/08-astra-comparisons.md)。

Reference 结果生成时间：`2026-08-14T20:00:31+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `pvt_transimpedance` | worst=8.13552 kOhm at ff/+85C/1.80V (requirement >8) |
| `pvt_bandwidth` | worst=764.863 MHz at ss/-40C/1.80V (requirement >750) |
| `pvt_power` | worst=4.29527 mW at ff/+85C/1.80V (requirement <5) |
| `pvt_noise_density` | worst=4.08673 pA/sqrt(Hz) at ss/+85C/1.80V (requirement <5) |
| `pvt_integrated_noise` | worst=0.0767408 uA rms at ss/+85C/1.80V (requirement <0.1) |
| `pvt_sfdr` | minimum SFDR=71.2431 dBc at fs/+85C/1.80V (>70); minimum large-signal ZT=8.07071 kOhm at ff/+85C/1.80V (>8) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/measure_ac.py](../sources/upstream/tasks/sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt/environment/starter/testbench/measure_ac.py) — 夹具、模板或数据处理辅助
- [environment/starter/testbench/measure_noise.py](../sources/upstream/tasks/sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt/environment/starter/testbench/measure_noise.py) — 夹具、模板或数据处理辅助
- [environment/starter/testbench/measure_sfdr.py](../sources/upstream/tasks/sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt/environment/starter/testbench/measure_sfdr.py) — 夹具、模板或数据处理辅助
- [environment/starter/testbench/run_public.py](../sources/upstream/tasks/sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt/environment/starter/testbench/run_public.py) — ac, noise
- [environment/starter/testbench/tb_ac_tt.spi](../sources/upstream/tasks/sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt/environment/starter/testbench/tb_ac_tt.spi) — ac, op
- [environment/starter/testbench/tb_noise_tt.spi](../sources/upstream/tasks/sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt/environment/starter/testbench/tb_noise_tt.spi) — noise
- [environment/starter/testbench/tb_sfdr_tt.spi](../sources/upstream/tasks/sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt/environment/starter/testbench/tb_sfdr_tt.spi) — tran
- [tests/benches/tb_ac_power.spi](../sources/upstream/tasks/sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt/tests/benches/tb_ac_power.spi) — ac, op
- [tests/benches/tb_noise.spi](../sources/upstream/tasks/sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt/tests/benches/tb_noise.spi) — noise
- [tests/benches/tb_sfdr.spi](../sources/upstream/tasks/sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt/tests/benches/tb_sfdr.spi) — tran

## 相邻案例

[08 自举互补源跟随器：小输入电流不等于小物理电容](08-sky130-buf-ppsf-bs-gain1-sfdr90.md) · [30 Gilbert 混频器：线性指标需要幅度斜率自检](30-sky130-gilbert-cell-mixer-2p4ghz-pvt-mismatch.md) · [43 2.4 GHz LNA：匹配、噪声与稳定性要使用同一端口定义](43-sky130-inductive-lna-2p4ghz-gain12-nf2-pvt.md)
