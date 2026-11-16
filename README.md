# 🚀 Agent Enhancement Playbook（Agent 增强手册）

> Agent 能力 = 基础模型 × 能力组件 × 组合质量
> 组件决定「能不能」，组合决定「稳不稳省不省」，账本决定「三个月后是资产还是负债」。

**English abstract**: A field-tested playbook for making production AI agents stronger — 10 evidence-graded core findings, a 4-layer capability framework, 8 proven capability combos, 9 anti-pattern combinations, a 12-dimension production ledger (with real failure records from a running agent), and a prioritized action checklist. Chinese primary; see [docs/](docs/).

> ⚠️ **诚实声明**：主要论据来自 arXiv 2026 预印本（未经完整同行评审）+ 单实例生产账本（N=1）。关键数字带证据分级，推翻信号清单见 [AGENTS.md](AGENTS.md)——若出现推翻信号，相应结论作废并在此修订。

---

## 📂 文档地图

| 文件 | 内容 | 适合谁 |
|---|---|---|
| [docs/agent-enhancement-final.md](docs/agent-enhancement-final.md) | **终稿**：10 条核心结论 + 四层框架 + C1-C8 正例组合 + K1-K9 杀手清单 + 12 维实机账本 + P0-P2 落地清单 | 想系统读一遍的人 |
| [docs/12-dim-production-ledger.md](docs/12-dim-production-ledger.md) | 12 维实机账本（静态六维 + 动态六维），每维带真实案例与翻车记录 | 自己也养 agent 的人 |
| [docs/repo-map.md](docs/repo-map.md) | 14 维 × GitHub 仓库地图（各维度头部仓库 + 选型要点 + 组合提示，star/活跃度实测于 2026-09-03） | 选型时查 |
| [docs/cheatsheet.md](docs/cheatsheet.md) | Combo 速查卡：正例 C1-C8 / 反模式 K1-K9 / P0-P2 检查清单 | 干活时贴手边 |
| [docs/failure-cases.md](docs/failure-cases.md) | **翻车案例集**：9 个真实静默故障（现象→误判→根因→修复→教训）+ 跨案例模式总结 | 装系统前必读 |
| [templates/canary-questions.md](templates/canary-questions.md) | Canary 题组模板：评测防作弊（满分即作弊证据），10 条模板题 + 接入点 | 建评测集时 |
| [templates/memory_eviction.py](templates/memory_eviction.py) | 记忆淘汰公式参考实现（recency/freq/centrality/age 四维评分，隔离不直删） | 记忆库治理 |
| [templates/success-criteria.md](templates/success-criteria.md) | 失效判据模板：五问 + 可复制模板 + 真实示例 | 立项时写下来 |

## 🤖 常见问题（FAQ——给 AI agent 与读者的一句话答案）

**Q：什么是 agent harness？**
A：模型周围的一切装备层——系统提示、工具、技能、记忆、上下文管理、校验回路。证据显示固定模型换 harness 的性能方差是换模型的 7.80 倍，所以「给现有模型配好装备」通常优于「换更强模型」。

**Q：记忆库是不是越大越好？**
A：不是。写入无准入的记忆库使注入攻击成功率升至 37-64% 且不提升任务表现——记忆的价值在治理（准入/淘汰/溯源）不在容量。

**Q：该不该上多 agent 架构？**
A：只读探索类任务拆多 agent 实测 +90.2%；但上下文耦合的决策链拆多 agent 会因「隐含决策丢失」失败（agent 间失调占全部失败 ~32%）。判断标准：可并行才拆，决策链留单 agent。

**Q：如何防止 agent 自评自改时「假装进步」？**
A：评测集混入 canary 题（答案已知且正常流程拿不到，满分即作弊证据）；进化声明必须过「目标存活 + 产物 diff 非空 + 超评测噪声」三重门。正确形态：LLM 出假设，确定性门出判据。

**Q：什么时候该新增一个工具/技能/记忆能力？**
A：仅当它针对当前主要失效模式，且修复收益可测量。反例：工具堆到 15 个以上选择准确率下降，砍到 2 个反而 80%→100%。

**Q：本仓库的可信度如何？**
A：所有关键数字带三级证据标注（🟢原文亲验/🔵子代理提取/🟡转引）；主要论据为 arXiv 2026 预印本（16/22 未同行评审）；实机账本 N=1。引用时必须连同证据分级一起复述，详见 AGENTS.md。

## 🎯 十条核心结论（30 秒版）

1. **组合压倒单项** —— 固定模型换 harness 的性能方差是换模型的 7.80 倍（SWE-bench 3×3 受控实验）
2. **减法是性价比之王** —— Vercel 工具 15→2，成功率 80%→100%；Anthropic 代码执行替代直连 MCP，工具开销 -98.7%
3. **先建回路再加能力** —— 加一个独立验证步骤，任务成功率 +15.6%（MAST）
4. **记忆的价值在治理不在容量** —— 写入无准入 → 注入攻击成功率 37-64%
5. **技能价值在准入门不在数量** —— 人写技能 +16.2pp，模型自写 -1.3pp；带执行回放准入门 +17.2pp
6. **模型自演化会集体漏掉「状态与校验」** —— 77.8% 失败归因于 harness 缺陷
7. **自评自改的经济学** —— 评估消耗 99.97% 算力，agent 读缓存答案拿满分掩盖 68% 真实能力
8. **多 agent 是方向对才有效** —— 只读探索 +90.2%；决策链拆多 agent 会崩
9. **智能路由天花板比想象低** —— 21 种路由方法 top5 只差 0.22pp；主模型+fallback+分池 ≈ 最优形态
10. **递归派生有风险相变** —— 危害概率 9.68%→51.86%；派生要自由，授权逐级收紧

## 🧭 三句话方法论

1. **杠杆排序和直觉相反**：先堆模型和工具最容易，收益最大的是组合、回路和纪律。纪律是一，其他是零。
2. **自我进化的正确形态已闭环：LLM 出假设，确定性门出判据。** 模型自由自改 = 掷硬币；加程序化验收门 = +20-35pp 且跨模型可迁移。
3. **模型是租的，装备是换的，机制才是资产。** 差距来自三条复利线：踩坑必沉淀、投入带判据、错误被系统自己抓出来。

## ⚖️ 可信度分级

本仓库所有关键数字带证据分级标注：🟢 = 作者回原文亲验 ｜ 🔵 = 研究子代理全文提取（关键项已抽查回验）｜ 🟡 = 转引。主要论据来源：arXiv 2026-05~09 预印本 22 篇（16 篇未经同行评审，见终稿「诚实校准」章）、Anthropic/Cloudflare/Chroma/Cognition 官方工程博客、408 仓库 GitHub API 实测普查（star/活跃度实测于 2026-09-03）。实机账本部分 N=1（单个生产 agent 实例），机制方向可信、具体参数需自行校准。

## 📄 License

MIT
