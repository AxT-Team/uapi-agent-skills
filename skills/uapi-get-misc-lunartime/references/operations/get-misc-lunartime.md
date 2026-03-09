# 查询农历时间

**接口地址**：`GET /misc/lunartime`

**分类**：[Misc](../resources/Misc.md)

**Operation ID**：`get-misc-lunartime`

## 这个接口适合什么时候用

需要在指定时区下查看某个时间点的农历信息？这个接口可以直接返回完整结果。

## 功能概述
支持传入 Unix 时间戳（秒或毫秒）和 IANA 时区名，返回公历时间、星期、农历年月日、干支、生肖、节气与节日信息。不传 `ts` 时默认使用当前时间，不传 `timezone` 时默认 `Asia/Shanghai`。

## 时区说明
- 支持标准 IANA 时区，例如 `Asia/Shanghai`、`Asia/Tokyo`
- 也支持别名：`Shanghai`、`Beijing`
- 时区非法时返回 400 并提示 `invalid timezone: xxx`

## 调用前检查

- 先确认用户真正需要的是最终结果，而不是某个中间步骤。
- 如果参数说明里写了互斥、默认值或生效条件，请严格按说明组织请求。
- 如果用户没有提供必要参数，先补齐参数再调用，不要靠猜。

## 参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `ts` | query | string | 否 | Unix 时间戳，支持 10 位秒级或 13 位毫秒级。不传则默认当前时间。 |
| `timezone` | query | string | 否 | 时区名称。支持 IANA 时区（如 Asia/Shanghai）和别名（Shanghai、Beijing）。默认 Asia/Shanghai。 |

## 响应码

| 状态码 | 说明 |
|--------|------|
| `200` | 查询成功，返回指定时间和时区下的农历信息。 |
| `400` | 请求参数错误。`timezone` 非法时返回 `invalid timezone: xxx`，`ts` 非法时返回 `invalid timestamp: xxx`。 |

