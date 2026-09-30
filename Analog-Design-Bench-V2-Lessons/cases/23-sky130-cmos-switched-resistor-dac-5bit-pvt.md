---
case_id: adb-v2-23
task_id: sky130-cmos-switched-resistor-dac-5bit-pvt
category: 采样与数据转换
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-cmos-switched-resistor-dac-5bit-pvt/instruction.md
  - ../sources/upstream/tasks/sky130-cmos-switched-resistor-dac-5bit-pvt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-cmos-switched-resistor-dac-5bit-pvt/tests/verify.py
  - ../sources/upstream/tasks/sky130-cmos-switched-resistor-dac-5bit-pvt/results/reference.json
---

# 23 · 5 bit 电阻 DAC：分母由固定支路决定

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

11 个 PVT 点、200 MS/s、1 pF；INL/DNL、绝对端点、输出电阻和多种进位跳变，另有八个固定失配回归样本。

## Reference 拓扑与尺寸线索（静态事实）

物理电阻宽度 0.75/1.5/3/6/12 µm、L=15 µm，电导二进制加权；额外永久 LSB 下拉使总权重为 32 而非 31，开关与驱动随位权扩展。

## 可复用的工程认识（推断，迁移时有条件）

要从导通支路和固定支路推导 VOUT，不可见到五位就默认 code/31。静态 INL 合格不能取代 3↔4、7↔8、15↔16 的动态检查；进位时开关时序和电荷注入会叠加。

## 不能由 pass 推出的结论

固定八种失配不是良率估计。不同代码的 Rout 和输入参考负载不同，应保留 bench 的电流注入方向与测试点。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-cmos-switched-resistor-dac-5bit-pvt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-cmos-switched-resistor-dac-5bit-pvt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-cmos-switched-resistor-dac-5bit-pvt)
- [Reference circuit](../sources/upstream/tasks/sky130-cmos-switched-resistor-dac-5bit-pvt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-cmos-switched-resistor-dac-5bit-pvt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-cmos-switched-resistor-dac-5bit-pvt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-cmos-switched-resistor-dac-5bit-pvt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-cmos-switched-resistor-dac-5bit-pvt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-cmos-switched-resistor-dac-5bit-pvt/circuit.spi) · [网站结果快照](../sources/astra/sky130-cmos-switched-resistor-dac-5bit-pvt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-cmos-switched-resistor-dac-5bit-pvt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-14T20:06:05+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `pvt_inl` | max=0.2173LSB at ss_1p62v_m40c (max 0.25LSB) |
| `pvt_dnl_monotonic` | max_abs=0.2204LSB at ss_1p62v_m40c; monotonic=True |
| `pvt_endpoints` | zero_max=0.545mV at ff_1p98v_125c; code31_max=3.775mV at ss_1p98v_125c |
| `mismatch_linearity_monotonic` | INL_max=0.2399LSB at tt_mm_seed_41002; DNL_max=0.2889LSB at tt_mm_seed_41006; monotonic=True |
| `pvt_major_carry_settling` | crossing_max=3.80ns at ss_1p62v_m40c; end_error_max=0.1038LSB at ss_1p62v_125c (limits 5ns, 0.25LSB) |
| `pvt_major_carry_excursion` | max=0.8835LSB at ss_1p62v_m40c (max 1LSB) |
| `pvt_output_resistance` | range=1.148kohm at ss_1p98v_125c/rout_code28_ohm .. 1.276kohm at ss_1p80v_27c/rout_code0_ohm (max 2kohm) |
| `pvt_power` | max=940.15uW at ff_1p98v_125c (max 1000uW) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/tb_code_window_tt.spi](../sources/upstream/tasks/sky130-cmos-switched-resistor-dac-5bit-pvt/environment/starter/testbench/tb_code_window_tt.spi) — tran
- [environment/starter/testbench/tb_mismatch_seed_40999.spi](../sources/upstream/tasks/sky130-cmos-switched-resistor-dac-5bit-pvt/environment/starter/testbench/tb_mismatch_seed_40999.spi) — tran
- [environment/starter/testbench/tb_output_resistance_code10_ss.spi](../sources/upstream/tasks/sky130-cmos-switched-resistor-dac-5bit-pvt/environment/starter/testbench/tb_output_resistance_code10_ss.spi) — tran
- [environment/starter/testbench/tb_transition_5_6_ff.spi](../sources/upstream/tasks/sky130-cmos-switched-resistor-dac-5bit-pvt/environment/starter/testbench/tb_transition_5_6_ff.spi) — tran
- [tests/benches/tb_code_ramp.spi](../sources/upstream/tasks/sky130-cmos-switched-resistor-dac-5bit-pvt/tests/benches/tb_code_ramp.spi) — tran
- [tests/benches/tb_major_carry.spi](../sources/upstream/tasks/sky130-cmos-switched-resistor-dac-5bit-pvt/tests/benches/tb_major_carry.spi) — tran
- [tests/benches/tb_mismatch_ramp.spi](../sources/upstream/tasks/sky130-cmos-switched-resistor-dac-5bit-pvt/tests/benches/tb_mismatch_ramp.spi) — tran
- [tests/benches/tb_output_resistance.spi](../sources/upstream/tasks/sky130-cmos-switched-resistor-dac-5bit-pvt/tests/benches/tb_output_resistance.spi) — tran

## 相邻案例

[20 8:1 模拟 MUX：Ron、关断耦合与输入源阻抗相互牵制](20-sky130-analog-input-mux-8to1-pvt.md) · [27 4 bit Flash ADC：前端采样与编码必须纳入转换链](27-sky130-flash-adc-4bit-50msps.md) · [46 3 bit Flash：阈值绝对位置与编码尾部延迟都要检查](46-sky130-flash-adc-3bit-pvt.md)
