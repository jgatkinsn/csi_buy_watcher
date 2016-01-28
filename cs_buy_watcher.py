"""
  Script to parse the CSI buy list for checking buy prices on certain cards
"""

import requests
from bs4 import BeautifulSoup
import sys
import json

DICEMASTERS_TEXT_URL = "http://www.coolstuffinc.com/buylist_text.php?pa=vbl&gn=mdm&dp=1"


def get_page(url):
    """ get the page and run it through BeautifulSoup """
    session = requests.Session()
    page = session.get(url)
    return BeautifulSoup(page.text)

def dump_json_page(page):
    """ simple function that takes the HTML and creates a JSON list"""


def main(args = sys.argv[1:]):
    """ Main routine for handle the parsing """
    print(get_page(DICEMASTERS_TEXT_URL))
    return True


if __name__ == "__main__":
    sys.exit(main() == False)
