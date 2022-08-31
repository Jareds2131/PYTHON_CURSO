A = float(input("INGRESE EL VALOR DE A: "))
B = float(input("INGRESE EL VALOR DE B: "))
C = float(input("INGRESE EL VALOR DE C: "))


bb = (B) * (B)
AC = (A) * (C)
CuAC  = (-4) * (AC)
raiz =  ((bb + CuAC))


Sol = ((-B + (((B**2) - (4 * A * C)) ** 0.5 ))/2*A)*(-1)
Sol1 = ((-B - (((B**2) - (4 * A * C)) ** 0.5 ))/2*A)*(-1)


if (raiz < 0 ):
    print ("SON SOLUCIONES COMPLEJAS")

if (Sol != Sol1) and ( raiz >= 0):
    print( Sol, Sol1, "SON SOLUCIONES REALES DISTINTAS")

if (Sol == Sol1):
    print( Sol, Sol1, "SON SOLUCIONES REALES IGUALES")






