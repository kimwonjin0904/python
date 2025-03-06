from tkinter import *
from tkinter import messagebox
import random
#.py to .exe
#pip install pyinstaller

app = Tk()
app.title("로또번호 생성기!")
app.geometry("250x50")
#app.iconbitmap('lotto.ico')
app.grid_columnconfigure(0,weight=1)
app.grid_columnconfigure(1,weight=1)
#app.grid_rowconfigure(0,weight=1)
#app.grid_rowconfigure(1,weight=1)

lab = Label(app, text='수량')
lab.grid(row=0 , column=0)
txt = Entry(app)
txt.grid(row=0, column=1)

def fn_click():
    msg = txt.get()
    lotto = ""
    for _ in range(int(msg)):
        lotto += f"{str(sorted(make_lotto()))} \n"
    #수량을 입력받아서
    #수량만큼 생성
    #생성 번호를 출력
    messagebox.showinfo("입력한거:", lotto)



def make_lotto():
    lotto_num = set()
    while len(lotto_num) < 6:
        lotto_num.add(random.randint(1, 45))
    return lotto_num


btn = Button(app, text='생성', command=fn_click)
btn.grid(row=1, column=0, columnspan=2, sticky='ew')

app.mainloop()