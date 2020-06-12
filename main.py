import argparse
from bs4 import BeautifulSoup
import requests


def contains_all(terms_list, string):
    if terms_list is None:
        return True
    for term in terms_list:
        if term not in string:
            return False
    return True


my_parser = argparse.ArgumentParser(description='Scrapes __ webpage for jobs and outputs the relevant urls')

my_parser.add_argument('--s',
                       metavar='search',
                       type=str,
                       nargs='*',
                       help='the search term for monster.co.uk')

my_parser.add_argument('--k',
                       metavar='keywords',
                       type=str,
                       nargs='*',
                       help='the keyword to search for')
my_parser.add_argument('Page',
                       metavar='page_number',
                       type=int,
                       help='The page number on monster')

args = my_parser.parse_args()

# Sets the keywords to search for in the results
keywords = args.k

# Sets the search term for the URL
search_term = '' if args.s is None else '-'.join(args.s)

# Sets the page number for the URL
page = args.Page
page_string = '' if page == 1 else "&stpage=1&page=" + str(page)

# Creates the URL according to the search terms and the page number
URL = "https://www.monster.co.uk/jobs/search/?q=" + search_term + "&where=London&client=power&cy=uk&rad=20&intcid=swoop_Hero_Search" + page_string

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')

job_elements = results.find_all('section', class_='card-content')

for element in job_elements:
    title = element.find('h2', class_='title')
    company = element.find('div', class_='company')
    location = element.find('div', class_='location')
    if None in (title, company, location):
        continue
    if contains_all(keywords, title.text.strip().lower()):
        url = title.a
        print(title.text.strip())
        print(company.text.strip())
        print(location.text.strip())
        print(url.get('href'))
        print()
