# Post Virality Analysis

[中文](README.md) · [Skill](skills/post-viral-analysis/SKILL.md) · [MIT License](LICENSE)

**Share a social-post link and ask an AI agent what makes it attract attention, what evidence supports its distribution, and what remains unknown.**

An Agent Skill for creators, marketers, editors and researchers. It connects actual wording, inspected media and visible metrics to content appeal and plausible sharing motives. It also considers account reach, timing, topical attention and observable amplification without inventing causes.

## Platforms and access

Targets include X/Twitter, LinkedIn, Threads, Facebook, Instagram, Reddit, Weibo, Xiaohongshu, Zhihu, WeChat articles and other readable social pages. Access depends on your agent's browsing tools, authorized sessions and the page itself. Compatibility is not a promise that every post can be fetched.

The agent reads the selected original, expands available text, inspects accessible media and snapshots visible metrics. If access fails, it can use a clearly labeled partial source or user-provided text/screenshots. An optional official X oEmbed helper supplies embedded text, not verified full content or live engagement counts.

## Install in Codex

```text
Use $skill-installer to install:
https://github.com/yycczq/post-viral-analysis/tree/main/skills/post-viral-analysis
```

Alternatively clone this repository and copy `skills/post-viral-analysis` into your project's `.agents/skills/`. Open Codex in that project. If the skill does not appear, restart Codex. See the [official skills guide](https://learn.chatgpt.com/docs/build-skills).

Other Agent Skills hosts can follow their own installation convention. Browsing access is required; visual evidence needs image-understanding tools. Other client integrations have not been individually tested.

## Use it

```text
Use $post-viral-analysis to analyze why this post received so much attention:
[paste the actual link]
Use concrete excerpts and sources. Separate content appeal, distribution evidence and hypotheses.
```

For a deeper report, ask it to record available metrics and the observation date, then save `POST_ANALYSIS.md`. Supply owner analytics or metric screenshots with their period and source if available. If file output is unavailable, the agent delivers the report inline.

The report leads with the strongest supported explanation, then includes the post's identity and metric snapshot, three to five evidence-based reasons, a compact evidence/hypothesis table, useful creative techniques and remaining questions. With no readable metrics, actual high traffic remains unverified.

## Optional X helper

Requires Python 3.10+ and network access; no third-party Python dependency or X API key:

```sh
python3 skills/post-viral-analysis/scripts/fetch_x_embed.py \
  "https://x.com/jack/status/20" --out post-analysis-results/x-snapshot.json
```

This public URL is a reading test, not a sample causal analysis. Replace it with your selected X/Twitter status. Windows may use `python` or `py`.

The helper uses the [official public oEmbed API](https://docs.x.com/x-for-websites/oembed-api), validates the returned post identity, saves attribution, paragraphs, links and the raw response, and keeps all traffic metrics unknown. It does not execute widget scripts, follow embedded links or overwrite existing files.

An embed does not establish long-post, media or thread completeness. Running the helper alone does not create a semantic report; the agent must inspect the evidence. Other platforms use the host's existing browsing capabilities.

## Interpretation limits

Views, likes, comments, reposts, saves and votes remain separate. Missing metrics are not zeros. A large count cannot prove organic distribution, recommendations, paid promotion, bots, conversion or revenue. X views are not unique-person counts; see [the official definition](https://help.x.com/en/using-x/view-counts).

Comparisons require relevant account, format and publication-age context. A few prominent comments are a sample, not a representative survey. The skill offers explanations and transferable techniques, not a validated predictor or a guarantee that copying a format reproduces its traffic.

It never automatically posts, likes, follows, reposts or sends messages. Interpretation uses your existing agent/model service and follows its privacy and billing arrangements. No additional model API integration is bundled.

## Tests and license

```sh
python3 -m unittest discover -s tests -v
```

Six offline tests exercise URL identity, source rejection, response ownership, HTML text handling, unknown metrics and preservation of Unicode snapshot files. A real public X post was separately used to verify the embed-reading path. No blanket platform-access or virality-prediction accuracy claim is made.

Issues and pull requests are welcome. Share only reproducible material that can be made public.

Released under the [MIT License](LICENSE), also included in the installable skill folder.
