#!/usr/bin/env python3
"""Scrape the Nolus tech-documentation Intercom collection to Markdown.

Downloads inline images locally so the docs stay self-contained after
Intercom's signed URLs expire.
"""
from __future__ import annotations

import re
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify

ARTICLES = [
    ("01-overview", "Overview", "https://hub.nolus.io/en/articles/9680214-overview"),
    ("02-borrow", "Borrow", "https://hub.nolus.io/en/articles/9680324-borrow"),
    ("03-lend", "Lend", "https://hub.nolus.io/en/articles/9680477-lend"),
    ("04-oracles-alarms", "Oracles & Alarms", "https://hub.nolus.io/en/articles/9680497-oracles-alarms"),
    ("05-interest-profit", "Interest & Profit", "https://hub.nolus.io/en/articles/9680486-interest-profit"),
    ("06-liquidations-risk", "Liquidations & Risk Framework", "https://hub.nolus.io/en/articles/11378238-liquidations-risk-framework"),
    ("07-security", "Security", "https://hub.nolus.io/en/articles/9680739-security"),
    ("08-pirin-mainnet", "Pirin (Mainnet) Services", "https://hub.nolus.io/en/articles/9680543-pirin-mainnet-services"),
    ("09-rila-testnet", "Rila (Testnet) Services", "https://hub.nolus.io/en/articles/9685743-rila-testnet-services"),
    ("10-mcp-server", "MCP Server", "https://hub.nolus.io/en/articles/14005928-mcp-server"),
]

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = REPO_ROOT / "protocol"
IMG_DIR = OUT_DIR / "images"


def fetch(url: str) -> str:
    r = requests.get(url, timeout=30, headers={"User-Agent": "nolus-gitbook-importer/1.0"})
    r.raise_for_status()
    return r.text


def download_image(src: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    r = requests.get(src, timeout=60, headers={"User-Agent": "nolus-gitbook-importer/1.0"})
    r.raise_for_status()
    dest.write_bytes(r.content)


def localize_images(soup_body, slug: str) -> None:
    """Download every <img> inside the body and rewrite its src to a local path."""
    for img in soup_body.select("img"):
        src = img.get("src")
        if not src or src.startswith("data:"):
            continue
        # Derive a filename from the URL path; ignore the query string (signed-URL noise).
        path = urlparse(src).path
        name = Path(path).name or "image"
        local_rel = f"images/{slug}/{name}"
        local_abs = OUT_DIR / "images" / slug / name
        try:
            download_image(src, local_abs)
        except Exception as exc:
            print(f"    warn: failed to download {src}: {exc}", flush=True)
            continue
        img["src"] = local_rel
        # Drop srcset — it would still point at the remote CDN.
        if img.has_attr("srcset"):
            del img["srcset"]


def extract_body(html: str, slug: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    body = soup.select_one("div.article_body") or soup.select_one("article")
    if body is None:
        raise RuntimeError("article body not found")
    for tag in body.select("script, style, noscript"):
        tag.decompose()
    localize_images(body, slug)
    return str(body)


def strip_related_articles(md: str) -> str:
    """Drop the trailing 'Related Articles' block Intercom appends to every page."""
    pattern = re.compile(r"\n-{3,}\s*\n+\s*Related Articles\s*\n.*\Z", re.DOTALL)
    return pattern.sub("", md)


def clean_md(md: str) -> str:
    md = strip_related_articles(md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip() + "\n"


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for slug, title, url in ARTICLES:
        print(f"  fetching {title} ...", flush=True)
        html = fetch(url)
        body_html = extract_body(html, slug)
        md = markdownify(body_html, heading_style="ATX", bullets="-")
        md = clean_md(md)
        front = f"# {title}\n\n_Source: {url}_\n\n"
        (OUT_DIR / f"{slug}.md").write_text(front + md, encoding="utf-8")
        time.sleep(0.5)
    print(f"wrote {len(ARTICLES)} files to {OUT_DIR}")
    print(f"images saved under {IMG_DIR}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
