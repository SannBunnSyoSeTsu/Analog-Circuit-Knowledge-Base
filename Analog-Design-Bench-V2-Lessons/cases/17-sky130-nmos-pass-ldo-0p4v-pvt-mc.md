---
case_id: adb-v2-17
task_id: sky130-nmos-pass-ldo-0p4v-pvt-mc
category: 电源与驱动
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-nmos-pass-ldo-0p4v-pvt-mc/instruction.md
  - ../sources/upstream/tasks/sky130-nmos-pass-ldo-0p4v-pvt-mc/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-nmos-pass-ldo-0p4v-pvt-mc/tests/verify.py
  - ../sources/upstream/tasks/sky130-nmos-pass-ldo-0p4v-pvt-mc/results/reference.json
---

# 17 · 0.4 V NMOS LDO：低输出电压改变输入级和驱动极性

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

54 个 PVT/负载点，1/5 mA、外部 10 pF，环路 PM/GM、工作区、静态电流和 50 个 tt_mm 样本。

## Reference 拓扑与尺寸线索（静态事实）

PMOS 输入误差放大器配镜像正反馈结构，LVT NMOS pass；栅端使用很大的 MOSCAP（w=l=10 µm、m=1600）和 PDK MIM。

## 可复用的工程认识（推断，迁移时有条件）

低 VOUT 并不意味着可任意压低放大器供电余量。需要沿输入共模、误差放大器输出、NMOS VGS 和 pass 压降逐节点做 headroom 预算。大栅电容能移动极点，同时提高充放电需求；环路 AC 稳定不能单独代表快速负载响应。

## 不能由 pass 推出的结论

工作区检查只对超过指定电流阈值的器件生效。内置大电容没有面积惩罚，静态电流口径还排除特定外部参考支路；不与 capless 的数字直接比较。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-nmos-pass-ldo-0p4v-pvt-mc/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-nmos-pass-ldo-0p4v-pvt-mc/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-nmos-pass-ldo-0p4v-pvt-mc)
- [Reference circuit](../sources/upstream/tasks/sky130-nmos-pass-ldo-0p4v-pvt-mc/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-nmos-pass-ldo-0p4v-pvt-mc/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-nmos-pass-ldo-0p4v-pvt-mc/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-nmos-pass-ldo-0p4v-pvt-mc/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-nmos-pass-ldo-0p4v-pvt-mc/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-nmos-pass-ldo-0p4v-pvt-mc/circuit.spi) · [网站结果快照](../sources/astra/sky130-nmos-pass-ldo-0p4v-pvt-mc/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-nmos-pass-ldo-0p4v-pvt-mc/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-15T02:08:42+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `complete_signoff` | PVT/load=54/54 MC=50/50 |
| `pvt_output_range` | VOUT=0.399V..0.403V |
| `quiescent_current` | Iq=316.330uA..381.082uA |
| `loop_stability` | PM_min=87.348deg GM_min=42.688dB |
| `psrr_1khz` | PSRR_min=49.711dB |
| `active_device_headroom` | min(\|VDS\|-\|VDSAT\|)=162.785mV |
| `mismatch_3sigma_output` | mean+/-3sigma: 1mA=0.3966..0.4052V, 5mA=0.3964..0.4050V |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/tb_nominal.spi](../sources/upstream/tasks/sky130-nmos-pass-ldo-0p4v-pvt-mc/environment/starter/testbench/tb_nominal.spi) — ac, op
- [tests/benches/tb_mc.spi](../sources/upstream/tasks/sky130-nmos-pass-ldo-0p4v-pvt-mc/tests/benches/tb_mc.spi) — op
- [tests/benches/tb_point.spi](../sources/upstream/tasks/sky130-nmos-pass-ldo-0p4v-pvt-mc/tests/benches/tb_point.spi) — ac, op

## 相邻案例

[07 5T 误差放大器 LDO：负载电容和 ESR 是环路参数](07-sky130-ldo-ota5-robust-pvt-mc.md) · [38 20 mA 无外部电容 LDO：片上储能仍可很大](38-sky130-capless-ldo-1v0-20ma-pvt.md) · [25 轨到轨 Class-AB 运放：输入 gm 平整和内部模态同样重要](25-sky130-complementary-folded-cascode-ab-opamp-pvt.md)
