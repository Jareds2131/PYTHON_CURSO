from cProfile import label
from cgitb import text
from tkinter import*
from tkinter import Tk, Label, Button, Entry

ventana = Tk()
ventana.title("CALCULADORA")
ventana.geometry("400x200")


lbl1 = Label(ventana,text= "primer numero", bg="pink", fg="white")
lbl1.place(x=10, y=10, width=100, height=30)

txt1 = Entry(ventana, bg="green")
txt1.place(x=120, y=10, width=100, height=30)

lbl2 = Label(ventana,text= "segundo numero", bg="pink")
lbl2.place(x=10, y=50, width=100, height=30)

txt2 = Entry(ventana, bg="green")
txt2.place(x=120, y=50, width=100, height=30)

lbl3 = Label(ventana,text= "RESULTADO", bg="grey")
lbl3.place(x=10, y=90, width=100, height=30)

txt3 = Label(ventana,text= lbl1 + lbl2 +lbl3, bg="green")
txt3.place(x=120, y=90, width=100, height=30)

ventana.mainloop()