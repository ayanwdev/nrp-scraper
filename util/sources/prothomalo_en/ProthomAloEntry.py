from dataclasses import dataclass
from feedparser import FeedParserDict


@dataclass
class ProthomAloEntry:
  id: str
  title: str
  link: str
  published_at: str
  updated_at: str
  authors: list[str]
  tags: list[str]


def parse_entry(entry: FeedParserDict) -> ProthomAloEntry:
  return ProthomAloEntry(
    id=str(entry.get("id", "")),
    title=str(entry.get("title", "")),
    link=str(entry.get("link", "")),
    published_at=str(entry.get("published", "")),
    updated_at=str(entry.get("updated", "")),
    authors=[str(a["name"]) for a in (entry.get("authors") or [])],
    tags=[str(t["term"]) for t in (entry.get("tags") or [])],
  )
