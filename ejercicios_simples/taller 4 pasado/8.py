#Leer el valor de N, imprimir y sumar los números de 1 a N.
n = int(input("ingrese el valor de n"))
suma= 0
for e in range (n+1) :
    suma = suma + e
    print (e)
    print ()
    print ("suma",suma)
    
    