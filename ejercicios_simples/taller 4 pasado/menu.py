print ("buenas tardes carlos")
print ()
print("6: Imprimir cinco veces la palabra “Sena”")
print("7: Leer el valor de N e imprimir los primeros N números naturales")
print("8: Leer el valor de N, imprimir y suma los números de 1 a N")
print("9: Calcular la suma de los primeros N números pares")
print("10: Imprimir la serie de los N primeros números impares y la suma de ellos")
print()
opcion = int(input("Que numero deseas escoger:"))
if opcion == 6:
    print ("elegiste la opcion 6")
    print ()
    for e in range (5):
        print("sena")
elif opcion == 7:
    print ("elegiste la opcion 7")
    print ()
    numero = int(input("ingrese valor de n"))
    for e in range (numero + 1)  :
        print (e)
elif opcion == 8:
    print ("elegiste la opcion 8")
    print ()
    n = int(input("ingrese el valor de n"))
    suma= 0
    for e in range (n+1) :
        suma = suma + e
        print (e)
        print ()
    print ("suma",suma)
elif opcion== 9:
    print ("elegiste la opcion 9")
    print ()
    n= int(input("ingrese el valor de n"))
    suma = 0
    for e in range (n+1):
        par = (e % 2) 
        if par == 0 :
            suma = suma + e 
            print (e)
        else:
            print ()
    print ("suma",suma)
elif opcion == 10 :
    print ("elegiste la opcion 10")
    print ()
    n= int(input("ingrese el valor de n"))
    suma = 0
    for e in range (n+1):
        impar = (e % 2) 
        if impar == 0 :
            print ()
        else :
            suma = suma + e 
            print (e)
    print ("suma",suma)
else:
    print ("bye")