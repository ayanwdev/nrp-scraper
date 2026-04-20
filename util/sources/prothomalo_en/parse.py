from feedparser import parse
from util.sources.prothomalo_en.ProthomAloEntry import ProthomAloEntry
from util.sources.prothomalo_en.ProthomAloEntry import parse_entry


def parse_rss(xml: str) -> list[ProthomAloEntry]:
  feed = parse(xml)
  res = [parse_entry(entry) for entry in feed.entries]
  print(res[0])

  return res
