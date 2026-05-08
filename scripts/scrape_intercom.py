#!/usr/bin/env python3
"""Scrape the Nolus tech-documentation Intercom collection to Markdown."""
from __future__ import annotations

import re
import sys
import time
from pathlib import Path

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

OUT_DIR = Path(__file__).resolve().parent.parent / "protocol"


def fetch(url: str) -> str:
    r = requests.get(url, timeout=30, headers={"User-Agent": "nolus-gitbook-importer/1.0"})
    r.raise_for_status()
    return r.text


def extract_body(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    body = soup.select_one("div.article_body") or soup.select_one("article")
    if body is None:
        raise RuntimeError("article body not found")
    for tag in body.select("script, style, noscript"):
        tag.decompose()
    return str(body)


def clean_md(md: str) -> str:
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip() + "\n"


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for slug, title, url in ARTICLES:
        print(f"  fetching {title} ...", flush=True)
        html = fetch(url)
        body_html = extract_body(html)
        md = markdownify(body_html, heading_style="ATX", bullets="-")
        md = clean_md(md)
        front = f"# {title}\n\n_Source: {url}_\n\n"
        (OUT_DIR / f"{slug}.md").write_text(front + md, encoding="utf-8")
        time.sleep(0.5)
    print(f"wrote {len(ARTICLES)} files to {OUT_DIR}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
