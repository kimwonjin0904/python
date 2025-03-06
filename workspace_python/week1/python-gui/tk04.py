from tkinter import *
from PIL import Image, ImageTk

app = Tk()
app.title("이미지 이동")

canvas = Canvas(app, width=400, height=300)
canvas.pack()

x = 20
y = 20
tk_tiger = None  # 전역 변수로 선언하여 유지


def create_img(canvas):
    global tk_tiger  # 함수 내에서 전역 변수를 사용
    img = Image.open('tiger.png')  # 이미지 불러오기
    img = img.resize((50, 50))  # 이미지 크기 조정
    tk_tiger = ImageTk.PhotoImage(img)  # 이미지 변환

    # 이미지가 사라지지 않도록 참조 유지
    canvas.image = tk_tiger
    canvas.create_image(100, 150, image=tk_tiger, tag='tiger', anchor=NW)


def move_right(event):
    canvas.move('tiger', x, 0)


def move_left(event):
    canvas.move('tiger', -x, 0)


def move_up(event):
    canvas.move('tiger', 0, -y)


def move_down(event):
    canvas.move('tiger', 0, y)


def move_jump(event):
    # 올라가는 애니메이션
    for i in range(5):  # 5번 위로 이동
        canvas.after(i * 50, lambda: canvas.move('tiger', 0, -10))

        # 내려오는 애니메이션 (0.3초 후 실행)
    for i in range(5, 10):  # 5번 아래로 이동
        canvas.after(i * 50, lambda: canvas.move('tiger', 0, 10))

#def move_jump(event):
 #   smooth_jump(up=True)  # 위로 이동
  #  canvas.after(200, lambda: smooth_jump(up=False))  # 0.2초 후 착지


create_img(canvas)

# 키보드 이벤트 바인딩 (bind_all 사용)
canvas.bind_all('<Right>', move_right)
canvas.bind_all('<Left>', move_left)
canvas.bind_all('<Up>', move_up)
canvas.bind_all('<Down>', move_down)
canvas.bind_all('<space>', move_jump)  # 스페이스바 이벤트 등록

app.mainloop()
