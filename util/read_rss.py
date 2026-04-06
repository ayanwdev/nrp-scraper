from feedparser import parse
from util.types.Entry import Entry, parse_entry

def read_rss(xml: str) -> list[Entry]:
    feed = parse(xml)
    return [parse_entry(e) for e in feed.entries]