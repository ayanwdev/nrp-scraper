import dataclasses
from datetime import datetime
import json
import os
import config
from util.types.Entry import Entry


def create_json_file(
  data: list[Entry],
  outdir_name: str = config.JSON_OUTPUT_DIR,
  filename_fmt: str = config.JSON_FILENAME_FMT,
):

  if not data:
    print("empty data, skipping write.")
    return

  try:
    json_data = [dataclasses.asdict(item) for item in data]
  except Exception as e:
    raise ValueError(f"failed to serialize data: {e}") from e

  try:
    filename = datetime.now().strftime(filename_fmt)
  except Exception as e:
    raise ValueError(f"invalid filename format '{filename_fmt}': {e}") from e

  try:
    os.makedirs(outdir_name, exist_ok=True)
  except OSError as e:
    raise OSError(f"could not create output directory '{outdir_name}': {e}") from e

  filepath = os.path.join(outdir_name, filename)

  try:
    with open(filepath, mode="w") as f:
      json.dump(json_data, f, separators=(",", ":"))
  except OSError as e:
    raise OSError(f"failed to write file '{filepath}': {e}") from e
