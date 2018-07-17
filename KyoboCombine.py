# 크롤링 import
import requests
from bs4 import BeautifulSoup
import os
# GUI import
from tkinter import *
# webBrowser import
import webbrowser

master = Tk()

# python 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('http://www.kyobobook.co.kr/bestseller/bestSellerMain.laf?orderClick=d79')


html = req.text
soup = BeautifulSoup(html, 'html.parser')

# 베스트 셀러 URL 크롤링
my_titles = soup.select(
    '#main_contents > ul > li > div.cover > a'
    )
link = {}

for title in my_titles:
    link[title.text] = title.get('href')
i = 0
for k in link.values():
    i = i+1
    # print('['+str(i)+']  '+k)
    print(f'[{i}] {k}')

# 베스트 셀러 URL 크롤링 완료

# 베스트 셀러 데이터 크롤링
my_titles = soup.select(
    '#main_contents > ul > li > div.detail > div.title > a > strong'
    )
data = {}

for title in my_titles:
    data[title.text] = title.get('text')
# 베스트 셀러 크롤링 완료

# 함수 정의
def practice(i):
# 래퍼 함수
    def inner():
        print('sucess')
        x = list(link.values())
        print(i)
        url = str(x[i-1])
        webbrowser.open(url)
    return inner

i = 0
for k in data.keys():
    i=i+1
    print('['+str(i)+']  '+k)
    a = Button(master,text='['+str(i)+']  '+k,command = practice(i))
    a.grid(row=i, column=10)
mainloop()
