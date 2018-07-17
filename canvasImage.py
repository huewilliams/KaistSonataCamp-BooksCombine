#카이스트 소나타 캠프 온라인 교육 Canvas Image 예제
# tkinter 라이브러리에서 모든 것(*로 표현)을 받아옵니다.
from tkinter import *
from PIL import ImageTk

master = Tk()
# canvas(그림판)의 크기를 가로 400, 세로 400으로 설정합니다.
canvas_width = 900
canvas_height = 1600
w = Canvas(master,
           width = canvas_width,
           height = canvas_height)
w.pack()

img = ImageTk.PhotoImage(file='huewilliams.jpg')
w.create_image(0,0, anchor=NW, image=img)
mainloop()