import json
from os import path
from pathlib import Path
import pytest
import config
from util.create_json_file import create_json_file
from util.sources.prothomalo_en.parse import parse_rss
from util.types.Source import Source

FIXTURE_PATH = path.join(path.dirname(__file__), "fixtures/prothomalo_en.xml")


@pytest.fixture
def parsed():
  xml = open(FIXTURE_PATH).read()
  return parse_rss(xml)


@pytest.fixture
def test_file(parsed):
  create_json_file(
    source=Source.PROTHOMALO_EN,
    data=parsed,
    filename_fmt="_test_" + config.JSON_FILENAME_FMT,
  )
  files = list(Path(config.JSON_OUTPUT_DIR).glob("_test_*.json"))
  yield files
  for f in files:
    f.unlink(missing_ok=True)


def test_create_json_file(test_file):
  assert len(test_file) > 0


def test_is_valid_json(test_file):
  assert len(test_file) > 0
  with open(test_file[0]) as f:
    try:
      file = json.load(f)
      assert file["source"] == Source.PROTHOMALO_EN.value
      assert isinstance(file["entries"], list)
    except json.JSONDecodeError:
      pytest.fail("generated file is not a valid JSON")
