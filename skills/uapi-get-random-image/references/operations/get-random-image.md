# 随机图片

**接口地址**：`GET /random/image`

**分类**：[Random](../resources/Random.md)

**Operation ID**：`get-random-image`

## 这个接口适合什么时候用

需要一张随机图片作为占位符或者背景吗？这个接口是你的不二之选。

## 功能概述
这是一个非常简单的接口，它会从我们庞大的图库和精选外部图床中随机挑选一张图片，然后通过 302 重定向让你直接访问到它。这使得它可以非常方便地直接用在 HTML 的 `<img>` 标签中。

你可以通过 `/api/v1/random/image?category=acg&type=4k` 这样的请求获取由UapiPro服务器提供的图片，也可以通过 `/api/v1/random/image?category=ai_drawing` 获取由外部图床精选的图片。

如果你不提供任何 category 参数，程序会从所有图片（包括本地的和URL的）中随机抽取一张（**全局随机图片不包含ikun和AI绘画**）。

> [!TIP]
> 如果你需要更精确地控制图片类型，请使用 `/image/random/{category}/{type}` 接口。

### 支持的主类别与子类别
- **acg**（二次元动漫）


    - pc
    - mb
- **外部图床精选/混合动漫**


  - **landscape**: 风景图。
  - **anime**: 混合了UapiPro服务器的acg和外部图床的general_anime分类下的图片。
  - **pc_wallpaper**: 电脑壁纸。
  - **mobile_wallpaper**: 手机壁纸。
  - **general_anime**: 动漫图。
  - **ai_drawing**: AI绘画。
- **其他分类**


  - **bq**（表情包/趣图）
    - eciyuan
    - ikun
    - xiongmao
    - waiguoren
    - maomao
  - **furry**（福瑞）
    - z4k
    - szs8k
    - s4k
    - 4k

> [!NOTE]
> 默认全局随机（未指定category参数）时，不会包含ikun和AI绘画（ai_drawing）类别的图片。


## 调用前检查

- 先确认用户真正需要的是最终结果，而不是某个中间步骤。
- 如果参数说明里写了互斥、默认值或生效条件，请严格按说明组织请求。
- 如果用户没有提供必要参数，先补齐参数再调用，不要靠猜。

## 参数

| 参数名 | 位置 | 类型 | 必填 | 说明 |
|--------|------|------|------|------|
| `category` | query | enum: acg, landscape, anime... | 否 | （可选）指定图片主类别。

**支持的主类别：**
- `acg`（二次元动漫，UapiPro服务器）
- `landscape`（风景图，外部图床）
- `anime`（混合动漫）
- `pc_wallpaper`（电脑壁纸，外部图床）
- `mobile_wallpaper`（手机壁纸，外部图床）
- `general_anime`（动漫图，外部图床）
- `ai_drawing`（AI绘画，外部图床）
- `bq`（表情包/趣图，UapiPro服务器）
- `furry`（福瑞，UapiPro服务器）

> [!TIP]
> 如果不指定，将从所有图片中随机抽取（不包含 `ikun` 和 `ai_drawing`）。
 |
| `type` | query | enum: pc, mb, eciyuan... | 否 | （可选，仅UapiPro服务器图片支持）指定图片子类别。

- **bq**: `xiongmao`, `waiguoren`, `maomao`, `ikun`, `eciyuan`
- **acg**: `pc`, `mb`
- **furry**: `z4k`, `szs8k`, `s4k`, `4k`

> [!TIP]
> 外部图床类别和 `anime` 混合类别不支持 `type` 参数。
 |

## 响应码

| 状态码 | 说明 |
|--------|------|
| `200` | 成功！将随机图片以图片二进制 (image/jpeg) 直接返回给客户端，可直接在 <img> 标签中使用。 |
| `404` | 未找到指定类别的图片。 |
| `500` | 服务器内部错误。 |

