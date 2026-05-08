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

# Each article is (output_path_relative_to_repo, title, source_url).
# The output path determines both the Markdown destination and the per-article
# image directory: images live next to the file under <parent>/images/<stem>/.
ARTICLES = [
    ("protocol/01-overview.md", "Overview", "https://hub.nolus.io/en/articles/9680214-overview"),
    ("protocol/02-borrow.md", "Borrow", "https://hub.nolus.io/en/articles/9680324-borrow"),
    ("protocol/03-lend.md", "Lend", "https://hub.nolus.io/en/articles/9680477-lend"),
    ("protocol/04-oracles-alarms.md", "Oracles & Alarms", "https://hub.nolus.io/en/articles/9680497-oracles-alarms"),
    ("protocol/05-interest-profit.md", "Interest & Profit", "https://hub.nolus.io/en/articles/9680486-interest-profit"),
    ("protocol/06-liquidations-risk.md", "Liquidations & Risk Framework", "https://hub.nolus.io/en/articles/11378238-liquidations-risk-framework"),
    ("protocol/07-security.md", "Security", "https://hub.nolus.io/en/articles/9680739-security"),
    ("operators/pirin-mainnet.md", "Pirin (Mainnet) Services", "https://hub.nolus.io/en/articles/9680543-pirin-mainnet-services"),
    ("operators/rila-testnet.md", "Rila (Testnet) Services", "https://hub.nolus.io/en/articles/9685743-rila-testnet-services"),
    ("agentic-workflows/README.md", "MCP Server", "https://hub.nolus.io/en/articles/14005928-mcp-server"),
]

REPO_ROOT = Path(__file__).resolve().parent.parent


def fetch(url: str) -> str:
    r = requests.get(url, timeout=30, headers={"User-Agent": "nolus-gitbook-importer/1.0"})
    r.raise_for_status()
    return r.text


def download_image(src: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    r = requests.get(src, timeout=60, headers={"User-Agent": "nolus-gitbook-importer/1.0"})
    r.raise_for_status()
    dest.write_bytes(r.content)


def localize_images(soup_body, image_dir: Path, image_slug: str) -> None:
    """Download every <img> inside the body and rewrite its src to a local path."""
    for img in soup_body.select("img"):
        src = img.get("src")
        if not src or src.startswith("data:"):
            continue
        # Derive a filename from the URL path; ignore the query string (signed-URL noise).
        path = urlparse(src).path
        name = Path(path).name or "image"
        local_rel = f"images/{image_slug}/{name}"
        local_abs = image_dir / name
        try:
            download_image(src, local_abs)
        except Exception as exc:
            print(f"    warn: failed to download {src}: {exc}", flush=True)
            continue
        img["src"] = local_rel
        if img.has_attr("srcset"):
            del img["srcset"]


def extract_body(html: str, image_dir: Path, image_slug: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    body = soup.select_one("div.article_body") or soup.select_one("article")
    if body is None:
        raise RuntimeError("article body not found")
    for tag in body.select("script, style, noscript"):
        tag.decompose()
    localize_images(body, image_dir, image_slug)
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
    for rel_path, title, url in ARTICLES:
        out_file = REPO_ROOT / rel_path
        out_file.parent.mkdir(parents=True, exist_ok=True)
        image_slug = out_file.stem
        image_dir = out_file.parent / "images" / image_slug
        print(f"  fetching {title} -> {rel_path} ...", flush=True)
        html = fetch(url)
        body_html = extract_body(html, image_dir, image_slug)
        md = markdownify(body_html, heading_style="ATX", bullets="-")
        md = clean_md(md)
        front = f"# {title}\n\n_Source: {url}_\n\n"
        out_file.write_text(front + md, encoding="utf-8")
        time.sleep(0.5)
    print(f"wrote {len(ARTICLES)} articles")
    return 0


if __name__ == "__main__":
    sys.exit(main())
