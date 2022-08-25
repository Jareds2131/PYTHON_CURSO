#ENTRADA
a = float(input("VALOR DE A: "))
b = float(input("VALOR DE B: "))
c = float(input("VALOR DE C: "))

#PROCESOS 
x_1 = ((-b) + (pow(b ** 2 - (4 * a*c),1/2)))/(2*a)
x_2 = ((-b) - (pow(b ** 2 - (4 * a*c),1/2)))/(2*a)

print("VALOR DE X1= ", x_1)
print("VALOR DE X2= ", x_2)


 
 