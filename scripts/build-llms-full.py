#!/usr/bin/env python3
"""确定性生成 llms-full.txt（修复 P0-3 包装漂移）。

llms-full.txt 是构建产物，不是手工维护文件。本脚本按固定顺序拼接源文件，
无时间戳/无随机量 → 重复运行字节一致。AGENTS.md 更新协议改为：改任何源文件后
运行 `python3 scripts/build-llms-full.py` 重新生成；CI/自查用 --check 检测漂移。

用法：
  python3 scripts/build-llms-full.py          # 重新生成 llms-full.txt
  python3 scripts/build-llms-full.py --check   # 只检测漂移，漂移则 exit 1（不写）
"""
import argparse, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 固定顺序：入口 → agent 规则 → 正文 → 技能 → 模板 → 索引 → 变更
SOURCES = [
    "README.md",
    "AGENTS.md",
    "docs/agent-enhancement-final.md",
    "docs/12-dim-production-ledger.md",
    "docs/repo-map.md",
    "docs/cheatsheet.md",
    "docs/failure-cases.md",
    "docs/references.md",
    "skills/agent-enhancement-cheatsheet/SKILL.md",
    "templates/canary-questions.md",
    "templates/success-criteria.md",
    "templates/memory_eviction.py",
    "llms.txt",
    "CHANGELOG.md",
]

HEADER = (
    "# agent-enhancement-playbook — 全文聚合（llms-full.txt）\n"
    "# 本文件由 scripts/build-llms-full.py 确定性生成，请勿手工编辑。\n"
    "# 改任何源文件后运行: python3 scripts/build-llms-full.py\n"
    "# 检测漂移: python3 scripts/build-llms-full.py --check\n"
)


def build():
    parts = [HEADER]
    for rel in SOURCES:
        p = ROOT / rel
        if not p.exists():
            raise SystemExit(f"缺少源文件: {rel}")
        text = p.read_text(encoding="utf-8").rstrip("\n")
        if rel.endswith(".py"):
            text = "```python\n" + text + "\n```"
        parts.append(f"\n\n<!-- ===== SOURCE: {rel} ===== -->\n\n{text}")
    return "\n".join(parts) + "\n"


def main():
    ap = argparse.ArgumentParser(description="确定性生成 llms-full.txt")
    ap.add_argument("--check", action="store_true", help="只检测漂移，不写文件")
    args = ap.parse_args()
    content = build()
    target = ROOT / "llms-full.txt"
    if args.check:
        old = target.read_text(encoding="utf-8") if target.exists() else ""
        if old != content:
            print("DRIFT: llms-full.txt 与源文件不一致，请运行 build-llms-full.py 重新生成")
            return 1
        print("OK: llms-full.txt 与源文件一致")
        return 0
    target.write_text(content, encoding="utf-8")
    print(f"生成 llms-full.txt（{len(content)} 字符，{len(SOURCES)} 个源文件）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
