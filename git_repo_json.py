# parser.py
import requests
from bs4 import BeautifulSoup
import json
import os

# python 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('https://github.com/huewilliams?tab=repositories')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
my_titles = soup.select(
    '#user-repositories-list > ul > li > div > h3 > a'
    )

data = {}

for title in my_titles:
    data[title.text] = title.get('text')

with open(os.path.join(BASE_DIR, 'resultGit.json'), 'w+') as json_file:
    json.dump(data, json_file)

