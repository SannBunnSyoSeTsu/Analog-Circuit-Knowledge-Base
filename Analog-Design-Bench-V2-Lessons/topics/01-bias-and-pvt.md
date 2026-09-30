# 偏置、匹配与 PVT：让比例对工作点负责

证据类型：电路结构来自 reference；结果来自发布文件；以下公式和迁移解释为静态工程推断。没有执行新仿真。

## 1. 电流比不是只有 W/L 比

[02 可编程 ICC/IPTAT 镜：比例正确还不够](../cases/02-sky130-programmable-icc-iptat-current-mirror-pvt.md) 的参考作者记录了一个很有价值的失败原因：二极管支路和镜输出支路采用不同 L，以 TT 尺寸修正名义误差后，跨角落仍严重漂移。最终统一 L，再用输出 cascode 控制 VDS。平方律示意式

`Iout/Iref ≈ [(W/L)out/(W/L)ref] · [(Vov,out/Vov,ref)²] · [(1+λout·VDS,out)/(1+λref·VDS,ref)]`

说明几何比只占一项；短沟道、体效应和模型 bin 差异还会破坏简化关系。这里不是用平方律重新预测 Sky130 电流，而是用它定位尺寸补偿为什么不稳。Astra 的长 L 解是另一种减少输出电导影响的方法，也付出更大面积/寄生。

可迁移顺序是：同器件类型和 L → 相近电流密度 → 相近体偏置与 VDS → 足够顺从电压 → 再优化面积/噪声。加 cascode 前先把最低输出电压下每个管的余量分配清楚。[47 PLL 电荷泵：静态匹配与短脉冲电荷是两套预算](../cases/47-sky130-pll-charge-pump-pvt.md) 进一步表明，静态 VDS 匹配还不够，电流切换时的 dummy 工作点也必须接近真实输出。

## 2. “恒电流”和“恒 gm”不是同一目标

[12 β 倍增偏置：恒 gm 条件来自器件比和电阻](../cases/12-sky130-beta-multiplier-reference-pvt-mc.md) 的 K=4 β 倍增单元，用电阻约束两只 NMOS 的 VGS 差。长沟道平方律、同体电位和饱和近似下，`gm,small=2(1−1/√K)/R`，因此 K=4 得 `gm≈1/R`。[13 恒 gm 稳增益：偏置单元必须映射到输入电流密度](../cases/13-sky130-constant-gm-stable-gain-amplifier-pvt.md) 把基准电流密度映射到信号输入对，才把这个关系转成近似稳定增益；简单保证尾电流不变并不能消除迁移率造成的 gm 变化。

参考的 RB=2 kΩ、RL=8 kΩ 给理想增益 4，但发布值约 3.41–3.64。应学到“电阻比提供主要标尺”，同时保留体效应和 ro 修正。[03 局部反馈恒 gm 放大器：用反馈压低有效跨导漂移](../cases/03-sky130-gmr-degen-amp-constant-gm-pvt.md) 选择局部反馈与退化实现另一种有效 gm 稳定方式，[04 简单退化差分对：有限 gm 是增益预算的一部分](../cases/04-sky130-gmr-degenerated-diff-amp-gain2-bw70m-power1p2mw-sdr60.md) 则接受有限 gm 进入增益预算。三个例子构成不同复杂度的路线，而非一个公式的三种抄写。

## 3. 启动是独立状态问题

[11 带隙基准：温度补偿、启动和噪声是三件事](../cases/11-sky130-bandgap-reference-pvt.md)、[12 β 倍增偏置：恒 gm 条件来自器件比和电阻](../cases/12-sky130-beta-multiplier-reference-pvt-mc.md)、[13 恒 gm 稳增益：偏置单元必须映射到输入电流密度](../cases/13-sky130-constant-gm-stable-gain-amplifier-pvt.md) 都有自偏置环路。一个正确的 DC 工作点并不排除另一个零电流平衡点。读电路时要回答：全零初值下谁先提供电流？正常工作后谁使启动支路关闭？供电、VCM、IREF 先后变化会不会把系统锁住？

已有 bench 的供电斜坡、从零能量启动和绝对输出误差，提供了比“OP 收敛”更强的证据。[49 2 GHz LC VCO：调谐范围、pushing 与启动初值分开记录](../cases/49-sky130-lc-vco-2ghz-pvt.md) 则明确使用不对称初值帮助振荡器启动，不能与这些从零状态的启动测试等同。

## 4. 工艺角落和失配保持两个维度

| 证据 | 可以支持 | 不能支持 |
|---|---|---|
| tt/ss/ff 全局角落 | 声明条件下的全局速度/电压余量 | 左右支路随机失调 |
| fs/sf | 上下拉非对称压力 | 任意相关工艺分布 |
| 物理无源角落 | 所包含电阻/电容模型的变化 | 未建模理想元件的公差 |
| 固定 tt_mm 种子 | 给定种子集合的局部失配回归 | 量产良率或任意极值 |
| mc + mismatch 开关 | 源配置定义的组合随机变化 | 分布准确性或已完成硅后验证 |

复用偏置案例时，先保存角落/温度/电源矩阵和失配模式，再保存最佳名义值。对 [34 增益 8 采样反馈 OTA：β=1/9 决定环路速度](../cases/34-sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc.md) 这类全差分设计，fs/sf 的共模压力可能比直观上的 ss 更关键。
