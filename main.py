import dataclasses
from datetime import datetime
import json
import os
from urllib import request
from constants.sources import sources_en
from util.read_rss import read_rss

def get_rss():
  success = False
  extracted_rss = []

  if not success:
    for source in sources_en["prothom_alo"]:
      try:
        res = request.urlopen(source)
        if res.status == 200:
          success = True
        extracted_rss.extend(read_rss(res))
        break
      except Exception as e:
        print(f"Failed to access {source}: {e}")

  return extracted_rss

def create_json(data):
  outdir_name = "artifacts"

  json_data = [dataclasses.asdict(item) for item in data]
  filename = datetime.now().strftime("%d-%m-%Y_%H-%M-%S.json")
  os.makedirs(outdir_name, exist_ok=True)
  with open(
    os.path.join(outdir_name, filename), "w"
  ) as f:
    json.dump(json_data, f, separators=(',', ':'))

def main():
  data = get_rss()
  create_json(data)

if __name__ == "__main__":
  main()