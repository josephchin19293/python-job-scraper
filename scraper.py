from bs4 import BeautifulSoup

import requests
URL = 'https://www.monster.co.uk/jobs/search/?q=Web-Developer&where=London&client=power&cy=uk&rad=20&intcid=swoop_Hero_Search'


page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
# print(results.prettify())

job_elems = results.find_all('section', class_='card-content')
# print(type(job_elems))
# print(job_elems[0].h2.string)
# for child in job_elems[0].h2.children:
#     print(child)

print()
for element in job_elems:
    title = element.find('h2', class_='title')
    company = element.find('div', class_='company')
    location = element.find('div', class_='location')
    if None in (title, company, location):
        continue
    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    print()
