---
case_id: adb-v2-29
task_id: sky130-ahuja-compensated-two-stage-load-range-pvt
category: 放大器与滤波
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-ahuja-compensated-two-stage-load-range-pvt/instruction.md
  - ../sources/upstream/tasks/sky130-ahuja-compensated-two-stage-load-range-pvt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-ahuja-compensated-two-stage-load-range-pvt/tests/verify.py
  - ../sources/upstream/tasks/sky130-ahuja-compensated-two-stage-load-range-pvt/results/reference.json
---

# 29 · Ahuja 补偿：补偿接入点的阻抗决定物理作用

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

45 点 PVT，20/200 pF 两端负载，另在五角落标称电压温度下检查 63 pF；要求单次有效跨频、不在后续频段再穿越，重载阶跃≤2 µs。

## Reference 拓扑与尺寸线索（静态事实）

折叠第一级与 NMOS 第二级，3.3 pF 从输出接至折叠支路 PMOS 共栅源端 f2；偏置另有 RC 去耦。

## 可复用的工程认识（推断，迁移时有条件）

补偿电流先进入低阻抗电流缓冲节点，不能简单等同于从输出接高阻第一增益节点的普通 Miller 电容。负载范围设计要同时看输出极点的移动、缓冲节点极点和偏置网络；端点加中间点能发现部分中间负载问题。

## 不能由 pass 推出的结论

63 pF 只在声明的子矩阵检查，不代表所有中间负载均有保证。采用局部电流缓冲补偿后仍需保留大信号恢复与偏置扰动检查。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-ahuja-compensated-two-stage-load-range-pvt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-ahuja-compensated-two-stage-load-range-pvt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-ahuja-compensated-two-stage-load-range-pvt)
- [Reference circuit](../sources/upstream/tasks/sky130-ahuja-compensated-two-stage-load-range-pvt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-ahuja-compensated-two-stage-load-range-pvt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-ahuja-compensated-two-stage-load-range-pvt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-ahuja-compensated-two-stage-load-range-pvt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-ahuja-compensated-two-stage-load-range-pvt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-ahuja-compensated-two-stage-load-range-pvt/circuit.spi) · [网站结果快照](../sources/astra/sky130-ahuja-compensated-two-stage-load-range-pvt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-ahuja-compensated-two-stage-load-range-pvt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-14T20:06:13+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `open_loop_gain` | worst=79.49dB at ff/1.62V/+125C (min 58dB) |
| `unity_gain_bandwidth` | worst=9.703MHz at fs/1.98V/+125C (min 6.5MHz) |
| `phase_margin_light_load` | worst=92.94deg at fs/1.98V/+125C (min 60deg) |
| `phase_margin_heavy_load` | worst=83.24deg at sf/1.62V/-40C (min 60deg) |
| `intermediate_load_stability` | PM_63p_min=91.06deg at fs/1.80V/+27C/63pF (min 60deg), return_above_0dB_points=0, repeak_max=-6.00dB at ff/1.98V/+27C (~-6dB means no re-approach) |
| `follower_offset` | worst=0.1268mV at ff/1.62V/+125C (max 6mV) |
| `heavy_load_settling` | settle_max=0.2613us at ss/1.62V/-40C (max 2us), err_end_max=0.1268mV at ff/1.62V/+125C (max 6mV) |
| `pvt_power` | worst=1.199mW at ff/1.98V/+125C (max 2mW) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/tb_ac_heavy_ss.spi](../sources/upstream/tasks/sky130-ahuja-compensated-two-stage-load-range-pvt/environment/starter/testbench/tb_ac_heavy_ss.spi) — ac
- [environment/starter/testbench/tb_ac_light_tt.spi](../sources/upstream/tasks/sky130-ahuja-compensated-two-stage-load-range-pvt/environment/starter/testbench/tb_ac_light_tt.spi) — ac, op
- [environment/starter/testbench/tb_step_tt.spi](../sources/upstream/tasks/sky130-ahuja-compensated-two-stage-load-range-pvt/environment/starter/testbench/tb_step_tt.spi) — tran
- [tests/benches/tb_ac_heavy.spi](../sources/upstream/tasks/sky130-ahuja-compensated-two-stage-load-range-pvt/tests/benches/tb_ac_heavy.spi) — ac
- [tests/benches/tb_ac_light.spi](../sources/upstream/tasks/sky130-ahuja-compensated-two-stage-load-range-pvt/tests/benches/tb_ac_light.spi) — ac, op
- [tests/benches/tb_ac_mid.spi](../sources/upstream/tasks/sky130-ahuja-compensated-two-stage-load-range-pvt/tests/benches/tb_ac_mid.spi) — ac
- [tests/benches/tb_step.spi](../sources/upstream/tasks/sky130-ahuja-compensated-two-stage-load-range-pvt/tests/benches/tb_step.spi) — tran

## 相邻案例

[16 200 MHz 两级 Miller：快环路与宽带积分噪声的代价](16-sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt.md) · [25 轨到轨 Class-AB 运放：输入 gm 平整和内部模态同样重要](25-sky130-complementary-folded-cascode-ab-opamp-pvt.md) · [37 三级 Nested Miller：增益乘积与速度预算要分开](37-sky130-three-stage-nested-miller-ota-pvt.md)
