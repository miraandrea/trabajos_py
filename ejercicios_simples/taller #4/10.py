#Imprimir la serie de los N primeros números impares y la suma de ellos.
numero = int(input("ingrese un numero"))
suma = 0
contador = 1
impares = 1
while(contador <= numero):
    contador = contador + 1
    print ( impares )
    suma = suma + contador
    print ("suma",suma)
    impares = impares + 3 -1
