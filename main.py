import pd as pd
import requests
import lxml as lxml
from bs4 import BeautifulSoup
from fake_headers import Headers
import json
import re
job_title = ["'Python'"]
url = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'
headers = Headers(os="macintosh", browser="safari", headers=True).generate()
KEYWORDS = ["Django", "Flask"]
response = requests.get(url, headers=headers)
text = response.text

soup = BeautifulSoup(text, features="lxml")
vacancies = soup.find_all("div", class_="vacancy-serp-item__layout")

data = []
for vacancy in vacancies:
    name = vacancy.find("a", class_="serp-item__title")
    link = vacancy.find("a", class_="serp-item__title", href=True)["href"]
    company = vacancy.find("div", class_="vacancy-serp-item-company")
    salary = vacancy.find("span",  class_="bloko-header-section-3")

    for el in KEYWORDS:
        if el in name.text:
            data.append(f"{link} | {name.text} | {company.text} | {salary.text}")

with open("data.json", 'w') as f:
    json.dump(data, f, ensure_ascii=False, sort_keys=True, indent="\t")
