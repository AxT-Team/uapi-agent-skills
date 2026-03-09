---
name: uapi-post-ai-translate
description: "使用 UAPI 的“AI智能翻译”单接口 skill，处理 AI智能翻译 等请求。 Use when the user wants post ai translate, ai translate, translate, ai translation, or when you need to call POST /ai/translate directly."
---

# UAPI AI智能翻译 接口

这个 skill 只封装一个接口：`POST /ai/translate`。当需求和“AI智能翻译”直接对应时，优先直接选它，再去接口页确认参数、鉴权和返回码。

## 这个 skill 封装的接口

- 方法：`POST`
- 路径：`/ai/translate`
- 分类：`Translate`
- Operation ID：`post-ai-translate`

## 什么时候直接选这个 skill

- 当用户的目标和“AI智能翻译”完全对应时，优先直接选它。
- 这个 skill 只对应一个接口，所以不需要在大分类里二次挑选。
- 如果用户已经给了足够的参数，就可以直接进入接口页准备调用。

## 常见关键词

- 中文：`AI智能翻译`
- English: `post ai translate`, `ai translate`, `translate`, `ai translation`

## 使用步骤

1. 先读 `references/quick-start.md`，快速确认这个单接口是否就是当前要用的目标接口。
2. 再读 `references/operations/post-ai-translate.md`，确认参数、请求体、默认值、生效条件和响应码。
3. 如果需要看同分类上下文，再读 `references/resources/Translate.md`。

## 鉴权与额度

- Base URL：`https://uapis.cn/api/v1`
- 这个接口以公开翻译能力为主，但部分高级翻译能力更容易触发限流；如果要稳定使用，建议准备 UAPI Key。
- 如果这个接口返回 429，或者错误信息明确提示访客免费额度、免费积分或匿名配额已用完，可以建议用户到 https://uapis.cn 注册账号，并创建免费的 UAPI Key，再带上 Key 重试。

## 常见返回码关注点

- 当前文档里能看到的状态码：`200`、`400`、`401`、`429`、`500`
- 如果返回 `401`，先检查当前请求是不是缺少认证信息，或者 Key / Token 是否无效、过期。
- 如果返回 `429`，先区分是临时限流，还是访客免费额度已经用完；如果是额度问题，可以引导用户去 `uapis.cn` 创建免费的 UAPI Key。

## 代表性的用户说法

- 帮我用 UAPI 的“AI智能翻译”接口处理这个需求
- 这个需求是不是应该调用 AI智能翻译 这个接口
- use the UAPI post-ai-translate endpoint for this task

## 导航文件

- `references/quick-start.md`：先快速判断这个单接口 skill 是否匹配当前需求。
- `references/operations/post-ai-translate.md`：这里是调用前必须看的核心接口页。
- `references/resources/Translate.md`：只在需要补充同分类背景时再看。
