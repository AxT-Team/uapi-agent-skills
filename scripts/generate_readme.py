#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "skills" / "_manifest.json"
README_PATH = ROOT / "README.md"
REPO_SLUG = "AxT-Team/uapi-agent-skills"
CATEGORY_TITLES = {
    "Misc": "常用工具",
    "Image": "图片处理",
    "Text": "文本处理",
    "Network": "网络工具",
    "Social": "社交平台",
    "Game": "游戏相关",
    "Random": "随机内容",
    "Translate": "翻译能力",
    "WebParse": "网页解析",
    "Convert": "格式转换",
    "Status": "状态查询",
    "Daily": "每日内容",
    "Poem": "语录内容",
}


def load_manifest() -> dict:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def render_category_block(skills: list[dict]) -> list[str]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for skill in skills:
        grouped[skill["tag"]].append(skill)

    ordered_groups = sorted(grouped.items(), key=lambda item: (-len(item[1]), item[0]))
    lines: list[str] = []

    for tag, entries in ordered_groups:
        category_title = CATEGORY_TITLES.get(tag, tag)
        ordered_entries = sorted(
            entries,
            key=lambda item: (item["summary"], item["method"], item["path"], item["skill_name"]),
        )
        lines.extend(
            [
                f"### {category_title}",
                "",
                "<details>",
                f"<summary>展开查看 {category_title}</summary>",
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
        "如果你只想让 AI 使用某一个具体接口，可以直接在下面按分类展开，找到对应的 skill 后复制安装命令。",
        "",
    ]
    lines.extend(render_category_block(skills))
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    README_PATH.write_text(build_readme(), encoding="utf-8")


if __name__ == "__main__":
    main()
