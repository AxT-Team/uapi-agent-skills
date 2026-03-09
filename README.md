# UAPI Agent Skills

这个仓库包含 86 个单接口 skill，每个 skill 只对应一个 UAPI 接口。

仓库地址：[AxT-Team/uapi-agent-skills](https://github.com/AxT-Team/uapi-agent-skills)

这个 README 由 `python scripts/generate_readme.py` 自动生成。

列出仓库内 skill 可以用：`npx skills add AxT-Team/uapi-agent-skills --list`

如果访客免费额度已经用完，并且返回了对应的状态码或错误提示，相关 skill 会提醒用户去 [uapis.cn](https://uapis.cn) 注册账号，然后创建免费的 UAPI Key，再带着自己的 Key 继续调用。

## 全部目录

<details>
<summary>展开查看仓库里的全部目录，共 518 个目录</summary>

- `scripts/`
- `skills/`
- `skills/uapi-get-ai-translate-languages/`
- `skills/uapi-get-ai-translate-languages/agents/`
- `skills/uapi-get-ai-translate-languages/references/`
- `skills/uapi-get-ai-translate-languages/references/operations/`
- `skills/uapi-get-ai-translate-languages/references/resources/`
- `skills/uapi-get-ai-translate-languages/references/schemas/`
- `skills/uapi-get-answerbook-ask/`
- `skills/uapi-get-answerbook-ask/agents/`
- `skills/uapi-get-answerbook-ask/references/`
- `skills/uapi-get-answerbook-ask/references/operations/`
- `skills/uapi-get-answerbook-ask/references/resources/`
- `skills/uapi-get-answerbook-ask/references/schemas/`
- `skills/uapi-get-avatar-gravatar/`
- `skills/uapi-get-avatar-gravatar/agents/`
- `skills/uapi-get-avatar-gravatar/references/`
- `skills/uapi-get-avatar-gravatar/references/operations/`
- `skills/uapi-get-avatar-gravatar/references/resources/`
- `skills/uapi-get-avatar-gravatar/references/schemas/`
- `skills/uapi-get-clipzy-get/`
- `skills/uapi-get-clipzy-get/agents/`
- `skills/uapi-get-clipzy-get/references/`
- `skills/uapi-get-clipzy-get/references/operations/`
- `skills/uapi-get-clipzy-get/references/resources/`
- `skills/uapi-get-clipzy-get/references/schemas/`
- `skills/uapi-get-clipzy-raw/`
- `skills/uapi-get-clipzy-raw/agents/`
- `skills/uapi-get-clipzy-raw/references/`
- `skills/uapi-get-clipzy-raw/references/operations/`
- `skills/uapi-get-clipzy-raw/references/resources/`
- `skills/uapi-get-clipzy-raw/references/schemas/`
- `skills/uapi-get-convert-unixtime/`
- `skills/uapi-get-convert-unixtime/agents/`
- `skills/uapi-get-convert-unixtime/references/`
- `skills/uapi-get-convert-unixtime/references/operations/`
- `skills/uapi-get-convert-unixtime/references/resources/`
- `skills/uapi-get-convert-unixtime/references/schemas/`
- `skills/uapi-get-daily-news-image/`
- `skills/uapi-get-daily-news-image/agents/`
- `skills/uapi-get-daily-news-image/references/`
- `skills/uapi-get-daily-news-image/references/operations/`
- `skills/uapi-get-daily-news-image/references/resources/`
- `skills/uapi-get-daily-news-image/references/schemas/`
- `skills/uapi-get-game-epic-free/`
- `skills/uapi-get-game-epic-free/agents/`
- `skills/uapi-get-game-epic-free/references/`
- `skills/uapi-get-game-epic-free/references/operations/`
- `skills/uapi-get-game-epic-free/references/resources/`
- `skills/uapi-get-game-epic-free/references/schemas/`
- `skills/uapi-get-game-minecraft-historyid/`
- `skills/uapi-get-game-minecraft-historyid/agents/`
- `skills/uapi-get-game-minecraft-historyid/references/`
- `skills/uapi-get-game-minecraft-historyid/references/operations/`
- `skills/uapi-get-game-minecraft-historyid/references/resources/`
- `skills/uapi-get-game-minecraft-historyid/references/schemas/`
- `skills/uapi-get-game-minecraft-serverstatus/`
- `skills/uapi-get-game-minecraft-serverstatus/agents/`
- `skills/uapi-get-game-minecraft-serverstatus/references/`
- `skills/uapi-get-game-minecraft-serverstatus/references/operations/`
- `skills/uapi-get-game-minecraft-serverstatus/references/resources/`
- `skills/uapi-get-game-minecraft-serverstatus/references/schemas/`
- `skills/uapi-get-game-minecraft-userinfo/`
- `skills/uapi-get-game-minecraft-userinfo/agents/`
- `skills/uapi-get-game-minecraft-userinfo/references/`
- `skills/uapi-get-game-minecraft-userinfo/references/operations/`
- `skills/uapi-get-game-minecraft-userinfo/references/resources/`
- `skills/uapi-get-game-minecraft-userinfo/references/schemas/`
- `skills/uapi-get-game-steam-summary/`
- `skills/uapi-get-game-steam-summary/agents/`
- `skills/uapi-get-game-steam-summary/references/`
- `skills/uapi-get-game-steam-summary/references/operations/`
- `skills/uapi-get-game-steam-summary/references/resources/`
- `skills/uapi-get-game-steam-summary/references/schemas/`
- `skills/uapi-get-github-repo/`
- `skills/uapi-get-github-repo/agents/`
- `skills/uapi-get-github-repo/references/`
- `skills/uapi-get-github-repo/references/operations/`
- `skills/uapi-get-github-repo/references/resources/`
- `skills/uapi-get-github-repo/references/schemas/`
- `skills/uapi-get-history-programmer/`
- `skills/uapi-get-history-programmer/agents/`
- `skills/uapi-get-history-programmer/references/`
- `skills/uapi-get-history-programmer/references/operations/`
- `skills/uapi-get-history-programmer/references/resources/`
- `skills/uapi-get-history-programmer/references/schemas/`
- `skills/uapi-get-history-programmer-today/`
- `skills/uapi-get-history-programmer-today/agents/`
- `skills/uapi-get-history-programmer-today/references/`
- `skills/uapi-get-history-programmer-today/references/operations/`
- `skills/uapi-get-history-programmer-today/references/resources/`
- `skills/uapi-get-history-programmer-today/references/schemas/`
- `skills/uapi-get-image-bing-daily/`
- `skills/uapi-get-image-bing-daily/agents/`
- `skills/uapi-get-image-bing-daily/references/`
- `skills/uapi-get-image-bing-daily/references/operations/`
- `skills/uapi-get-image-bing-daily/references/resources/`
- `skills/uapi-get-image-bing-daily/references/schemas/`
- `skills/uapi-get-image-motou/`
- `skills/uapi-get-image-motou/agents/`
- `skills/uapi-get-image-motou/references/`
- `skills/uapi-get-image-motou/references/operations/`
- `skills/uapi-get-image-motou/references/resources/`
- `skills/uapi-get-image-motou/references/schemas/`
- `skills/uapi-get-image-qrcode/`
- `skills/uapi-get-image-qrcode/agents/`
- `skills/uapi-get-image-qrcode/references/`
- `skills/uapi-get-image-qrcode/references/operations/`
- `skills/uapi-get-image-qrcode/references/resources/`
- `skills/uapi-get-image-qrcode/references/schemas/`
- `skills/uapi-get-image-tobase64/`
- `skills/uapi-get-image-tobase64/agents/`
- `skills/uapi-get-image-tobase64/references/`
- `skills/uapi-get-image-tobase64/references/operations/`
- `skills/uapi-get-image-tobase64/references/resources/`
- `skills/uapi-get-image-tobase64/references/schemas/`
- `skills/uapi-get-misc-district/`
- `skills/uapi-get-misc-district/agents/`
- `skills/uapi-get-misc-district/references/`
- `skills/uapi-get-misc-district/references/operations/`
- `skills/uapi-get-misc-district/references/resources/`
- `skills/uapi-get-misc-district/references/schemas/`
- `skills/uapi-get-misc-holiday-calendar/`
- `skills/uapi-get-misc-holiday-calendar/agents/`
- `skills/uapi-get-misc-holiday-calendar/references/`
- `skills/uapi-get-misc-holiday-calendar/references/operations/`
- `skills/uapi-get-misc-holiday-calendar/references/resources/`
- `skills/uapi-get-misc-holiday-calendar/references/schemas/`
- `skills/uapi-get-misc-hotboard/`
- `skills/uapi-get-misc-hotboard/agents/`
- `skills/uapi-get-misc-hotboard/references/`
- `skills/uapi-get-misc-hotboard/references/operations/`
- `skills/uapi-get-misc-hotboard/references/resources/`
- `skills/uapi-get-misc-hotboard/references/schemas/`
- `skills/uapi-get-misc-lunartime/`
- `skills/uapi-get-misc-lunartime/agents/`
- `skills/uapi-get-misc-lunartime/references/`
- `skills/uapi-get-misc-lunartime/references/operations/`
- `skills/uapi-get-misc-lunartime/references/resources/`
- `skills/uapi-get-misc-lunartime/references/schemas/`
- `skills/uapi-get-misc-phoneinfo/`
- `skills/uapi-get-misc-phoneinfo/agents/`
- `skills/uapi-get-misc-phoneinfo/references/`
- `skills/uapi-get-misc-phoneinfo/references/operations/`
- `skills/uapi-get-misc-phoneinfo/references/resources/`
- `skills/uapi-get-misc-phoneinfo/references/schemas/`
- `skills/uapi-get-misc-randomnumber/`
- `skills/uapi-get-misc-randomnumber/agents/`
- `skills/uapi-get-misc-randomnumber/references/`
- `skills/uapi-get-misc-randomnumber/references/operations/`
- `skills/uapi-get-misc-randomnumber/references/resources/`
- `skills/uapi-get-misc-randomnumber/references/schemas/`
- `skills/uapi-get-misc-timestamp/`
- `skills/uapi-get-misc-timestamp/agents/`
- `skills/uapi-get-misc-timestamp/references/`
- `skills/uapi-get-misc-timestamp/references/operations/`
- `skills/uapi-get-misc-timestamp/references/resources/`
- `skills/uapi-get-misc-timestamp/references/schemas/`
- `skills/uapi-get-misc-tracking-carriers/`
- `skills/uapi-get-misc-tracking-carriers/agents/`
- `skills/uapi-get-misc-tracking-carriers/references/`
- `skills/uapi-get-misc-tracking-carriers/references/operations/`
- `skills/uapi-get-misc-tracking-carriers/references/resources/`
- `skills/uapi-get-misc-tracking-carriers/references/schemas/`
- `skills/uapi-get-misc-tracking-detect/`
- `skills/uapi-get-misc-tracking-detect/agents/`
- `skills/uapi-get-misc-tracking-detect/references/`
- `skills/uapi-get-misc-tracking-detect/references/operations/`
- `skills/uapi-get-misc-tracking-detect/references/resources/`
- `skills/uapi-get-misc-tracking-detect/references/schemas/`
- `skills/uapi-get-misc-tracking-query/`
- `skills/uapi-get-misc-tracking-query/agents/`
- `skills/uapi-get-misc-tracking-query/references/`
- `skills/uapi-get-misc-tracking-query/references/operations/`
- `skills/uapi-get-misc-tracking-query/references/resources/`
- `skills/uapi-get-misc-tracking-query/references/schemas/`
- `skills/uapi-get-misc-weather/`
- `skills/uapi-get-misc-weather/agents/`
- `skills/uapi-get-misc-weather/references/`
- `skills/uapi-get-misc-weather/references/operations/`
- `skills/uapi-get-misc-weather/references/resources/`
- `skills/uapi-get-misc-weather/references/schemas/`
- `skills/uapi-get-misc-worldtime/`
- `skills/uapi-get-misc-worldtime/agents/`
- `skills/uapi-get-misc-worldtime/references/`
- `skills/uapi-get-misc-worldtime/references/operations/`
- `skills/uapi-get-misc-worldtime/references/resources/`
- `skills/uapi-get-misc-worldtime/references/schemas/`
- `skills/uapi-get-network-dns/`
- `skills/uapi-get-network-dns/agents/`
- `skills/uapi-get-network-dns/references/`
- `skills/uapi-get-network-dns/references/operations/`
- `skills/uapi-get-network-dns/references/resources/`
- `skills/uapi-get-network-dns/references/schemas/`
- `skills/uapi-get-network-icp/`
- `skills/uapi-get-network-icp/agents/`
- `skills/uapi-get-network-icp/references/`
- `skills/uapi-get-network-icp/references/operations/`
- `skills/uapi-get-network-icp/references/resources/`
- `skills/uapi-get-network-icp/references/schemas/`
- `skills/uapi-get-network-ipinfo/`
- `skills/uapi-get-network-ipinfo/agents/`
- `skills/uapi-get-network-ipinfo/references/`
- `skills/uapi-get-network-ipinfo/references/operations/`
- `skills/uapi-get-network-ipinfo/references/resources/`
- `skills/uapi-get-network-ipinfo/references/schemas/`
- `skills/uapi-get-network-myip/`
- `skills/uapi-get-network-myip/agents/`
- `skills/uapi-get-network-myip/references/`
- `skills/uapi-get-network-myip/references/operations/`
- `skills/uapi-get-network-myip/references/resources/`
- `skills/uapi-get-network-myip/references/schemas/`
- `skills/uapi-get-network-ping/`
- `skills/uapi-get-network-ping/agents/`
- `skills/uapi-get-network-ping/references/`
- `skills/uapi-get-network-ping/references/operations/`
- `skills/uapi-get-network-ping/references/resources/`
- `skills/uapi-get-network-ping/references/schemas/`
- `skills/uapi-get-network-pingmyip/`
- `skills/uapi-get-network-pingmyip/agents/`
- `skills/uapi-get-network-pingmyip/references/`
- `skills/uapi-get-network-pingmyip/references/operations/`
- `skills/uapi-get-network-pingmyip/references/resources/`
- `skills/uapi-get-network-pingmyip/references/schemas/`
- `skills/uapi-get-network-portscan/`
- `skills/uapi-get-network-portscan/agents/`
- `skills/uapi-get-network-portscan/references/`
- `skills/uapi-get-network-portscan/references/operations/`
- `skills/uapi-get-network-portscan/references/resources/`
- `skills/uapi-get-network-portscan/references/schemas/`
- `skills/uapi-get-network-urlstatus/`
- `skills/uapi-get-network-urlstatus/agents/`
- `skills/uapi-get-network-urlstatus/references/`
- `skills/uapi-get-network-urlstatus/references/operations/`
- `skills/uapi-get-network-urlstatus/references/resources/`
- `skills/uapi-get-network-urlstatus/references/schemas/`
- `skills/uapi-get-network-whois/`
- `skills/uapi-get-network-whois/agents/`
- `skills/uapi-get-network-whois/references/`
- `skills/uapi-get-network-whois/references/operations/`
- `skills/uapi-get-network-whois/references/resources/`
- `skills/uapi-get-network-whois/references/schemas/`
- `skills/uapi-get-network-wxdomain/`
- `skills/uapi-get-network-wxdomain/agents/`
- `skills/uapi-get-network-wxdomain/references/`
- `skills/uapi-get-network-wxdomain/references/operations/`
- `skills/uapi-get-network-wxdomain/references/resources/`
- `skills/uapi-get-network-wxdomain/references/schemas/`
- `skills/uapi-get-random-image/`
- `skills/uapi-get-random-image/agents/`
- `skills/uapi-get-random-image/references/`
- `skills/uapi-get-random-image/references/operations/`
- `skills/uapi-get-random-image/references/resources/`
- `skills/uapi-get-random-image/references/schemas/`
- `skills/uapi-get-random-string/`
- `skills/uapi-get-random-string/agents/`
- `skills/uapi-get-random-string/references/`
- `skills/uapi-get-random-string/references/operations/`
- `skills/uapi-get-random-string/references/resources/`
- `skills/uapi-get-random-string/references/schemas/`
- `skills/uapi-get-saying/`
- `skills/uapi-get-saying/agents/`
- `skills/uapi-get-saying/references/`
- `skills/uapi-get-saying/references/operations/`
- `skills/uapi-get-saying/references/resources/`
- `skills/uapi-get-saying/references/schemas/`
- `skills/uapi-get-search-engines/`
- `skills/uapi-get-search-engines/agents/`
- `skills/uapi-get-search-engines/references/`
- `skills/uapi-get-search-engines/references/operations/`
- `skills/uapi-get-search-engines/references/resources/`
- `skills/uapi-get-search-engines/references/schemas/`
- `skills/uapi-get-sensitive-word-analyze-query/`
- `skills/uapi-get-sensitive-word-analyze-query/agents/`
- `skills/uapi-get-sensitive-word-analyze-query/references/`
- `skills/uapi-get-sensitive-word-analyze-query/references/operations/`
- `skills/uapi-get-sensitive-word-analyze-query/references/resources/`
- `skills/uapi-get-sensitive-word-analyze-query/references/schemas/`
- `skills/uapi-get-social-bilibili-archives/`
- `skills/uapi-get-social-bilibili-archives/agents/`
- `skills/uapi-get-social-bilibili-archives/references/`
- `skills/uapi-get-social-bilibili-archives/references/operations/`
- `skills/uapi-get-social-bilibili-archives/references/resources/`
- `skills/uapi-get-social-bilibili-archives/references/schemas/`
- `skills/uapi-get-social-bilibili-liveroom/`
- `skills/uapi-get-social-bilibili-liveroom/agents/`
- `skills/uapi-get-social-bilibili-liveroom/references/`
- `skills/uapi-get-social-bilibili-liveroom/references/operations/`
- `skills/uapi-get-social-bilibili-liveroom/references/resources/`
- `skills/uapi-get-social-bilibili-liveroom/references/schemas/`
- `skills/uapi-get-social-bilibili-replies/`
- `skills/uapi-get-social-bilibili-replies/agents/`
- `skills/uapi-get-social-bilibili-replies/references/`
- `skills/uapi-get-social-bilibili-replies/references/operations/`
- `skills/uapi-get-social-bilibili-replies/references/resources/`
- `skills/uapi-get-social-bilibili-replies/references/schemas/`
- `skills/uapi-get-social-bilibili-userinfo/`
- `skills/uapi-get-social-bilibili-userinfo/agents/`
- `skills/uapi-get-social-bilibili-userinfo/references/`
- `skills/uapi-get-social-bilibili-userinfo/references/operations/`
- `skills/uapi-get-social-bilibili-userinfo/references/resources/`
- `skills/uapi-get-social-bilibili-userinfo/references/schemas/`
- `skills/uapi-get-social-bilibili-videoinfo/`
- `skills/uapi-get-social-bilibili-videoinfo/agents/`
- `skills/uapi-get-social-bilibili-videoinfo/references/`
- `skills/uapi-get-social-bilibili-videoinfo/references/operations/`
- `skills/uapi-get-social-bilibili-videoinfo/references/resources/`
- `skills/uapi-get-social-bilibili-videoinfo/references/schemas/`
- `skills/uapi-get-social-qq-groupinfo/`
- `skills/uapi-get-social-qq-groupinfo/agents/`
- `skills/uapi-get-social-qq-groupinfo/references/`
- `skills/uapi-get-social-qq-groupinfo/references/operations/`
- `skills/uapi-get-social-qq-groupinfo/references/resources/`
- `skills/uapi-get-social-qq-groupinfo/references/schemas/`
- `skills/uapi-get-social-qq-userinfo/`
- `skills/uapi-get-social-qq-userinfo/agents/`
- `skills/uapi-get-social-qq-userinfo/references/`
- `skills/uapi-get-social-qq-userinfo/references/operations/`
- `skills/uapi-get-social-qq-userinfo/references/resources/`
- `skills/uapi-get-social-qq-userinfo/references/schemas/`
- `skills/uapi-get-status-ratelimit/`
- `skills/uapi-get-status-ratelimit/agents/`
- `skills/uapi-get-status-ratelimit/references/`
- `skills/uapi-get-status-ratelimit/references/operations/`
- `skills/uapi-get-status-ratelimit/references/resources/`
- `skills/uapi-get-status-ratelimit/references/schemas/`
- `skills/uapi-get-status-usage/`
- `skills/uapi-get-status-usage/agents/`
- `skills/uapi-get-status-usage/references/`
- `skills/uapi-get-status-usage/references/operations/`
- `skills/uapi-get-status-usage/references/resources/`
- `skills/uapi-get-status-usage/references/schemas/`
- `skills/uapi-get-text-md5/`
- `skills/uapi-get-text-md5/agents/`
- `skills/uapi-get-text-md5/references/`
- `skills/uapi-get-text-md5/references/operations/`
- `skills/uapi-get-text-md5/references/resources/`
- `skills/uapi-get-text-md5/references/schemas/`
- `skills/uapi-get-web-tomarkdown-async-status/`
- `skills/uapi-get-web-tomarkdown-async-status/agents/`
- `skills/uapi-get-web-tomarkdown-async-status/references/`
- `skills/uapi-get-web-tomarkdown-async-status/references/operations/`
- `skills/uapi-get-web-tomarkdown-async-status/references/resources/`
- `skills/uapi-get-web-tomarkdown-async-status/references/schemas/`
- `skills/uapi-get-webparse-extractimages/`
- `skills/uapi-get-webparse-extractimages/agents/`
- `skills/uapi-get-webparse-extractimages/references/`
- `skills/uapi-get-webparse-extractimages/references/operations/`
- `skills/uapi-get-webparse-extractimages/references/resources/`
- `skills/uapi-get-webparse-extractimages/references/schemas/`
- `skills/uapi-get-webparse-metadata/`
- `skills/uapi-get-webparse-metadata/agents/`
- `skills/uapi-get-webparse-metadata/references/`
- `skills/uapi-get-webparse-metadata/references/operations/`
- `skills/uapi-get-webparse-metadata/references/resources/`
- `skills/uapi-get-webparse-metadata/references/schemas/`
- `skills/uapi-post-ai-translate/`
- `skills/uapi-post-ai-translate/agents/`
- `skills/uapi-post-ai-translate/references/`
- `skills/uapi-post-ai-translate/references/operations/`
- `skills/uapi-post-ai-translate/references/resources/`
- `skills/uapi-post-ai-translate/references/schemas/`
- `skills/uapi-post-answerbook-ask/`
- `skills/uapi-post-answerbook-ask/agents/`
- `skills/uapi-post-answerbook-ask/references/`
- `skills/uapi-post-answerbook-ask/references/operations/`
- `skills/uapi-post-answerbook-ask/references/resources/`
- `skills/uapi-post-answerbook-ask/references/schemas/`
- `skills/uapi-post-clipzy-store/`
- `skills/uapi-post-clipzy-store/agents/`
- `skills/uapi-post-clipzy-store/references/`
- `skills/uapi-post-clipzy-store/references/operations/`
- `skills/uapi-post-clipzy-store/references/resources/`
- `skills/uapi-post-clipzy-store/references/schemas/`
- `skills/uapi-post-convert-json/`
- `skills/uapi-post-convert-json/agents/`
- `skills/uapi-post-convert-json/references/`
- `skills/uapi-post-convert-json/references/operations/`
- `skills/uapi-post-convert-json/references/resources/`
- `skills/uapi-post-convert-json/references/schemas/`
- `skills/uapi-post-image-compress/`
- `skills/uapi-post-image-compress/agents/`
- `skills/uapi-post-image-compress/references/`
- `skills/uapi-post-image-compress/references/operations/`
- `skills/uapi-post-image-compress/references/resources/`
- `skills/uapi-post-image-compress/references/schemas/`
- `skills/uapi-post-image-frombase64/`
- `skills/uapi-post-image-frombase64/agents/`
- `skills/uapi-post-image-frombase64/references/`
- `skills/uapi-post-image-frombase64/references/operations/`
- `skills/uapi-post-image-frombase64/references/resources/`
- `skills/uapi-post-image-frombase64/references/schemas/`
- `skills/uapi-post-image-motou/`
- `skills/uapi-post-image-motou/agents/`
- `skills/uapi-post-image-motou/references/`
- `skills/uapi-post-image-motou/references/operations/`
- `skills/uapi-post-image-motou/references/resources/`
- `skills/uapi-post-image-motou/references/schemas/`
- `skills/uapi-post-image-nsfw/`
- `skills/uapi-post-image-nsfw/agents/`
- `skills/uapi-post-image-nsfw/references/`
- `skills/uapi-post-image-nsfw/references/operations/`
- `skills/uapi-post-image-nsfw/references/resources/`
- `skills/uapi-post-image-nsfw/references/schemas/`
- `skills/uapi-post-image-speechless/`
- `skills/uapi-post-image-speechless/agents/`
- `skills/uapi-post-image-speechless/references/`
- `skills/uapi-post-image-speechless/references/operations/`
- `skills/uapi-post-image-speechless/references/resources/`
- `skills/uapi-post-image-speechless/references/schemas/`
- `skills/uapi-post-image-svg/`
- `skills/uapi-post-image-svg/agents/`
- `skills/uapi-post-image-svg/references/`
- `skills/uapi-post-image-svg/references/operations/`
- `skills/uapi-post-image-svg/references/resources/`
- `skills/uapi-post-image-svg/references/schemas/`
- `skills/uapi-post-misc-date-diff/`
- `skills/uapi-post-misc-date-diff/agents/`
- `skills/uapi-post-misc-date-diff/references/`
- `skills/uapi-post-misc-date-diff/references/operations/`
- `skills/uapi-post-misc-date-diff/references/resources/`
- `skills/uapi-post-misc-date-diff/references/schemas/`
- `skills/uapi-post-search-aggregate/`
- `skills/uapi-post-search-aggregate/agents/`
- `skills/uapi-post-search-aggregate/references/`
- `skills/uapi-post-search-aggregate/references/operations/`
- `skills/uapi-post-search-aggregate/references/resources/`
- `skills/uapi-post-search-aggregate/references/schemas/`
- `skills/uapi-post-sensitive-word-analyze/`
- `skills/uapi-post-sensitive-word-analyze/agents/`
- `skills/uapi-post-sensitive-word-analyze/references/`
- `skills/uapi-post-sensitive-word-analyze/references/operations/`
- `skills/uapi-post-sensitive-word-analyze/references/resources/`
- `skills/uapi-post-sensitive-word-analyze/references/schemas/`
- `skills/uapi-post-sensitive-word-quick-check/`
- `skills/uapi-post-sensitive-word-quick-check/agents/`
- `skills/uapi-post-sensitive-word-quick-check/references/`
- `skills/uapi-post-sensitive-word-quick-check/references/operations/`
- `skills/uapi-post-sensitive-word-quick-check/references/resources/`
- `skills/uapi-post-sensitive-word-quick-check/references/schemas/`
- `skills/uapi-post-text-aes-decrypt/`
- `skills/uapi-post-text-aes-decrypt/agents/`
- `skills/uapi-post-text-aes-decrypt/references/`
- `skills/uapi-post-text-aes-decrypt/references/operations/`
- `skills/uapi-post-text-aes-decrypt/references/resources/`
- `skills/uapi-post-text-aes-decrypt/references/schemas/`
- `skills/uapi-post-text-aes-decrypt-advanced/`
- `skills/uapi-post-text-aes-decrypt-advanced/agents/`
- `skills/uapi-post-text-aes-decrypt-advanced/references/`
- `skills/uapi-post-text-aes-decrypt-advanced/references/operations/`
- `skills/uapi-post-text-aes-decrypt-advanced/references/resources/`
- `skills/uapi-post-text-aes-decrypt-advanced/references/schemas/`
- `skills/uapi-post-text-aes-encrypt/`
- `skills/uapi-post-text-aes-encrypt/agents/`
- `skills/uapi-post-text-aes-encrypt/references/`
- `skills/uapi-post-text-aes-encrypt/references/operations/`
- `skills/uapi-post-text-aes-encrypt/references/resources/`
- `skills/uapi-post-text-aes-encrypt/references/schemas/`
- `skills/uapi-post-text-aes-encrypt-advanced/`
- `skills/uapi-post-text-aes-encrypt-advanced/agents/`
- `skills/uapi-post-text-aes-encrypt-advanced/references/`
- `skills/uapi-post-text-aes-encrypt-advanced/references/operations/`
- `skills/uapi-post-text-aes-encrypt-advanced/references/resources/`
- `skills/uapi-post-text-aes-encrypt-advanced/references/schemas/`
- `skills/uapi-post-text-analyze/`
- `skills/uapi-post-text-analyze/agents/`
- `skills/uapi-post-text-analyze/references/`
- `skills/uapi-post-text-analyze/references/operations/`
- `skills/uapi-post-text-analyze/references/resources/`
- `skills/uapi-post-text-analyze/references/schemas/`
- `skills/uapi-post-text-base64-decode/`
- `skills/uapi-post-text-base64-decode/agents/`
- `skills/uapi-post-text-base64-decode/references/`
- `skills/uapi-post-text-base64-decode/references/operations/`
- `skills/uapi-post-text-base64-decode/references/resources/`
- `skills/uapi-post-text-base64-decode/references/schemas/`
- `skills/uapi-post-text-base64-encode/`
- `skills/uapi-post-text-base64-encode/agents/`
- `skills/uapi-post-text-base64-encode/references/`
- `skills/uapi-post-text-base64-encode/references/operations/`
- `skills/uapi-post-text-base64-encode/references/resources/`
- `skills/uapi-post-text-base64-encode/references/schemas/`
- `skills/uapi-post-text-convert/`
- `skills/uapi-post-text-convert/agents/`
- `skills/uapi-post-text-convert/references/`
- `skills/uapi-post-text-convert/references/operations/`
- `skills/uapi-post-text-convert/references/resources/`
- `skills/uapi-post-text-convert/references/schemas/`
- `skills/uapi-post-text-md5/`
- `skills/uapi-post-text-md5/agents/`
- `skills/uapi-post-text-md5/references/`
- `skills/uapi-post-text-md5/references/operations/`
- `skills/uapi-post-text-md5/references/resources/`
- `skills/uapi-post-text-md5/references/schemas/`
- `skills/uapi-post-text-md5-verify/`
- `skills/uapi-post-text-md5-verify/agents/`
- `skills/uapi-post-text-md5-verify/references/`
- `skills/uapi-post-text-md5-verify/references/operations/`
- `skills/uapi-post-text-md5-verify/references/resources/`
- `skills/uapi-post-text-md5-verify/references/schemas/`
- `skills/uapi-post-translate-stream/`
- `skills/uapi-post-translate-stream/agents/`
- `skills/uapi-post-translate-stream/references/`
- `skills/uapi-post-translate-stream/references/operations/`
- `skills/uapi-post-translate-stream/references/resources/`
- `skills/uapi-post-translate-stream/references/schemas/`
- `skills/uapi-post-translate-text/`
- `skills/uapi-post-translate-text/agents/`
- `skills/uapi-post-translate-text/references/`
- `skills/uapi-post-translate-text/references/operations/`
- `skills/uapi-post-translate-text/references/resources/`
- `skills/uapi-post-translate-text/references/schemas/`
- `skills/uapi-post-web-tomarkdown-async/`
- `skills/uapi-post-web-tomarkdown-async/agents/`
- `skills/uapi-post-web-tomarkdown-async/references/`
- `skills/uapi-post-web-tomarkdown-async/references/operations/`
- `skills/uapi-post-web-tomarkdown-async/references/resources/`
- `skills/uapi-post-web-tomarkdown-async/references/schemas/`

</details>

下面按分类展开全部接口。每个接口都直接附上可以复制的 Vercel Skills CLI 安装命令。

### Misc

<details>
<summary>展开查看 Misc 分类下的 15 个接口</summary>

| 接口说明 | Skill | 接口 | 安装命令 |
| --- | --- | --- | --- |
| Adcode 国内外行政区域查询 | `uapi-get-misc-district` | `GET /misc/district` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-misc-district` |
| 查询世界时间 | `uapi-get-misc-worldtime` | `GET /misc/worldtime` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-misc-worldtime` |
| 查询农历时间 | `uapi-get-misc-lunartime` | `GET /misc/lunartime` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-misc-lunartime` |
| 查询天气 | `uapi-get-misc-weather` | `GET /misc/weather` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-misc-weather` |
| 查询快递物流信息 | `uapi-get-misc-tracking-query` | `GET /misc/tracking/query` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-misc-tracking-query` |
| 查询手机归属地 | `uapi-get-misc-phoneinfo` | `GET /misc/phoneinfo` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-misc-phoneinfo` |
| 查询热榜 | `uapi-get-misc-hotboard` | `GET /misc/hotboard` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-misc-hotboard` |
| 查询节假日与万年历 | `uapi-get-misc-holiday-calendar` | `GET /misc/holiday-calendar` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-misc-holiday-calendar` |
| 程序员历史上的今天 | `uapi-get-history-programmer-today` | `GET /history/programmer/today` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-history-programmer-today` |
| 程序员历史事件 | `uapi-get-history-programmer` | `GET /history/programmer` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-history-programmer` |
| 获取支持的快递公司列表 | `uapi-get-misc-tracking-carriers` | `GET /misc/tracking/carriers` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-misc-tracking-carriers` |
| 计算两个日期之间的时间差值 | `uapi-post-misc-date-diff` | `POST /misc/date-diff` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-misc-date-diff` |
| 识别快递公司 | `uapi-get-misc-tracking-detect` | `GET /misc/tracking/detect` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-misc-tracking-detect` |
| 转换时间戳 (旧版，推荐使用/convert/unixtime) | `uapi-get-misc-timestamp` | `GET /misc/timestamp` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-misc-timestamp` |
| 随机数生成 | `uapi-get-misc-randomnumber` | `GET /misc/randomnumber` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-misc-randomnumber` |

</details>

### Image

<details>
<summary>展开查看 Image 分类下的 11 个接口</summary>

| 接口说明 | Skill | 接口 | 安装命令 |
| --- | --- | --- | --- |
| SVG转图片 | `uapi-post-image-svg` | `POST /image/svg` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-image-svg` |
| 图片敏感检测 | `uapi-post-image-nsfw` | `POST /image/nsfw` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-image-nsfw` |
| 图片转 Base64 | `uapi-get-image-tobase64` | `GET /image/tobase64` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-image-tobase64` |
| 必应壁纸 | `uapi-get-image-bing-daily` | `GET /image/bing-daily` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-image-bing-daily` |
| 无损压缩图片 | `uapi-post-image-compress` | `POST /image/compress` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-image-compress` |
| 生成二维码 | `uapi-get-image-qrcode` | `GET /image/qrcode` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-image-qrcode` |
| 生成你们怎么不说话了表情包 | `uapi-post-image-speechless` | `POST /image/speechless` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-image-speechless` |
| 生成摸摸头GIF | `uapi-post-image-motou` | `POST /image/motou` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-image-motou` |
| 生成摸摸头GIF (QQ号) | `uapi-get-image-motou` | `GET /image/motou` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-image-motou` |
| 获取Gravatar头像 | `uapi-get-avatar-gravatar` | `GET /avatar/gravatar` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-avatar-gravatar` |
| 通过Base64编码上传图片 | `uapi-post-image-frombase64` | `POST /image/frombase64` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-image-frombase64` |

</details>

### Text

<details>
<summary>展开查看 Text 分类下的 11 个接口</summary>

| 接口说明 | Skill | 接口 | 安装命令 |
| --- | --- | --- | --- |
| AES 加密 | `uapi-post-text-aes-encrypt` | `POST /text/aes/encrypt` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-text-aes-encrypt` |
| AES 解密 | `uapi-post-text-aes-decrypt` | `POST /text/aes/decrypt` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-text-aes-decrypt` |
| AES高级加密 | `uapi-post-text-aes-encrypt-advanced` | `POST /text/aes/encrypt-advanced` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-text-aes-encrypt-advanced` |
| AES高级解密 | `uapi-post-text-aes-decrypt-advanced` | `POST /text/aes/decrypt-advanced` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-text-aes-decrypt-advanced` |
| Base64 编码 | `uapi-post-text-base64-encode` | `POST /text/base64/encode` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-text-base64-encode` |
| Base64 解码 | `uapi-post-text-base64-decode` | `POST /text/base64/decode` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-text-base64-decode` |
| MD5 哈希 | `uapi-get-text-md5` | `GET /text/md5` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-text-md5` |
| MD5 哈希 (POST) | `uapi-post-text-md5` | `POST /text/md5` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-text-md5` |
| MD5 校验 | `uapi-post-text-md5-verify` | `POST /text/md5/verify` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-text-md5-verify` |
| 文本分析 | `uapi-post-text-analyze` | `POST /text/analyze` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-text-analyze` |
| 格式转换 | `uapi-post-text-convert` | `POST /text/convert` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-text-convert` |

</details>

### Network

<details>
<summary>展开查看 Network 分类下的 10 个接口</summary>

| 接口说明 | Skill | 接口 | 安装命令 |
| --- | --- | --- | --- |
| Ping 主机 | `uapi-get-network-ping` | `GET /network/ping` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-network-ping` |
| Ping 我的 IP | `uapi-get-network-pingmyip` | `GET /network/pingmyip` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-network-pingmyip` |
| 执行DNS解析查询 | `uapi-get-network-dns` | `GET /network/dns` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-network-dns` |
| 查询 IP | `uapi-get-network-ipinfo` | `GET /network/ipinfo` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-network-ipinfo` |
| 查询域名ICP备案信息 | `uapi-get-network-icp` | `GET /network/icp` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-network-icp` |
| 查询域名的WHOIS注册信息 | `uapi-get-network-whois` | `GET /network/whois` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-network-whois` |
| 查询我的 IP | `uapi-get-network-myip` | `GET /network/myip` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-network-myip` |
| 检查URL的可访问性状态 | `uapi-get-network-urlstatus` | `GET /network/urlstatus` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-network-urlstatus` |
| 检查域名在微信中的访问状态 | `uapi-get-network-wxdomain` | `GET /network/wxdomain` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-network-wxdomain` |
| 端口扫描 | `uapi-get-network-portscan` | `GET /network/portscan` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-network-portscan` |

</details>

### Social

<details>
<summary>展开查看 Social 分类下的 8 个接口</summary>

| 接口说明 | Skill | 接口 | 安装命令 |
| --- | --- | --- | --- |
| 查询 B站投稿 | `uapi-get-social-bilibili-archives` | `GET /social/bilibili/archives` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-social-bilibili-archives` |
| 查询 B站用户 | `uapi-get-social-bilibili-userinfo` | `GET /social/bilibili/userinfo` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-social-bilibili-userinfo` |
| 查询 B站直播间 | `uapi-get-social-bilibili-liveroom` | `GET /social/bilibili/liveroom` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-social-bilibili-liveroom` |
| 查询 B站视频 | `uapi-get-social-bilibili-videoinfo` | `GET /social/bilibili/videoinfo` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-social-bilibili-videoinfo` |
| 查询 B站评论 | `uapi-get-social-bilibili-replies` | `GET /social/bilibili/replies` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-social-bilibili-replies` |
| 查询 GitHub 仓库 | `uapi-get-github-repo` | `GET /github/repo` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-github-repo` |
| 查询 QQ 信息 | `uapi-get-social-qq-userinfo` | `GET /social/qq/userinfo` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-social-qq-userinfo` |
| 查询 QQ 群信息 | `uapi-get-social-qq-groupinfo` | `GET /social/qq/groupinfo` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-social-qq-groupinfo` |

</details>

### Game

<details>
<summary>展开查看 Game 分类下的 5 个接口</summary>

| 接口说明 | Skill | 接口 | 安装命令 |
| --- | --- | --- | --- |
| Epic 免费游戏 | `uapi-get-game-epic-free` | `GET /game/epic-free` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-game-epic-free` |
| 查询 MC 曾用名 | `uapi-get-game-minecraft-historyid` | `GET /game/minecraft/historyid` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-game-minecraft-historyid` |
| 查询 MC 服务器 | `uapi-get-game-minecraft-serverstatus` | `GET /game/minecraft/serverstatus` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-game-minecraft-serverstatus` |
| 查询 MC 玩家 | `uapi-get-game-minecraft-userinfo` | `GET /game/minecraft/userinfo` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-game-minecraft-userinfo` |
| 查询 Steam 用户 | `uapi-get-game-steam-summary` | `GET /game/steam/summary` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-game-steam-summary` |

</details>

### Random

<details>
<summary>展开查看 Random 分类下的 4 个接口</summary>

| 接口说明 | Skill | 接口 | 安装命令 |
| --- | --- | --- | --- |
| 答案之书 | `uapi-get-answerbook-ask` | `GET /answerbook/ask` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-answerbook-ask` |
| 答案之书 (POST) | `uapi-post-answerbook-ask` | `POST /answerbook/ask` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-answerbook-ask` |
| 随机图片 | `uapi-get-random-image` | `GET /random/image` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-random-image` |
| 随机字符串 | `uapi-get-random-string` | `GET /random/string` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-random-string` |

</details>

### Translate

<details>
<summary>展开查看 Translate 分类下的 4 个接口</summary>

| 接口说明 | Skill | 接口 | 安装命令 |
| --- | --- | --- | --- |
| AI智能翻译 | `uapi-post-ai-translate` | `POST /ai/translate` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-ai-translate` |
| AI翻译配置 | `uapi-get-ai-translate-languages` | `GET /ai/translate/languages` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-ai-translate-languages` |
| 流式翻译（中英互译） | `uapi-post-translate-stream` | `POST /translate/stream` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-translate-stream` |
| 翻译 | `uapi-post-translate-text` | `POST /translate/text` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-translate-text` |

</details>

### WebParse

<details>
<summary>展开查看 WebParse 分类下的 4 个接口</summary>

| 接口说明 | Skill | 接口 | 安装命令 |
| --- | --- | --- | --- |
| 提取网页元数据 | `uapi-get-webparse-metadata` | `GET /webparse/metadata` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-webparse-metadata` |
| 提取网页图片 | `uapi-get-webparse-extractimages` | `GET /webparse/extractimages` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-webparse-extractimages` |
| 网页转 Markdown | `uapi-post-web-tomarkdown-async` | `POST /web/tomarkdown/async` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-web-tomarkdown-async` |
| 转换任务状态 | `uapi-get-web-tomarkdown-async-status` | `GET /web/tomarkdown/async/{task_id}` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-web-tomarkdown-async-status` |

</details>

### Clipzy 在线剪贴板

<details>
<summary>展开查看 Clipzy 在线剪贴板 分类下的 3 个接口</summary>

| 接口说明 | Skill | 接口 | 安装命令 |
| --- | --- | --- | --- |
| 步骤1：上传加密数据 | `uapi-post-clipzy-store` | `POST /api/store` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-clipzy-store` |
| 步骤2 (方法一): 获取加密数据 | `uapi-get-clipzy-get` | `GET /api/get` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-clipzy-get` |
| 步骤2 (方法二): 获取原始文本 | `uapi-get-clipzy-raw` | `GET /api/raw/{id}` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-clipzy-raw` |

</details>

### 敏感词识别

<details>
<summary>展开查看 敏感词识别 分类下的 3 个接口</summary>

| 接口说明 | Skill | 接口 | 安装命令 |
| --- | --- | --- | --- |
| 分析敏感词 | `uapi-post-sensitive-word-analyze` | `POST /sensitive-word/analyze` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-sensitive-word-analyze` |
| 敏感词分析 (GET) | `uapi-get-sensitive-word-analyze-query` | `GET /sensitive-word/analyze-query` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-sensitive-word-analyze-query` |
| 敏感词检测（快速） | `uapi-post-sensitive-word-quick-check` | `POST /text/profanitycheck` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-sensitive-word-quick-check` |

</details>

### Convert

<details>
<summary>展开查看 Convert 分类下的 2 个接口</summary>

| 接口说明 | Skill | 接口 | 安装命令 |
| --- | --- | --- | --- |
| JSON 格式化 | `uapi-post-convert-json` | `POST /convert/json` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-convert-json` |
| 时间戳转换 | `uapi-get-convert-unixtime` | `GET /convert/unixtime` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-convert-unixtime` |

</details>

### Status

<details>
<summary>展开查看 Status 分类下的 2 个接口</summary>

| 接口说明 | Skill | 接口 | 安装命令 |
| --- | --- | --- | --- |
| 获取API端点使用统计 | `uapi-get-status-usage` | `GET /status/usage` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-status-usage` |
| 限流状态 | `uapi-get-status-ratelimit` | `GET /status/ratelimit` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-status-ratelimit` |

</details>

### 智能搜索

<details>
<summary>展开查看 智能搜索 分类下的 2 个接口</summary>

| 接口说明 | Skill | 接口 | 安装命令 |
| --- | --- | --- | --- |
| 搜索引擎配置 | `uapi-get-search-engines` | `GET /search/engines` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-search-engines` |
| 智能搜索 | `uapi-post-search-aggregate` | `POST /search/aggregate` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-post-search-aggregate` |

</details>

### Daily

<details>
<summary>展开查看 Daily 分类下的 1 个接口</summary>

| 接口说明 | Skill | 接口 | 安装命令 |
| --- | --- | --- | --- |
| 每日新闻图 | `uapi-get-daily-news-image` | `GET /daily/news-image` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-daily-news-image` |

</details>

### Poem

<details>
<summary>展开查看 Poem 分类下的 1 个接口</summary>

| 接口说明 | Skill | 接口 | 安装命令 |
| --- | --- | --- | --- |
| 一言 | `uapi-get-saying` | `GET /saying` | `npx skills add AxT-Team/uapi-agent-skills --skill uapi-get-saying` |

</details>
