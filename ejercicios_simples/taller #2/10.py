#Un obrero necesita calcular su salario semanal, el cual se obtiene de la siguiente manera: Si trabaja 
# 40 horas o menos se le paga un salario de $16 por hora, si trabaja más de 40 horas se le paga un salario 
# de $16 por cada una de las primeras 40 horas y un salario de $20 por cada hora extra
horas = int(input("cuantas horas elaboro"))
pago = (horas*16)
if horas < 40:
    print("su pago es",pago)
else:
    PAGO = horas -40
    PAGO = (horas*20)
    print("su pago es", PAGO)
