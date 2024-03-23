from tkinter import Button, Entry, Label, StringVar, Tk
from tkinter import *
import tkinter.messagebox as MessageBox

screen = Tk()
screen.title("TASK 1")
screen.geometry('800x600')
screen.configure(background ="light blue")

text=Label(screen, text="CALCULATOR")
text.configure(font =("calibiri", 35))
text.configure(background ="pink", foreground="red",width=20)
text.pack()
text.place(x=120, y=10)

expression=""

def button_click(value):
    global expression
    expression+=value
    calculate.configure(text=expression)
    calculate.delete(0, END)
    calculate.insert(END, expression)


def calculate1():
    global expression
    result=""
    if expression!="":
        try:
            result= eval(expression)
        except:
            result="Error"
            expression=""
    calculate.configure(text=result)
    calculate.delete(0, END)
    calculate.insert(END, result)

def clear():
    global expression
    expression = ""
    calculate.delete(0, END)


no1 = Button(screen, text="1",width=8,height=1, font=('calibiri', 18),fg='black', background="white", command=lambda: button_click("1"))
no1.pack()
no1.place(x=50, y=400)

no2 = Button(screen, text="2",width=8,height=1, font=('calibiri', 18),fg='black', background="white", command=lambda: button_click("2"))
no2.pack()
no2.place(x=180, y=400)

no3 = Button(screen, text="3",width=8,height=1, font=('calibiri', 18),fg='black', background="white", command=lambda: button_click("3"))
no3.pack()
no3.place(x=310, y=400)

no4 = Button(screen, text="4",width=8,height=1, font=('calibiri', 18),fg='black', background="white", command=lambda: button_click("4"))
no4.pack()
no4.place(x=50, y=335)

no5 = Button(screen, text="5",width=8,height=1, font=('calibiri', 18),fg='black', background="white", command=lambda: button_click("5"))
no5.pack()
no5.place(x=180, y=335)

no6 = Button(screen, text="6",width=8,height=1, font=('calibiri', 18),fg='black', background="white", command=lambda: button_click("6"))
no6.pack()
no6.place(x=310, y=335)

no7 = Button(screen, text="7",width=8,height=1, font=('calibiri', 18),fg='black', background="white", command=lambda: button_click("7"))
no7.pack()
no7.place(x=50, y=270)

no8 = Button(screen, text="8",width=8,height=1, font=('calibiri', 18),fg='black', background="white", command=lambda: button_click("8"))
no8.pack()
no8.place(x=180, y=270)

no9 = Button(screen, text="9",width=8,height=1, font=('calibiri', 18),fg='black', background="white", command=lambda: button_click("9"))
no9.pack()
no9.place(x=310, y=270)

no10 = Button(screen, text="0",width=8,height=1, font=('calibiri', 18),fg='black', background="white", command=lambda: button_click("0"))
no10.pack()
no10.place(x=50, y=465)

no11 = Button(screen, text="00",width=8,height=1, font=('calibiri', 18),fg='black', background="white", command=lambda: button_click("00"))
no11.pack()
no11.place(x=180, y=465)

no12 = Button(screen, text=".",width=8,height=1, font=('calibiri', 18),fg='black', background="white", command=lambda: button_click("."))
no12.pack()
no12.place(x=310, y=465)

sign1 = Button(screen, text="+",width=8,height=1, font=('calibiri', 18),fg='black', background="white", command=lambda: button_click("+"))
sign1.pack()
sign1.place(x=440, y=465)

sign2 = Button(screen, text="-",width=8,height=1, font=('calibiri', 18),fg='black', background="white", command=lambda: button_click("-"))
sign2.pack()
sign2.place(x=440, y=400)

sign3 = Button(screen, text="*",width=8,height=1, font=('calibiri', 18),fg='black', background="white", command=lambda: button_click("*"))
sign3.pack()
sign3.place(x=440, y=335)

sign4 = Button(screen, text="/",width=8,height=1, font=('calibiri', 18),fg='black', background="white", command=lambda: button_click("/"))
sign4.pack()
sign4.place(x=440, y=270)

sign5 = Button(screen, text="C",width=8,height=1, font=('calibiri', 18),fg='white', background="red", command= clear)
sign5.pack()
sign5.place(x=310, y=205)

sign6 = Button(screen, text="=",width=8,height=1, font=('calibiri', 18),fg='black', background="white", command= calculate1)
sign6.pack()
sign6.place(x=440, y=205)

calculate=Entry(screen,font=('calibiri', 20, 'normal'))
calculate.pack()
calculate.place(x=250, y=120)

screen.mainloop()