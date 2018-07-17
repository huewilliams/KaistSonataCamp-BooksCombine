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
    '#page_best > div.book_macro_wrapper.js_book_macro_wrapper > div > div.book_metadata_wrapper > h3 > a'
    )
data = {}

for title in my_titles:
    data[title.text] = title.get('href')
i = 0
for k in data.values():
    i=i+1
    # print('['+str(i)+']  '+k)
    print(f'[{i}] https://ridibooks.com{k}')
    if (i>=20):
        break