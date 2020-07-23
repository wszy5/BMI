#author:Wiktor Szymański
#version: 2.0.1
#date 23.07.2020

import tkinter as tk
from tkinter.messagebox import showerror,showinfo
from PIL import ImageTk, Image
import time

main = tk.Tk()
main.geometry("500x330")
main.title("Kalkulator BMI")
main.resizable(False,False)

load = Image.open("photo.png")
load = load.resize((150, 150), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)

img = tk.Label(main, image=render)
img.image = render
img.place(x=308,y=60)

w = tk.StringVar()
h = tk.StringVar()

lweight = tk.Label(main,text='Podaj wagę',justify="left",font = ("Times New Roman", 16))
lweight.place(x=50,y=75)
mes = tk.Label(main,text='kg',justify="left",font = ("Times New Roman", 16))
mes.place(x=228,y=75)
weight = tk.Entry(main,width=5,textvariable=w)
weight.place(x=190,y=78)

lheight = tk.Label(main,text="Podaj wzrost",justify="left",font = ("Times New Roman", 16))
lheight.place(x=50,y=110)
mes = tk.Label(main,text='cm',justify="left",font = ("Times New Roman", 16))
mes.place(x=228,y=116)
height = tk.Entry(main,width=5,textvariable=h)
height.place(x=190,y=116)


def run():
    try:
        w = int(weight.get())
        h = int(height.get())
    except:
        showerror("Błąd","Źle wprowadzone dane!")
        reset()
    bmi = round(((w/h**2)*10000),2)
    res.set(bmi)
    if bmi<18.5:
        result = tk.Label(main,textvariable=res,bg="blue").place(x=220,y=299)
    elif bmi==18.5 or bmi<=24.99:
        result = tk.Label(main,textvariable=res,bg="green").place(x=220,y=299)
    else:
        result = tk.Label(main,textvariable=res,bg="red").place(x=220,y=299)




def reset():
    res.set('')
    w.set('')
    h.set('')



def info():
    showinfo("Zakresy wskaźnika BMI","""
    < 16 = wygłodzenie,

    16 – 16,99 = wychudzenie,

    17 – 18,49 = niedowaga,

    18,5 – 24,99 = wartość prawidłowa,

    25 – 29,99 = nadwaga,

    30 – 34,99 = otyłość I stopnia,

    35 – 39,99 = otyłość II stopnia,

    > 40 = otyłość III stopnia.""")


ok = tk.Button(main,text="OK",command=run,justify="center",width=20,background='lightblue',fg='blue').place(x=85,y=175)
ok = tk.Button(main,text="RESET",command=reset,justify="center",width=20,background='white',fg='red').place(x=85,y=210)


res = tk.StringVar()
#result = tk.Label(main,textvariable=res).grid(row=3)
des = tk.Label(main,text="Twoje BMI wynosi",justify="left",font = ("Times New Roman", 16)).place(x=50,y=295)
info = tk.Button(main,text="Dowiedz się więcej...",command=info,justify="center",width=20,background='white',fg='red').place(x=345,y=295)
tk.mainloop()

#< 16 = wygłodzenie,
#16 – 16,99 = wychudzenie,
#17 – 18,49 = niedowaga,
#18,5 – 24,99 = wartość prawidłowa,
#25 – 29,99 = nadwaga,
#30 – 34,99 = otyłość I stopnia,
#35 – 39,99 = otyłość II stopnia,
#> 40 = otyłość III stopnia.
