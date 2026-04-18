from util.create_json_file import create_json_file
from util.fetch_rss import fetch_rss


def main():
  data = fetch_rss()
  create_json_file(data)


if __name__ == "__main__":
  main()
