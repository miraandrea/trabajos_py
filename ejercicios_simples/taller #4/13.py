# Calcular e imprimir la suma de S definida por la siguiente serie S = 1 – 2 + 3 – 4 + 5 – 6 … + n

contador = 1
n = int(input("valor de N: "))
textoSuma = "S = "
esPositivo = 1
suma = 0


while(contador <= n):
    print(contador)

    if(esPositivo == 1):
        #LA secuencia es positiva (el valor siguiente)
        textoSuma = textoSuma + " + " + str(contador)
        suma = suma + contador
        #Al final, cambiamos el valor de es Positivo, a no es positivo (Variable esPositivo)
        esPositivo = 0
    else:
        #La secuencia es negativa (El valor siguiete)
        textoSuma = textoSuma + " - " + str(contador)
        suma = suma - contador
        #Al final, cambiamos el valor de no es positivo a es positivo (Variable esPositivo)
        esPositivo = 1
    
    contador = contador + 1

print(textoSuma)
print("s = ", suma)