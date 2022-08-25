# EJEMPLO DE OPERACIONES MATEMATICAS

#IMPRTAR LIBRERIA PARA USA FUNCIONES MATEMATICAS
#SINTAXIS
import math 
# ENTRADA DE DATOS
numero_1 = int(input("ESCRIBE EL PRIMER NUMERO: "))
numero_2 = int(input("ESCRIBE EL NUMEO 2: "))

#PROCESOS (OERECIONES O CALCULOS Y/O LOGICOS)

suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicacion =  (numero_1) * (numero_2)
division =  (numero_1) / (numero_2)
potencia =  (numero_1) ** (numero_2)
cuadrado = pow(numero_2,2)
cubo =  pow(numero_2,3)

raiz_cuadrada1 = pow(9, 0.5)
raiz_cuadrada2 = math.sqrt(numero_1)
raiz_Cubica = pow(numero_2,1/3)




#SALIDA DE DATOS 
print("LA SUMA ES =", suma)
print("lA SUMA ES = " + str(suma))
print(f"la suma es = {suma}")

print("La multiplicacion es", multiplicacion) 
print("La division es", division)
print("la potencia es ", potencia)
print("El cuadrado es", cuadrado)
print("EL CUBO ES: ", cubo)

print("La raiz cuadrada", round(raiz_cuadrada1,2))
print("La raiz cuadrada2", round(raiz_cuadrada2,2))
print("La raiz cuadrada", round(raiz_Cubica,3))




