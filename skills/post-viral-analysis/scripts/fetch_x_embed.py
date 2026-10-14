#!/usr/bin/env python3
"""Read a public X post through official oEmbed; never infer its traffic metrics."""
import argparse
from datetime import datetime, timezone
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlencode, urlsplit
from urllib.request import Request, urlopen

ALLOWED_HOSTS = {"x.com", "www.x.com", "mobile.x.com", "twitter.com", "www.twitter.com", "mobile.twitter.com"}
ENDPOINT = "https://publish.x.com/oembed"
MAX_RESPONSE_BYTES = 512 * 1024


def post_identity(url):
    parsed = urlsplit(url)
    if parsed.scheme not in {"http", "https"} or parsed.hostname not in ALLOWED_HOSTS or parsed.username or parsed.password or parsed.port is not None:
        raise ValueError("Provide a normal X/Twitter post URL, not a profile, proxy or authenticated URL")
    match = re.fullmatch(r"/(?:[A-Za-z0-9_]+/status|i/web/status|i/status)/([0-9]+)(?:/(?:photo|video)/[0-9]+)?/?", parsed.path)
    if not match or int(match[1]) <= 0:
        raise ValueError("URL must identify a specific X/Twitter status")
    post_id = match[1]
    base = re.sub(r"/(?:photo|video)/[0-9]+/?$", "", parsed.path).rstrip("/")
    return post_id, f"https://x.com{base}"


class EmbedText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.paragraphs = []
        self.links = []
        self.chunks = None
        self.ignored = 0

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style"}:
            self.ignored += 1
        if self.ignored:
            return
        if tag == "p":
            self.chunks = []
        elif tag == "br" and self.chunks is not None:
            self.chunks.append("\n")
        elif tag == "a":
            href = dict(attrs).get("href")
            if href:
                self.links.append(href)

    def handle_endtag(self, tag):
        if tag in {"script", "style"}:
            self.ignored = max(0, self.ignored - 1)
        if not self.ignored and tag == "p" and self.chunks is not None:
            self.paragraphs.append("".join(self.chunks).strip())
            self.chunks = None

    def handle_data(self, data):
        if not self.ignored and self.chunks is not None:
            self.chunks.append(data)


def snapshot_from_response(requested_url, response, retrieved_at):
    expected_id, canonical_requested_url = post_identity(requested_url)
    if not isinstance(response, dict) or not isinstance(response.get("url"), str) or not isinstance(response.get("html"), str):
        raise ValueError("oEmbed did not return a post URL and HTML")
    observed_id, observed_url = post_identity(response["url"])
    if expected_id != observed_id:
        raise ValueError("oEmbed returned a different status; discard this response")
    parser = EmbedText()
    parser.feed(response["html"])
    paragraphs = [p for p in parser.paragraphs if p]
    if not paragraphs:
        raise ValueError("No readable embedded paragraphs; inspect the original page instead")
    return {
        "schema": "post-viral-evidence/1",
        "source": {"kind": "official_public_oembed", "requested_url": requested_url,
                   "canonical_requested_url": canonical_requested_url, "observed_url": observed_url,
                   "post_id": observed_id, "endpoint": ENDPOINT, "retrieved_at": retrieved_at},
        "post": {"author_name": response.get("author_name"), "author_url": response.get("author_url"),
                 "embedded_paragraphs": paragraphs, "embedded_links": parser.links,
                 "full_text_completeness": "unverified", "media_inspected": False, "thread_complete": False},
        "metrics": {"status": "not_available_from_this_source", "views": None, "likes": None,
                    "replies": None, "reposts": None, "quotes": None, "saves": None},
        "raw_response": response,
        "limitations": ["An embed does not establish full text, media or thread completeness.",
                        "No live metrics or causal explanation were obtained; null is unknown, not zero."]}


def fetch(url):
    _, canonical = post_identity(url)
    endpoint_url = ENDPOINT + "?" + urlencode({"url": canonical, "omit_script": "true", "dnt": "true"})
    request = Request(endpoint_url, headers={"User-Agent": "post-viral-analysis/1.0", "Accept": "application/json"})
    with urlopen(request, timeout=20) as response:
        if urlsplit(response.geturl()).hostname not in {"publish.x.com", "publish.twitter.com"}:
            raise ValueError("Unexpected endpoint redirect; use the original page")
        raw = response.read(MAX_RESPONSE_BYTES + 1)
        if len(raw) > MAX_RESPONSE_BYTES:
            raise ValueError("Embed response exceeds the local size limit; use browser reading")
    return snapshot_from_response(url, json.loads(raw.decode("utf-8")), datetime.now(timezone.utc).isoformat())


def save_snapshot(snapshot, path):
    text = json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n"
    path = Path(path).expanduser()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as stream:
        stream.write(text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    parser.add_argument("--out", help="New JSON file; existing files are not overwritten")
    args = parser.parse_args()
    try:
        if args.out and Path(args.out).expanduser().exists():
            raise ValueError("Output exists; select a new snapshot file")
        snapshot = fetch(args.url)
        if args.out:
            save_snapshot(snapshot, args.out)
            print(json.dumps({"status": "text_snapshot_ready_metrics_unknown", "output": args.out}))
        else:
            print(json.dumps(snapshot))
    except (ValueError, OSError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
