#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "skills" / "_manifest.json"
README_PATH = ROOT / "README.md"
REPO_SLUG = "AxT-Team/uapi-agent-skills"


def load_manifest() -> dict:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def render_category_block(skills: list[dict]) -> list[str]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for skill in skills:
        grouped[skill["tag"]].append(skill)

    ordered_groups = sorted(grouped.items(), key=lambda item: (-len(item[1]), item[0]))
    lines: list[str] = []

    for tag, entries in ordered_groups:
        ordered_entries = sorted(
            entries,
            key=lambda item: (item["summary"], item["method"], item["path"], item["skill_name"]),
        )
        lines.extend(
            [
                f"### {tag}",
                "",
                "<details>",
                f"<summary>展开查看 {tag}</summary>",
                "",
            ]
        )

        for entry in ordered_entries:
            install_command = f"npx skills add {REPO_SLUG} --skill {entry['skill_name']}"
            lines.extend(
                [
                    "<details>",
                    f"<summary>{entry['summary']}</summary>",
                    "",
                    f"- Skill：`{entry['skill_name']}`",
                    f"- 接口：`{entry['method']} {entry['path']}`",
                    f"- 安装命令：`{install_command}`",
                    "",
                    "</details>",
                    "",
                ]
            )

        lines.extend(["", "</details>", ""])

    return lines


def build_readme() -> str:
    manifest = load_manifest()
    skills = manifest["skills"]

    lines = [
        "# UAPI Agent Skills",
        "",
        f"这个仓库包含 {manifest['skill_count']} 个单接口 skill，每个 skill 只对应一个 UAPI 接口。",
        "",
        "适合按接口粒度给 AI 安装和调用。下面按分类展开，点开具体接口后可以直接复制安装命令。",
        "",
    ]
    lines.extend(render_category_block(skills))
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    README_PATH.write_text(build_readme(), encoding="utf-8")


if __name__ == "__main__":
    main()
