from urllib import request
from util.read_rss import read_rss
from constants.sources import sources_en

def fetch_rss():
  extracted_rss = []
  for source in sources_en.get("prothom_alo", []):
    try:
      res = request.urlopen(source, timeout=10)
      if res.status == 200:
        extracted_rss.extend(read_rss(res))
        break
    except Exception as e:
      print(f"failed to access {source}: {e}")
      continue

  if not extracted_rss:
    print("no RSS entries fetched from any source")

  return extracted_rss