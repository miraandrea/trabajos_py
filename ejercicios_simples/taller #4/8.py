#Leer el valor de N, imprimir y sumar los números de 1 a N.
numero = int(input("valor n"))
print (numero)
suma = 0
contador = 1
while(contador <= numero):
    print ( contador )
    suma = suma + contador
    print ("suma",suma)
    contador = contador + 1
