#Calcular e imprimir la serie y el valor de S definida por: S = 1 – 2 + 3 + 4 – 5 + 6 + 7 + 8 – 9 + 10 + 11 + 12 + 13 – 14 + … + N
contador = 1
n = int(input("valor de N: "))

textoSuma = "S = "
positivo = 0
esnegativo = 1
suma = 0

while(contador <= n):
    print(contador)

    if(positivo < esnegativo):
        textoSuma = textoSuma + " + " + str(contador)
        positivo =positivo + 1
        suma = suma + contador
    else:
        textoSuma = textoSuma + " - " + str(contador)
        positivo = 0
        esnegativo = esnegativo +1
        suma = suma - contador 

    contador = contador + 1
print(textoSuma)
print ("s=",suma)