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
    '#page_best > div.book_macro_wrapper.js_book_macro_wrapper > div > div.book_metadata_wrapper > h3 > a > span'
    )

data = {}

for title in my_titles:
    data[title.text] = title.get('text')
i = 0
for k in data.keys():
    i=i+1
    tmp = k.strip()
    print('['+str(i)+']  ' + tmp)
    if (i>=20):
        break;


