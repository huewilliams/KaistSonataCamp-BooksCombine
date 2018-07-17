#카이스트 소나타 캠프 온라인 교육 Canvas Polygon 예제
# tkinter 라이브러리에서 모든 것(*로 표현)을 받아옵니다.
from tkinter import *
master = Tk()
# canvas(그림판)의 크기를 가로 200, 세로 200으로 설정합니다.
canvas_width = 200
canvas_height = 200
python_green = "#476042"
#w를 canvas 객체로 지정해줍니다. 즉, w가 하나의 그림판을 뜻하게 됩니다.
w = Canvas(master,
           width = canvas_width,
           height = canvas_height)
# pack이란 해당 요소들을 부모 요소에 모두 패킹하여 불필요한 공간을 없앤다는 뜻 입니다.
# w 라는 canvas에 있는 불필요한 공간을 없애줍니다.
w.pack()
points = [100, 140, 110, 110, 140, 100, 110, 90, 100, 60, 90, 90, 60, 100, 90, 110]
# 각 포인터는 두 개씩 짝 지어져 (x,y)좌표를 나타낸다.
w.create_polygon(points, outline = python_green, fill='yellow', width=3)
mainloop()