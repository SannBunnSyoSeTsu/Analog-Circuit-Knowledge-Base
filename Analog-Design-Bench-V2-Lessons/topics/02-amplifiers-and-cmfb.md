# 放大器：从闭环任务反推 gm、补偿和共模预算

本页把案例间的共同结构写成选型依据。数值以各案例发布记录为证据，没有新增稳定性计算或仿真。

## 拓扑选择需要带上负载和误差定义

| 任务族 | 结构选择及得到的能力 | 主要代价/边界 |
|---|---|---|
| [44 5T OTA：最小拓扑也需要闭环噪声和环路定义](../cases/44-sky130-ota-5t-gain40-pm60-noise50uv-pvt.md) | 5T 加偏置，低复杂度单级 | ro 限制 DC 增益，输出高阻节点受负载影响 |
| [36 套筒 OTA：堆叠余量与共模感测极点](../cases/36-sky130-telescopic-cascode-ota-pvt-fix.md) | 套筒堆叠，提高单级增益 | 输入共模、摆幅和 cascode 余量 |
| [16 200 MHz 两级 Miller：快环路与宽带积分噪声的代价](../cases/16-sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt.md)、[41 高 PSRR 中速 Miller：偏置供电路径决定抑制能力](../cases/41-sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt.md) | 两级 Miller，分别偏高速与高 PSRR | 补偿零点、第二级 gm、噪声积分带宽不同 |
| [29 Ahuja 补偿：补偿接入点的阻抗决定物理作用](../cases/29-sky130-ahuja-compensated-two-stage-load-range-pvt.md) | Ahuja 低阻节点电流缓冲补偿 | 新局部节点与偏置极点，宽负载需额外覆盖 |
| [37 三级 Nested Miller：增益乘积与速度预算要分开](../cases/37-sky130-three-stage-nested-miller-ota-pvt.md) | 三级嵌套补偿，低功耗驱动 200 pF | 多环路模态、µs 级建立 |
| [50 130 dB 高速 OTA：局部增益增强环与外环必须分层分析](../cases/50-sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt.md) | 增益增强局部环叠加主环 | 局部稳定、再穿越与寄生余量 |

这些是任务条件下的可行路线，不能只按 gain/UGB 两列选赢家。尤其 [50 130 dB 高速 OTA：局部增益增强环与外环必须分层分析](../cases/50-sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt.md) 的 topology-neutral 条款允许其他实现，网站 pass 也不能反过来证明标题结构。

## 信号增益、噪声增益和反馈系数

[33 增益 1 采样反馈 OTA：差模建立和 CMFB 要分开验收](../cases/33-sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc.md) 的 Cs=Cf=1 pF 给信号增益 1，但输入端其他节点交流固定时，简化反馈系数为 `β=Cf/(Cs+Cf)=1/2`。[34 增益 8 采样反馈 OTA：β=1/9 决定环路速度](../cases/34-sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc.md) 的 Cs/Cf=8，则 β≈1/9，噪声增益约 9。输入/开关寄生会进一步改变 β。

在单主极点且小信号条件下，可用 `fclosed≈β·fu`、`tε≈ln(1/ε)/(2πβfu)` 做初始预算。以 ε=1%、t=10 ns、β=1/9 代入，只得到约 660 MHz 的单极点 fu 量级估算；不是对 reference 实际 UGB 或可达建立时间的测量。压摆率、非主极点、振铃和输出目标误差还会增加时间。因此要先确定步幅、CL、反馈系数和误差带，再定电流和 Cc，不能仅靠电容比改增益。

普通两级 Miller 的 `fu≈gm1/(2πCc)` 也仅为初步估算；Rc 是否消除 RHP 零点取决于第二级 gm 和结构。[29 Ahuja 补偿：补偿接入点的阻抗决定物理作用](../cases/29-sky130-ahuja-compensated-two-stage-load-range-pvt.md) 电容连到低阻共栅源端，与普通接第一高阻节点的 Miller 不同，不能照抄同一个 Rc 公式。

## 共模环路有自己的输入、执行器和极点

[33 增益 1 采样反馈 OTA：差模建立和 CMFB 要分开验收](../cases/33-sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc.md)–[35 全差分两级 Miller：高差模增益不能替代电源抑制](../cases/35-sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt.md) 的输出平均网络既有电阻也有电容，后者改变高频共模感测。感测放大器再驱动大电流源栅电容，必须分别观察感测节点和执行节点。差模 PM 好，不意味着共模环路稳定；CMRR 高，也不意味着输出共模恢复快。

[26 OTA-C 双二阶滤波器：状态节点的共模预算不能合并](../cases/26-sky130-fully-differential-ota-c-biquad-pvt.md) 给出更具体的教训：积分状态节点的上拉/下拉支路数不对称，CMFB 复制比例必须按真实电流求和。[25 轨到轨 Class-AB 运放：输入 gm 平整和内部模态同样重要](../cases/25-sky130-complementary-folded-cascode-ab-opamp-pvt.md) 的互补输入 gm 交接还会改变折叠级偏置；作者加入内部栅节点阻尼，是处理额外动态模态的线索，而不是通用固定电容值。

## 静态余量优先于“通过”标签

[34 增益 8 采样反馈 OTA：β=1/9 决定环路速度](../cases/34-sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc.md) 发布建立约 9.748 ns / 上限 10 ns，共模偏差约 24.499 mV / 上限 25 mV；[35 全差分两级 Miller：高差模增益不能替代电源抑制](../cases/35-sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt.md) 虽有约 101.5 dB 增益，功耗和 PSRR 仍接近门槛；[50 130 dB 高速 OTA：局部增益增强环与外环必须分层分析](../cases/50-sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt.md) UGB 与 PM 也只略超要求。这些例子说明应把每个指标的最坏工况和离门槛距离保存为知识，而不是只写“设计成功”。

建立时间应使用命令终值和 last-entry：进入误差带后，剩余窗口内全部样本都要留在带内。用最终均值重新定义目标会把 DC 增益误差隐藏掉。外环一次 PM 读数也不能代替首个下降跨频后无再穿越的检查。
