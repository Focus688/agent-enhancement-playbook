# Changelog

## v1.3 — 2026-11-16（质量审计修复）

按 2026-11-16 质量评估（4 个 P0 + P1/P2）修复。Focus/Vex 审计，Pigman 维护提交。
核验层级与一手出处见 `docs/references.md`。

### P0 修复
- **P0-1 全库零链接** → 新增 `docs/references.md`：19 篇 arXiv 论文 + 5 个官方博客的可溯源链接
  （存在性/标题已核验 🟢），正文级数字标 🔵，未定位出处标 ⚪ 待维护者补充。
  `docs/repo-map.md` 98 个仓库全部加 GitHub 链接（逐个 gh api 核验存活，0 死亡）。
- **P0-2 memory_eviction.py 五缺陷** → 重写 `templates/memory_eviction.py`：
  1. 缺字段/非法时间戳不再 KeyError 崩溃（parse_ts 容错 + .get 回退）；
  2. docstring 公式与代码统一为 `w_age*(1-age_norm)`（越老越倾向淘汰）；
  3. freq 注释与代码统一为 log 归一化；
  4. 默认不覆盖输入（写 `.kept.json`），`--in-place` 才覆盖且自动 `.bak` 备份；
  5. 「隔离区保留 90 天」落地为按文件名日期自动清理（`--quarantine-retention-days`）。
  新增 `--self-test` 内置断言（缺字段/越老分低/log 频次/备份隔离/90 天清理）。
- **P0-3 包装漂移** → `llms-full.txt` 改为构建产物：新增 `scripts/build-llms-full.py`
  确定性生成（`--check` 检测漂移）；重新生成补齐 FAQ/英文摘要/SKILL.md/references；
  三入口（README/AGENTS/llms.txt）文档地图补 `skills/`、`llms-full.txt`、`references.md`。
  AGENTS.md 更新协议改为「改源文件后跑生成脚本 + --check 门」。
- **P0-4 README 30 秒版无分级** → 10 条结论逐条加证据分级（🟢/🔵/⚪），与 AGENTS.md 规则 1 对齐。

### P1/P2 修复
- **反证校准 C8** → references.md D 节引入 2607.12227（harness 进化不稳赢 test-time scaling、
  新任务泛化有限），C8 证伪条款获一手支撑。
- **Vercel 计数更正** → 旧稿「15→2」与一手来源不符，更正为「18→2」（计数 🔵 ZenML 转录），
  成功率 80%→100% 保持 🟢（原文核验）；详见 references.md C 节。
- **AGENTS.md 更新协议** → 由人工同步改为脚本生成 + --check 门，根除漂移成因。

### 核验声明（诚实边界）
- 论文存在性 + 标题 + 部分摘要级数字已核验（2026-11-16）；正文级数字为作者声明（🔵），
  未逐一回验 PDF 正文。22 篇中 16 篇预印本（未经同行评审）；7.80× 仅限 100 题子集。
- repo-map 98 仓库全部存活（gh api 逐个核验）；星数为 2026-09-03 快照，引用须标日期。
- 待维护者补充的一手出处见 references.md E 节（PROCTOR / K4 / K8 / K9 / 图谱-0.050 /
  结论7 / 结论10 / 结论9 置信门控）。

## v1.2 — 审计前基线（HEAD b737efd）
- 方法论 + 证据汇编 + N=1 生产台账，skills.sh 包装，MIT。
