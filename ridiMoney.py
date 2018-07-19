# parser.py
import requests
from bs4 import BeautifulSoup
import os

# python 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('https://ridibooks.com/bestsellers/general?order=monthly')

html = req.text
soup = BeautifulSoup(html, 'html.parser')
my_titles = soup.select(
    '#page_best > div > div > div.book_metadata_wrapper > div > p > span.price > span'
    )

data = {}

for title in my_titles:
    data[title.text] = title.get('text')
i = 0
print(data)
for k in data.keys():
    i=i+1
    tmp = k.strip()
    print('['+str(i)+']   ' + tmp+'원')
    if (i>=20):
        break
