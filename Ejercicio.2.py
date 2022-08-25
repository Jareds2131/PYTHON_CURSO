#ENTRADA

Pi = 3.1416
diametro = float(input("ESCRIBA EL DIAMETRO: "))
radio = float(input("ESCRIBA EL RADIO: "))

#PROCESOS

area = (Pi * radio **2)
perimetro = (diametro * Pi)

#SALIDA
print("EL AREA ES: ", round(area,2))
print("EL PERIMETRO ES: ", round(perimetro))
