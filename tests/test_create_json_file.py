import json
from os import path
from pathlib import Path
import pytest
import config
from util.create_json_file import create_json_file
from util.read_rss import read_rss

FIXTURE_PATH = path.join(path.dirname(__file__), "fixtures/prothom_alo.xml")


@pytest.fixture
def parsed():
  xml = open(FIXTURE_PATH).read()
  return read_rss(xml)


def test_create_json_file(parsed):
  create_json_file(
    data=parsed,
    filename_fmt="test_" + config.JSON_FILENAME_FMT,
  )
  files = list((Path(config.JSON_OUTPUT_DIR)).glob("test_*.json"))
  assert len(files) > 0


def test_is_valid_json():
  files = list((Path(config.JSON_OUTPUT_DIR)).glob("test_*.json"))
  assert len(files) > 0

  with open(files[0]) as f:
    try:
      json.load(f)
    except json.JSONDecodeError:
      pytest.fail("Generated file is not a valid JSON")
