---
case_id: adb-v2-47
task_id: sky130-pll-charge-pump-pvt
category: 偏置与基准
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-pll-charge-pump-pvt/instruction.md
  - ../sources/upstream/tasks/sky130-pll-charge-pump-pvt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-pll-charge-pump-pvt/tests/verify.py
  - ../sources/upstream/tasks/sky130-pll-charge-pump-pvt/results/reference.json
---

# 47 · PLL 电荷泵：静态匹配与短脉冲电荷是两套预算

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

27 点 PVT，25 µA 参考生成约 50 µA UP/DN；输出顺从范围、平坦度、匹配、关断漏电、重叠电流，20 个连续固定种子及 10/1 ns 脉冲。

## Reference 拓扑与尺寸线索（静态事实）

级联电流转向结构，常偏置 dummy 支路，PMOS L=3/NMOS L=6 µm 复制镜，较大面积与偏置去耦，控制驱动强度不对称。

## 可复用的工程认识（推断，迁移时有条件）

保持镜支路导通并把电流切到 dummy，可减小每次重建工作点的延迟；dummy 电压应接近真实输出工作点，避免镜管 VDS 大跳。10 ns 脉冲以该点 DC 电流归一，1 ns 再对 10 ns 比例归一，可区分 DC 误差与脉冲边沿损失。

## 不能由 pass 推出的结论

小 DC 上下拉失配不保证零参考杂散；实际 PLL 中的死区、环路滤波、控制时序和布局注入未全部覆盖。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-pll-charge-pump-pvt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-pll-charge-pump-pvt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-pll-charge-pump-pvt)
- [Reference circuit](../sources/upstream/tasks/sky130-pll-charge-pump-pvt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-pll-charge-pump-pvt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-pll-charge-pump-pvt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-pll-charge-pump-pvt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-pll-charge-pump-pvt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-pll-charge-pump-pvt/circuit.spi) · [网站结果快照](../sources/astra/sky130-pll-charge-pump-pvt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-pll-charge-pump-pvt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-15T18:00:00Z`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `pvt_current_accuracy` | 27-point PVT current accuracy, flatness, and UP/DN matching passed |
| `pvt_inactive_modes` | off leakage and simultaneous-command net current passed |
| `tt_mm_up_dn_matching` | worst=1.136% at seed=31006; current=50.63..51.63 uA; seeds=20 |
| `representative_pulse_fidelity` | 10 ns, 1 ns, and overlap-charge pulse checks passed |
| `pvt_switching_speed` | turn-on and turn-off limits passed at all representative PVT points |
| `pvt_power` | all-port transient power passed the 500 uW limit |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/tb_dc_tt.spi](../sources/upstream/tasks/sky130-pll-charge-pump-pvt/environment/starter/testbench/tb_dc_tt.spi) — dc
- [environment/starter/testbench/tb_mm_tt.spi](../sources/upstream/tasks/sky130-pll-charge-pump-pvt/environment/starter/testbench/tb_mm_tt.spi) — dc
- [environment/starter/testbench/tb_pulse_tt.spi](../sources/upstream/tasks/sky130-pll-charge-pump-pvt/environment/starter/testbench/tb_pulse_tt.spi) — tran
- [tests/benches/tb_dc.spi](../sources/upstream/tasks/sky130-pll-charge-pump-pvt/tests/benches/tb_dc.spi) — dc
- [tests/benches/tb_pulse.spi](../sources/upstream/tasks/sky130-pll-charge-pump-pvt/tests/benches/tb_pulse.spi) — tran

## 相邻案例

[02 可编程 ICC/IPTAT 镜：比例正确还不够](02-sky130-programmable-icc-iptat-current-mirror-pvt.md) · [12 β 倍增偏置：恒 gm 条件来自器件比和电阻](12-sky130-beta-multiplier-reference-pvt-mc.md) · [24 限流环 VCO：调谐单调性与增益一致性需要独立约束](24-sky130-current-starved-ring-vco-pvt.md)
