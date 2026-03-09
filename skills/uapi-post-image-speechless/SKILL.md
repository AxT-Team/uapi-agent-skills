---
name: uapi-post-image-speechless
description: "使用 UAPI 的“生成你们怎么不说话了表情包”单接口 skill，处理 生成你们怎么不说话了表情包、表情包生成 等请求。 Use when the user wants post image speechless, image speechless, speechless, image compression, image to base64, base64 to image, or when you need to call POST /image/speechless directly."
---

# UAPI 生成你们怎么不说话了表情包 接口

这个 skill 只封装一个接口：`POST /image/speechless`。当需求和“生成你们怎么不说话了表情包”直接对应时，优先直接选它，再去接口页确认参数、鉴权和返回码。

## 这个 skill 封装的接口

- 方法：`POST`
- 路径：`/image/speechless`
- 分类：`Image`
- Operation ID：`post-image-speechless`

## 什么时候直接选这个 skill

- 当用户的目标和“生成你们怎么不说话了表情包”完全对应时，优先直接选它。
- 这个 skill 只对应一个接口，所以不需要在大分类里二次挑选。
- 如果用户已经给了足够的参数，就可以直接进入接口页准备调用。

## 常见关键词

- 中文：`生成你们怎么不说话了表情包`、`表情包生成`
- English: `post image speechless`, `image speechless`, `speechless`, `image compression`, `image to base64`, `base64 to image`, `svg to image`, `nsfw image detection`

## 使用步骤

1. 先读 `references/quick-start.md`，快速确认这个单接口是否就是当前要用的目标接口。
2. 再读 `references/operations/post-image-speechless.md`，确认参数、请求体、默认值、生效条件和响应码。
3. 如果需要看同分类上下文，再读 `references/resources/Image.md`。

## 鉴权与额度

- Base URL：`https://uapis.cn/api/v1`
- 这个接口大多面向公开使用场景，可以先直接调用；如果某次请求被要求认证，再补 UAPI Key。
- 如果这个接口返回 429，或者错误信息明确提示访客免费额度、免费积分或匿名配额已用完，可以建议用户到 https://uapis.cn 注册账号，并创建免费的 UAPI Key，再带上 Key 重试。

## 常见返回码关注点

- 当前文档里能看到的状态码：`200`、`400`、`500`

## 代表性的用户说法

- 帮我用 UAPI 的“生成你们怎么不说话了表情包”接口处理这个需求
- 这个需求是不是应该调用 生成你们怎么不说话了表情包 这个接口
- use the UAPI post-image-speechless endpoint for this task

## 导航文件

- `references/quick-start.md`：先快速判断这个单接口 skill 是否匹配当前需求。
- `references/operations/post-image-speechless.md`：这里是调用前必须看的核心接口页。
- `references/resources/Image.md`：只在需要补充同分类背景时再看。
