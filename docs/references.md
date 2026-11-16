# 参考文献与来源核验（references）

> 本文件为全库引用的可溯源清单，修复「零 URL」缺陷（P0-1）。新增/修改关键数字须在此登记一手出处。
> **核验层级（2026-11-16，Focus/Vex 外部审计）**：
> - 🟢 已核验 = arXiv API 确认论文存在 + 标题匹配，或官方博客 HTTP 200 + 标题匹配；摘要级数字已交叉核对的另行标注。
> - 🔵 正文级数字 = 作者声明，审计未逐一回验论文正文（只验存在性与摘要）。
> - ⚪ 待补 = 审计未能定位一手出处，**待维护者补充**，补充前不得标 🟢。
> 引用纪律（AGENTS.md 规则 1）：引数字必带分级；预印本标「未经同行评审」。

## A. arXiv 论文（存在性 + 标题已核验 🟢，2026-11-16）

| ID | 标题 | 用于 | 数字核验状态 | 链接 |
|---|---|---|---|---|
| 2605.23950 | Stop Comparing LLM Agents Without Disclosing the Harness | 结论1 / 结语 / ledger#1（HV/MV 方差分解） | 7.80×（正文，仅 SWE-bench 100 题子集）🔵 | https://arxiv.org/abs/2605.23950 |
| 2608.24804 | StarHarness: Evolving Harnesses with Stratified Search for Enterprise Environments | 结论2 / C8 / 结语 | +20–35pp（摘要确认）🟢；33.1%→79.4%/+46.3pp（正文）🔵 | https://arxiv.org/abs/2608.24804 |
| 2609.01437 | HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness? | 结论6 / C8 对照 | 77.8%/53.1%（正文）🔵 | https://arxiv.org/abs/2609.01437 |
| 2609.01294 | Explore Before Committing: Hypothesis-Guided Search for Deep Research Agents（HypoSearch） | C5 | +13.3pp、省 29–35% 调用（正文）🔵 | https://arxiv.org/abs/2609.01294 |
| 2602.12670 | SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks | C1 / K4 | 87 tasks、33.9%→50.5%（+16.6pp 聚合，摘要）🟢；+16.2pp/-1.3pp（正文分配置）🔵 | https://arxiv.org/abs/2602.12670 |
| 2609.02783 | EarlyEval: Cheaper Agent Evaluation via Early Outcome Prediction | C7 / ledger#7 | 13–26% steps、44.1% input tokens、89–97% accuracy（摘要确认）🟢 | https://arxiv.org/abs/2609.02783 |
| 2608.09153 | TRACE: TRajectory Attribution for Automated Context Engineering | K8 / ledger#8 / P2#9 | 96% operation、72.7% root-cause、82% end-to-end fix（摘要确认）🟢 | https://arxiv.org/abs/2608.09153 |
| 2503.13657 | Why Do Multi-Agent LLM Systems Fail?（MAST） | 结论3 / C3 / K6 / repo-map 3.9 | +15.6% verification、~32% miscoordination（正文）🔵 | https://arxiv.org/abs/2503.13657 |
| 2608.01050 | Don't Offer What Can't Be Done: Deterministic Executability Gating for LLM Skill Selection at Scale（Wix Helpmate） | C1 执行门 | 756.6K messages / 174,927 retained（摘要）；+17.2pp/12-12（正文）🔵 | https://arxiv.org/abs/2608.01050 |
| 2608.09168 | From Relevance to Execution Utility: Reward-Aware Dynamic Execution Gating for Skill-Based LLM Agents（RADEG） | C1 执行门（对照） | — | https://arxiv.org/abs/2608.09168 |
| 2609.13889 | When Malicious Instructions Persist: Persistent Memory Poisoning Attack on Harness-Based Agents（PMPA） | 结论4 / K1 | 37–64%（正文）🔵 | https://arxiv.org/abs/2609.13889 |
| 2606.00150 | Persona Attack: Incremental Memory Injection Jailbreak Attack against Large Language Models | K2 | — | https://arxiv.org/abs/2606.00150 |
| 2607.28103 | MIND: Lightweight and Effective Memory Injection Defense for LLM Agents via Intent-Aware Information Bottleneck | K1 防御 | -62% attack / -3–5% utility（正文）🔵 | https://arxiv.org/abs/2607.28103 |
| 2603.04445 | Dynamic Model Routing and Cascading for Efficient LLM Inference: A Survey | 结论9 / C6 | 0.22pp、21 methods（正文）🔵 | https://arxiv.org/abs/2603.04445 |
| 2609.11987 | Harness or Model? Isolating the Harness Effect in Agentic Coding with a Contamination-Controlled Private Suite | K4（部分） | 9.0pp/23.7pp on 61 repo/19 contest tasks、cost 1.3–1.6×（摘要）🟢；K4「61–94% rewrite」非此摘要数字 ⚪ | https://arxiv.org/abs/2609.11987 |
| 2608.27912 | ITER: Interaction-Aware Retrieval for Agentic Search | C4 检索去冗余 | redundancy negatives（摘要确认主题）🟢；-5.8pp（正文）🔵 | https://arxiv.org/abs/2608.27912 |
| 2608.08311 | Ouroboros: A Self-Developing Frontier Coding Agent with Reviewed Core Evolution | repo-map Q00/ouroboros；结论7 候选 | 99.97%/45M/0.03%（正文，待核）⚪ | https://arxiv.org/abs/2608.08311 |
| 2607.16211 | Accurate and Efficient Long-Term Memory for LLM Agents（MOSAIC 系统） | 结论4 相关（**方向相反**，见 E） | 主张结构化记忆优于扁平 ⚠️ | https://arxiv.org/abs/2607.16211 |
| 2607.12227 | Rethinking the Evaluation of Harness Evolution for Agents | C8 证伪校准（反证） | harness 进化不稳赢 test-time scaling、新任务泛化有限（摘要）🟢 | https://arxiv.org/abs/2607.12227 |

## B. 官方博客（HTTP 200 + 标题已核验 🟢，2026-11-16）

| 来源 | 标题 | 用于 | 链接 |
|---|---|---|---|
| Anthropic | How we built our multi-agent research system | 结论8（+90.2%、token×15） | https://www.anthropic.com/engineering/built-multi-agent-research-system |
| Anthropic | Code execution with MCP for efficient agents | 结论2 / C2（150K→2K、-98.7%） | https://www.anthropic.com/engineering/code-execution-with-mcp |
| Chroma | Context Rot: How Increasing Input Tokens Impacts LLM Performance | 结论5（18 模型上下文退化） | https://research.trychroma.com/context-rot |
| Cognition | Don't Build Multi-Agents | 结论3 / K6（决策链拆多 agent 会崩） | https://cognition.ai/blog/dont-build-multi-agents |
| Vercel | We removed 80% of our agent's tools | 结论2 / K5（80%→100%） | https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools |

## C. Vercel 工具计数更正（审计发现）

- 旧稿写「15→2 工具」🟢 —— **与一手来源不符，已更正**。
- 一手原文（Vercel 博客）标题为「We removed 80% of our agent's tools」，正文确认成功率 **80%→100%**、3.5× 更快、37% 更少 token（🟢 已核验）。
- 工具具体计数：ZenML LLMOps 数据库转录为 **18→2**（🔵 二手）；原文 HTML 为 JS 渲染，计数未清晰提取。
- 处理：正文改用「18→2」并标注计数为 🔵（ZenML 转录），成功率 80%→100% 保持 🟢（原文核验）。ZenML 条目：https://www.zenml.io/llmops-database/simplifying-text-to-sql-agents-by-removing-80-of-tools
- ⚠️ 18→2 = 移除 89%，与标题「80%」略有出入，可能原文基线不同；**精确计数待维护者回验原文**。

## D. 反证校准（C8）

- 2607.12227（Rethinking the Evaluation of Harness Evolution for Agents）指出 harness 进化**不能稳定赢过** test-time scaling，且新任务泛化有限。
- 据此 C8「harness 进化 +20–35pp」应保留**证伪信号**：收益依赖任务分布与基线强度，非普适；跨任务/跨模型须重测。本手册 C8 已含证伪条款，此论文为其提供一手支撑。引用 +20–35pp 时须连同此反证一起复述。

## E. 待维护者补充的一手出处 ⚪（审计未定位，补充前不得标 🟢）

| 主张 | 现状 |
|---|---|
| PROCTOR 五层护栏 / 11 种评估失败 / 68% / 100% 满分（C3、K3） | gh + arXiv 标题搜索均未定位名为 PROCTOR 的 agent 评估系统；疑为内部系统或未公开论文，**待补一手出处** |
| K4「61–94% rewrite、3% replay valid」 | 2609.11987 摘要的「61」是任务数非 rewrite 比例；具体出处待补 |
| K8「10.1%→88.2%（Opus→Gemini 重复查询）」 | 未定位一手出处，待补 |
| K9「5/5 unseen bases drop」 | 未定位一手出处，待补 |
| 结论4「图谱 vs 扁平 F1 -0.050」 | MOSAIC（2607.16211）主张相反（结构化优于扁平）；-0.050 的具体出处待补，**勿引 MOSAIC 支撑此句** |
| 结论7「99.97% compute / 45M tokens / 0.03% / 68%」 | Ouroboros（2608.08311）为候选，正文数字待核 |
| 结论10「9.68%→51.86% / 51.10%」递归推导风险 | 候选 2609.31186 / 2610.35193（递归自改进安全），精确出处待核 |
| 结论9「78.0%@45K / 73.8%@71.3K」置信门控 | 路由综述正文或另文，待核 |

## F. repo-map 仓库核验（2026-11-16）

- repo-map 共 **98 个真实仓库条目，全部存活**（gh api 逐个核验，0 死亡）；已全部加 GitHub 链接。
- 星数为 **2026-09-03 快照**，与实时值有漂移（如 headroom 68.7k→79.8k），引用须标快照日期。
- tensorzero/tensorzero 已 archived（与 repo-map「归档只读」标注一致）。
- 「meta-harness/swarm」为 ruflo 架构散文描述，**非仓库条目**（gh 404），不链接。
- 刷星嫌疑剔除 3 / 降级 3 的判定见 repo-map 原文（热度信号 ≠ 质量）。

## G. 核验局限（诚实声明）

- 本审计核验到**论文存在性 + 标题 + 部分摘要级数字**；正文级具体数字（标 🔵 者）为作者声明，未逐一回验 PDF 正文。
- 22 篇论文中 16 篇为预印本（未经同行评审），引用须保留此标注。
- 7.80× 仅限 SWE-bench 100 题子集、3 个模型，作者自声明不普适。
