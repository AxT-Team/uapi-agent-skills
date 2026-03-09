# UAPI Agent Skills

这个仓库包含 86 个单接口 skill，每个 skill 只对应一个 UAPI 接口。

适合按接口粒度给 AI 安装和调用。下面按分类展开，点开具体接口后可以直接复制安装命令。

### 常用工具

<details>
<summary>展开查看 常用工具</summary>

<details>
<summary>Adcode 国内外行政区域查询</summary>

- Skill：`uapi-get-misc-district`
- 接口：`GET /misc/district`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-misc-district`

</details>

<details>
<summary>查询世界时间</summary>

- Skill：`uapi-get-misc-worldtime`
- 接口：`GET /misc/worldtime`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-misc-worldtime`

</details>

<details>
<summary>查询农历时间</summary>

- Skill：`uapi-get-misc-lunartime`
- 接口：`GET /misc/lunartime`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-misc-lunartime`

</details>

<details>
<summary>查询天气</summary>

- Skill：`uapi-get-misc-weather`
- 接口：`GET /misc/weather`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-misc-weather`

</details>

<details>
<summary>查询快递物流信息</summary>

- Skill：`uapi-get-misc-tracking-query`
- 接口：`GET /misc/tracking/query`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-misc-tracking-query`

</details>

<details>
<summary>查询手机归属地</summary>

- Skill：`uapi-get-misc-phoneinfo`
- 接口：`GET /misc/phoneinfo`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-misc-phoneinfo`

</details>

<details>
<summary>查询热榜</summary>

- Skill：`uapi-get-misc-hotboard`
- 接口：`GET /misc/hotboard`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-misc-hotboard`

</details>

<details>
<summary>查询节假日与万年历</summary>

- Skill：`uapi-get-misc-holiday-calendar`
- 接口：`GET /misc/holiday-calendar`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-misc-holiday-calendar`

</details>

<details>
<summary>程序员历史上的今天</summary>

- Skill：`uapi-get-history-programmer-today`
- 接口：`GET /history/programmer/today`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-history-programmer-today`

</details>

<details>
<summary>程序员历史事件</summary>

- Skill：`uapi-get-history-programmer`
- 接口：`GET /history/programmer`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-history-programmer`

</details>

<details>
<summary>获取支持的快递公司列表</summary>

- Skill：`uapi-get-misc-tracking-carriers`
- 接口：`GET /misc/tracking/carriers`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-misc-tracking-carriers`

</details>

<details>
<summary>计算两个日期之间的时间差值</summary>

- Skill：`uapi-post-misc-date-diff`
- 接口：`POST /misc/date-diff`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-misc-date-diff`

</details>

<details>
<summary>识别快递公司</summary>

- Skill：`uapi-get-misc-tracking-detect`
- 接口：`GET /misc/tracking/detect`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-misc-tracking-detect`

</details>

<details>
<summary>转换时间戳 (旧版，推荐使用/convert/unixtime)</summary>

- Skill：`uapi-get-misc-timestamp`
- 接口：`GET /misc/timestamp`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-misc-timestamp`

</details>

<details>
<summary>随机数生成</summary>

- Skill：`uapi-get-misc-randomnumber`
- 接口：`GET /misc/randomnumber`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-misc-randomnumber`

</details>


</details>

### 图片处理

<details>
<summary>展开查看 图片处理</summary>

<details>
<summary>SVG转图片</summary>

- Skill：`uapi-post-image-svg`
- 接口：`POST /image/svg`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-image-svg`

</details>

<details>
<summary>图片敏感检测</summary>

- Skill：`uapi-post-image-nsfw`
- 接口：`POST /image/nsfw`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-image-nsfw`

</details>

<details>
<summary>图片转 Base64</summary>

- Skill：`uapi-get-image-tobase64`
- 接口：`GET /image/tobase64`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-image-tobase64`

</details>

<details>
<summary>必应壁纸</summary>

- Skill：`uapi-get-image-bing-daily`
- 接口：`GET /image/bing-daily`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-image-bing-daily`

</details>

<details>
<summary>无损压缩图片</summary>

- Skill：`uapi-post-image-compress`
- 接口：`POST /image/compress`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-image-compress`

</details>

<details>
<summary>生成二维码</summary>

- Skill：`uapi-get-image-qrcode`
- 接口：`GET /image/qrcode`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-image-qrcode`

</details>

<details>
<summary>生成你们怎么不说话了表情包</summary>

- Skill：`uapi-post-image-speechless`
- 接口：`POST /image/speechless`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-image-speechless`

</details>

<details>
<summary>生成摸摸头GIF</summary>

- Skill：`uapi-post-image-motou`
- 接口：`POST /image/motou`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-image-motou`

</details>

<details>
<summary>生成摸摸头GIF (QQ号)</summary>

- Skill：`uapi-get-image-motou`
- 接口：`GET /image/motou`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-image-motou`

</details>

<details>
<summary>获取Gravatar头像</summary>

- Skill：`uapi-get-avatar-gravatar`
- 接口：`GET /avatar/gravatar`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-avatar-gravatar`

</details>

<details>
<summary>通过Base64编码上传图片</summary>

- Skill：`uapi-post-image-frombase64`
- 接口：`POST /image/frombase64`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-image-frombase64`

</details>


</details>

### 文本处理

<details>
<summary>展开查看 文本处理</summary>

<details>
<summary>AES 加密</summary>

- Skill：`uapi-post-text-aes-encrypt`
- 接口：`POST /text/aes/encrypt`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-text-aes-encrypt`

</details>

<details>
<summary>AES 解密</summary>

- Skill：`uapi-post-text-aes-decrypt`
- 接口：`POST /text/aes/decrypt`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-text-aes-decrypt`

</details>

<details>
<summary>AES高级加密</summary>

- Skill：`uapi-post-text-aes-encrypt-advanced`
- 接口：`POST /text/aes/encrypt-advanced`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-text-aes-encrypt-advanced`

</details>

<details>
<summary>AES高级解密</summary>

- Skill：`uapi-post-text-aes-decrypt-advanced`
- 接口：`POST /text/aes/decrypt-advanced`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-text-aes-decrypt-advanced`

</details>

<details>
<summary>Base64 编码</summary>

- Skill：`uapi-post-text-base64-encode`
- 接口：`POST /text/base64/encode`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-text-base64-encode`

</details>

<details>
<summary>Base64 解码</summary>

- Skill：`uapi-post-text-base64-decode`
- 接口：`POST /text/base64/decode`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-text-base64-decode`

</details>

<details>
<summary>MD5 哈希</summary>

- Skill：`uapi-get-text-md5`
- 接口：`GET /text/md5`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-text-md5`

</details>

<details>
<summary>MD5 哈希 (POST)</summary>

- Skill：`uapi-post-text-md5`
- 接口：`POST /text/md5`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-text-md5`

</details>

<details>
<summary>MD5 校验</summary>

- Skill：`uapi-post-text-md5-verify`
- 接口：`POST /text/md5/verify`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-text-md5-verify`

</details>

<details>
<summary>文本分析</summary>

- Skill：`uapi-post-text-analyze`
- 接口：`POST /text/analyze`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-text-analyze`

</details>

<details>
<summary>格式转换</summary>

- Skill：`uapi-post-text-convert`
- 接口：`POST /text/convert`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-text-convert`

</details>


</details>

### 网络工具

<details>
<summary>展开查看 网络工具</summary>

<details>
<summary>Ping 主机</summary>

- Skill：`uapi-get-network-ping`
- 接口：`GET /network/ping`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-network-ping`

</details>

<details>
<summary>Ping 我的 IP</summary>

- Skill：`uapi-get-network-pingmyip`
- 接口：`GET /network/pingmyip`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-network-pingmyip`

</details>

<details>
<summary>执行DNS解析查询</summary>

- Skill：`uapi-get-network-dns`
- 接口：`GET /network/dns`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-network-dns`

</details>

<details>
<summary>查询 IP</summary>

- Skill：`uapi-get-network-ipinfo`
- 接口：`GET /network/ipinfo`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-network-ipinfo`

</details>

<details>
<summary>查询域名ICP备案信息</summary>

- Skill：`uapi-get-network-icp`
- 接口：`GET /network/icp`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-network-icp`

</details>

<details>
<summary>查询域名的WHOIS注册信息</summary>

- Skill：`uapi-get-network-whois`
- 接口：`GET /network/whois`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-network-whois`

</details>

<details>
<summary>查询我的 IP</summary>

- Skill：`uapi-get-network-myip`
- 接口：`GET /network/myip`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-network-myip`

</details>

<details>
<summary>检查URL的可访问性状态</summary>

- Skill：`uapi-get-network-urlstatus`
- 接口：`GET /network/urlstatus`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-network-urlstatus`

</details>

<details>
<summary>检查域名在微信中的访问状态</summary>

- Skill：`uapi-get-network-wxdomain`
- 接口：`GET /network/wxdomain`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-network-wxdomain`

</details>

<details>
<summary>端口扫描</summary>

- Skill：`uapi-get-network-portscan`
- 接口：`GET /network/portscan`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-network-portscan`

</details>


</details>

### 社交平台

<details>
<summary>展开查看 社交平台</summary>

<details>
<summary>查询 B站投稿</summary>

- Skill：`uapi-get-social-bilibili-archives`
- 接口：`GET /social/bilibili/archives`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-social-bilibili-archives`

</details>

<details>
<summary>查询 B站用户</summary>

- Skill：`uapi-get-social-bilibili-userinfo`
- 接口：`GET /social/bilibili/userinfo`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-social-bilibili-userinfo`

</details>

<details>
<summary>查询 B站直播间</summary>

- Skill：`uapi-get-social-bilibili-liveroom`
- 接口：`GET /social/bilibili/liveroom`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-social-bilibili-liveroom`

</details>

<details>
<summary>查询 B站视频</summary>

- Skill：`uapi-get-social-bilibili-videoinfo`
- 接口：`GET /social/bilibili/videoinfo`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-social-bilibili-videoinfo`

</details>

<details>
<summary>查询 B站评论</summary>

- Skill：`uapi-get-social-bilibili-replies`
- 接口：`GET /social/bilibili/replies`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-social-bilibili-replies`

</details>

<details>
<summary>查询 GitHub 仓库</summary>

- Skill：`uapi-get-github-repo`
- 接口：`GET /github/repo`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-github-repo`

</details>

<details>
<summary>查询 QQ 信息</summary>

- Skill：`uapi-get-social-qq-userinfo`
- 接口：`GET /social/qq/userinfo`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-social-qq-userinfo`

</details>

<details>
<summary>查询 QQ 群信息</summary>

- Skill：`uapi-get-social-qq-groupinfo`
- 接口：`GET /social/qq/groupinfo`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-social-qq-groupinfo`

</details>


</details>

### 游戏相关

<details>
<summary>展开查看 游戏相关</summary>

<details>
<summary>Epic 免费游戏</summary>

- Skill：`uapi-get-game-epic-free`
- 接口：`GET /game/epic-free`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-game-epic-free`

</details>

<details>
<summary>查询 MC 曾用名</summary>

- Skill：`uapi-get-game-minecraft-historyid`
- 接口：`GET /game/minecraft/historyid`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-game-minecraft-historyid`

</details>

<details>
<summary>查询 MC 服务器</summary>

- Skill：`uapi-get-game-minecraft-serverstatus`
- 接口：`GET /game/minecraft/serverstatus`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-game-minecraft-serverstatus`

</details>

<details>
<summary>查询 MC 玩家</summary>

- Skill：`uapi-get-game-minecraft-userinfo`
- 接口：`GET /game/minecraft/userinfo`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-game-minecraft-userinfo`

</details>

<details>
<summary>查询 Steam 用户</summary>

- Skill：`uapi-get-game-steam-summary`
- 接口：`GET /game/steam/summary`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-game-steam-summary`

</details>


</details>

### 随机内容

<details>
<summary>展开查看 随机内容</summary>

<details>
<summary>答案之书</summary>

- Skill：`uapi-get-answerbook-ask`
- 接口：`GET /answerbook/ask`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-answerbook-ask`

</details>

<details>
<summary>答案之书 (POST)</summary>

- Skill：`uapi-post-answerbook-ask`
- 接口：`POST /answerbook/ask`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-answerbook-ask`

</details>

<details>
<summary>随机图片</summary>

- Skill：`uapi-get-random-image`
- 接口：`GET /random/image`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-random-image`

</details>

<details>
<summary>随机字符串</summary>

- Skill：`uapi-get-random-string`
- 接口：`GET /random/string`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-random-string`

</details>


</details>

### 翻译能力

<details>
<summary>展开查看 翻译能力</summary>

<details>
<summary>AI智能翻译</summary>

- Skill：`uapi-post-ai-translate`
- 接口：`POST /ai/translate`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-ai-translate`

</details>

<details>
<summary>AI翻译配置</summary>

- Skill：`uapi-get-ai-translate-languages`
- 接口：`GET /ai/translate/languages`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-ai-translate-languages`

</details>

<details>
<summary>流式翻译（中英互译）</summary>

- Skill：`uapi-post-translate-stream`
- 接口：`POST /translate/stream`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-translate-stream`

</details>

<details>
<summary>翻译</summary>

- Skill：`uapi-post-translate-text`
- 接口：`POST /translate/text`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-translate-text`

</details>


</details>

### 网页解析

<details>
<summary>展开查看 网页解析</summary>

<details>
<summary>提取网页元数据</summary>

- Skill：`uapi-get-webparse-metadata`
- 接口：`GET /webparse/metadata`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-webparse-metadata`

</details>

<details>
<summary>提取网页图片</summary>

- Skill：`uapi-get-webparse-extractimages`
- 接口：`GET /webparse/extractimages`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-webparse-extractimages`

</details>

<details>
<summary>网页转 Markdown</summary>

- Skill：`uapi-post-web-tomarkdown-async`
- 接口：`POST /web/tomarkdown/async`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-web-tomarkdown-async`

</details>

<details>
<summary>转换任务状态</summary>

- Skill：`uapi-get-web-tomarkdown-async-status`
- 接口：`GET /web/tomarkdown/async/{task_id}`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-web-tomarkdown-async-status`

</details>


</details>

### Clipzy 在线剪贴板

<details>
<summary>展开查看 Clipzy 在线剪贴板</summary>

<details>
<summary>步骤1：上传加密数据</summary>

- Skill：`uapi-post-clipzy-store`
- 接口：`POST /api/store`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-clipzy-store`

</details>

<details>
<summary>步骤2 (方法一): 获取加密数据</summary>

- Skill：`uapi-get-clipzy-get`
- 接口：`GET /api/get`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-clipzy-get`

</details>

<details>
<summary>步骤2 (方法二): 获取原始文本</summary>

- Skill：`uapi-get-clipzy-raw`
- 接口：`GET /api/raw/{id}`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-clipzy-raw`

</details>


</details>

### 敏感词识别

<details>
<summary>展开查看 敏感词识别</summary>

<details>
<summary>分析敏感词</summary>

- Skill：`uapi-post-sensitive-word-analyze`
- 接口：`POST /sensitive-word/analyze`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-sensitive-word-analyze`

</details>

<details>
<summary>敏感词分析 (GET)</summary>

- Skill：`uapi-get-sensitive-word-analyze-query`
- 接口：`GET /sensitive-word/analyze-query`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-sensitive-word-analyze-query`

</details>

<details>
<summary>敏感词检测（快速）</summary>

- Skill：`uapi-post-sensitive-word-quick-check`
- 接口：`POST /text/profanitycheck`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-sensitive-word-quick-check`

</details>


</details>

### 格式转换

<details>
<summary>展开查看 格式转换</summary>

<details>
<summary>JSON 格式化</summary>

- Skill：`uapi-post-convert-json`
- 接口：`POST /convert/json`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-convert-json`

</details>

<details>
<summary>时间戳转换</summary>

- Skill：`uapi-get-convert-unixtime`
- 接口：`GET /convert/unixtime`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-convert-unixtime`

</details>


</details>

### 状态查询

<details>
<summary>展开查看 状态查询</summary>

<details>
<summary>获取API端点使用统计</summary>

- Skill：`uapi-get-status-usage`
- 接口：`GET /status/usage`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-status-usage`

</details>

<details>
<summary>限流状态</summary>

- Skill：`uapi-get-status-ratelimit`
- 接口：`GET /status/ratelimit`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-status-ratelimit`

</details>


</details>

### 智能搜索

<details>
<summary>展开查看 智能搜索</summary>

<details>
<summary>搜索引擎配置</summary>

- Skill：`uapi-get-search-engines`
- 接口：`GET /search/engines`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-search-engines`

</details>

<details>
<summary>智能搜索</summary>

- Skill：`uapi-post-search-aggregate`
- 接口：`POST /search/aggregate`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-search-aggregate`

</details>


</details>

### 每日内容

<details>
<summary>展开查看 每日内容</summary>

<details>
<summary>每日新闻图</summary>

- Skill：`uapi-get-daily-news-image`
- 接口：`GET /daily/news-image`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-daily-news-image`

</details>


</details>

### 语录内容

<details>
<summary>展开查看 语录内容</summary>

<details>
<summary>一言</summary>

- Skill：`uapi-get-saying`
- 接口：`GET /saying`
- 安装命令：`npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-saying`

</details>


</details>
