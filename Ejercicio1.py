#ENTRADAS
calificacion1 = float(input("INGRESE CALF. 1: "))
calificacion2 = float(input("INGRESE CALF. 2: "))
calificacion3 = float (input("INGRESE CALF. 3: "))

#PORCESO
promedio = (calificacion1 + calificacion2 + calificacion3)/3
if promedio >= 0 and promedio < 5:
    print("REPROBADO")

elif promedio > 5 and promedio <= 6:
    print("DE PANSAZO")
elif promedio > 6 and promedio <= 10:
    print("APROBADO")
else:
    print("CALIFICACION INVALIDA")

#SALIDA 

print("SU PROMEDIO ES: ",round(promedio,2))

