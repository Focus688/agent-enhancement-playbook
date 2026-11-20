#!/usr/bin/env python3
"""记忆淘汰参考实现（C4：记忆 × 遥测 × 淘汰公式）

原理：记忆库不设淘汰 = 上下文污染 + 攻击面放大（K1）。本脚本按四维评分淘汰：
  score = w_recency*recency + w_freq*freq + w_centrality*centrality + w_age*(1 - age_norm)
  其中 age_norm = min(1, 创建至今天数/365)：越老 age_norm 越大、(1-age_norm) 越小、
  score 越低 → 越倾向淘汰（防「古董记忆」永久占位）。
  score < threshold 的记忆进候选淘汰池（先隔离，不直接删——失效显式化优于静默丢失）。

输入约定：一份带遥测的记忆导出 JSON（list of dicts）：
  [{"id": str, "content": str, "created_at": iso8601, "last_accessed": iso8601,
    "access_count": int, "scope": "global"|"session", "links": [id, ...]}, ...]
  字段缺失不再崩溃：last_accessed 缺省回退 created_at；created_at 缺省时 age 取中性 0.5；
  access_count 缺省 0；links 缺省 []；时间戳非法按缺省处理。

权重为起步值（源自 2026-09 记忆治理研究），务必用你自己的数据校准：
  recency 0.35 / freq 0.25 / centrality 0.20 / age 0.20

安全默认（可逆性优先）：
  - 默认不覆盖输入：保留项写到 <input>.kept.json，隔离项写到 isolate-dir/quarantined_<date>.json。
  - --in-place 才覆盖输入，且覆盖前自动备份 <input>.bak-<UTC时间戳>。
  - 隔离区默认保留 90 天（--quarantine-retention-days），过期文件按文件名日期自动清理（--no-prune 关闭）。
  - 写回（.kept.json / --in-place）默认剥离内部临时键 _score / _keep_reasons，不污染原始记忆 Schema；
    需要保留评分明细时加 --keep-scores。

用法：
  python3 memory_eviction.py memories.json --now 2026-11-16T00:00:00Z \
      [--threshold 0.25] [--isolate-dir ./quarantine] [--dry-run] [--in-place] [--keep-scores]
  python3 memory_eviction.py --self-test   # 内置断言自检，不依赖外部文件
"""
import argparse, json, math, os, sys, tempfile
from datetime import datetime, timezone


def parse_ts(s):
    """ISO8601 → UTC datetime；缺失/非法返回 None（不崩溃）。"""
    if not s:
        return None
    try:
        return datetime.fromisoformat(str(s).replace("Z", "+00:00")).astimezone(timezone.utc)
    except (ValueError, TypeError):
        return None


def evict(memories, now,
          w_recency=0.35, w_freq=0.25, w_centrality=0.20, w_age=0.20,
          half_life_days=30.0):
    link_count = {}
    for m in memories:
        for lid in m.get("links", []) or []:
            link_count[lid] = link_count.get(lid, 0) + 1

    scored = []
    for m in memories:
        created = parse_ts(m.get("created_at"))
        accessed = parse_ts(m.get("last_accessed")) or created
        # recency: 指数衰减的最近访问（半衰期默认 30 天）；无任何时间戳 → 0（视为从未访问）
        if accessed is None:
            recency = 0.0
        else:
            days_since = max(0.0, (now - accessed).total_seconds() / 86400)
            recency = 0.5 ** (days_since / half_life_days)
        # freq: log 归一化的访问频次（1 次≈0.15，100 次→1.0）
        freq = min(1.0, math.log1p(max(0, m.get("access_count", 0) or 0)) / math.log1p(100))
        # centrality: 被其他记忆引用的次数（图谱关联度）
        centrality = min(1.0, link_count.get(m.get("id"), 0) / 5.0)
        # age: 越老越倾向淘汰；created_at 缺失 → 中性 0.5（不惩罚未知年龄）
        if created is None:
            age_keep = 0.5
        else:
            age_days = max(0.0, (now - created).total_seconds() / 86400)
            age_keep = 1.0 - min(1.0, age_days / 365.0)

        score = (w_recency * recency + w_freq * freq
                 + w_centrality * centrality + w_age * age_keep)
        scored.append({**m, "_score": round(score, 4),
                       "_keep_reasons": {
                           "recency": round(recency, 3), "freq": round(freq, 3),
                           "centrality": round(centrality, 3), "age_keep": round(age_keep, 3)}})
    return sorted(scored, key=lambda x: x["_score"])


INTERNAL_KEYS = ("_score", "_keep_reasons")


def strip_internal(items):
    """剥离内部评分键，保证写回的 JSON 与原始记忆 Schema 一致（可重复执行）。"""
    return [{k: v for k, v in m.items() if k not in INTERNAL_KEYS} for m in items]


def prune_quarantine(isolate_dir, now, retention_days):
    """按文件名日期清理超过保留期的隔离文件（兑现「保留 90 天」承诺）。"""
    removed = []
    if not os.path.isdir(isolate_dir):
        return removed
    for fn in sorted(os.listdir(isolate_dir)):
        if not (fn.startswith("quarantined_") and fn.endswith(".json")):
            continue
        date_str = fn[len("quarantined_"):-len(".json")]
        d = parse_ts(date_str + "T00:00:00Z")
        if d is None:
            continue
        if (now - d).total_seconds() / 86400 > retention_days:
            os.remove(os.path.join(isolate_dir, fn))
            removed.append(fn)
    return removed


def main_argv(argv):
    """供 self_test 调用 main 的入口（临时替换 sys.argv）。"""
    old = sys.argv
    sys.argv = ["memory_eviction.py"] + argv
    try:
        return main()
    finally:
        sys.argv = old


def main():
    ap = argparse.ArgumentParser(description="记忆淘汰参考实现（四维评分 + 隔离不直删）")
    ap.add_argument("memories_json", nargs="?", help="记忆导出 JSON")
    ap.add_argument("--now", help="ISO8601 当前时间（保证可复现）")
    ap.add_argument("--threshold", type=float, default=0.25)
    ap.add_argument("--isolate-dir", default="./quarantine")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--in-place", action="store_true", help="覆盖输入（自动先备份 .bak）")
    ap.add_argument("--quarantine-retention-days", type=float, default=90.0)
    ap.add_argument("--no-prune", action="store_true", help="不清理过期隔离文件")
    ap.add_argument("--keep-scores", action="store_true",
                    help="写回时保留 _score/_keep_reasons（默认剥离，避免污染原始 Schema）")
    ap.add_argument("--self-test", action="store_true", help="运行内置断言自检")
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    if not args.memories_json or not args.now:
        ap.error("需要 memories_json 与 --now（或用 --self-test）")
    now = parse_ts(args.now)
    if now is None:
        ap.error(f"--now 非法 ISO8601: {args.now}")
    with open(args.memories_json, encoding="utf-8") as f:
        memories = json.load(f)
    scored = evict(memories, now)
    to_evict = [m for m in scored if m["_score"] < args.threshold]
    keep = [m for m in scored if m["_score"] >= args.threshold]
    print(f"total={len(scored)}  evict_candidates={len(to_evict)}  threshold={args.threshold}")
    for m in to_evict:
        print(f"  [{m['_score']}] {m.get('id')}: {str(m.get('content',''))[:60]!r}  {m['_keep_reasons']}")

    if args.dry_run:
        print("dry-run: 未写任何文件")
        return 0

    os.makedirs(args.isolate_dir, exist_ok=True)
    # 用解析后的 UTC 日期，而不是对 --now 原字符串切片：
    # 传入 +08:00 等偏移时，字符串切片会得到错误日期，与 prune_quarantine 的 UTC 语义不一致。
    out_path = os.path.join(args.isolate_dir, f"quarantined_{now.strftime('%Y-%m-%d')}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(to_evict, f, ensure_ascii=False, indent=2)

    if args.in_place:
        bak = f"{args.memories_json}.bak-{now.strftime('%Y%m%dT%H%M%SZ')}"
        with open(args.memories_json, encoding="utf-8") as f:
            original = f.read()
        with open(bak, "w", encoding="utf-8") as f:
            f.write(original)
        out_items = keep if args.keep_scores else strip_internal(keep)
        with open(args.memories_json, "w", encoding="utf-8") as f:
            json.dump(out_items, f, ensure_ascii=False, indent=2)
        print(f"in-place 覆盖输入（备份 -> {bak}）")
    else:
        kept_path = f"{args.memories_json}.kept.json"
        out_items = keep if args.keep_scores else strip_internal(keep)
        with open(kept_path, "w", encoding="utf-8") as f:
            json.dump(out_items, f, ensure_ascii=False, indent=2)
        print(f"kept -> {kept_path}（输入未改动；如需覆盖加 --in-place）")

    pruned = [] if args.no_prune else prune_quarantine(args.isolate_dir, now, args.quarantine_retention_days)
    print(f"isolated -> {out_path}  (隔离≠删除：保留 {args.quarantine_retention_days:.0f} 天供人工复查)")
    if pruned:
        print(f"pruned 过期隔离文件 {len(pruned)}: {pruned}")
    return 0


def self_test():
    """内置断言：缺字段不崩溃 / 越老分越低 / log 频次 / 备份与隔离落地 / 90 天清理。"""
    now = parse_ts("2026-11-16T00:00:00Z")
    ok = 0

    def check(cond, msg):
        nonlocal ok
        assert cond, "FAIL: " + msg
        ok += 1
        print("  PASS:", msg)

    # 1. 缺字段 / 非法时间戳不崩溃
    mem = [{"id": "a", "content": "no timestamps"},
           {"id": "b", "content": "bad ts", "created_at": "not-a-date", "last_accessed": None},
           {"id": "c", "content": "full", "created_at": "2026-11-01T00:00:00Z",
            "last_accessed": "2026-11-15T00:00:00Z", "access_count": 50, "links": ["a"]}]
    scored = evict(mem, now)
    check(len(scored) == 3, "缺字段/非法时间戳不崩溃，3 条全部评分")
    check(all("_score" in m for m in scored), "每条都有 _score")

    # 2. 越老（创建久 + 久未访问）分越低
    old = {"id": "old", "content": "antique", "created_at": "2020-01-01T00:00:00Z",
           "last_accessed": "2020-01-01T00:00:00Z", "access_count": 0}
    new = {"id": "new", "content": "fresh", "created_at": "2026-11-10T00:00:00Z",
           "last_accessed": "2026-11-15T00:00:00Z", "access_count": 100}
    s = {m["id"]: m["_score"] for m in evict([old, new], now)}
    check(s["old"] < s["new"], f"古董记忆分({s['old']}) < 新鲜记忆分({s['new']})")

    # 3. freq 用 log（100 次→1.0）
    f100 = evict([{**new, "access_count": 100}], now)[0]["_keep_reasons"]["freq"]
    check(abs(f100 - 1.0) < 1e-6, "freq log 归一化 100 次→1.0")

    # 4. 文件落地：默认不覆盖输入 + 隔离写入 + 90 天清理 + --in-place 备份
    with tempfile.TemporaryDirectory() as td:
        inp = os.path.join(td, "mem.json")
        with open(inp, "w", encoding="utf-8") as f:
            json.dump([old, new], f)
        iso = os.path.join(td, "quarantine")
        os.makedirs(iso)
        with open(os.path.join(iso, "quarantined_2026-01-01.json"), "w") as f:
            f.write("[]")  # 预置过期隔离文件（距 now >90 天）
        rc = main_argv([inp, "--now", "2026-11-16T00:00:00Z", "--isolate-dir", iso])
        check(rc == 0, "默认运行 exit 0")
        check(os.path.exists(inp + ".kept.json"), "默认写出 .kept.json")
        with open(inp, encoding="utf-8") as f:
            check(len(json.load(f)) == 2, "默认不覆盖输入（仍 2 条）")
        check(os.path.exists(os.path.join(iso, "quarantined_2026-11-16.json")), "隔离文件写入")
        check(not os.path.exists(os.path.join(iso, "quarantined_2026-01-01.json")),
              "过期隔离文件被清理（90 天承诺生效）")
        rc = main_argv([inp, "--now", "2026-11-16T00:00:00Z", "--isolate-dir", iso, "--in-place"])
        baks = [x for x in os.listdir(td) if ".bak-" in x]
        check(rc == 0 and len(baks) == 1, "--in-place 覆盖前生成 1 个 .bak 备份")
        with open(inp, encoding="utf-8") as f:
            check(len(json.load(f)) == 1, "--in-place 后输入只剩保留项")

    # 5. 非 UTC 时区：隔离文件名必须取 UTC 日期（+08:00 凌晨 2 点 = 前一日 18:00Z）
    with tempfile.TemporaryDirectory() as td:
        inp = os.path.join(td, "mem.json")
        with open(inp, "w", encoding="utf-8") as f:
            json.dump([old, new], f)
        iso = os.path.join(td, "q")
        rc = main_argv([inp, "--now", "2026-11-16T02:00:00+08:00", "--isolate-dir", iso])
        check(rc == 0 and os.path.exists(os.path.join(iso, "quarantined_2026-11-15.json")),
              "+08:00 时区 -> 隔离文件按 UTC 日期命名 (2026-11-15)")
        check(not os.path.exists(os.path.join(iso, "quarantined_2026-11-16.json")),
              "不按本地字符串切片生成错误日期")

    # 6. 写回剥离内部键；--keep-scores 可显式保留
    with tempfile.TemporaryDirectory() as td:
        inp = os.path.join(td, "mem.json")
        with open(inp, "w", encoding="utf-8") as f:
            json.dump([old, new], f)
        iso = os.path.join(td, "q")
        main_argv([inp, "--now", "2026-11-16T00:00:00Z", "--isolate-dir", iso, "--in-place"])
        with open(inp, encoding="utf-8") as f:
            saved = json.load(f)
        check(all("_score" not in m and "_keep_reasons" not in m for m in saved),
              "--in-place 写回剥离 _score/_keep_reasons（原始 Schema 不被污染）")
        inp2 = os.path.join(td, "mem2.json")
        with open(inp2, "w", encoding="utf-8") as f:
            json.dump([old, new], f)
        main_argv([inp2, "--now", "2026-11-16T00:00:00Z", "--isolate-dir", iso, "--keep-scores"])
        with open(inp2 + ".kept.json", encoding="utf-8") as f:
            kept = json.load(f)
        check(all("_score" in m for m in kept), "--keep-scores 保留评分明细（显式选择）")
    print(f"SELF-TEST PASS ({ok} assertions)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
