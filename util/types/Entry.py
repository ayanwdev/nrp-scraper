from dataclasses import dataclass


@dataclass
class Entry:
  id: str
  title: str
  link: str
  published_at: str
  updated_at: str
  authors: list[str]
  tags: list[str]


def parse_entry(entry) -> Entry:
  return Entry(
    id=entry.get("id", ""),
    title=entry.get("title", ""),
    link=entry.get("link", ""),
    published_at=entry.get("published", ""),
    updated_at=entry.get("updated", ""),
    authors=[a["name"] for a in entry.get("authors", [])],
    tags=[t["term"] for t in entry.get("tags", [])],
  )
