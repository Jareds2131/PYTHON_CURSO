#Calculadora Financiera

#c = int( input("INGRESE EL CAPITAL:")) t = float(input("INGRESE LA TASA DE INTERES")) P = int(input("INGRESE LOS MESES QUE GUSTARÍA INVERTIR SU DINERO"))

c = int( input("INGRESE EL CAPITAL: "))
t = 0.09
P = int(input("INGRESE LOS MESES QUE GUSTARÍA INVERTIR SU DINERO: "))


Rendimiento = c* (1+t)**P
RenPorMes = Rendimiento/P

print("SU RENDIMIENTO ES", round( Rendimiento, 2))
print("SU RENDIMIENTO POR MES ES DE: ", round(RenPorMes,2))

#print("Su rendimiento por mes es de:", RPM)
