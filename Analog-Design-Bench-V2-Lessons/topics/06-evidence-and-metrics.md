# 证据与指标：发布通过究竟证明了什么

## 本知识集的四层证据

| 层 | 本次内容 | 可信边界 |
|---|---|---|
| 静态事实 | instruction、端口、连接、元件值、verifier 公式 | 文本事实；不等于真实工作区或稳定性 |
| 上游发布测量 | reference.json 与网站 Astra result.json | 上游报告结果；本次没有重跑 |
| 工程推断 | 简化模型、权衡、迁移建议 | 写明假设，不能当测量数值 |
| 未覆盖 | 寄生、版图、随机噪声、缺失角落等 | 不补造数据，不从 pass 外推 |

50 个 reference 的 circuit、instruction、task.toml SHA-256 都与发布 provenance 一致，说明笔记所对应的这些文件确实是被该发布记录标识的版本。对正式 verifier 另保存文件哈希；本次没有重建容器，也没有独立复核其 image digest。哈希相符只证明来源一致，不验证模拟器正确性或测量有效性。

## 指标名称不能替代公式

| 容易混淆的词 | 应记录的区别 | 案例 |
|---|---|---|
| 建立时间 | 第一次越入 / last-entry / 末段均值 | [33 增益 1 采样反馈 OTA：差模建立和 CMFB 要分开验收](../cases/33-sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc.md)、[50 130 dB 高速 OTA：局部增益增强环与外环必须分层分析](../cases/50-sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt.md) |
| 百分比误差 | 目标增益偏差 / 保持期变化 | [06 三级 Ring Amp：电容比、死区与动态终止共同定增益](../cases/06-sky130-ring-amp-3stage-gain8-400uw.md)、[28 FCT 残差放大器：保持稳定度不是目标建立误差](../cases/28-sky130-fct-residue-amplifier-900msps.md) |
| 相位裕度 | 哪个跨频、是否允许再穿越、哪个环路 | [29 Ahuja 补偿：补偿接入点的阻抗决定物理作用](../cases/29-sky130-ahuja-compensated-two-stage-load-range-pvt.md)、[35 全差分两级 Miller：高差模增益不能替代电源抑制](../cases/35-sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt.md)、[50 130 dB 高速 OTA：局部增益增强环与外环必须分层分析](../cases/50-sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt.md) |
| 50 µVrms | 输入或输出折算、积分上下限是否随带宽变化 | [16 200 MHz 两级 Miller：快环路与宽带积分噪声的代价](../cases/16-sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt.md)、[34 增益 8 采样反馈 OTA：β=1/9 决定环路速度](../cases/34-sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc.md)、[41 高 PSRR 中速 Miller：偏置供电路径决定抑制能力](../cases/41-sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt.md)、[44 5T OTA：最小拓扑也需要闭环噪声和环路定义](../cases/44-sky130-ota-5t-gain40-pm60-noise50uv-pvt.md) |
| SDR/SFDR/SNDR | 拟合残差、最大杂散、带内总噪声失真 | [03 局部反馈恒 gm 放大器：用反馈压低有效跨导漂移](../cases/03-sky130-gmr-degen-amp-constant-gm-pvt.md)、[22 自举采样驱动：VGS 平坦要与采样失真一起看](../cases/22-sky130-bootstrap-sampler-fft.md)、[40 一阶 ΔΣ：先划清 DUT 与外部模拟核心](../cases/40-sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40.md) |
| ENOB | 原始 SNDR 换算 / 量程归一化、N 与刺激幅度 | [42 6 bit 异步 SAR：采集窗、握手与最终寄存都影响正确性](../cases/42-sky130-sar-adc-6bit-async.md)、[48 4 bit 异步 SAR：采样率与输出延迟不能互相代替](../cases/48-sky130-sar-adc-4bit-async.md) |
| 功耗 | 哪些端口、供电符号、稳态窗口、回灌处理 | [18 受控升压泵：先确定控制变量和关断边界](../cases/18-sky130-regulated-charge-pump-10mhz-pvt.md)、[19 2:1 开关电容降压：轻载效率揭示固定开关损耗](../cases/19-sky130-switched-capacitor-2to1-converter-pvt.md)、[32 28 Gb/s CML 发射器：带宽还需眼图和群延迟约束](../cases/32-sky130-cml-tx-driver-28g-nrz-pvt.md) |
| PVT 通过 | 完整乘积 / 声明代表点 / 某项只测子集 | [25 轨到轨 Class-AB 运放：输入 gm 平整和内部模态同样重要](../cases/25-sky130-complementary-folded-cascode-ab-opamp-pvt.md)、[29 Ahuja 补偿：补偿接入点的阻抗决定物理作用](../cases/29-sky130-ahuja-compensated-two-stage-load-range-pvt.md)、[32 28 Gb/s CML 发射器：带宽还需眼图和群延迟约束](../cases/32-sky130-cml-tx-driver-28g-nrz-pvt.md) |

例如 [50 130 dB 高速 OTA：局部增益增强环与外环必须分层分析](../cases/50-sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt.md) 要求首个下降跨频后不再越过 0 dB；只读第一次 PM 会漏掉后续不稳定风险。[46 3 bit Flash：阈值绝对位置与编码尾部延迟都要检查](../cases/46-sky130-flash-adc-3bit-pvt.md) 的输出延迟取编码链最终稳定，不能替换成比较器首次再生时间。

## 两个结果数据的读取陷阱

1. Reference 的扁平 `metrics` 有时只给一个极值并丢掉范围，个别单位还不可靠。[06 三级 Ring Amp：电容比、死区与动态终止共同定增益](../cases/06-sky130-ring-amp-3stage-gain8-400uw.md) 的 `static_error` 应按 verifier 和 checks 中的相对误差定义读，不把 V 标签当真实电压。案例页因此优先保存原 `checks.message`。
2. Astra 的网站 `result.tests_passed/tests_total` 可同时为零，但顶层 `pass=true`、`binary_pass=1`、完整 gates 为 passed。这是网站数据结构，不能读成“0 项检查证明通过”，也不能据此断言没有验收。快照保留所有原字段；报告以明确的 pass 和 gates 为依据。

## 固定测试的价值及边界

全码中心加输入诱饵能检查 ADC 是否真正在指定窗采样；绝对阈值加 INL/DNL 能避免拟合消除偏移；两个输入幅度的 IIP3 斜率检查能防止错误外推；启动、偏置电流与输出响应联合能排除休眠假解。这些都值得复用为测试设计知识。

但声明矩阵之外仍没有结论。[32 28 Gb/s CML 发射器：带宽还需眼图和群延迟约束](../cases/32-sky130-cml-tx-driver-28g-nrz-pvt.md) 只有三个配对 PVT 点；[25 轨到轨 Class-AB 运放：输入 gm 平整和内部模态同样重要](../cases/25-sky130-complementary-folded-cascode-ab-opamp-pvt.md) 的 25 点是每角落五个 V/T 组合；[29 Ahuja 补偿：补偿接入点的阻抗决定物理作用](../cases/29-sky130-ahuja-compensated-two-stage-load-range-pvt.md) 的中间负载只有子矩阵。固定三、八、二十、三十或五十个种子是可复查的回归覆盖，不是 3σ 量产良率证明。理想 R/C 不随 PDK 无源角落漂移；理想 R 在 noise 分析中通常仍有热噪声，不能笼统称为“理想元件无噪声”。

本次只做文件完整性、链接与来源一致性检查；所有缺失条件保持缺失，没有启动任何补充模拟。
