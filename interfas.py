from tkinter import *
ventana = Tk()
def funcion ():
    print(" TE AMO")


ventana.title("HOLA MUNDO")
ventana.geometry("400x200")


lbl =Label(ventana, text ="Este es un Label")
lbl.pack()
btn = Button(ventana, text= "Presionar",command= funcion)
btn.config(fg="blue",bg="red")
btn.place(x=10, y=50, width=100, height=30)
btn.pack()
ventana.mainloop()