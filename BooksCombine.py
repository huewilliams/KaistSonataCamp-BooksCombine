# GUI import
from tkinter import *

import shutil
import os

# 크롤링 import
import requests
from bs4 import BeautifulSoup
# webBrowser import
import webbrowser

from PIL import ImageTk

# 메인 GUI (인터넷 서점 사이트 선택 버튼)
master = Tk()
master.title("BestSellerList")
decide = 0
# decide : 도서 구매 사이트 결정 변수 0:default, 1:교보, 2:11번가, 3:리디북스


def best():
    print('베스트셀러 리스트입니다')
    a = Button(master, text='교보문고', command=kyobo)
    a.grid(row=1, column=0)

    a = Button(master, text='11번가 도서', command=book11st)
    a.grid(row=1, column=1)

    a = Button(master, text='리디북스', command=ridi)
    a.grid(row=1, column=2)


def kyobo():
    print('교보문고 베스트셀러 목록')
    mKyobo = Tk()
    mKyobo.title("교보문고")

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
        a = Button(mKyobo, text='[' + str(i) + ']  ' + k, command=practice(i))
        a.config(width=75, height=1)
        a.pack(side=TOP)


def book11st():
    print('11번가 베스트셀러 목록')
    m11st = Tk()
    m11st.title("11번가 도서")

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

    # 가격 정보 크롤링
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select(
        '#layBody > div.books_subWrap > div.thumbnail_list.thumb_w780 > ul > li > div > div > div.pub_priceW > strong'
    )
    price = {}

    for title in my_titles:
        price[title.text] = title.get('text')
    i = 0
    for p in price.keys():
        i = i + 1
        # print('['+str(i)+']  '+k)
        print(f'[{i}] {p}')
        if (i >= 20):
            break
    # 가격 정보 크롤링 완료

    # 베스트셀러 이미지 크롤링
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select(
        '#layBody > div > div > ul > li > div > div.pub_photo > a > span > img'
    )
    directory = os.path.dirname('./img/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    data = []
    source = []
    print(my_titles)
    for title in my_titles:
        data.append(title.get('alt'))
        source.append(title.get('src'))
    print(data)
    print(source)
    i = 0
    for src in source:
        img_src = source[i]
        img_name = str(i)
        i = i + 1
        r = requests.get(img_src, stream=True, headers={'User-agent': 'Mozilla/5.0'})
        if r.status_code == 200:
            with open('./img/' + img_name + '.jpeg', 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
        if i == 20:
            break
    # 베스트셀러 이미지 크롤링 완료

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
            def goUrl():
                url = str(x[i-1])
                webbrowser.open(url)
            print('sucess')
            x = list(link.values())
            p = list(price.keys())
            k = list(data.keys())
            print(p)
            def showImage():
                print(source[i-1])
                SI = Toplevel()
                canvas_width = 150
                canvas_height = 200
                w = Canvas(SI,
                           width=canvas_width,
                           height=canvas_height)
                w.pack()
                img = ImageTk.PhotoImage(file="./img/"+str(i-1)+'.jpeg')
                print("./img/"+str(i-1)+'.jpeg')
                w.create_image(0, 0, anchor=NW, image=img)  # 이미지를 마진을 설정
                SI.mainloop()
            i11st = Tk()
            i11st.title('책 정보 : '+k[i-1])
            ia = Button(i11st, text='가격 : '+p[i-2])
            ia.config(width=30, height=2)
            ia.pack(side=TOP)
            ia = Button(i11st, text='사러가기',command=goUrl)
            ia.config(width=30, height=2)
            ia.pack(side=TOP)
            ia = Button(i11st, text='책 이미지보기', command=showImage)
            ia.config(width=30, height=2)
            ia.pack(side=TOP)
            print(i)
            print(p[i])

        return inner

    i = 0
    for k in data.keys():
        i = i + 1
        print('[' + str(i) + ']  ' + k)
        a = Button(m11st, text='[' + str(i) + ']  ' + k, command=practice(i))
        a.config(width=100, height=1)
        a.pack(side=TOP)
        if (i >= 20):
            break

def ridi():
    print('리디북스 베스트셀러 목록')

    mRidi = Tk()
    mRidi.title("리디북스")
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
        print(f'[{i}] {k}')
        i = i + 1
        # print('['+str(i)+']  '+k)
        if (i >= 21):
            break


    # 베스트 셀러 URL 크롤링 완료

    #가격 정보 크롤링

    my_titles = soup.select(
        '#page_best > div > div > div.book_metadata_wrapper > div > p > span.price > span'
    )

    price = {}

    for title in my_titles:
        price[title.text] = title.get('text')
    i = 0
    print(price)
    for p in price.keys():
        i = i + 1
        tmp = p.strip()
        print('[' + str(i) + ']   ' + tmp + '원')
        if (i >= 20):
            break
    #가격 정보 크롤링 완료

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
            def goUrl():
                url = 'https://ridibooks.com' + str(x[i])
                webbrowser.open(url)
            x = list(link.values())
            p = list(price.keys())
            k = list(data.keys())

            iRidi = Tk()
            iRidi.title('책 정보 : ' + k[i].strip())

            ia = Button(iRidi, text='가격 : ' + p[i])
            ia.config(width=30, height=1)
            ia.pack(side=TOP)
            ia = Button(iRidi, text='사러가기', command=goUrl)
            ia.config(width=30, height=1)
            ia.pack(side=TOP)
            print(i)
            print(p[i])

        return inner

    i = 0
    for k in data.keys():
        print('[' + str(i) + ']  ' + k)
        tmp = k.strip()
        if (i == 0):
            print('예외 처리')
        else :
            iText = '[' + str(i) + ']  ' + tmp
            a = Button(mRidi, text=iText, command=practice(i))
            a.config(width=75, height=1)
            a.pack(side=TOP)
        i = i + 1
        if (i >= 21):
            break


a = Button(master, text='베스트셀러 리스트', command=best)
a.grid(row=0, column=1)


mainloop()