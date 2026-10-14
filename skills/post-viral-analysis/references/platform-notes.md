# Platform reading notes

Use these as routing questions, not guarantees that a site will remain publicly readable. Layouts, counters and access rules change. Prefer an available authorized connector or normal browser reading of the actual selected item.

| Target | What to verify |
| --- | --- |
| X / Twitter | Exact status ID and author; expand readable long text; separate one post from a thread, quote and replies. View, reply, repost and like counts are different facts. |
| LinkedIn | Selected post versus a linked article or profile; full expanded text; observable reactions/comments/reposts; inaccessible analytics remain unknown. |
| Threads, Facebook, Instagram | Resolve the share link to the actual post; inspect carousel pages when relevant; distinguish text/caption, image, reel and account counts. Existing access may be necessary. |
| Reddit | Read the selected submission and context; preserve interface labels such as score and comments; neither is a view count. Sorted comments are a sample. |
| 微博 | Read the original post, expanded content and media; distinguish original metrics from repost commentary and topic-page metrics. |
| 小红书 | Resolve a share link normally to the selected note; inspect title, body and available image pages; visible likes/saves/comments do not establish impressions. |
| 知乎 | Distinguish question, selected answer and article; do not assign an entire question's attention to one answer. Preserve the displayed metric labels. |
| 微信公众号 | Read the actual article; public text and article analytics can have different availability. Use screenshots or owner-provided analytics only with source/date labels. |
| Other readable social pages | Identify the item and metric definitions before analyzing; unsupported access is not a reason to manufacture facts. |

## X fallback

The helper requests the official [public oEmbed API](https://docs.x.com/x-for-websites/oembed-api), retaining the response as data. It does not execute the returned widget JavaScript, access account cookies, use a paid API key or fetch links contained in the post.

An embed is a partial reading surface. Its paragraphs can omit long-form continuation, media details, context and all current interaction counts. The helper explicitly marks full-text completeness as unverified. Use a readable original page for those gaps or state them.

The [X view-count help page](https://help.x.com/en/using-x/view-counts) explains that repeated views can count, an author's own views can count, and promoted posts can show views. Thus a visible view count is not a unique-person count and cannot prove organic traffic. Older or other post types may lack this field. Check the current definition when using it.

## Links and snapshots

Keep the requested URL and final item URL. Remove tracking parameters only after identifying the actual item; do not accidentally discard a required share-link parameter. A quoted post, parent reply, author's current profile and news coverage are separately identified sources.

Preserve compact labels (`1.2M`, `3.4万`, `10K+`) as displayed. If an interpretation requires numeric conversion, document the unit and rounding or lower-bound ambiguity. A screenshot's date is not the live page's observation date.

Search-result excerpts and platform embeds can provide text while failing to establish metrics or completeness. The report should reflect that difference rather than call every successful fetch a complete analysis.
