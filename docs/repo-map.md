# 🗺️ 14 维 × GitHub 仓库地图

> 各能力维度的头部仓库 + 选型要点 + 组合提示。star/活跃度为 **2026-09-03 gh api 实测快照**（引用请注明时点）。活跃度：🟢 <60 天 ｜ 🟡 <180 天 ｜ 🔴 >180 天未更新。
> ⚠️ star 是热度代理不是质量证明：普查剔除 3 个刷星嫌疑仓库（增速异常 + README 营销口径），另有 3 个增速超官方旗舰但 watcher 比异常偏低（按热度信号对待）。

## 3.1 搜索
- [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)（175.9k 🟢）—— 网页搜索+抓取+交互的 context API，事实标准
- [browser-use/browser-use](https://github.com/browser-use/browser-use)（112.1k 🟢）—— 把网站变成 agent 可操作界面
- [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)（81.2k 🟢）/ [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)（78.1k 🟢）—— LLM 友好爬虫双雄
- [bytedance/deer-flow](https://github.com/bytedance/deer-flow)（81.3k 🟢）—— 长程 SuperAgent harness，深度搜索完整参考实现
- [ItzCrazyKns/Vane](https://github.com/ItzCrazyKns/Vane)（36.6k 🟢，原 Perplexica）—— 开源自建 Perplexity
- [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill)（6.0k 🟢）—— AI agent 统一实时搜索（低 star 高实用的品牌型 API 代表）
- ⚠️ [Alibaba-NLP/DeepResearch](https://github.com/Alibaba-NLP/DeepResearch)（19.9k 🔴188 天）—— 路线好，别当基建押注
- **组合提示**：分水岭从「搜到」转向「何时承诺」——探索失败占深度搜索任务失败的 78%，先分叉假设再证据聚合（=C5）

## 3.2 记忆
- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)（93.1k 🟢）—— 会话压缩记忆层（⚠️ star 增速已达官方旗舰量级，按热度信号对待）
- [mem0ai/mem0](https://github.com/mem0ai/mem0)（64.6k 🟢）—— drop-in 记忆 API 层，生态兼容最广
- [volcengine/OpenViking](https://github.com/volcengine/OpenViking)（35.3k 🟢）—— 自演化上下文数据库（记忆+知识+技能统一）
- [getzep/graphiti](https://github.com/getzep/graphiti)（30.5k 🟢）—— 实时时序知识图谱，时间推理专用
- [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory)（29.2k 🟢）—— 记忆+上下文引擎，可本地跑
- [topoteretes/cognee](https://github.com/topoteretes/cognee)（30.4k 🟢）/ [letta-ai/letta](https://github.com/letta-ai/letta)（24.6k 🟢）/ [MemTensor/MemOS](https://github.com/MemTensor/MemOS)（11.2k 🟢）
- **组合提示**：必须与「生命周期治理」组合，单独堆是负资产——先做 access 遥测+淘汰+last-write-wins，再考虑换存储结构（图谱表征实测输给扁平向量 -0.050 F1）

## 3.3 工具调用
- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)（93.9k 🟢）+ [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)（90.0k 🟢）—— MCP 生态目录与官方实现
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)（36.8k 🟢）—— 浏览器自动化官方级
- [ComposioHQ/composio](https://github.com/ComposioHQ/composio)（30.0k 🟢）—— 1000+ 工具集+工具检索+鉴权+沙箱，工具面治理标杆
- [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI)（28.9k 🟢）—— 把任意网站变成 CLI
- [Skyvern-AI/skyvern](https://github.com/Skyvern-AI/skyvern)（22.9k 🟢）—— 视觉+DOM 双模浏览器工作流
- [browserbase/stagehand](https://github.com/browserbase/stagehand)（24.1k 🟢）/ [e2b-dev/E2B](https://github.com/e2b-dev/E2B)（13.7k 🟢）—— 浏览器 agent SDK / 安全沙箱基建
- **组合提示**：头号 combo = 「工具→文件系统→代码 API」渐进披露（=C2）；⚠️ 工具 >10-15 个后选择准确率下降，工具面当预算管

## 3.4 Skill 调用 / 准入
- [obra/superpowers](https://github.com/obra/superpowers)（281.0k 🟢）—— skills 框架+开发方法论，事实标杆（⚠️ watcher/star 比偏低，热度信号）
- [anthropics/skills](https://github.com/anthropics/skills)（173.3k 🟢）—— 官方 SKILL.md 规范源头
- [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)（33.7k 🟢）/ [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)（53.4k 🟢）—— 生态货架
- [agentskills/agentskills](https://github.com/agentskills/agentskills)（24.9k 🟢）—— Agent Skills 开放规范（跨 Claude Code/Cursor/Hermes 通用）
- [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt)（16.7k 🟢）—— 文本空间技能优化器（把技能当可训练参数迭代）
- **组合提示**：「新增技能」必须与「校验执行门」组合（=C1）；技能多了之后 SkillOps（生命周期治理）反成瓶颈

## 3.5 提示词
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)（78.0k 🟡）—— 教程库，但重心已从 prompt 转向 context engineering
- [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)（37.7k 🟢）—— 「编程而非提示」，声明式 pipeline+自动优化（GEPA/MIPROv2）
- [microsoft/promptflow](https://github.com/microsoft/promptflow)（11.2k 🟢）/ [zou-group/textgrad](https://github.com/zou-group/textgrad)（3.7k 🟢）
- [dottxt-ai/outlines](https://github.com/dottxt-ai/outlines)（15.7k 🟢）/ [567-labs/instructor](https://github.com/567-labs/instructor)（13.8k 🟢）—— 结构化输出双子星（与校验维度结合最紧）
- **组合提示**：孤立提示词技巧已接近零收益（模型越强越不需要咒语）；但作为 harness 组件（系统提示=控制面、技能文件=按需加载提示片段）依然关键

## 3.6 知识库 / RAG
- [langgenius/dify](https://github.com/langgenius/dify)（154.3k 🟢）/ [langchain-ai/langchain](https://github.com/langchain-ai/langchain)（145.6k 🟢）—— 平台级
- [infiniflow/ragflow](https://github.com/infiniflow/ragflow)（90.0k 🟢）—— 深度文档理解 RAG 引擎
- [upstash/context7](https://github.com/upstash/context7)（61.6k 🟢）—— 实时库文档 MCP，代码知识专用
- [run-llama/llama_index](https://github.com/run-llama/llama_index)（52.0k 🟢）
- [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)（39.4k 🟢）/ [microsoft/graphrag](https://github.com/microsoft/graphrag)（35.8k 🟢）—— 图谱 RAG 代表
- [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)（35.5k 🟢）—— 无向量、推理式 RAG（文档树索引），长 PDF 黑马
- [vibrantlabsai/ragas](https://github.com/vibrantlabsai/ragas)（15.6k 🟡）—— RAG 评估事实标准（KB×校验的天然桥）
- **组合提示**：RAG 价值在「增量」不在「相关」——按边际信息增益重排优于堆候选数；检索 top-K 与风险单调耦合（K=1→7 攻击成功率 <12%→>36%）；必须带 provenance 来源标签

## 3.7 上下文
- [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)（68.7k 🟢）—— 工具输出/日志/RAG 块进模型前压缩
- [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering)（17.9k 🟢）—— 上下文工程技能库（两篇综述引用为奠基）
- [microsoft/LLMLingua](https://github.com/microsoft/LLMLingua)（6.6k 🟢）—— 20× prompt 压缩经典
- [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering)（4.0k 🟢）—— harness 工程 13 原语清单（普查中信息密度最高）
- [wquguru/harness-books](https://github.com/wquguru/harness-books)（2.9k 🟢）—— 两本 harness 设计哲学书
- **组合提示**：Chroma《Context Rot》实测 18 个模型——任务难度不变、只加长输入，性能即降且非均匀。「上下文是有限注意力预算」是一切 combo 的物理约束；compaction 先清工具结果、笔记外置、子 agent 只回 1-2K 摘要

## 3.8 模型路由 / serving
- [BerriAI/litellm](https://github.com/BerriAI/litellm)（57.9k 🟢）—— 100+ provider 网关事实标准
- [musistudio/claude-code-router](https://github.com/musistudio/claude-code-router)（37.0k 🟢）—— 本地多模型控制面
- [vllm-project/vllm](https://github.com/vllm-project/vllm)（90.8k 🟢）/ [sgl-project/sglang](https://github.com/sgl-project/sglang)（33.6k 🟢）/ [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)（126.9k 🟢）—— serving 三支柱
- [tensorzero/tensorzero](https://github.com/tensorzero/tensorzero)（11.7k 🟢）—— 网关+评估+优化一体
- ⚠️ [lm-sys/RouteLLM](https://github.com/lm-sys/RouteLLM)（5.4k 🔴754 天）—— 经典但停摆
- **组合提示**：路由增益大部分只是任务类型（21 种方法 top5 差 0.22pp，离 oracle 10-30pp）；便宜规则（置信度门控、按任务分池）≈ 昂贵路由器（=C6）

## 3.9 规划
- [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)（41.0k 🟢）—— 图状态机，耐久规划 + checkpoint
- [FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT)（70.2k 🟢）/ [FoundationAgents/OpenManus](https://github.com/FoundationAgents/OpenManus)（58.2k 🟢）—— 多角色协作 / 通用 harness 参考实现
- [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)（58.0k 🟢）/ [microsoft/agent-framework](https://github.com/microsoft/agent-framework)（13.3k 🟢）/ [openai/openai-agents-python](https://github.com/openai/openai-agents-python)（29.2k 🟢）/ [google/adk-python](https://github.com/google/adk-python)（21.4k 🟢）/ [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai)（19.7k 🟢）
- [huggingface/smolagents](https://github.com/huggingface/smolagents)（29.1k 🟢）—— 代码即动作的最小 loop
- ⚠️ [openai/swarm](https://github.com/openai/swarm) 已被 Agents SDK 取代；[princeton-nlp/tree-of-thought-llm](https://github.com/princeton-nlp/tree-of-thought-llm) 属研究代码性质
- **组合提示**：规划维度最大失败源是「任务目标本身没定清楚」（MAST 系统设计类占 44%）——任务简报写「目标+约束+完成判据」三件套，完成判据必须可机检

## 3.10 校验
- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo)（24.8k 🟢）—— prompt/agent/RAG 测试+红队，CI 集成
- [confident-ai/deepeval](https://github.com/confident-ai/deepeval)（18.1k 🟢）—— LLM 评估框架
- [guardrails-ai/guardrails](https://github.com/guardrails-ai/guardrails)（7.3k 🟢）/ [NVIDIA-NeMo/Guardrails](https://github.com/NVIDIA-NeMo/Guardrails)（7.0k 🟢）—— 输出护栏
- [BoundaryML/baml](https://github.com/BoundaryML/baml)（9.1k 🟢）—— 把校验写进类型系统
- **组合提示**：校验是全部维度中「必须组合」的维度——没有独立校验的记忆=污染源、技能=供应链、自改进=放大器（=C3）

## 3.11 灰度测试 / 评测
- [langfuse/langfuse](https://github.com/langfuse/langfuse)（34.1k 🟢）—— trace+实验+评分+A/B 一体，自托管首选
- [mlflow/mlflow](https://github.com/mlflow/mlflow)（27.8k 🟢）/ [comet-ml/opik](https://github.com/comet-ml/opik)（21.8k 🟢）
- [evidentlyai/evidently](https://github.com/evidentlyai/evidently)（7.9k 🟢）—— 漂移与质量监控
- [Helicone/helicone](https://github.com/Helicone/helicone)（6.1k 🟢）—— 网关侧观测
- [SWE-bench/SWE-bench](https://github.com/SWE-bench/SWE-bench)（5.8k 🟢）/ [UKGovernmentBEIS/inspect_ai](https://github.com/UKGovernmentBEIS/inspect_ai)（2.7k 🟢）—— 本仓库大量 harness 数字的原生基准与官方评测框架
- **组合提示**：灰度的真义 = 用最少算力获得统计意义上的放行决策（同准确率系统的人审需求可差 10pp）；评测集混 canary 防作弊（=K3 防御）

## 3.12 复盘修复
- [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)（11.3k 🟢）—— trace 分析+评估（OTel GenAI 标准）
- [AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops)（5.8k 🟢）—— 运行监控/成本
- [matt1398/claude-devtools](https://github.com/matt1398/claude-devtools)（3.9k 🟢）—— Claude Code 会话/工具调用检视器
- **组合提示**：TRACE 配方——从轨迹隐式不满信号（改写/追问/弃会，频率是满意信号 2 倍）做逆序归因 → 修复建议 CRUD 准确率 96%、端到端修复有效 82% 🔵。前置条件：全量结构化轨迹留痕，没留痕就没有自动复盘

## 3.13 高效 Loop
- [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)（86.0k 🟢）—— 事件驱动 agent loop 最大开源实现
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo)（70.3k 🟢）—— meta-harness/swarm 编排
- [cline/cline](https://github.com/cline/cline)（67.4k 🟢）—— IDE/CLI/SDK 三形态编码 loop
- [HKUDS/nanobot](https://github.com/HKUDS/nanobot)（47.7k 🟢）/ [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent)（46.8k 🟢）—— 轻量全功能个人 agent 运行时
- [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)（187.1k 🟢）—— 历史原型（现转型平台）；[agent0ai/agent-zero](https://github.com/agent0ai/agent-zero)（19.1k 🟢）/ [elizaOS/eliza](https://github.com/elizaOS/eliza)（19.2k 🟢）—— 高装机独立运行时
- [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow)（4.0k 🟢）—— loop 内级联成本/延迟/质量决策
- **组合提示**：最小可用 loop = ReAct + 显式撤销/压缩语义 + 停止规则——backtrack（撤销污染）+ summary（压缩入栈）两个显式动作是长程预算能兑现的前提（去掉平均 -6.2pp）

## 3.14 迭代改善
- [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent)（19.7k 🟢）—— 自改进 RLM agent（架构拆解见 12 维账本）
- [lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent)（14.1k 🟢）—— 从 3.3K 行种子自生长技能树
- [NousResearch/hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution)（5.2k 🟢）—— GEPA/DSPy 进化线
- [Q00/ouroboros](https://github.com/Q00/ouroboros)（5.8k 🟢）—— 「agent 自己变聪明，人只握评分命令」的 loop OS
- [facebookresearch/HyperAgents](https://github.com/facebookresearch/HyperAgents)（2.7k 🟢）/ [ShengranHu/ADAS](https://github.com/ShengranHu/ADAS)（1.6k 🔴）—— DGM/ADAS 论文官方码停更，思想仍对，押注绕开仓库本身
- **组合提示**：自我改进已知天花板——反馈集打分涨、held-out 同向率仅 53.1%；泛化测量要贵于改进本身，否则进化的是噪声（正确形态 = C8：LLM 出假设，确定性门出判据）

---

*快照声明：以上 star/活跃度数据采集于 2026-09-03（gh api 实测），仅作选型时点参考。热度过高且 watcher/star 比异常（<0.35%，对照 AutoGPT 0.83%）的仓库按「热度信号」而非「质量信号」对待。*
