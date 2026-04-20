import pytest
from os import path

from util.sources.prothomalo_en.parse import parse_rss

FIXTURE_PATH = path.join(path.dirname(__file__), "fixtures/prothomalo_en.xml")


@pytest.fixture
def parsed():
  xml = open(FIXTURE_PATH).read()
  return parse_rss(xml)


@pytest.fixture
def item(parsed):
  return parsed[0]


def test_parsed_is_list(parsed):
  assert isinstance(parsed, list)


def test_parsed_is_not_empty(parsed):
  assert len(parsed) > 0


def test_item_fields(item):
  assert item.id == "urn:uuid:512fa75d-95d3-40d7-9738-273f6e83628a"
  assert item.title == "Govt not planning online classes for now: State minister"
  assert item.link == "https://en.prothomalo.com/youth/education/ksdcfs5s72"
  assert item.published_at == "2026-04-06T16:06:14.860Z"
  assert item.updated_at == "2026-04-06T16:06:14.860Z"
  assert isinstance(item.authors, list)
  assert item.authors[0] == "Staff Correspondent"
  assert isinstance(item.tags, list)
  assert item.tags[0] == "Education"
