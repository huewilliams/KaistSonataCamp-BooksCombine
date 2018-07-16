# parser.py
import requests
from bs4 import BeautifulSoup
import os

# python 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('http://www.kyobobook.co.kr/bestseller/bestSellerMain.laf?orderClick=d79')

html = req.text
soup = BeautifulSoup(html, 'html.parser')
my_titles = soup.select(
    '#main_contents > ul > li > div.detail > div.title > a > strong'
    )
data = {}

for title in my_titles:
    data[title.text] = title.get('text')
i = 0
for k in data.keys():
    i=i+1
    print('['+str(i)+']  '+k)
