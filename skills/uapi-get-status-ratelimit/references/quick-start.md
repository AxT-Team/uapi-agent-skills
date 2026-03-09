# 快速上手

这个 skill 只封装一个接口：`GET /status/ratelimit`。当需求和“限流状态”直接对应时，优先直接选它，再去接口页确认参数、鉴权和返回码。

## 什么时候直接调用

- 当用户明确要做“限流状态”这件事时，直接选这个 skill。
- 当前 skill 只对应一个接口：`GET /status/ratelimit`。
- 如果参数还不完整，先去接口页补齐必填项，再调用。

## 核心资料

- 接口页：`references/operations/get-status-ratelimit.md`
- 分类页：`references/resources/Status.md`

## 调用前检查

1. 先确认用户真正要的是最终结果，而不是某个中间步骤。
2. 再确认参数是否齐全，尤其是路径参数、查询参数和请求体里的必填字段。
3. 如果接口页提到了第三方 Key、管理员 Token 或解密 key，先补凭证再继续。

## 鉴权与报错

- 这个接口需要管理员级别的 Bearer Token，不是普通公开 Key；如果返回 401 或 403，优先检查管理员凭证。
- 如果返回 `401` 或 `403`，优先检查管理员级别 Bearer Token 是否存在、是否过期，以及是否具备对应权限。

## 关键词索引

- 中文：`限流状态`、`并发状态`
- English: `get status ratelimit`, `status ratelimit`, `ratelimit`, `rate limit status`, `concurrency status`

## 示例说法

- 帮我用 UAPI 的“限流状态”接口处理这个需求
- 这个需求是不是应该调用 限流状态 这个接口
- use the UAPI get-status-ratelimit endpoint for this task
