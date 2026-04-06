from util.types.Language import Language

class Scraper:
  def __init__(self, name: str, rss_urls_en: list[str] = [], rss_urls_bn: list[str] = []):
    self.name = name
    self.rss_urls_en = rss_urls_en
    self.rss_urls_bn = rss_urls_bn