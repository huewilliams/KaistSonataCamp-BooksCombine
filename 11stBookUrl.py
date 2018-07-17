# parser.py
import requests
from bs4 import BeautifulSoup
import os

# python 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('http://books.11st.co.kr/booksmall/BooksAction.tmall?ID=BOOKS&ctgrNo=63548')

html = req.text
soup = BeautifulSoup(html, 'html.parser')
my_titles = soup.select(
    '#layBody > div.books_subWrap > div > ul > li > div > div > div.pup_title > a'
    )
data = {}

for title in my_titles:
    data[title.text] = title.get('href')
i = 0
for k in data.values():
    i=i+1
    # print('['+str(i)+']  '+k)
    print(f'[{i}] {k}')
    if (i>=20):
        break