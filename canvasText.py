#카이스트 소나타 캠프 온라인 교육 Canvas Line 예제
# tkinter 라이브러리에서 모든 것(*로 표현)을 받아옵니다.
from tkinter import *
master = Tk()
# canvas(그림판)의 크기를 가로 80, 세로 40으로 설정합니다.
canvas_width = 80
canvas_height = 40
#w를 canvas 객체로 지정해줍니다. 즉, w가 하나의 그림판을 뜻하게 됩니다.
w = Canvas(master,
           width = canvas_width,
           height = canvas_height)
# pack이란 해당 요소들을 부모 요소에 모두 패킹하여 불필요한 공간을 없앤다는 뜻 입니다.
# w 라는 canvas에 있는 불필요한 공간을 없애줍니다.
w.pack()
w.create_text(canvas_width / 2,
              canvas_height / 2,
              text = " BestSeller List ")
mainloop()