# Imprimir la serie de los N primeros números impares y la suma de ellos.
suma = 0
for e in range (11):
    impar = (e % 2) 
    if impar == 0 :
        print ()
    else :
        suma = suma + e 
        print (e,suma)
        