# 爆款帖文分析 · Post Virality Analysis

[English](README.en.md) · [技能说明](skills/post-viral-analysis/SKILL.md) · [MIT License](LICENSE)

**发一个 X 或其他主流平台的帖文链接，让 AI 助手解释：哪些内容吸引人，哪些证据支持流量来源，哪些原因还只是推测。**

适合分析推文、长帖、社交图文、平台文章和帖子。它会读原文、查看可访问的配图、记录可见指标，再把具体证据与传播机制联系起来。

## 介绍与用途

- **创作者**：拆解开头、标题、观点、故事、信息价值和表达方式。
- **营销与运营人员**：研究评论、收藏、转发的可能动机，区分内容表现与传播渠道。
- **品牌与研究者**：判断互动来自认同、争议还是其他因素，识别证据缺口。
- **学习者**：学习值得参考的写作方法，避免把大数字直接归因于“算法喜欢”。

报告通常包含：一句话结论、原帖与数据快照、三到五条主要原因、证据与推测对照表、可参考的方法，以及仍需验证的问题。

每条原因都应有原文片段或已检查的视觉证据，而不是“文案好、有共鸣、标题吸引人”这类笼统标签。

## 哪些平台可以用

目标包括 **X / Twitter、LinkedIn、Threads、Facebook、Instagram、Reddit、微博、小红书、知乎和微信公众号**，以及其他可读的社交内容页。

读取能力取决于 AI 助手的浏览器、联网工具、现有账号访问权限和平台页面状态。这个技能不会保证所有平台、所有帖子都能直接读取。

- 可读的原帖：优先分析完整正文、可查看媒体和实际显示的指标。
- 页面需要现有登录：使用助手具备的授权浏览器或平台连接器。
- X 正常页面无法读取：可以尝试随附的官方公开嵌入读取工具，取得部分正文与署名。
- 链接仍不可读：明确说明缺失内容，使用用户提供的正文、截图或分析后台数据，不编造结果。

## 安装

在 Codex 中发送：

```text
用 $skill-installer 安装这个技能：
https://github.com/yycczq/post-viral-analysis/tree/main/skills/post-viral-analysis
```

安装后通过 `$post-viral-analysis` 调用。若未出现在列表里，重启 Codex；安装方式见 [OpenAI 官方技能文档](https://learn.chatgpt.com/docs/build-skills)。

也可以手动复制到自己的项目。macOS / Linux：

```sh
git clone https://github.com/yycczq/post-viral-analysis.git
mkdir -p /path/to/your-project/.agents/skills
cp -R post-viral-analysis/skills/post-viral-analysis /path/to/your-project/.agents/skills/
```

Windows PowerShell：

```powershell
git clone https://github.com/yycczq/post-viral-analysis.git
New-Item -ItemType Directory -Force -Path "C:\your-project\.agents\skills"
Copy-Item -Recurse "post-viral-analysis\skills\post-viral-analysis" "C:\your-project\.agents\skills\"
```

将路径替换为自己的项目目录，在该项目中打开 Codex。其他支持 Agent Skills 的助手可按各自的安装方式使用；需要网页读取能力，分析图片时还需要图像理解能力，其他客户端未逐一实测。

## 怎么使用

### 发一个链接

```text
用 $post-viral-analysis 分析这条帖文为何流量这么多：
【粘贴实际链接】
给出原文证据，区分内容吸引力、传播因素和未知项。
```

### 深入分析

```text
用 $post-viral-analysis 分析这个链接：
【粘贴实际链接】
重点拆解第一句、信息价值、情绪和转发动机。
如果原帖显示了浏览量、点赞、评论或转发，请分别记录并标注观察日期。
把完整报告保存为 POST_ANALYSIS.md。
```

### 比较两条帖文

```text
用 $post-viral-analysis 比较这两个链接：
【链接一】
【链接二】
分别核对内容和可见指标，考虑账号、发布时间和帖文年龄的差异。
解释哪些写作方式值得学习，不把互动数直接当成阅读量。
```

### 有自己的后台数据

```text
用 $post-viral-analysis 分析这个链接：
【粘贴实际链接】
我提供的截图是该帖文发布后 24 小时的分析后台。
请将后台数据与当前公开页面分别标注，讨论它们能支持哪些原因。
```

正文、指标与评论的来源和日期会分别记录。缺少指标时，助手可以分析内容的潜在吸引力，但必须明确“实际高流量尚未核实”。

## X 正文读取工具

正常使用主要依赖助手现有的网页读取能力。随附工具只是 X 公共正文的备用读取方式，使用 **Python 3.10+ 标准库**，无额外 Python 依赖，也不需要 X API key：

```sh
python3 skills/post-viral-analysis/scripts/fetch_x_embed.py \
  "https://x.com/jack/status/20" --out post-analysis-results/x-snapshot.json
```

这是读取验证用的公开示例帖，不是爆款分析样例。实际使用时替换为你的 X / Twitter 帖文链接。Windows 可以使用 `python` 或 `py`；技能安装在别处时使用实际技能目录。

它请求 [X 官方公开 oEmbed 接口](https://docs.x.com/x-for-websites/oembed-api)，保存：

- 请求链接、返回的原帖链接、帖文 ID 和读取时间。
- 嵌入正文段落、署名、正文中的链接和原始响应。
- 明确的读取范围与未知项。

**它不会取得可靠的实时浏览量、点赞或转发量，也不保证包含全文、整个串帖或媒体内容。** 这些字段保持未知，不会填成零。正文里的链接不会被自动打开，返回的网页脚本也不会执行。已有快照文件不会覆盖。

单独运行工具只得到正文证据；“为什么流量多”的报告由 AI 助手检查证据后完成。其他平台使用助手已有的读取工具，没有附带通用爬虫。

## 分析原则

| 问题 | 技能如何处理 |
| --- | --- |
| 什么内容吸引人？ | 用具体措辞、结构、信息或已检查的图片解释。 |
| 真有很多流量吗？ | 记录显示出来的指标；缺失则标注未知。 |
| 为什么传播？ | 将有证据的账号、热点、引用或转发路径与内容假设分开。 |
| 算法、投放或刷量导致的吗？ | 不能仅凭大数字下结论；有来源才讨论。 |
| 能照着做出同样效果吗？ | 给可参考的方法，不承诺复制流量。 |

不同指标不混用；当前粉丝数不直接当成发布时受众数；少量热门评论不代表全部观众。X 的浏览量也不等于独立人数，参见 [X 官方指标说明](https://help.x.com/en/using-x/view-counts)。

技能不自动发帖、点赞、转发、关注或私信。分析使用你现有的 AI 助手及模型服务；隐私处理与费用取决于该服务。本项目不另行调用模型 API。

## 验证与许可

```sh
python3 -m unittest discover -s tests -v
```

6 项测试覆盖链接身份、错误来源、返回内容归属、正文与脚本/页脚区分、未知指标及快照保留。测试不需要登录、网络或第三方包。

开发时还用真实公开 X 帖文验证了官方嵌入读取路径。没有对全部平台或全部帖文做读取保证，也没有验证“预测爆款”的准确率。跨平台测试状态可在仓库 Actions 查看。

欢迎通过 Issue / Pull Request 提交反馈。公开复现材料请只包含可以公开分享的内容。

[MIT License](LICENSE) 允许使用、修改和分发。安装用的技能目录也包含完整许可。
