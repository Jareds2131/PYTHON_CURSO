# ENTRADAS

pago = 250 
diasTrabajados = 31

#PROCESO
bruto = pago * diasTrabajados
ivaTras = bruto * 0.16
subTotal = bruto + ivaTras
ivaRet = ivaTras * 2/3
isrRet = bruto * .10
pagoNeto = subTotal - ivaRet - isrRet


 
#Salida
print("TU PAGO BRUTO ES DE: ",round(bruto,2))
print("TU IVA TRASLADADO ES DE: ",round(ivaTras,2))
print("TU SUB TOTAL ES DE: ",round(subTotal,2))
print("TU  IVA RETENIDO ES DE: ",round(ivaRet,2))
print("TU ISR RETENIDO ES DE: ",round(isrRet,2))
print("TU PAGO NETO ES DE: ",round(pagoNeto,2))
