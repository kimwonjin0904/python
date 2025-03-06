from tkinter import *
app = Tk()
app.title("이벤트 처리")

def fn_click(event):
    print(f"마우스 클릭 위치: {event.x}, {event.y}")

def fn_push(event):
    print(f"키보드 입력: {event.char}")

frame = Frame(app, width=300, height=300, bg="lightgray")
frame.pack()

# 왼쪽 마우스 클릭 이벤트 바인딩
frame.bind('<Button-1>', fn_click)

# 키보드 입력 이벤트 바인딩
frame.bind('<Key>', fn_push)

# 포커스 설정 (키보드 입력a을 받으려면 포커스를 설정해야 함)
frame.focus_set()

app.mainloop()
