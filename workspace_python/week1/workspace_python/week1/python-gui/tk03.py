
from tkinter import *
app =Tk()
canvas = Canvas(app, width=400, height=300)
canvas.pack()

x = 20
y = 20

def move_right(event):
    canvas.move('redball', x, 0)
    canvas.after(100)
    canvas.update()

def move_left(event):
    canvas.move('redball', -x, 0)
    canvas.after(10)
    canvas.update()

def move_up(event):
    canvas.move('redball', 0, -y)
    canvas.after(10)
    canvas.update()

def move_down(event):
    canvas.move('redball', 0, y)
    canvas.after(10)
    canvas.update()

canvas.create_oval(100, 150, 150, 200, fill='red', tag='redball')
canvas.bind('<Right>', move_right)
canvas.bind('<Left>', move_left)
canvas.bind('<Up>', move_up)
canvas.bind('<Down>', move_down)
canvas.focus_set()
app.mainloop()