"""
  Script to parse the CSI buy list for checking buy prices on certain cards
"""

import requests
from bs4 import BeautifulSoup
import sys
import json

DICEMASTERS_TEXT_URL = "http://www.coolstuffinc.com/buylist_text.php?pa=vbl&gn=mdm&dp=1"

DICEMASTERS_CONTENT_MAP = {1:"name",2:"Condition",3:"Set",4:"Rarity",5:"Price"}

def get_page(url):
    """ get the page and run it through BeautifulSoup """
    session = requests.Session()
    page = session.get(url)
    return BeautifulSoup(page.text, "lxml")

def extract_table_data(page):
    """ simple function that takes the HTML and extracts the table data into a list of dictionaries"""
    data = []
    outer_table = page.find('table', attrs={'cellpadding':'1'})
    #walk the rows and check table in table
    outer_table_rows = outer_table.find_all('tr')
    for outer_row in outer_table_rows:
        inner_data_sets = outer_row.find_all('td')
        if len(inner_data_sets) > 1:
            card_data = {}
            count = 0
            for inner_data in inner_data_sets:
                table_check = inner_data.find('table')
                if (table_check is None and inner_data.string is not None
                    and inner_data.string.isspace() == False and "valign" not in inner_data.string):
                    count += 1
                    card_data[DICEMASTERS_CONTENT_MAP[count]] = inner_data.string

            #check for empty card data for those weird rows, could filter elsewhere
            if card_data != {}:
                data.append(card_data)

    return data


def main(args = sys.argv[1:]):
    """ Main routine for handle the parsing """
    page = get_page(DICEMASTERS_TEXT_URL)
    data_list = extract_table_data(page)
    print(data_list)

    return True


if __name__ == "__main__":
    sys.exit(main() == False)
