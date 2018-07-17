# GUI import
from tkinter import *

master = Tk()


def best():
    print('베스트셀러 리스트입니다')


def kyobo():
    print('교보문고 베스트셀러 목록')


def book11st():
    print('11번가 베스트셀러 목록')


def ridi():
    print('리디북스 베스트셀러 목록')


a = Button(master, text='베스트셀러 리스트', command=best)
a.grid(row=0, column=1)

a = Button(master, text='교보문고', command=kyobo)
a.grid(row=1, column=0)

a = Button(master, text='11번가 도서', command=book11st)
a.grid(row=1, column=1)

a = Button(master, text='리디북스', command=ridi)
a.grid(row=1, column=2)
mainloop()