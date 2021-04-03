import requests
from bs4 import BeautifulSoup

URL = 'https://www.indeed.com/jobs?q=software+developer&l=Concord%2C+MA'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='resultsBodyContent')
job_elems = results.find_all(
    'div', class_='jobsearch-SerpJobCard unifiedRow row result clickcard')
for job_elem in job_elems:
    title_elem = job_elem.find('a', class_='jobtitle turnstileLink ')
    company_elem = job_elem.find('span', class_='company')
    location_elem = job_elem.find(
        'div', class_='location accessible-contrast-color-location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()
