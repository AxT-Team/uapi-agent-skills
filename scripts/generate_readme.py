#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "skills" / "_manifest.json"
README_PATH = ROOT / "README.md"
REPO_SLUG = "AxT-Team/uapi-agent-skills"
REPO_URL = f"https://github.com/{REPO_SLUG}"


def load_manifest() -> dict:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def collect_directories() -> list[str]:
    directories: list[str] = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_dir():
            continue
        if ".git" in path.parts or "__pycache__" in path.parts:
            continue
        directories.append(path.relative_to(ROOT).as_posix() + "/")
    return directories


def render_all_directories_block(directories: list[str]) -> list[str]:
    lines = [
        "## 全部目录",
        "",
        "<details>",
        f"<summary>展开查看仓库里的全部目录，共 {len(directories)} 个目录</summary>",
        "",
    ]

    for directory in directories:
        lines.append(f"- `{directory}`")

    lines.extend(["", "</details>", ""])
    return lines


def render_category_block(skills: list[dict]) -> list[str]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for skill in skills:
        grouped[skill["tag"]].append(skill)

    ordered_groups = sorted(grouped.items(), key=lambda item: (-len(item[1]), item[0]))
    lines = [
        "下面按分类展开全部接口。每个接口都直接附上可以复制的 Vercel Skills CLI 安装命令。",
        "",
    ]

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
                f"<summary>展开查看 {tag} 分类下的 {len(ordered_entries)} 个接口</summary>",
                "",
                "| 接口说明 | Skill | 接口 | 安装命令 |",
                "| --- | --- | --- | --- |",
            ]
        )

        for entry in ordered_entries:
            install_command = f"npx skills add {REPO_SLUG} --skill {entry['skill_name']}"
            lines.append(
                f"| {entry['summary']} | `{entry['skill_name']}` | `{entry['method']} {entry['path']}` | `{install_command}` |"
            )

        lines.extend(["", "</details>", ""])

    return lines


def build_readme() -> str:
    manifest = load_manifest()
    skills = manifest["skills"]
    directories = collect_directories()

    lines = [
        "# UAPI Agent Skills",
        "",
        f"这个仓库包含 {manifest['skill_count']} 个单接口 skill，每个 skill 只对应一个 UAPI 接口。",
        "",
        f"仓库地址：[{REPO_SLUG}]({REPO_URL})",
        "",
        "这个 README 由 `python scripts/generate_readme.py` 自动生成。",
        "",
        f"列出仓库内 skill 可以用：`npx skills add {REPO_SLUG} --list`",
        "",
        "如果访客免费额度已经用完，并且返回了对应的状态码或错误提示，相关 skill 会提醒用户去 [uapis.cn](https://uapis.cn) 注册账号，然后创建免费的 UAPI Key，再带着自己的 Key 继续调用。",
        "",
    ]
    lines.extend(render_all_directories_block(directories))
    lines.extend(render_category_block(skills))
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    README_PATH.write_text(build_readme(), encoding="utf-8")


if __name__ == "__main__":
    main()
