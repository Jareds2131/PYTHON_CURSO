 
print("ESTE PROGRAMA TE AYUDA A ORDENAR NUMEROS DE FORMA ASENDENTE PORQUE AL PROFE SERRANO LE GUSTA HACERNOS TRABAJAR")

A = float(input("INGRESA NUMERO 1: "))
B = float(input("INGRESA NUMERO 2: "))
C = float(input("INGRESA NUMERO 3: "))

if (A < B) and (B < C):
    print(A, B, C)

if (B < A) and (A < C):
    print(B, A, C)

if (C < B) and (B < A):
    print(C, B, A)

if (A < C) and (C < B):
    print(A, C, B)

if (B < C) and (C < A):
    print(B, C, A)

if (C < A) and (A < B):
    print(C, A, B)