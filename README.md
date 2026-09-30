# Analog Circuit Knowledge Base

模拟电路基础知识、Analog Design Bench V2 案例学习与 SMIC18 实测复现资料。

**Credit / 致谢：基础知识库来自 [Arcadia-1/Analog-Circuit-Knowledge-Base](https://github.com/Arcadia-1/Analog-Circuit-Knowledge-Base)，上游现名 [Arcadia-1/circuits-and-systems-classroom](https://github.com/Arcadia-1/circuits-and-systems-classroom)。本仓库保留本机使用的 `3dab708` 版本及其 Git 历史，感谢 Arcadia-1 / Token Zhang 的原始工作。**

案例与复现基于 **[Arcadia-1/analog-design-bench](https://github.com/Arcadia-1/analog-design-bench)**，固定版本 `c23f124de1e461655d2e02ce6cfae2654ccea0d3`。来源、版权及各部分的许可见 [NOTICE](NOTICE.md)。

| 内容 | 入口 | 范围 |
|---|---|---|
| 模拟电路基础 | 下方原知识库目录 | 放大器、噪声、采样、动态放大与补偿 |
| Benchmark 学习笔记 | [50 个案例与 8 个专题](Analog-Design-Bench-V2-Lessons/INDEX.md) | 原题、参考电路和测量定义的静态阅读 |
| SMIC18 实测复现 | [复现索引](SMIC18-Benchmark-Reproduction/README.md) | 50 项 TT/nominal 原理图级复现 |
| Markdown / PDF 报告 | [全部 50 份报告](SMIC18-Benchmark-Reproduction/MARKDOWN-REPORTS.md) | 可编辑表格、独立图表、完整电路图，28 份 Mermaid 框图 |
| 复现工程 | [配套 GitHub 仓库](https://github.com/SannBunnSyoSeTsu/smic18-benchmark-reproduction) | 仿真与测量脚本、运行输入、合同与冻结来源 |

Markdown 已于 2026-09-30 完成可读性修订：去除整页 PDF 重复插图、坐标文字堆叠与重复网表，保留原测量表格。详见 [修订记录](SMIC18-Benchmark-Reproduction/documentation/MARKDOWN-REVISION.md)。

## 原知识库说明

A knowledge repository for analog circuit design fundamentals, focusing on amplifier theory, signal processing techniques, noise reduction, and ADC architectures.

## Contents

### Basic Amplifier Topologies

#### `Single-Transistor-Amplifier-Configurations.md`
Reference guide for the three fundamental MOSFET amplifier topologies (Common Source, Common Gate, Common Drain). Includes voltage gain, input/output impedance analysis, and typical applications for each configuration.

#### `5T-Differential-Amplifier-Analysis.md`
Complete mathematical analysis of 5-transistor differential amplifiers including differential/common-mode gains, CMRR, PSRR, noise analysis (thermal and flicker), frequency response (poles, zeros, transfer function), and pole-zero doublet settling time analysis.

#### `Miller-Compensated-Two-Stage-Amplifier.md`
Classical two-stage operational amplifier with Miller compensation. Comprehensive reference covering DC gain equations, dominant/non-dominant poles, RHP zero analysis, GBW calculations, phase margin design, slew rate, settling time, noise analysis, CMRR/PSRR, and complete design procedure with sizing equations.

### Dynamic and Advanced Amplifiers

#### `Ring-Amplifier.md`
Ring amplifier (Ringamp) topology using dynamically stabilized inverter stages. Covers working principle, dead-zone design, bandwidth/power equations, dead-zone degeneration (DZD), multi-stage configurations, and state-of-the-art pipelined ADC applications.

#### `Floating-Inverter-Amplifier.md`
Floating Inverter Amplifier (FIA/FIDA) with floating supply reservoir. Includes gain formulas, common-mode stability, reservoir capacitor sizing, cross-coupled body biasing (CCBB) for enhanced gain, and applications in DTDSM and SAR ADCs.

#### `Floating-Charge-Transfer-Amplifier.md`
Floating Charge Transfer (FCT) amplifier with complementary common-gate topology and cross-coupled capacitor biasing (C³B). Covers charge conservation equations, PVT-robust gain, filter-embedded Pipe-SAR ADC architecture achieving 172 dB Schreier FoM.

### Noise Reduction Techniques

#### `kTC-Noise-Cancellation.md`
Thermal noise cancellation achieving up to 70% noise power reduction using auxiliary capacitors. Includes basic cancellation, presampling techniques (>5× sampling rate improvement), design equations, capacitor sizing, and applications in high-resolution SAR ADCs and ΔΣ modulators.

#### `Correlated-Double-Sampling.md`
Correlated Double Sampling (CDS) for removing offset, reset noise, and 1/f noise. Covers frequency response, noise shaping, reset noise cancellation, switched-capacitor implementation, Correlated Multiple Sampling (CMS), and comparison with other techniques.

#### `Correlated-Level-Shifting.md`
Correlated Level Shifting (CLS) for gain enhancement achieving effective gain A² from opamp with gain A. Enables >60 dB performance from 30 dB opamps. Includes sequential CLS (SCLS), noise analysis, pipelined SAR ADC applications, and look-ahead CLS techniques.

### Sampling and Data Conversion

#### `Current-Integration-Sampling.md`
Current integration sampling for converting current signals to voltage. Covers fundamental equations, integrating ADC architectures (dual-slope, incremental ΔΣ, multi-slope), photodiode integrators, noise analysis (kT/C, shot noise), jitter performance comparison with voltage sampling, and design equations.

### Analysis and Calculations

#### `Amplifier-Bandwidth-Calculations.md`
Comprehensive guide to amplifier bandwidth theory including gain-bandwidth product (GBW) fundamentals, closed-loop bandwidth calculations, gain-bandwidth tradeoffs, and multi-stage bandwidth analysis with visual comparisons.

#### `Phase-Noise-Calculations.md`
Bidirectional conversion formulas between phase noise and amplitude noise, including definitions, step-by-step derivations, direct formulas, and worked examples for high-speed applications.

#### `Comparator-Noise-Calculation.md`
Statistical analysis of comparator noise using Gaussian distribution theory. Covers probability density/cumulative distribution functions, noise sigma extraction formulas (inverse CDF method), visualization of noise impact on decision probability, and figures of merit (FoM₁, FoM₂) for comparator performance evaluation.

#### `Capacitance-AC-Simulation.md`
Practical method for extracting capacitance values from AC simulation results using current-frequency relationships. Includes derivation from I = jωCV, formulas for imaginary current component analysis, and ready-to-use Virtuoso Calculator expressions for automated capacitance extraction.

### Source Degeneration Analysis

#### `Degenerated-Resistor-Noise.md`
Complete noise analysis comparing non-degenerated vs source-degenerated resistor configurations. Covers transistor and resistor noise contributions, output current/voltage noise PSD derivations, frequency-dependent behavior, noise ratio calculations, and numerical examples showing noise contribution breakdown for different γ and gₘRₛ values.

#### `Degenerated-Resistor-Current-Noise.md`
Focused current noise analysis for source-degenerated circuits. Derives output current noise PSD for both cases, includes sanity checks for limiting cases (Rₛ→0 and gₘRₛ≫1), and provides simplified noise ratio formulas for design calculations.

#### `Degenerated-Resistor-Charging-Time.md`
Charging time comparison between RC charging and constant-current source degeneration. Includes time-to-Vdd/2 derivations, equivalence conditions for matched speed, design tables mapping gₘ/Rₛ/Rₗ values, effective transconductance calculations, and output resistance boosting analysis.

## Directories

### `code/`
Python scripts for generating figures and visualizations.

### `figures/`
Generated plots and images referenced in the documentation.

### `reference/`
Local reference materials including LaTeX source documents and papers.
