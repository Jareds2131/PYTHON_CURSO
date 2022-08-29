

A= input("¿QUE AREA QUIERES SABER, TRIANGULO O RECTANGULO?: ")

if ( A == "RECTANGULO"):
     a = float (input("INGRESA BASE DEL RECTANGULO: "))
     b = float(input("INGRESA LA ALTURA: ")) 
     print("SU AREA ES: ", (a * b))
     print(" Y SU PERIMETRO ES", (2*a + 2 * b))

if (A == "TRIANGULO"):
    c = float (input("INGRESA BASE: "))
    d = float(input("INGRESA LA ALTURA: "))
    print("SU AREA ES: ", (c * d)/2)




