# Analog Design Bench V2 工程案例学习库

已将 **50 个任务**整理为逐任务笔记，并从 reference circuit、testbench 和测量逻辑中提炼出 **8 篇专题**。另归档 Astra Max 的 50 份 R1 最终通过例，对其中 **8 例**做结构与代价对照。

**本次没有进行任何仿真验证。** 没有运行上游 verifier、公开测试脚本、容器或 PDK；没有调用外部模型。文中的性能值均来自发布记录，静态事实、工程推断和未覆盖条件分别标明。文件哈希/链接检查仅用于确认资料完整性。

## 阅读入口

- [50 个案例索引](INDEX.md)：每例包含场景、参考结构、尺寸线索、工程认识、测试边界、原始结果和 bench 链接。
- [来源、版本及授权说明](SOURCES.md)：固定仓库版本、网站快照、来源追溯与许可。
- [静态完整性检查](STATIC-REVIEW.md)：50 项覆盖、哈希、链接与未执行仿真的边界。
- [机器可读案例清单](case-manifest.json) · [bench 文件索引](bench-inventory.tsv)。

## 跨任务知识

| 专题 | 主要收获 |
|---|---|
| [偏置与 PVT](topics/01-bias-and-pvt.md) | 同 L 与同工作点的电流镜；恒电流与恒 gm；自偏置启动 |
| [放大器与 CMFB](topics/02-amplifiers-and-cmfb.md) | 信号增益不等于噪声增益；补偿接入点；差模和共模分别验收 |
| [采样与 ADC](topics/03-sampling-and-adcs.md) | 存储电压、采集窗、异步延迟、保持漂移及 FFT 定义 |
| [电源与功率](topics/04-power-and-startup.md) | 多端口供能、LDO 储能/ESR、轻载开关损耗 |
| [射频与时钟](topics/05-rf-and-clocks.md) | 复位语义、调谐/pushing、确定性 jitter、RF 端口与稳定性 |
| [证据与指标](topics/06-evidence-and-metrics.md) | 代表点不等于全 PVT；固定种子不等于良率；结果字段陷阱 |
| [PDK 与已有知识连接](topics/07-pdk-and-reuse.md) | 几何/乘数/端序规则；与现有 Ring、FCT、Miller 等笔记互链 |
| [Astra Max 对照](topics/08-astra-comparisons.md) | 8 种替代设计的机制、收益，以及面积/输入加载等未约束成本 |

## 使用这批知识的方式

先选与目标的负载、输入共模、速度、误差带和供能边界一致的案例，再阅读参考网表及正式测量定义。元件尺寸是该模型和合同下的线索，不是可直接流片的默认参数；网站通过也不补足布局寄生、随机噪声、失配或缺失工况。

所有新增内容都位于本文件夹，原知识库文件未修改。目录内 `sources/upstream` 保存上游原始材料；`sources/astra` 保存网站最终电路和结果，作为可追溯证据，不是本次运行产物。

来源：[Analog Design Bench V2](https://analog-design-bench.tokenzhang.com/task/v2)，[公开仓库固定版本](https://github.com/Arcadia-1/analog-design-bench/tree/c23f124de1e461655d2e02ce6cfae2654ccea0d3)。资料获取日：2026-09-20。上游 benchmark 内容采用 CC BY-NC 4.0，软件采用 Apache-2.0；详见 [来源说明](SOURCES.md)。
