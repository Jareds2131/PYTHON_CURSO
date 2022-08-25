#ENTRADA 

from tkinter import N


niveldeAgua = float(input("INGRESE EL NIVEL DEL AGUA: "))

if (niveldeAgua < 0):
    print("FUGA DE CISTERNA")
elif niveldeAgua == 0:
    print("ENCENDER BOMBA DE AGUA")
elif niveldeAgua > 0 and niveldeAgua < 2:
    print("ACELERAR BOMBA DE AGUA")
elif niveldeAgua > 2 and niveldeAgua < 4:
    print("BOMBA TRABAANJANDO!")
elif niveldeAgua > 4 and niveldeAgua < 6:
    print("DESACELERAR BOMBA DE AGUA")
elif niveldeAgua ==  6:
    print("APAGAR BOMBA BOMBA DE AGUA")
elif niveldeAgua > 6:
    print("DESBORDAMIENTO DE AGUA EN CISTERNA")
else:
    print("ERROR")


