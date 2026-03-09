---
name: uapi-get-status-ratelimit
description: "使用 UAPI 的“限流状态”单接口 skill，处理 限流状态、并发状态 等请求。 Use when the user wants get status ratelimit, status ratelimit, ratelimit, rate limit status, concurrency status, or when you need to call GET /status/ratelimit directly."
---

# UAPI 限流状态 接口

这个 skill 只封装一个接口：`GET /status/ratelimit`。当需求和“限流状态”直接对应时，优先直接选它，再去接口页确认参数、鉴权和返回码。

## 这个 skill 封装的接口

- 方法：`GET`
- 路径：`/status/ratelimit`
- 分类：`Status`
- Operation ID：`get-status-ratelimit`

## 什么时候直接选这个 skill

- 当用户的目标和“限流状态”完全对应时，优先直接选它。
- 这个 skill 只对应一个接口，所以不需要在大分类里二次挑选。
- 如果用户已经给了足够的参数，就可以直接进入接口页准备调用。

## 常见关键词

- 中文：`限流状态`、`并发状态`
- English: `get status ratelimit`, `status ratelimit`, `ratelimit`, `rate limit status`, `concurrency status`

## 使用步骤

1. 先读 `references/quick-start.md`，快速确认这个单接口是否就是当前要用的目标接口。
2. 再读 `references/operations/get-status-ratelimit.md`，确认参数、请求体、默认值、生效条件和响应码。
3. 如果需要看同分类上下文，再读 `references/resources/Status.md`。

## 鉴权与额度

- Base URL：`https://uapis.cn/api/v1`
- 这个接口需要管理员级别的 Bearer Token，不是普通公开 Key；如果返回 401 或 403，优先检查管理员凭证。
- 这组接口是管理员范围能力，重点先检查管理员 Token，而不是普通公开 Key。

## 常见返回码关注点

- 当前文档里能看到的状态码：`200`、`401`
- 如果返回 `401`，先检查当前请求是不是缺少认证信息，或者 Key / Token 是否无效、过期。

## 代表性的用户说法

- 帮我用 UAPI 的“限流状态”接口处理这个需求
- 这个需求是不是应该调用 限流状态 这个接口
- use the UAPI get-status-ratelimit endpoint for this task

## 导航文件

- `references/quick-start.md`：先快速判断这个单接口 skill 是否匹配当前需求。
- `references/operations/get-status-ratelimit.md`：这里是调用前必须看的核心接口页。
- `references/resources/Status.md`：只在需要补充同分类背景时再看。
