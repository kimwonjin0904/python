from tkinter import *
import threading
import  time

def long_task():
    print("시작")
    time.sleep(5)
    print("종료")

def on_button_click():
    #daemon = True 앱 종료시 스레드도 종료되도록
    threading.Thread(target=long_task, daemon=True).start()

app = Tk()

btn = Button(app, text='시작!', command=on_button_click)  #클릭하여 시작버튼누르고 바로 돌아옴
btn.pack(pady=20)
app.mainloop()