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


def render_skill_directory_block(skill_names: list[str]) -> list[str]:
    lines = [
        "## Skill 目录索引",
        "",
        "<details>",
        f"<summary>展开查看全部 {len(skill_names)} 个顶层 skill 目录</summary>",
        "",
    ]

    for name in skill_names:
        lines.append(f"- `skills/{name}`")

    lines.extend(["", "</details>", ""])
    return lines


def render_install_block() -> list[str]:
    return [
        "## 用 Vercel Skills CLI 安装",
        "",
        "这个仓库最适合按需安装单个接口 skill。先列出仓库里的 skill，再装你真正需要的那几个就可以。",
        "",
        "### 先看这个仓库里有哪些 skill",
        "",
        "```bash",
        f"npx skills add {REPO_SLUG} --list",
        "```",
        "",
        "### 通过仓库名安装单个 skill",
        "",
        "```bash",
        f"npx skills add {REPO_SLUG} --skill uapi-get-misc-weather",
        "```",
        "",
        "### 直接安装某个 skill 目录",
        "",
        "```bash",
        f"npx skills add {REPO_URL}/tree/main/skills/uapi-get-misc-weather",
        "```",
        "",
        "### 一次安装多个 skill",
        "",
        "```bash",
        f"npx skills add {REPO_SLUG} --skill uapi-get-misc-weather --skill uapi-post-search-aggregate --skill uapi-post-ai-translate",
        "```",
        "",
        "### 把这个仓库里的全部 skill 装到指定 agent",
        "",
        "```bash",
        f"npx skills add {REPO_SLUG} --skill '*' -a codex",
        "```",
        "",
        "### 把这个仓库里的全部 skill 装到所有 agent",
        "",
        "```bash",
        f"npx skills add {REPO_SLUG} --all",
        "```",
        "",
        "### 非交互安装示例",
        "",
        "```bash",
        f"npx skills add {REPO_SLUG} --skill uapi-get-misc-weather -a codex -y",
        "```",
        "",
    ]


def render_quota_block() -> list[str]:
    return [
        "## 免费额度用完怎么办",
        "",
        "如果访客免费额度已经用完，并且返回了对应的状态码或错误提示，相关 skill 会提醒用户去 [uapis.cn](https://uapis.cn) 注册一个账号，然后创建免费的 UAPI Key，再带着自己的 Key 继续调用。",
        "",
    ]


def render_category_overview(skills: list[dict]) -> list[str]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for skill in skills:
        grouped[skill["tag"]].append(skill)

    ordered = sorted(grouped.items(), key=lambda item: (-len(item[1]), item[0]))
    lines = [
        "## 分类速览",
        "",
        f"当前一共分成 {len(ordered)} 个分类。下面这一段先给出分类数量，后面再按分类展开全部接口。",
        "",
    ]

    for tag, entries in ordered:
        lines.append(f"- `{tag}`：{len(entries)} 个接口")

    lines.append("")
    return lines


def render_category_tables(skills: list[dict]) -> list[str]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for skill in skills:
        grouped[skill["tag"]].append(skill)

    ordered = sorted(grouped.items(), key=lambda item: (-len(item[1]), item[0]))
    lines = [
        "## 分类与接口",
        "",
        "下面每个分类都用 `<details>` 展开。安装时直接把“安装名”带进 `--skill` 后面就可以。",
        "",
    ]

    for tag, entries in ordered:
        sorted_entries = sorted(
            entries,
            key=lambda item: (item["summary"], item["method"], item["path"], item["skill_name"]),
        )
        lines.extend(
            [
                f"### {tag}",
                "",
                "<details>",
                f"<summary>展开查看 {tag} 分类下的 {len(sorted_entries)} 个接口</summary>",
                "",
                "| 安装名 | 接口说明 | Method | Path | Operation ID |",
                "| --- | --- | --- | --- | --- |",
            ]
        )

        for entry in sorted_entries:
            lines.append(
                f"| `{entry['skill_name']}` | {entry['summary']} | `{entry['method']}` | `{entry['path']}` | `{entry['operation_id']}` |"
            )

        lines.extend(["", "</details>", ""])

    return lines


def render_regen_block() -> list[str]:
    return [
        "## 重新生成 README",
        "",
        "这个 README 是脚本生成的。如果 `skills/_manifest.json` 有变动，可以直接运行下面这条命令重新生成：",
        "",
        "```bash",
        "python scripts/generate_readme.py",
        "```",
        "",
    ]


def build_readme() -> str:
    manifest = load_manifest()
    skills = manifest["skills"]
    skill_names = sorted(item["skill_name"] for item in skills)
    directories = collect_directories()

    lines = [
        "# UAPI Agent Skills",
        "",
        f"这个仓库包含 {manifest['skill_count']} 个单接口 skill，每个 skill 只对应一个 UAPI 接口。",
        "",
        "这种结构更适合让 AI 按接口粒度直接选、直接读、直接调用，也更方便按功能拆分安装。",
        "",
        f"仓库地址：[{REPO_SLUG}]({REPO_URL})",
        "",
    ]
    lines.extend(render_all_directories_block(directories))
    lines.extend(render_skill_directory_block(skill_names))
    lines.extend(render_install_block())
    lines.extend(render_quota_block())
    lines.extend(render_category_overview(skills))
    lines.extend(render_category_tables(skills))
    lines.extend(render_regen_block())
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    README_PATH.write_text(build_readme(), encoding="utf-8")


if __name__ == "__main__":
    main()
