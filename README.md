# UAPI Agent Skills

This repository contains 86 installable UAPI skills in a single repo.

Each skill wraps one UAPI endpoint, so AI agents can choose a narrow skill, read a focused `SKILL.md`, and call the matching interface directly.

## Repository Layout

```text
skills/
  uapi-get-misc-weather/
  uapi-post-search-aggregate/
  uapi-post-ai-translate/
  ...
```

Every skill folder includes:

- `SKILL.md`
- `agents/openai.yaml`
- `references/quick-start.md`
- generated operation and resource references

## What Is Included

- 86 single-endpoint skills generated from the current UAPI OpenAPI spec
- keyword-oriented skill descriptions for easier AI selection
- per-interface usage notes, response code notes, and auth hints
- visitor quota guidance that points users to [uapis.cn](https://uapis.cn) for a free UAPI Key when `429` is caused by free quota exhaustion

## Suggested Usage

Use the skill whose folder name matches the target operation, for example:

- `uapi-get-misc-weather`
- `uapi-post-search-aggregate`
- `uapi-post-ai-translate`

You can also inspect [skills/_manifest.json](./skills/_manifest.json) to see the full generated list.

## Notes

- Most public endpoint skills can be used directly.
- Some skills mention third-party credentials, such as Steam Web API keys.
- Admin-only endpoints such as rate limit and usage stats require admin Bearer credentials rather than a normal public UAPI Key.

## Related Links

- UAPI docs: [uapis.cn/docs](https://uapis.cn/docs)
- UAPI site: [uapis.cn](https://uapis.cn)
