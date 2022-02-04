#Generar e imprimir la serie y la suma definida por: S = 2/3 + 4/5 + 6/7 + 8/9 + …+(N*2)/(N*2 + 1)

contador = 2
n = int(input("ingrese un numero: \n"))
textoSuma = "S = "
division = 2
suma = 0

while(contador <= n):
    print(contador)

    if(division == 1):
        textoSuma = textoSuma + " / " + str(contador)
        suma = suma % contador
        division = 0
    else:
        textoSuma = textoSuma + " + "+ str(contador) 
        suma = suma + contador 
        division = 1

    contador = contador + 1

print(textoSuma)
print("s = ", suma)
