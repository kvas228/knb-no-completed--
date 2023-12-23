from knb import *
from tkinter import *
root: Tk = Tk()
root["bg"] = "#58c46a"
root.title("Menu")
root.wm_attributes("-alpha", 0.95)
root.geometry("350x550")
root.resizable(width=True, height=True)

def sa():
    app()
    breakpoint()

def sb():
    btn1 = Frame(bg="Start")
    btn1.place(relx=0.25, rely=0.50, relwidth=0.50, relheight=0.055)
    title1 = Label(btn1, text="Elegido", bg="yellow", font=35)
    title1.pack()

def ss():
    btn1 = Frame(bg="green")
    btn1.place(relx=0.25, rely=0.60, relwidth=0.50, relheight=0.055)
    title1 = Label(btn1, text="Elegido", bg="green", font=35)
    title1.pack()

def sc():
    btn1 = Frame(bg="red")
    btn1.place(relx=0.25, rely=0.65, relwidth=0.50, relheight=0.055)
    title1 = Label(btn1, text="Elegido", bg="red", font=35)
    title1.pack()

def zz():
    exit()

canvas = Canvas(root, height=950, width=750, bg="#58c46a")
canvas.pack()

frame1 = Frame(bg="#3d6e45")
frame1.place(relx=0.25, rely=0.09, relwidth=0.50, relheight=0.80)
frame3 = Frame(bg="white")
frame3.place(relx=0.5, rely=0.9, relwidth=0.40, relheight=0.035)
title = Label(frame1, text="Menu", bg="white", font=35)
title.pack()
btn = Button(frame1, text="amarillo", bg="white", command=sb)
btn.place(relx=0.9, rely=0.9, relwidth=0.9, relheight=0.9)
btn.pack()
btn = Button(frame1, text="verde", bg="white", command=ss)
btn.pack()
btn = Button(frame1, text="azul", bg="white", command=sa)
btn.pack()
btn = Button(frame1, text="rojo", bg="white", command=sc)
btn.pack()
btn1 = Button(frame3, text="Exit", bg="white", command=zz)
btn1.pack()
btn1 = Button(frame3, text="Start game", bg="white", command=zz)
btn1.pack()

root.mainloop()