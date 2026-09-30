# 电源、功率与启动：把全部供能端口放回系统

## 同样的 µW 数字可能没有相同边界

| 案例 | 发布指标的重要边界 | 迁移含义 |
|---|---|---|
| [01 Class-D 半桥：导通损耗与驱动损耗必须一起算](../cases/01-sky130-class-d-halfbridge-eff95-tt.md) | 效率包含驱动时钟供能 | 大功率管栅电荷不能免费 |
| [19 2:1 开关电容降压：轻载效率揭示固定开关损耗](../cases/19-sky130-switched-capacitor-2to1-converter-pvt.md) | 各时钟源正向功率计入，不抵扣回灌 | 不是所有源净功率直接求和 |
| [10 宽带 TIA：跨阻、输入噪声与大信号不能分开定规格](../cases/10-sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt.md) | VDD 与 VCM 都进入功率 | 共模端不能作为隐藏电源 |
| [18 受控升压泵：先确定控制变量和关断边界](../cases/18-sky130-regulated-charge-pump-10mhz-pvt.md) | AVDD 指标排除指定 1 µA 外部偏置 | 不能直接当完整转换器功耗 |
| [28 FCT 残差放大器：保持稳定度不是目标建立误差](../cases/28-sky130-fct-residue-amplifier-900msps.md) | 计 DUT 多端口，排除理想采样夹具 | 核心功耗不等于系统功耗 |
| [32 28 Gb/s CML 发射器：带宽还需眼图和群延迟约束](../cases/32-sky130-cml-tx-driver-28g-nrz-pvt.md) | 输出两只 50 Ω 终端供能必须计入 | CML 负载电流也是发送机耗电 |
| [40 一阶 ΔΣ：先划清 DUT 与外部模拟核心](../cases/40-sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40.md) | 含外部 OTA/比较器 VDD，排除外部时钟 | 任务交付范围与计功耗范围并不相同 |

SPICE 电压源电流通常以流入其正端为正，供能源可能显示负值。应从 verifier 的符号与聚合式建立账本，不能机械取绝对值；正向功率截断和允许回灌抵扣是不同的物理/计费模型。时间窗口同样影响结论：启动充电与稳态转换不应混算后再互相比较。

## LDO 有三种很不同的储能条件

[07 5T 误差放大器 LDO：负载电容和 ESR 是环路参数](../cases/07-sky130-ldo-ota5-robust-pvt-mc.md) 借助外部 µF 级电容与 ESR；[17 0.4 V NMOS LDO：低输出电压改变输入级和驱动极性](../cases/17-sky130-nmos-pass-ldo-0p4v-pvt-mc.md) 用 NMOS pass、很大的内部 MOSCAP 和小外部负载；[38 20 mA 无外部电容 LDO：片上储能仍可很大](../cases/38-sky130-capless-ldo-1v0-20ma-pvt.md) 虽名为 capless，允许内部总计 1 nF 理想电容。三者无法只按“20/30 mA、几十 mV 瞬态”排序。

瞬态初步关系 `ΔV≈ΔI·Δt/C + ΔI·ESR` 可用来判断控制器开始响应前的储能要求，但 Δt 必须对应真实驱动/环路延迟，不能事后任取。随负载移动的输出极点、pass 栅极极点、反馈前馈零点、ESR 零点都需要对应到具体连接。[38 20 mA 无外部电容 LDO：片上储能仍可很大](../cases/38-sky130-capless-ldo-1v0-20ma-pvt.md) 的输出串阻阻尼与 lead 电容就是不同动态路径，不能简单加成一个“输出 C”。

此外，低负载静态调节和零负载阶跃是不同条件；[38 20 mA 无外部电容 LDO：片上储能仍可很大](../cases/38-sky130-capless-ldo-1v0-20ma-pvt.md) 的动态起点是 0.5 mA，不是 0。供电源、基准源以及电压裕量也属于合同的一部分。

## 电荷泵与开关电容转换器的共同预算

[15 开环升压电荷泵：关断状态仍有时钟压力](../cases/15-sky130-unregulated-charge-pump-10mhz-pvt.md) 的开环升压、[18 受控升压泵：先确定控制变量和关断边界](../cases/18-sky130-regulated-charge-pump-10mhz-pvt.md) 的受控时钟摆幅升压、[19 2:1 开关电容降压：轻载效率揭示固定开关损耗](../cases/19-sky130-switched-capacitor-2to1-converter-pvt.md) 的交错 2:1 降压，都需要把理想转换比与有限电荷转移分开。慢开关近似下电阻随 `1/(f·Cfly)` 变化，但快开关区由 Ron 与互连主导；提升 f/C 会增大底板和栅驱损耗。

[19 2:1 开关电容降压：轻载效率揭示固定开关损耗](../cases/19-sky130-switched-capacitor-2to1-converter-pvt.md) 的轻载效率明显低于重载，是固定开关损耗的直接案例；[15 开环升压电荷泵：关断状态仍有时钟压力](../cases/15-sky130-unregulated-charge-pump-10mhz-pvt.md)/[18 受控升压泵：先确定控制变量和关断边界](../cases/18-sky130-regulated-charge-pump-10mhz-pvt.md) 的 enable 关闭时仍检查外部时钟存在，提醒门控位置必须真正隔离内部翻转和偏置。

## 启动不是把 transient 延长一点

自偏置需要逃离零电流平衡点；储能系统需要正确的初始充电路径；振荡器需要扰动增长与幅度限制。三者的判据分别可能是稳定工作电流、输出进入目标窗、连续有效周期。[11 带隙基准：温度补偿、启动和噪声是三件事](../cases/11-sky130-bandgap-reference-pvt.md)/[12 β 倍增偏置：恒 gm 条件来自器件比和电阻](../cases/12-sky130-beta-multiplier-reference-pvt-mc.md) 的关断启动支路、[05 高侧自举驱动：以源极为参考检查 VGS](../cases/05-sky130-bootstrap-driver-pt.md) 的最短自举充电时间、[49 2 GHz LC VCO：调谐范围、pushing 与启动初值分开记录](../cases/49-sky130-lc-vco-2ghz-pvt.md) 的预设不对称初值应各自记录，不能统一写成“启动成功”。
