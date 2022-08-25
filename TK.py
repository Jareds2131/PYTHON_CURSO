from tkinter import*

a = Tk()
b = Tk()
a.title("Primera Hoja")
b.title("Segunda Hoja")

a.resizable(1,1)
b.resizable(0,0)
a.geometry("200x200")
b.geometry("400x200")



a.mainloop()
b.mainloop()



