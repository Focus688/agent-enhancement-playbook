# Changelog

## v1.3.1 — 2026-11-20（矩阵审计修复）

按 2026-11 矩阵改造工单修复证据分级与模板工程问题。未改动任何已跑数或历史实验数据。

### P0 修复
- **证据分级违规**：按 `docs/references.md` E 节与 AGENTS.md 规则 1（未能定位一手出处不得标 🟢），
  将 4 处降级为 ⚪（保留原警示文字）：结论 4「图谱 vs 扁平 -0.050」、结论 10「9.68%→51.86%」、
  K4「61-94% rewrite / 3% replay」、C6/结论 9「78.0%@45K 置信门控」。
- **图例自洽**：README / 终稿 / 速查卡 / SKILL.md 的证据分级图例统一补 ⚪ = 一手出处待补。

### P1 修复
- **`templates/memory_eviction.py` 加固**：
  1. 隔离文件名改用解析后的 UTC 日期（`now.strftime('%Y-%m-%d')`），修复非 UTC 时区下字符串切片错位；
  2. `evict()` 删除未使用的 `threshold` 参数（淘汰判定只在 main 中做）；
  3. 写回（`.kept.json` / `--in-place`）默认剥离 `_score` / `_keep_reasons`，新增 `--keep-scores` 显式保留；
     `--self-test` 增加 +08:00 时区与 Schema 无污染断言（15 assertions）。
- **CI 硬门**：新增 `.github/workflows/ci.yml` —— `build-llms-full.py --check` 零漂移 + `memory_eviction.py --self-test`。
- **README**：徽章、Quick Start、四层框架 Mermaid 图、安全边界交叉链接（→ agent-security-skills）、
  Focus688 Open Source Matrix；K1/K2 在终稿与速查卡中补安全侧链接。

### 核验声明（诚实边界）
- 本次只改标注与工程实现，**未新增任何实验数据**，也未改动 `docs/` 中已核验的论文数字。
- ⚪ 四处的原始表述保留在正文中，降级只表示「一手出处未定位」，不表示结论被推翻。

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
