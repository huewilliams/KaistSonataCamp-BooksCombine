# GUI import
from tkinter import *

# 크롤링 import
import requests
from bs4 import BeautifulSoup
import os

# webBrowser import
import webbrowser

#메인 GUI (인터넷 서점 사이트 선택 버튼)
master = Tk()

decide = 0
# decide : 도서 구매 사이트 결정 변수 0:default, 1:교보, 2:11번가, 3:리디북스


def best():
    print('베스트셀러 리스트입니다')


def kyobo():
    print('교보문고 베스트셀러 목록')

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
        i = i + 1
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
            url = str(x[i - 1])
            webbrowser.open(url)

        return inner

    i = 0
    for k in data.keys():
        i = i + 1
        print('[' + str(i) + ']  ' + k)
        a = Button(master, text='[' + str(i) + ']  ' + k, command=practice(i))
        a.grid(row=i, column=10)


def book11st():
    print('11번가 베스트셀러 목록')
    req = requests.get('http://books.11st.co.kr/booksmall/BooksAction.tmall?ID=BOOKS&ctgrNo=63548')

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    # 베스트 셀러 URL 크롤링
    my_titles = soup.select(
        '#layBody > div.books_subWrap > div > ul > li > div > div > div.pup_title > a'
    )
    link = {}

    for title in my_titles:
        link[title.text] = title.get('href')
    i = 0
    for k in link.values():
        i = i + 1
        # print('['+str(i)+']  '+k)
        print(f'[{i}] {k}')
        if (i >= 20):
            break

    # 베스트 셀러 URL 크롤링 완료

    # 베스트 셀러 데이터 크롤링
    my_titles = soup.select(
        '#layBody > div.books_subWrap > div > ul > li > div > div > div.pup_title > a'
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
            url = str(x[i - 1])
            webbrowser.open(url)

        return inner

    i = 0
    for k in data.keys():
        i = i + 1
        print('[' + str(i) + ']  ' + k)
        a = Button(master, text='[' + str(i) + ']  ' + k, command=practice(i))
        a.grid(row=i, column=10)
        if (i >= 20):
            break


def ridi():
    print('리디북스 베스트셀러 목록')

    req = requests.get('https://ridibooks.com/bestsellers/general?order=monthly')

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    # 베스트 셀러 URL 크롤링
    my_titles = soup.select(
        '#page_best > div.book_macro_wrapper.js_book_macro_wrapper > div > div.book_metadata_wrapper > h3 > a'
    )
    link = {}

    for title in my_titles:
        link[title.text] = title.get('href')
    i = 0
    for k in link.values():
        i = i + 1
        # print('['+str(i)+']  '+k)
        print(f'[{i}] {k}')
        if (i >= 20):
            break

    # 베스트 셀러 URL 크롤링 완료

    # 베스트 셀러 데이터 크롤링
    my_titles = soup.select(
        '#page_best > div.book_macro_wrapper.js_book_macro_wrapper > div > div.book_metadata_wrapper > h3 > a > span'
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
            url = 'https://ridibooks.com' + str(x[i - 1])
            webbrowser.open(url)

        return inner

    i = 0
    for k in data.keys():
        i = i + 1
        print('[' + str(i) + ']  ' + k)
        tmp = k.strip()
        a = Button(master, text='[' + str(i) + ']  ' + tmp, command=practice(i))
        a.grid(row=i, column=10)
        if (i >= 20):
            break

a = Button(master, text='베스트셀러 리스트', command=best)
a.grid(row=0, column=1)

a = Button(master, text='교보문고', command=kyobo)
a.grid(row=1, column=0)

a = Button(master, text='11번가 도서', command=book11st)
a.grid(row=1, column=1)

a = Button(master, text='리디북스', command=ridi)
a.grid(row=1, column=2)
#메인 GUI 끝

mainloop()