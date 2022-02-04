#Diseñe un algoritmo que lea un número de tres cifras y determine si es o no capicúa. Un número es 
# capicúa si es igual al derecho y al revés del número
numero = int(input("ingresa un numero de tres cifras"))
if numero%10==(numero%1000-numero%100)//100:
    print("si es capicua")
else:
    print("no es capicua")

