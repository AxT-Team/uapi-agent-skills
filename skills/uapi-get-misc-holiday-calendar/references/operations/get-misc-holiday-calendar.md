# 查询节假日与万年历

**接口地址**：`GET /misc/holiday-calendar`

**分类**：[Misc](../resources/Misc.md)

**Operation ID**：`get-misc-holiday-calendar`

## 这个接口适合什么时候用

查询指定日期、月份或年份的万年历与节假日信息。

## 功能概述
这个接口支持三种查询方式：按天（`date`）、按月（`month`）和按年（`year`）。调用时三者选一个传入即可。

如果你只关心某一类事件，可以通过 `holiday_type` 进行筛选，例如只看法定休假/调休、公历节日、农历节日或节气。

在 `date` 模式下，传 `include_nearby=true` 可以额外返回该日期前后最近的节日；返回数量由 `nearby_limit` 控制，默认 7，最大 30。

## 调用前检查

- 先确认用户真正需要的是最终结果，而不是某个中间步骤。
- 如果参数说明里写了互斥、默认值或生效条件，请严格按说明组织请求。
- 如果用户没有提供必要参数，先补齐参数再调用，不要靠猜。

## 参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `date` | query | string | 否 | 按天查询时填写这个参数，例如查某一天。格式：`YYYY-MM-DD`。和 `month`、`year` 三选一。 |
| `month` | query | string | 否 | 按月查询时填写这个参数，例如查某个月。格式：`YYYY-MM`。和 `date`、`year` 三选一。 |
| `year` | query | string | 否 | 按年查询时填写这个参数，例如查某一年。格式：`YYYY`。和 `date`、`month` 三选一。 |
| `timezone` | query | string | 否 | 时区名称，默认 Asia/Shanghai。 |
| `holiday_type` | query | enum: all, legal, legal_rest... | 否 | 节日筛选类型，默认 all。 |
| `include_nearby` | query | enum: false, true | 否 | 是否返回前后最近节日，仅 date 模式生效，默认 false。month/year 模式会忽略此参数。 |
| `nearby_limit` | query | integer | 否 | 返回最近节日数量限制，默认 7，最大 30。仅 date 模式 + include_nearby=true 生效。 |

## 响应码

| 状态码 | 说明 |
|--------|------|
| `200` | 查询成功，返回指定范围的万年历与节假日信息。 |
| `400` | 请求参数错误。常见原因：
- `date`、`month`、`year` 未传或同时传入多个
- 日期格式错误：`date` 必须为 `YYYY-MM-DD`、`month` 必须为 `YYYY-MM`、`year` 必须为 `YYYY`
- `holiday_type` 非法
- `timezone` 非法 |

