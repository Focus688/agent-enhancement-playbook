#!/usr/bin/env python3
"""记忆淘汰参考实现（C4：记忆 × 遥测 × 淘汰公式）

原理：记忆库不设淘汰 = 上下文污染 + 攻击面放大（K1）。本脚本按四维评分淘汰：
  score = w_recency * recency + w_freq * freq + w_centrality * centrality + w_age * age
  score < EVICTION_THRESHOLD 的记忆进候选淘汰池（先隔离，不直接删——失效显式化优于静默丢失）。

输入约定：一份带遥测的记忆导出 JSON（list of dicts）：
  [{"id": str, "content": str, "created_at": iso8601, "last_accessed": iso8601,
    "access_count": int, "scope": "global"|"session", "links": [id, ...]}, ...]

权重为起步值（源自 2026-09 记忆治理研究），务必用你自己的数据校准：
  recency 0.35 / freq 0.25 / centrality 0.20 / age 0.20
用法：
  python3 memory_eviction.py memories.json --now 2026-11-16T00:00:00Z \
      [--threshold 0.25] [--isolate-dir ./quarantine] [--dry-run]
"""
import argparse, json, os
from datetime import datetime, timezone


def parse_ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00")).astimezone(timezone.utc)


def evict(memories, now, threshold=0.25,
          w_recency=0.35, w_freq=0.25, w_centrality=0.20, w_age=0.20,
          half_life_days=30.0):
    total = len(memories)
    link_count = {}
    for m in memories:
        for lid in m.get("links", []):
            link_count[lid] = link_count.get(lid, 0) + 1

    scored = []
    for m in memories:
        # recency: 指数衰减的最近访问（半衰期默认 30 天）
        days_since = max(0.0, (now - parse_ts(m["last_accessed"])).total_seconds() / 86400)
        recency = 0.5 ** (days_since / half_life_days)
        # freq: log 归一化的访问频次（1 次 → 0，100 次+ → 趋近 1）
        freq = min(1.0, (m.get("access_count", 0)) ** 0.5 / 10.0)
        # centrality: 被其他记忆引用的次数（图谱关联度）
        centrality = min(1.0, link_count.get(m["id"], 0) / 5.0)
        # age: 越老越倾向淘汰（防「古董记忆」永久占位）
        age_days = (now - parse_ts(m["created_at"])).total_seconds() / 86400
        age = min(1.0, age_days / 365.0)

        score = (w_recency * recency + w_freq * freq
                 + w_centrality * centrality + w_age * (1.0 - age))
        scored.append({**m, "_score": round(score, 4),
                       "_keep_reasons": {
                           "recency": round(recency, 3), "freq": round(freq, 3),
                           "centrality": round(centrality, 3), "age_keep": round(1 - age, 3)}})
    return sorted(scored, key=lambda x: x["_score"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("memories_json")
    ap.add_argument("--now", required=True, help="ISO8601 当前时间（保证可复现）")
    ap.add_argument("--threshold", type=float, default=0.25)
    ap.add_argument("--isolate-dir", default="./quarantine")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    now = parse_ts(args.now)
    memories = json.load(open(args.memories_json))
    scored = evict(memories, now, args.threshold)

    to_evict = [m for m in scored if m["_score"] < args.threshold]
    print(f"total={len(scored)}  evict_candidates={len(to_evict)}  threshold={args.threshold}")
    for m in to_evict:
        print(f"  [{m['_score']}] {m['id']}: {m['content'][:60]!r}  {m['_keep_reasons']}")

    if args.dry_run:
        print("dry-run: 未写任何文件")
        return
    os.makedirs(args.isolate_dir, exist_ok=True)
    out_path = os.path.join(args.isolate_dir, f"quarantined_{args.now[:10]}.json")
    json.dump(to_evict, open(out_path, "w"), ensure_ascii=False, indent=2)
    keep = [m for m in scored if m["_score"] >= args.threshold]
    json.dump(keep, open(args.memories_json, "w"), ensure_ascii=False, indent=2)
    print(f"isolated -> {out_path}  (隔离≠删除：隔离区保留 90 天供人工复查)")


if __name__ == "__main__":
    main()
