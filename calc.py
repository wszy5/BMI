import tkinter as tk

main = tk.Tk()
main.geometry("190x100")
main.title("Kalkulator BMI")


lweight = tk.Label(main,text="Podaj wagę",justify="right")
lweight.grid(column=0,row=0)
lheight = tk.Label(main,text="Podaj wzrost w cm",justify="right")
lheight.grid(column=0,row=1)

weight = tk.Entry(main,width=5)
weight.grid(column=1,row=0)
height = tk.Entry(main,width=5)
height.grid(column=1,row=1)

def run():
    try:
        w = int(weight.get())
        h = int(height.get())
    except:
        tk.mainloop()
    bmi = round(((w/h**2)*10000),2)
    res.set(bmi)
    if bmi<18.5:
        result = tk.Label(main,textvariable=res,bg="blue").grid(row=3,column=1)
    elif bmi==18.5 or bmi<=24.99:
        result = tk.Label(main,textvariable=res,bg="green").grid(row=3,column=1)
    else:
        result = tk.Label(main,textvariable=res,bg="red").grid(row=3,column=1)

ok = tk.Button(main,text="OK",command=run,justify="center").grid(row=2,column=1)

res = tk.StringVar()
#result = tk.Label(main,textvariable=res).grid(row=3)
des = tk.Label(main,text="Twoje BMI wynosi").grid(row=3,column=0)
tk.mainloop()

#< 16 = wygłodzenie,
#16 – 16,99 = wychudzenie,
#17 – 18,49 = niedowaga,
#18,5 – 24,99 = wartość prawidłowa,
#25 – 29,99 = nadwaga,
#30 – 34,99 = otyłość I stopnia,
#35 – 39,99 = otyłość II stopnia,
#> 40 = otyłość III stopnia.
