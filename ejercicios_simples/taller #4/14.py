#Calcular e imprimir el valor de S definida por la siguiente serie S = 1/12 + 1/32 + 1/52 + 1/72 + 1/N2
n = int(input("ingrese un numero"))
textosuma = "s="
contador = 1
while (contador <= n):
    print (textosuma , "1/" , contador ,"^2" , "+")
    contador = contador + 3 -1