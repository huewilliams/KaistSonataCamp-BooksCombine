from tkinter import *
master = Tk()
# practice()라는 함수를 새로 만듭니다. 이 함수는 "연습중입니다"를 화면에 출력합니다
def practice():
    print("연습중입니다")
# a는 새로 생성된 버튼을 뜻합니다. Button()은 tkinter 안에 내장되어 있는 함수이다.
# 현재는 master, text, command의 세 매개변수를 입력받아 maseter에 해당하는 tkinter에 버튼을 만들어 text에 쓰여진 글자를 보여주며
# command에 나타낸 함수를 실행합니다.
a = Button(master,text = "연습",command=practice)
a.pack()
mainloop()