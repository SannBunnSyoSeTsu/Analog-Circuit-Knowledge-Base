# 50 个任务索引

编号采用冻结版 `tasks/benchmark.toml` 的 slot，不随网站排序变化。全部 50 项已阅读任务约束、参考拓扑及相关测量定义，并形成案例笔记；数值均引用发布记录。

| 编号 | 案例 | 方向 | Astra R1 定向比较 |
|---|---|---|---|
| 01 | [Class-D 半桥：导通损耗与驱动损耗必须一起算](cases/01-sky130-class-d-halfbridge-eff95-tt.md) | 电源与驱动 | 仅归档 |
| 02 | [可编程 ICC/IPTAT 镜：比例正确还不够](cases/02-sky130-programmable-icc-iptat-current-mirror-pvt.md) | 偏置与基准 | 是 |
| 03 | [局部反馈恒 gm 放大器：用反馈压低有效跨导漂移](cases/03-sky130-gmr-degen-amp-constant-gm-pvt.md) | 放大器与滤波 | 仅归档 |
| 04 | [简单退化差分对：有限 gm 是增益预算的一部分](cases/04-sky130-gmr-degenerated-diff-amp-gain2-bw70m-power1p2mw-sdr60.md) | 放大器与滤波 | 仅归档 |
| 05 | [高侧自举驱动：以源极为参考检查 VGS](cases/05-sky130-bootstrap-driver-pt.md) | 电源与驱动 | 仅归档 |
| 06 | [三级 Ring Amp：电容比、死区与动态终止共同定增益](cases/06-sky130-ring-amp-3stage-gain8-400uw.md) | 采样与数据转换 | 是 |
| 07 | [5T 误差放大器 LDO：负载电容和 ESR 是环路参数](cases/07-sky130-ldo-ota5-robust-pvt-mc.md) | 电源与驱动 | 仅归档 |
| 08 | [自举互补源跟随器：小输入电流不等于小物理电容](cases/08-sky130-buf-ppsf-bs-gain1-sfdr90.md) | 放大器与滤波 | 仅归档 |
| 09 | [宽频 CML 二分频：判定锁定需要周期级证据](cases/09-sky130-cml-divider-div2-range1gto10g.md) | 时钟与射频 | 仅归档 |
| 10 | [宽带 TIA：跨阻、输入噪声与大信号不能分开定规格](cases/10-sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt.md) | 放大器与滤波 | 是 |
| 11 | [带隙基准：温度补偿、启动和噪声是三件事](cases/11-sky130-bandgap-reference-pvt.md) | 偏置与基准 | 仅归档 |
| 12 | [β 倍增偏置：恒 gm 条件来自器件比和电阻](cases/12-sky130-beta-multiplier-reference-pvt-mc.md) | 偏置与基准 | 仅归档 |
| 13 | [恒 gm 稳增益：偏置单元必须映射到输入电流密度](cases/13-sky130-constant-gm-stable-gain-amplifier-pvt.md) | 放大器与滤波 | 是 |
| 14 | [低功耗 2 MHz 振荡器：缓冲与启动都占功率预算](cases/14-sky130-low-power-oscillator-2mhz-pvt.md) | 时钟与射频 | 仅归档 |
| 15 | [开环升压电荷泵：关断状态仍有时钟压力](cases/15-sky130-unregulated-charge-pump-10mhz-pvt.md) | 电源与驱动 | 仅归档 |
| 16 | [200 MHz 两级 Miller：快环路与宽带积分噪声的代价](cases/16-sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt.md) | 放大器与滤波 | 仅归档 |
| 17 | [0.4 V NMOS LDO：低输出电压改变输入级和驱动极性](cases/17-sky130-nmos-pass-ldo-0p4v-pvt-mc.md) | 电源与驱动 | 仅归档 |
| 18 | [受控升压泵：先确定控制变量和关断边界](cases/18-sky130-regulated-charge-pump-10mhz-pvt.md) | 电源与驱动 | 仅归档 |
| 19 | [2:1 开关电容降压：轻载效率揭示固定开关损耗](cases/19-sky130-switched-capacitor-2to1-converter-pvt.md) | 电源与驱动 | 仅归档 |
| 20 | [8:1 模拟 MUX：Ron、关断耦合与输入源阻抗相互牵制](cases/20-sky130-analog-input-mux-8to1-pvt.md) | 采样与数据转换 | 仅归档 |
| 21 | [高 PSRR 带隙：低频环路与高频滤波各有作用](cases/21-sky130-high-psrr-bandgap-reference-pvt.md) | 偏置与基准 | 仅归档 |
| 22 | [自举采样驱动：VGS 平坦要与采样失真一起看](cases/22-sky130-bootstrap-sampler-fft.md) | 采样与数据转换 | 仅归档 |
| 23 | [5 bit 电阻 DAC：分母由固定支路决定](cases/23-sky130-cmos-switched-resistor-dac-5bit-pvt.md) | 采样与数据转换 | 仅归档 |
| 24 | [限流环 VCO：调谐单调性与增益一致性需要独立约束](cases/24-sky130-current-starved-ring-vco-pvt.md) | 时钟与射频 | 仅归档 |
| 25 | [轨到轨 Class-AB 运放：输入 gm 平整和内部模态同样重要](cases/25-sky130-complementary-folded-cascode-ab-opamp-pvt.md) | 放大器与滤波 | 是 |
| 26 | [OTA-C 双二阶滤波器：状态节点的共模预算不能合并](cases/26-sky130-fully-differential-ota-c-biquad-pvt.md) | 放大器与滤波 | 仅归档 |
| 27 | [4 bit Flash ADC：前端采样与编码必须纳入转换链](cases/27-sky130-flash-adc-4bit-50msps.md) | 采样与数据转换 | 仅归档 |
| 28 | [FCT 残差放大器：保持稳定度不是目标建立误差](cases/28-sky130-fct-residue-amplifier-900msps.md) | 采样与数据转换 | 仅归档 |
| 29 | [Ahuja 补偿：补偿接入点的阻抗决定物理作用](cases/29-sky130-ahuja-compensated-two-stage-load-range-pvt.md) | 放大器与滤波 | 仅归档 |
| 30 | [Gilbert 混频器：线性指标需要幅度斜率自检](cases/30-sky130-gilbert-cell-mixer-2p4ghz-pvt-mismatch.md) | 时钟与射频 | 仅归档 |
| 31 | [底板采样：存储电压必须按两端差计算](cases/31-sky130-bottom-plate-sampler-pvt.md) | 采样与数据转换 | 仅归档 |
| 32 | [28 Gb/s CML 发射器：带宽还需眼图和群延迟约束](cases/32-sky130-cml-tx-driver-28g-nrz-pvt.md) | 时钟与射频 | 仅归档 |
| 33 | [增益 1 采样反馈 OTA：差模建立和 CMFB 要分开验收](cases/33-sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc.md) | 放大器与滤波 | 仅归档 |
| 34 | [增益 8 采样反馈 OTA：β=1/9 决定环路速度](cases/34-sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc.md) | 放大器与滤波 | 是 |
| 35 | [全差分两级 Miller：高差模增益不能替代电源抑制](cases/35-sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt.md) | 放大器与滤波 | 仅归档 |
| 36 | [套筒 OTA：堆叠余量与共模感测极点](cases/36-sky130-telescopic-cascode-ota-pvt-fix.md) | 放大器与滤波 | 仅归档 |
| 37 | [三级 Nested Miller：增益乘积与速度预算要分开](cases/37-sky130-three-stage-nested-miller-ota-pvt.md) | 放大器与滤波 | 仅归档 |
| 38 | [20 mA 无外部电容 LDO：片上储能仍可很大](cases/38-sky130-capless-ldo-1v0-20ma-pvt.md) | 电源与驱动 | 是 |
| 39 | [低功耗线路驱动：Class-AB 的价值是峰值/静态电流比](cases/39-sky130-low-power-line-driver-pvt.md) | 放大器与滤波 | 仅归档 |
| 40 | [一阶 ΔΣ：先划清 DUT 与外部模拟核心](cases/40-sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40.md) | 采样与数据转换 | 仅归档 |
| 41 | [高 PSRR 中速 Miller：偏置供电路径决定抑制能力](cases/41-sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt.md) | 放大器与滤波 | 仅归档 |
| 42 | [6 bit 异步 SAR：采集窗、握手与最终寄存都影响正确性](cases/42-sky130-sar-adc-6bit-async.md) | 采样与数据转换 | 仅归档 |
| 43 | [2.4 GHz LNA：匹配、噪声与稳定性要使用同一端口定义](cases/43-sky130-inductive-lna-2p4ghz-gain12-nf2-pvt.md) | 时钟与射频 | 仅归档 |
| 44 | [5T OTA：最小拓扑也需要闭环噪声和环路定义](cases/44-sky130-ota-5t-gain40-pm60-noise50uv-pvt.md) | 放大器与滤波 | 仅归档 |
| 45 | [晶体管二分频：复位必须清除内部状态](cases/45-sky130-transistor-divide-by-2.md) | 时钟与射频 | 仅归档 |
| 46 | [3 bit Flash：阈值绝对位置与编码尾部延迟都要检查](cases/46-sky130-flash-adc-3bit-pvt.md) | 采样与数据转换 | 仅归档 |
| 47 | [PLL 电荷泵：静态匹配与短脉冲电荷是两套预算](cases/47-sky130-pll-charge-pump-pvt.md) | 偏置与基准 | 仅归档 |
| 48 | [4 bit 异步 SAR：采样率与输出延迟不能互相代替](cases/48-sky130-sar-adc-4bit-async.md) | 采样与数据转换 | 仅归档 |
| 49 | [2 GHz LC VCO：调谐范围、pushing 与启动初值分开记录](cases/49-sky130-lc-vco-2ghz-pvt.md) | 时钟与射频 | 仅归档 |
| 50 | [130 dB 高速 OTA：局部增益增强环与外环必须分层分析](cases/50-sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt.md) | 放大器与滤波 | 是 |

机器可读入口：[case-manifest.json](case-manifest.json)；bench 文件/文本分析类别：[bench-inventory.tsv](bench-inventory.tsv)。两者都由本次静态读取生成，没有调用上游脚本。
