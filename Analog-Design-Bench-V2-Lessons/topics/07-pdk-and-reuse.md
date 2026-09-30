# PDK 语法、抽象条件与已有知识的连接

## 从实际案例保留下来的模型使用规则

主要依据：[上游 Sky130 netlist guide](../sources/upstream/tasks/sky130-analog-input-mux-8to1-pvt/environment/starter/SKY130_NETLIST_GUIDE.md)，结合 [05 高侧自举驱动：以源极为参考检查 VGS](../cases/05-sky130-bootstrap-driver-pt.md)、[06 三级 Ring Amp：电容比、死区与动态终止共同定增益](../cases/06-sky130-ring-amp-3stage-gain8-400uw.md)、[43 2.4 GHz LNA：匹配、噪声与稳定性要使用同一端口定义](../cases/43-sky130-inductive-lna-2p4ghz-gain12-nf2-pvt.md)、[49 2 GHz LC VCO：调谐范围、pushing 与启动初值分开记录](../cases/49-sky130-lc-vco-2ghz-pvt.md)。这些规则属于所归档的模型/包装版本，不自动适用于其他 PDK。

- MOS 使用 `X` 子电路，端序 D G S B；模型 `.option scale=1u` 环境下裸 l/w 为微米几何。不要把 `w=10` 与 `w=10u` 无条件视为同一输入。
- guide 中 w 表示总宽，nf 分指使每指宽约 w/nf；并联倍数增加器件副本。不同的 nf/m 组合可能进入不同 model bin、寄生与布局条件。[06 三级 Ring Amp：电容比、死区与动态终止共同定增益](../cases/06-sky130-ring-amp-3stage-gain8-400uw.md) 的模型报错修订是几何合法性线索，不能证明改 nf 后电气完全不变。
- 标准 1.8 V NMOS/PMOS 和 NMOS LVT 的最小 L 不能套到 PMOS LVT；guide 给后者最小 L=0.35 µm。混合高压自举路径还要用相应 5 V 器件约束。
- 物理电阻有第三衬底端，几何 l 不是欧姆值；MIM 的 `mf`、变容的 `vm` 与 MOS 的 `m/nf` 各有包装语义。电感四端为 a/b/ct/sub，半绕组接法需明确闲置端。
- SPICE `M` 是 milli；mega 用 `meg`。理想正电阻/电容是否允许，以每题 checker 参数为准，不以标题或别题经验判断。
- [05 高侧自举驱动：以源极为参考检查 VGS](../cases/05-sky130-bootstrap-driver-pt.md) 面积 checker 的 W·L·nf·m 是本题计分式，与 guide 总宽语义不同；保留这个差异，不把计分乘积改写成晶体管物理面积公式。

本次没有生成 gm/ID 曲线或调用 gmoverid：既有网表只能提供尺寸和偏置线索，不能反推出精确 gm/ID、fT 或器件工作区。未来若进行新尺寸设计，再使用安装的 gmoverid 技能及相应模型资产；这不属于本次已做工作。

## 如何与已有知识库一起使用

| 已有理论笔记（未修改） | 新的工程例子 | 增补的经验维度 |
|---|---|---|
| [5T 差分放大器](../../5T-Differential-Amplifier-Analysis.md) | [44 5T OTA：最小拓扑也需要闭环噪声和环路定义](../cases/44-sky130-ota-5t-gain40-pm60-noise50uv-pvt.md)、[07 5T 误差放大器 LDO：负载电容和 ESR 是环路参数](../cases/07-sky130-ldo-ota5-robust-pvt-mc.md) | 27 点 PVT；作为 LDO 误差放大器时的外部储能条件 |
| [Miller 两级](../../Miller-Compensated-Two-Stage-Amplifier.md) | [16 200 MHz 两级 Miller：快环路与宽带积分噪声的代价](../cases/16-sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt.md)、[41 高 PSRR 中速 Miller：偏置供电路径决定抑制能力](../cases/41-sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt.md)、[35 全差分两级 Miller：高差模增益不能替代电源抑制](../cases/35-sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt.md) | 噪声带宽、PSRR、CMFB 与补偿余量 |
| [带宽计算](../../Amplifier-Bandwidth-Calculations.md) | [29 Ahuja 补偿：补偿接入点的阻抗决定物理作用](../cases/29-sky130-ahuja-compensated-two-stage-load-range-pvt.md)、[33 增益 1 采样反馈 OTA：差模建立和 CMFB 要分开验收](../cases/33-sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc.md)、[34 增益 8 采样反馈 OTA：β=1/9 决定环路速度](../cases/34-sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc.md) | Ahuja 接入点、反馈系数、last-entry 建立 |
| [Ring Amplifier](../../Ring-Amplifier.md) | [06 三级 Ring Amp：电容比、死区与动态终止共同定增益](../cases/06-sky130-ring-amp-3stage-gain8-400uw.md) | 外部复位/自动调零，死区及采样斜率验证 |
| [Floating Charge Transfer](../../Floating-Charge-Transfer-Amplifier.md) | [28 FCT 残差放大器：保持稳定度不是目标建立误差](../cases/28-sky130-fct-residue-amplifier-900msps.md) | 理想夹具边界，保持漂移与增益误差的区别 |
| [Floating Inverter](../../Floating-Inverter-Amplifier.md) | [28 FCT 残差放大器：保持稳定度不是目标建立误差](../cases/28-sky130-fct-residue-amplifier-900msps.md) | 浮动储能思想相邻，但不是相同拓扑的等价证明 |
| [退化电阻噪声](../../Degenerated-Resistor-Noise.md) | [03 局部反馈恒 gm 放大器：用反馈压低有效跨导漂移](../cases/03-sky130-gmr-degen-amp-constant-gm-pvt.md)、[04 简单退化差分对：有限 gm 是增益预算的一部分](../cases/04-sky130-gmr-degenerated-diff-amp-gain2-bw70m-power1p2mw-sdr60.md)、[13 恒 gm 稳增益：偏置单元必须映射到输入电流密度](../cases/13-sky130-constant-gm-stable-gain-amplifier-pvt.md)、[30 Gilbert 混频器：线性指标需要幅度斜率自检](../cases/30-sky130-gilbert-cell-mixer-2p4ghz-pvt-mismatch.md) | 有限 gm、线性、增益与真实偏置的联合预算 |
| [比较器噪声](../../Comparator-Noise-Calculation.md) | [27 4 bit Flash ADC：前端采样与编码必须纳入转换链](../cases/27-sky130-flash-adc-4bit-50msps.md)、[42 6 bit 异步 SAR：采集窗、握手与最终寄存都影响正确性](../cases/42-sky130-sar-adc-6bit-async.md)、[46 3 bit Flash：阈值绝对位置与编码尾部延迟都要检查](../cases/46-sky130-flash-adc-3bit-pvt.md) | 确定性通过不补充噪声/亚稳态统计证据 |
| [kT/C 噪声抵消](../../kTC-Noise-Cancellation.md)、[CDS](../../Correlated-Double-Sampling.md) | [22 自举采样驱动：VGS 平坦要与采样失真一起看](../cases/22-sky130-bootstrap-sampler-fft.md)、[31 底板采样：存储电压必须按两端差计算](../cases/31-sky130-bottom-plate-sampler-pvt.md)、[40 一阶 ΔΣ：先划清 DUT 与外部模拟核心](../cases/40-sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40.md) | 时序与存储量的工程实例；不冒充噪声抵消实测 |
| [相位噪声](../../Phase-Noise-Calculations.md) | [14 低功耗 2 MHz 振荡器：缓冲与启动都占功率预算](../cases/14-sky130-low-power-oscillator-2mhz-pvt.md)、[24 限流环 VCO：调谐单调性与增益一致性需要独立约束](../cases/24-sky130-current-starved-ring-vco-pvt.md)、[49 2 GHz LC VCO：调谐范围、pushing 与启动初值分开记录](../cases/49-sky130-lc-vco-2ghz-pvt.md) | 初值、调谐及 pushing；明确缺少相噪测量 |

已有知识库文件维持原样；新的证据与解释集中在本目录。这里的交叉链接表示相邻主题，不暗示原理论已由这些任务完整验证。

## 复用时保存“合同包”

最小合同包应含：端口/夹具、模型版本、器件与理想元件限制、刺激/负载/时序、角落矩阵、测量公式、发布结果与源文件哈希。只拿 reference circuit 会丢掉其中大部分约束；只拿 pass 表又看不到物理机制。50 个案例把两者保持相邻，便于以后按实际系统需求挑选。
