# 查询域名的WHOIS注册信息

**接口地址**：`GET /network/whois`

**分类**：[Network](../resources/Network.md)

**Operation ID**：`get-network-whois`

## 这个接口适合什么时候用

想知道一个域名是什么时候注册的、注册商是谁、什么时候到期？WHOIS信息可以告诉你这一切。

## 功能概述
这是一个在线的WHOIS查询工具。你可以通过如下两种方式获取WHOIS信息：

- **默认行为**（不带参数）：`GET /api/v1/network/whois?domain=google.com`
  - 返回一个JSON对象，`whois` 字段为原始、未处理的WHOIS文本字符串。
- **JSON格式化**：`GET /api/v1/network/whois?domain=google.com&format=json`
  - 返回一个JSON对象，`whois` 字段为解析后的JSON对象，包含WHOIS信息中的键值对。

这样你既可以获得最全的原始信息，也可以方便地处理结构化数据。

## 调用前检查

- 先确认用户真正需要的是最终结果，而不是某个中间步骤。
- 如果参数说明里写了互斥、默认值或生效条件，请严格按说明组织请求。
- 如果用户没有提供必要参数，先补齐参数再调用，不要靠猜。

## 参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `domain` | query | string | 是 | 你需要查询WHOIS信息的域名。 |
| `format` | query | enum: text, json | 否 | 返回格式。留空或为 'text' 时返回原始WHOIS文本，设为 'json' 时返回结构化JSON。 |

## 响应码

| 状态码 | 说明 |
|--------|------|
| `200` | 查询成功！根据 format 参数返回原始WHOIS文本或结构化JSON。 |
| `400` | 请求参数无效。请检查 `domain` 参数是否提供且格式正确。 |
| `404` | 查询失败或域名不存在。 |

