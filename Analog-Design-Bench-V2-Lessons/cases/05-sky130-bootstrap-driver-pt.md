---
case_id: adb-v2-05
task_id: sky130-bootstrap-driver-pt
category: 电源与驱动
retrieved_date: 2026-09-20
source_commit: c23f124de1e461655d2e02ce6cfae2654ccea0d3
evidence: static-source-review-and-published-results
local_simulation: false
astra_r1_detailed_review: false
derived_from:
  - ../sources/upstream/tasks/sky130-bootstrap-driver-pt/instruction.md
  - ../sources/upstream/tasks/sky130-bootstrap-driver-pt/solution/circuit.spi
  - ../sources/upstream/tasks/sky130-bootstrap-driver-pt/tests/verify.py
  - ../sources/upstream/tasks/sky130-bootstrap-driver-pt/results/reference.json
---

# 05 · 高侧自举驱动：以源极为参考检查 VGS

本页为静态学习笔记；下方结果是上游已发布结果，本次没有运行电路、testbench、verifier 或 PDK。拓扑事实与工程推断分开记录。

## 场景与测试边界

被设计对象仅为半桥栅驱动，功率 NMOS 与 3.6 Ω 负载由 bench 提供；包含自举及电源路径寄生。tt/fs/sf × 27/80/125 °C × 20/50/80 ns 脉宽，共 27 点。

## Reference 拓扑与尺寸线索（静态事实）

浮动缓冲用 1.8 V 器件，电平转换/充电路径用 5 V 器件；外部 620 pF 自举电容，内部 MIM 为 30×30 µm、m=30。

## 可复用的工程认识（推断，迁移时有条件）

高侧必须测 VGN−VSW，而非栅极对地电压；平均栅压、峰值栅压、VBST、死区与峰值电流各约束不同故障模式。自举电容要兼顾栅电荷、漏电与最短充电时间。记录面积时须使用本题 check_area.py 的计分规则，不能自行把所有乘数都当作可互换参数。

## 不能由 pass 推出的结论

本题 MOS 面积计分采用 W·L·nf·m；通用 guide 则说明 W 是总宽、nf 为分指。两者应分别记录为计分口径和模型几何，不能把计分式推广为物理面积。峰值高侧电流包含负载电流，不等于纯直通电流。

## 证据入口

- [任务说明](../sources/upstream/tasks/sky130-bootstrap-driver-pt/instruction.md) · [任务配置](../sources/upstream/tasks/sky130-bootstrap-driver-pt/task.toml) · [网站任务](https://analog-design-bench.tokenzhang.com/task/v2/sky130-bootstrap-driver-pt)
- [Reference circuit](../sources/upstream/tasks/sky130-bootstrap-driver-pt/solution/circuit.spi) · [发布结果](../sources/upstream/tasks/sky130-bootstrap-driver-pt/results/reference.json)
- [正式测量/聚合逻辑](../sources/upstream/tasks/sky130-bootstrap-driver-pt/tests/verify.py) · [测试目录](../sources/upstream/tasks/sky130-bootstrap-driver-pt/tests) · [公开诊断材料](../sources/upstream/tasks/sky130-bootstrap-driver-pt/environment/starter)
- [Astra Max R1 最终电路](../sources/astra/sky130-bootstrap-driver-pt/circuit.spi) · [网站结果快照](../sources/astra/sky130-bootstrap-driver-pt/result.json) · [网站运行记录](https://analog-design-bench.tokenzhang.com/task/v2/sky130-bootstrap-driver-pt/runs/gpt-6-astra-thinking-max/run-1)

该 R1 的最终电路与结果已归档；本轮未对它做逐器件比较，不据此解释模型的求解过程。

Reference 结果生成时间：`2026-08-14T20:05:47+00:00`；源记录 ngspice `46`，Sky130 commit `c6d73a35f524070e85faff4a6a9eef49553ebc2b`。这仅描述上游环境；没有安装或调用它。

电路、instruction、task.toml 的三个 SHA-256 均与 reference provenance 一致。完整快照摘要见 [来源说明](../SOURCES.md)。

## 上游 reference 检查摘要（原文）

保留 `checks.message` 的单位、范围及最坏工况，避免扁平 metrics 把区间压成一个数；以下均为发布记录中的 `passed`，不是本次复验。

| 检查 | 发布测量/覆盖摘要 |
|---|---|
| `g1_deadtime_tt` | deadtime=[4.06,5.87]ns (need all in [3,7]) |
| `g2_power_tt` | max_power=2.93mW (limit < 3.5mW) |
| `g3_vgs_avg_min_tt` | min_vgs_avg=1.666V (need >= 1.65) |
| `g3_vgs_avg_max_tt` | max_vgs_avg=1.667V (need <= 1.85) |
| `g4_vgs_peak_tt` | max_vgs_peak=2.045V (limit < 2.15V) |
| `g5_hs_peak_tt` | max_hs_current=536.4mA (limit < 800mA) |
| `g6_1p8v_nodes_tt` | max_1p8v_voltage=[vbst-vlx=2.102V,gn2=1.890V] (limit < 2.15V) |
| `g6_5v_node_tt` | max_5v_voltage=vbst=4.192V (limit < 5.65V) |
| `g1_deadtime_fs` | deadtime=[3.75,5.63]ns (need all in [3,7]) |
| `g2_power_fs` | max_power=2.97mW (limit < 3.5mW) |
| `g3_vgs_avg_min_fs` | min_vgs_avg=1.669V (need >= 1.65) |
| `g3_vgs_avg_max_fs` | max_vgs_avg=1.670V (need <= 1.85) |
| `g4_vgs_peak_fs` | max_vgs_peak=2.004V (limit < 2.15V) |
| `g5_hs_peak_fs` | max_hs_current=538.4mA (limit < 800mA) |
| `g6_1p8v_nodes_fs` | max_1p8v_voltage=[vbst-vlx=2.135V,gn2=1.912V] (limit < 2.15V) |
| `g6_5v_node_fs` | max_5v_voltage=vbst=4.220V (limit < 5.65V) |
| `g1_deadtime_sf` | deadtime=[4.39,6.15]ns (need all in [3,7]) |
| `g2_power_sf` | max_power=2.90mW (limit < 3.5mW) |
| `g3_vgs_avg_min_sf` | min_vgs_avg=1.664V (need >= 1.65) |
| `g3_vgs_avg_max_sf` | max_vgs_avg=1.665V (need <= 1.85) |
| `g4_vgs_peak_sf` | max_vgs_peak=2.071V (limit < 2.15V) |
| `g5_hs_peak_sf` | max_hs_current=531.6mA (limit < 800mA) |
| `g6_1p8v_nodes_sf` | max_1p8v_voltage=[vbst-vlx=2.103V,gn2=1.861V] (limit < 2.15V) |
| `g6_5v_node_sf` | max_5v_voltage=vbst=4.153V (limit < 5.65V) |

## Testbench 查阅索引

下面是公开诊断、正式 deck 与辅助夹具的文件入口；分析类别来自文本扫描，只用于定位。含激励表的长文件不把逐行数据枚举视为新的工程结论。

- [environment/starter/testbench/tb_bootstrap_driver_tt_1p80v_27c.spi](../sources/upstream/tasks/sky130-bootstrap-driver-pt/environment/starter/testbench/tb_bootstrap_driver_tt_1p80v_27c.spi) — tran
- [tests/benches/tb_fs.spi](../sources/upstream/tasks/sky130-bootstrap-driver-pt/tests/benches/tb_fs.spi) — tran
- [tests/benches/tb_sf.spi](../sources/upstream/tasks/sky130-bootstrap-driver-pt/tests/benches/tb_sf.spi) — tran
- [tests/benches/tb_tt.spi](../sources/upstream/tasks/sky130-bootstrap-driver-pt/tests/benches/tb_tt.spi) — tran

## 相邻案例

[01 Class-D 半桥：导通损耗与驱动损耗必须一起算](01-sky130-class-d-halfbridge-eff95-tt.md) · [22 自举采样驱动：VGS 平坦要与采样失真一起看](22-sky130-bootstrap-sampler-fft.md) · [31 底板采样：存储电压必须按两端差计算](31-sky130-bottom-plate-sampler-pvt.md)
