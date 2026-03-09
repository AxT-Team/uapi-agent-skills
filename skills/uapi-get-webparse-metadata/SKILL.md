---
name: uapi-get-webparse-metadata
description: "使用 UAPI 的“提取网页元数据”单接口 skill，处理 提取网页元数据、网页转Markdown、网页元数据、提取网页图片、网页解析 等请求。 Use when the user wants get webparse metadata, webparse metadata, metadata, extract metadata, or when you need to call GET /webparse/metadata directly."
---

# UAPI 提取网页元数据 接口

这个 skill 只封装一个接口：`GET /webparse/metadata`。当需求和“提取网页元数据”直接对应时，优先直接选它，再去接口页确认参数、鉴权和返回码。

## 这个 skill 封装的接口

- 方法：`GET`
- 路径：`/webparse/metadata`
- 分类：`WebParse`
- Operation ID：`get-webparse-metadata`

## 什么时候直接选这个 skill

- 当用户的目标和“提取网页元数据”完全对应时，优先直接选它。
- 这个 skill 只对应一个接口，所以不需要在大分类里二次挑选。
- 如果用户已经给了足够的参数，就可以直接进入接口页准备调用。

## 常见关键词

- 中文：`提取网页元数据`、`网页转Markdown`、`网页元数据`、`提取网页图片`、`网页解析`
- English: `get webparse metadata`, `webparse metadata`, `metadata`, `extract metadata`

## 使用步骤

1. 先读 `references/quick-start.md`，快速确认这个单接口是否就是当前要用的目标接口。
2. 再读 `references/operations/get-webparse-metadata.md`，确认参数、请求体、默认值、生效条件和响应码。
3. 如果需要看同分类上下文，再读 `references/resources/WebParse.md`。

## 鉴权与额度

- Base URL：`https://uapis.cn/api/v1`
- 这个接口大多可以直接调用，但网页转换任务更容易遇到排队或限流；必要时请补 UAPI Key。
- 如果这个接口返回 429，或者错误信息明确提示访客免费额度、免费积分或匿名配额已用完，可以建议用户到 https://uapis.cn 注册账号，并创建免费的 UAPI Key，再带上 Key 重试。

## 常见返回码关注点

- 当前文档里能看到的状态码：`200`、`400`、`500`

## 代表性的用户说法

- 帮我用 UAPI 的“提取网页元数据”接口处理这个需求
- 这个需求是不是应该调用 提取网页元数据 这个接口
- use the UAPI get-webparse-metadata endpoint for this task

## 导航文件

- `references/quick-start.md`：先快速判断这个单接口 skill 是否匹配当前需求。
- `references/operations/get-webparse-metadata.md`：这里是调用前必须看的核心接口页。
- `references/resources/WebParse.md`：只在需要补充同分类背景时再看。
