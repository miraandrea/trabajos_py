#Generar e imprimir la serie y la suma los primero N números múltiplos de M
n = int(10)
numero = int(input("ingese un numero"))
suma = 0
multiple = 1
contador = 1
while(contador <= n):
    print ( contador )
    suma = suma + contador
    multiplo = contador  * numero 
    print ("suma",suma, " multiplo",multiplo)
    multiplo = multiplo + 1
    contador = contador + 1
