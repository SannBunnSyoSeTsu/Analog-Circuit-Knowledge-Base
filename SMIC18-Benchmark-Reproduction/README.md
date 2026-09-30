# SMIC18 Benchmark 复现知识库

**来源：[Arcadia-1/analog-design-bench](https://github.com/Arcadia-1/analog-design-bench)。** [配套复现工程](https://github.com/SannBunnSyoSeTsu/smic18-benchmark-reproduction) · [Markdown 可读性修订](documentation/MARKDOWN-REVISION.md)

[全部50项Markdown与系统框图](MARKDOWN-REPORTS.md)

目标为全部50项，在SMIC18MMRF nominal条件下完成模拟gm/ID设计、HD数字单元实现、指标验证及每模块可审查PDF。当前已完成电气验证和PDF交付 **50/50**，剩余 **0项**；不能把Sky130历史通过计入本统计。

工作工程：[smic18_benchmark_repro](https://github.com/SannBunnSyoSeTsu/smic18-benchmark-reproduction/blob/6ae3e1434914297c4ed12b93cb8d6a297ef8339a/README.md)。允许10%–15%性能下降的换算规则见 [验收规则](https://github.com/SannBunnSyoSeTsu/smic18-benchmark-reproduction/blob/6ae3e1434914297c4ed12b93cb8d6a297ef8339a/contracts/acceptance-policy.md)。原始工艺学习资料在 [Analog Design Bench V2](../Analog-Design-Bench-V2-Lessons/README.md)，不做覆盖。

现有 **50份报告含完整电路图，共212页图纸**；模拟部分绘制晶体管及工艺无源，数字部分使用原厂标准单元符号。各份报告及总图见下表。2026-09-23的历史26项补图记录保存在原目录（本地归档，未随仓库分发），该历史批次没有新增仿真或修改电气结果。

2026-09-26新增第11项一阶带隙基准：TT范围内14项原门槛全部通过，11页PDF含3页完整电路图。20项测量交叉核对及27实例/94端子核对通过；本次对话授权完成知识库更新。随后按用户继续工作指令推进剩余模块。

2026-09-26续作完成第21项高PSRR带隙：5项TT原门槛通过，低频/1MHz抑制70.625/35.392dB，126点温漂40.308ppm/°C；11页PDF含3页完整图纸。

2026-09-26续作完成第09项CML二分频：1/2/5/10GHz全部原门槛通过，10GHz最小逐周期摆幅210.371mVpp，静态功耗1.455351mW；10页PDF含2页完整图纸，17项独立数值复核通过。

2026-09-26续作新增第15项未稳压电荷泵：保留TT/40°C、10MHz、开启50uA负载及独立关闭电流测试；完整结果、数值收敛对照和图纸见分项报告。

2026-09-26续作完成第01项Class-D半桥：TT双温度14负载点，完整供电与时钟功率积分、六点数值复核；15页PDF含6页完整图纸。

2026-09-26续作完成第33项增益1采样反馈OTA：14项nominal检查在10%边界内，仅开环3dB摆幅需要放宽；12页PDF含4页完整图纸，PVT/20次失配明确未执行。

2026-09-26续作完成第34项增益8采样反馈OTA：双向建立约6.1ns，14项nominal检查在10%边界内；补偿迭代、12页PDF及完整四页电路图保留，PVT/失配明确未执行。

2026-09-26续作完成第39项低功耗线驱动：保留300Ω交流耦合线路和200pF负载，10项标称原门槛通过；数值对照、独立验收和完整晶体管图见分项报告，其他44个PVT点未执行。

2026-09-26续作完成第32项28Gb/s CML发送器：原始PRBS7及低摆幅激励全部保留，37项独立测量通过，带宽20.027GHz与低摆幅输出228.107mV需10%放宽；完整眼图、抖动、数值对照与晶体管图见分项报告，其他两个配对PVT点未执行。

2026-09-26续作完成第43项2.4GHz LNA：全部标称原门槛通过，原生工艺电感/MIM/电阻保持；201点通带/噪声及1601点宽频稳定性、独立测量与完整图纸随报告归档，其他26个PVT点未执行。

| 编号 | 原任务 | 状态 | 本地知识/PDF |
|---|---|---|---|
| 01 | sky130-class-d-halfbridge-eff95-tt | complete_10pct | [知识笔记](cases/01-class-d.md) · [PDF](evidence/01-class-d/review.pdf) · [MD](evidence/01-class-d/review_report.md) · [系统框图](evidence/01-class-d/review_report.md#系统框图) · [电路总图](evidence/01-class-d/schematic/full.svg) |
| 02 | sky130-programmable-icc-iptat-current-mirror-pvt | complete_original | [知识笔记](cases/02-mirror.md) · [PDF](evidence/02-mirror/review.pdf) · [MD](evidence/02-mirror/review_report.md) · [系统框图](evidence/02-mirror/review_report.md#系统框图) · [电路总图](evidence/02-mirror/schematic/full.svg) |
| 03 | sky130-gmr-degen-amp-constant-gm-pvt | complete_original | [知识笔记](cases/03-selfbiased-gmr.md) · [PDF](evidence/03-selfbiased-gmr/review.pdf) · [MD](evidence/03-selfbiased-gmr/review_report.md) · [电路总图](evidence/03-selfbiased-gmr/schematic/full.svg) |
| 04 | sky130-gmr-degenerated-diff-amp-gain2-bw70m-power1p2mw-sdr60 | complete_original | [知识笔记](cases/04-gmr.md) · [PDF](evidence/04-gmr/review.pdf) · [MD](evidence/04-gmr/review_report.md) · [电路总图](evidence/04-gmr/schematic/full.svg) |
| 05 | sky130-bootstrap-driver-pt | complete_10pct | [知识笔记](cases/05-bootstrap-driver.md) · [PDF](evidence/05-bootstrap-driver/review.pdf) · [MD](evidence/05-bootstrap-driver/review_report.md) · [系统框图](evidence/05-bootstrap-driver/review_report.md#系统框图) · [电路总图](evidence/05-bootstrap-driver/schematic/full.svg) |
| 06 | sky130-ring-amp-3stage-gain8-400uw | complete_original | [知识笔记](cases/06-ring-amplifier.md) · [PDF](evidence/06-ring-amplifier/review.pdf) · [MD](evidence/06-ring-amplifier/review_report.md) · [系统框图](evidence/06-ring-amplifier/review_report.md#系统框图) · [电路总图](evidence/06-ring-amplifier/schematic/full.svg) |
| 07 | sky130-ldo-ota5-robust-pvt-mc | complete_15pct | [知识笔记](cases/07-ldo-ota5.md) · [PDF](evidence/07-ldo-ota5/review.pdf) · [MD](evidence/07-ldo-ota5/review_report.md) · [系统框图](evidence/07-ldo-ota5/review_report.md#系统框图) · [电路总图](evidence/07-ldo-ota5/schematic/full.svg) |
| 08 | sky130-buf-ppsf-bs-gain1-sfdr90 | complete_original | [知识笔记](cases/08-ppsf.md) · [PDF](evidence/08-ppsf/review.pdf) · [MD](evidence/08-ppsf/review_report.md) · [电路总图](evidence/08-ppsf/schematic/full.svg) |
| 09 | sky130-cml-divider-div2-range1gto10g | complete_original | [知识笔记](cases/09-cml-divider.md) · [PDF](evidence/09-cml-divider/review.pdf) · [MD](evidence/09-cml-divider/review_report.md) · [系统框图](evidence/09-cml-divider/review_report.md#系统框图) · [电路总图](evidence/09-cml-divider/schematic/full.svg) |
| 10 | sky130-tia-zt8k-bw750m-noise5p-sfdr70-power5m-pt | complete_15pct | [知识笔记](cases/10-tia.md) · [PDF](evidence/10-tia/review.pdf) · [MD](evidence/10-tia/review_report.md) · [电路总图](evidence/10-tia/schematic/full.svg) |
| 11 | sky130-bandgap-reference-pvt | complete_original | [知识笔记](cases/11-bandgap.md) · [PDF](evidence/11-bandgap/review.pdf) · [MD](evidence/11-bandgap/review_report.md) · [电路总图](evidence/11-bandgap/schematic/full.svg) |
| 12 | sky130-beta-multiplier-reference-pvt-mc | complete_original | [知识笔记](cases/12-beta.md) · [PDF](evidence/12-beta/review.pdf) · [MD](evidence/12-beta/review_report.md) · [电路总图](evidence/12-beta/schematic/full.svg) |
| 13 | sky130-constant-gm-stable-gain-amplifier-pvt | complete_original | [知识笔记](cases/13-constant-gm.md) · [PDF](evidence/13-constant-gm/review.pdf) · [MD](evidence/13-constant-gm/review_report.md) · [电路总图](evidence/13-constant-gm/schematic/full.svg) |
| 14 | sky130-low-power-oscillator-2mhz-pvt | complete_original | [知识笔记](cases/14-oscillator.md) · [PDF](evidence/14-oscillator/review.pdf) · [MD](evidence/14-oscillator/review_report.md) · [电路总图](evidence/14-oscillator/schematic/full.svg) |
| 15 | sky130-unregulated-charge-pump-10mhz-pvt | complete_10pct | [知识笔记](cases/15-unregulated-pump.md) · [PDF](evidence/15-unregulated-pump/review.pdf) · [MD](evidence/15-unregulated-pump/review_report.md) · [系统框图](evidence/15-unregulated-pump/review_report.md#系统框图) · [电路总图](evidence/15-unregulated-pump/schematic/full.svg) |
| 16 | sky130-two-stage-miller-opamp-gain60-ugb200-pm60-noise50uv-pvt | complete_10pct | [知识笔记](cases/16-miller.md) · [PDF](evidence/16-miller/review.pdf) · [MD](evidence/16-miller/review_report.md) · [电路总图](evidence/16-miller/schematic/full.svg) |
| 17 | sky130-nmos-pass-ldo-0p4v-pvt-mc | complete_original | [知识笔记](cases/17-nmos-ldo.md) · [PDF](evidence/17-nmos-ldo/review.pdf) · [MD](evidence/17-nmos-ldo/review_report.md) · [系统框图](evidence/17-nmos-ldo/review_report.md#系统框图) · [电路总图](evidence/17-nmos-ldo/schematic/full.svg) |
| 18 | sky130-regulated-charge-pump-10mhz-pvt | complete_10pct | [知识笔记](cases/18-regulated-pump.md) · [PDF](evidence/18-regulated-pump/review.pdf) · [MD](evidence/18-regulated-pump/review_report.md) · [系统框图](evidence/18-regulated-pump/review_report.md#系统框图) · [电路总图](evidence/18-regulated-pump/schematic/full.svg) |
| 19 | sky130-switched-capacitor-2to1-converter-pvt | complete_original | [知识笔记](cases/19-sc-converter.md) · [PDF](evidence/19-sc-converter/review.pdf) · [MD](evidence/19-sc-converter/review_report.md) · [系统框图](evidence/19-sc-converter/review_report.md#系统框图) · [电路总图](evidence/19-sc-converter/schematic/full.svg) |
| 20 | sky130-analog-input-mux-8to1-pvt | complete_original | [知识笔记](cases/20-mux.md) · [PDF](evidence/20-mux/review.pdf) · [MD](evidence/20-mux/review_report.md) · [系统框图](evidence/20-mux/review_report.md#系统框图) · [电路总图](evidence/20-mux/schematic/full.svg) |
| 21 | sky130-high-psrr-bandgap-reference-pvt | complete_original | [知识笔记](cases/21-highpsrr-bandgap.md) · [PDF](evidence/21-highpsrr-bandgap/review.pdf) · [MD](evidence/21-highpsrr-bandgap/review_report.md) · [电路总图](evidence/21-highpsrr-bandgap/schematic/full.svg) |
| 22 | sky130-bootstrap-sampler-fft | complete_original | [知识笔记](cases/22-bootstrap.md) · [PDF](evidence/22-bootstrap/review.pdf) · [MD](evidence/22-bootstrap/review_report.md) · [系统框图](evidence/22-bootstrap/review_report.md#系统框图) · [电路总图](evidence/22-bootstrap/schematic/full.svg) |
| 23 | sky130-cmos-switched-resistor-dac-5bit-pvt | complete_original | [知识笔记](cases/23-resistor-dac.md) · [PDF](evidence/23-resistor-dac/review.pdf) · [MD](evidence/23-resistor-dac/review_report.md) · [系统框图](evidence/23-resistor-dac/review_report.md#系统框图) · [电路总图](evidence/23-resistor-dac/schematic/full.svg) |
| 24 | sky130-current-starved-ring-vco-pvt | complete_original | [知识笔记](cases/24-ring-vco.md) · [PDF](evidence/24-ring-vco/review.pdf) · [MD](evidence/24-ring-vco/review_report.md) · [电路总图](evidence/24-ring-vco/schematic/full.svg) |
| 25 | sky130-complementary-folded-cascode-ab-opamp-pvt | complete_original | [知识笔记](cases/25-complementary-ab.md) · [PDF](evidence/25-complementary-ab/review.pdf) · [MD](evidence/25-complementary-ab/review_report.md) · [电路总图](evidence/25-complementary-ab/schematic/full.svg) |
| 26 | sky130-fully-differential-ota-c-biquad-pvt | complete_original | [知识笔记](cases/26-ota-c-biquad.md) · [PDF](evidence/26-ota-c-biquad/review.pdf) · [MD](evidence/26-ota-c-biquad/review_report.md) · [系统框图](evidence/26-ota-c-biquad/review_report.md#系统框图) · [电路总图](evidence/26-ota-c-biquad/schematic/full.svg) |
| 27 | sky130-flash-adc-4bit-50msps | complete_original | [知识笔记](cases/27-flash-adc4bit.md) · [PDF](evidence/27-flash-adc4bit/review.pdf) · [MD](evidence/27-flash-adc4bit/review_report.md) · [系统框图](evidence/27-flash-adc4bit/review_report.md#系统框图) · [电路总图](evidence/27-flash-adc4bit/schematic/full.svg) |
| 28 | sky130-fct-residue-amplifier-900msps | complete_15pct | [知识笔记](cases/28-fct-amplifier.md) · [PDF](evidence/28-fct-amplifier/review.pdf) · [MD](evidence/28-fct-amplifier/review_report.md) · [系统框图](evidence/28-fct-amplifier/review_report.md#系统框图) · [电路总图](evidence/28-fct-amplifier/schematic/full.svg) |
| 29 | sky130-ahuja-compensated-two-stage-load-range-pvt | complete_original | [知识笔记](cases/29-ahuja.md) · [PDF](evidence/29-ahuja/review.pdf) · [MD](evidence/29-ahuja/review_report.md) · [电路总图](evidence/29-ahuja/schematic/full.svg) |
| 30 | sky130-gilbert-cell-mixer-2p4ghz-pvt-mismatch | complete_original | [知识笔记](cases/30-gilbert-mixer.md) · [PDF](evidence/30-gilbert-mixer/review.pdf) · [MD](evidence/30-gilbert-mixer/review_report.md) · [电路总图](evidence/30-gilbert-mixer/schematic/full.svg) |
| 31 | sky130-bottom-plate-sampler-pvt | complete_original | [知识笔记](cases/31-bottom-plate.md) · [PDF](evidence/31-bottom-plate/review.pdf) · [MD](evidence/31-bottom-plate/review_report.md) · [系统框图](evidence/31-bottom-plate/review_report.md#系统框图) · [电路总图](evidence/31-bottom-plate/schematic/full.svg) |
| 32 | sky130-cml-tx-driver-28g-nrz-pvt | complete_10pct | [知识笔记](cases/32-cml-tx.md) · [PDF](evidence/32-cml-tx/review.pdf) · [MD](evidence/32-cml-tx/review_report.md) · [系统框图](evidence/32-cml-tx/review_report.md#系统框图) · [电路总图](evidence/32-cml-tx/schematic/full.svg) |
| 33 | sky130-fd-sampling-feedback-ota-gain1-settling40ns-noise300uv-pvt-mc | complete_10pct | [知识笔记](cases/33-sampling-ota-gain1.md) · [PDF](evidence/33-sampling-ota-gain1/review.pdf) · [MD](evidence/33-sampling-ota-gain1/review_report.md) · [系统框图](evidence/33-sampling-ota-gain1/review_report.md#系统框图) · [电路总图](evidence/33-sampling-ota-gain1/schematic/full.svg) |
| 34 | sky130-fd-sampling-feedback-ota-gain8-settling10ns-noise1mv-pvt-mc | complete_10pct | [知识笔记](cases/34-sampling-ota-gain8.md) · [PDF](evidence/34-sampling-ota-gain8/review.pdf) · [MD](evidence/34-sampling-ota-gain8/review_report.md) · [系统框图](evidence/34-sampling-ota-gain8/review_report.md#系统框图) · [电路总图](evidence/34-sampling-ota-gain8/schematic/full.svg) |
| 35 | sky130-fd-two-stage-miller-opamp-gain60-pm60-noise50uv-pvt | complete_original | [知识笔记](cases/35-fd-miller.md) · [PDF](evidence/35-fd-miller/review.pdf) · [MD](evidence/35-fd-miller/review_report.md) · [电路总图](evidence/35-fd-miller/schematic/full.svg) |
| 36 | sky130-telescopic-cascode-ota-pvt-fix | complete_original | [知识笔记](cases/36-telescopic.md) · [PDF](evidence/36-telescopic/review.pdf) · [MD](evidence/36-telescopic/review_report.md) · [电路总图](evidence/36-telescopic/schematic/full.svg) |
| 37 | sky130-three-stage-nested-miller-ota-pvt | complete_original | [知识笔记](cases/37-nested-miller.md) · [PDF](evidence/37-nested-miller/review.pdf) · [MD](evidence/37-nested-miller/review_report.md) · [电路总图](evidence/37-nested-miller/schematic/full.svg) |
| 38 | sky130-capless-ldo-1v0-20ma-pvt | complete_original | [知识笔记](cases/38-capless-ldo.md) · [PDF](evidence/38-capless-ldo/review.pdf) · [MD](evidence/38-capless-ldo/review_report.md) · [系统框图](evidence/38-capless-ldo/review_report.md#系统框图) · [电路总图](evidence/38-capless-ldo/schematic/full.svg) |
| 39 | sky130-low-power-line-driver-pvt | complete_original | [知识笔记](cases/39-line-driver.md) · [PDF](evidence/39-line-driver/review.pdf) · [MD](evidence/39-line-driver/review_report.md) · [系统框图](evidence/39-line-driver/review_report.md#系统框图) · [电路总图](evidence/39-line-driver/schematic/full.svg) |
| 40 | sky130-delta-sigma-adc-1bit-first-order-osr32-sndr40 | complete_original | [知识笔记](cases/40-delta-sigma.md) · [PDF](evidence/40-delta-sigma/review.pdf) · [MD](evidence/40-delta-sigma/review_report.md) · [系统框图](evidence/40-delta-sigma/review_report.md#系统框图) · [电路总图](evidence/40-delta-sigma/schematic/full.svg) |
| 41 | sky130-two-stage-miller-opamp-gain70-ugb20-pm60-noise50uv-pvt | complete_original | [知识笔记](cases/41-lowpower-miller.md) · [PDF](evidence/41-lowpower-miller/review.pdf) · [MD](evidence/41-lowpower-miller/review_report.md) · [电路总图](evidence/41-lowpower-miller/schematic/full.svg) |
| 42 | sky130-sar-adc-6bit-async | complete_original | [知识笔记](cases/42-sar-adc6bit.md) · [PDF](evidence/42-sar-adc6bit/review.pdf) · [MD](evidence/42-sar-adc6bit/review_report.md) · [系统框图](evidence/42-sar-adc6bit/review_report.md#系统框图) · [电路总图](evidence/42-sar-adc6bit/schematic/full.svg) |
| 43 | sky130-inductive-lna-2p4ghz-gain12-nf2-pvt | complete_original | [知识笔记](cases/43-inductive-lna.md) · [PDF](evidence/43-inductive-lna/review.pdf) · [MD](evidence/43-inductive-lna/review_report.md) · [电路总图](evidence/43-inductive-lna/schematic/full.svg) |
| 44 | sky130-ota-5t-gain40-pm60-noise50uv-pvt | complete_original | [知识笔记](cases/44-ota5.md) · [PDF](evidence/44-ota5/review.pdf) · [MD](evidence/44-ota5/review_report.md) · [电路总图](evidence/44-ota5/schematic/full.svg) |
| 45 | sky130-transistor-divide-by-2 | complete_original | [知识笔记](cases/45-divider.md) · [PDF](evidence/45-divider/review.pdf) · [MD](evidence/45-divider/review_report.md) · [系统框图](evidence/45-divider/review_report.md#系统框图) · [电路总图](evidence/45-divider/schematic/full.svg) |
| 46 | sky130-flash-adc-3bit-pvt | complete_original | [知识笔记](cases/46-flash-adc3bit.md) · [PDF](evidence/46-flash-adc3bit/review.pdf) · [MD](evidence/46-flash-adc3bit/review_report.md) · [系统框图](evidence/46-flash-adc3bit/review_report.md#系统框图) · [电路总图](evidence/46-flash-adc3bit/schematic/full.svg) |
| 47 | sky130-pll-charge-pump-pvt | complete_original | [知识笔记](cases/47-charge-pump.md) · [PDF](evidence/47-charge-pump/review.pdf) · [MD](evidence/47-charge-pump/review_report.md) · [系统框图](evidence/47-charge-pump/review_report.md#系统框图) · [电路总图](evidence/47-charge-pump/schematic/full.svg) |
| 48 | sky130-sar-adc-4bit-async | complete_original | [知识笔记](cases/48-sar-adc4bit.md) · [PDF](evidence/48-sar-adc4bit/review.pdf) · [MD](evidence/48-sar-adc4bit/review_report.md) · [系统框图](evidence/48-sar-adc4bit/review_report.md#系统框图) · [电路总图](evidence/48-sar-adc4bit/schematic/full.svg) |
| 49 | sky130-lc-vco-2ghz-pvt | complete_15pct | [知识笔记](cases/49-lc-vco.md) · [PDF](evidence/49-lc-vco/review.pdf) · [MD](evidence/49-lc-vco/review_report.md) · [电路总图](evidence/49-lc-vco/schematic/full.svg) |
| 50 | sky130-folded-cascode-ota-gain130-pm60-noise50uv-pvt | complete_original | [知识笔记](cases/50-gainboosted-folded.md) · [PDF](evidence/50-gainboosted-folded/review.pdf) · [MD](evidence/50-gainboosted-folded/review_report.md) · [电路总图](evidence/50-gainboosted-folded/schematic/full.svg) |

本目录仅新增用户授权的SMIC18复现记录；其他知识库文件保持不变。所有结果为原理图级本地仿真，不等同于PVT或版图签核。
