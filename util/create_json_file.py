import dataclasses
from datetime import datetime
import json
import os
import config
from util.types.Entry import Entry
from util.types.Source import Source


def create_json_file(
  source: Source,
  data: list[Entry],
  outdir_base: str = config.JSON_OUTPUT_DIR,
  filename_fmt: str = config.JSON_FILENAME_FMT,
):

  if not data[0]:
    print("empty data, skipping write")
    return

  try:
    json_data = {
      "source": str(source.value),
      "entries": [dataclasses.asdict(item) for item in data],
    }
  except Exception as e:
    raise ValueError(f"failed to serialize data: {e}") from e

  try:
    filename = datetime.now().strftime(filename_fmt)
  except Exception as e:
    raise ValueError(f"invalid filename format '{filename_fmt}': {e}") from e

  try:
    os.makedirs(outdir_base, exist_ok=True)
  except OSError as e:
    raise OSError(f"could not create output directory '{outdir_base}': {e}") from e

  filepath = os.path.join(outdir_base, filename)

  try:
    with open(filepath, mode="w") as f:
      json.dump(json_data, f, separators=(",", ":"))
  except OSError as e:
    raise OSError(f"failed to write file '{filepath}': {e}") from e
