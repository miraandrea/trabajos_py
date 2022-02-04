n= int(input("ingrese un numero:"))
divi= 0
contador = 1
while contador <= n:
    if n % contador == 0:
        divi= divi + 1
    contador = contador + 1
    if divi == 2:
        print (contador)
    else: 
        print ("")





n= int(input("ingrese un numero:"))
contador = 1
while contador <= n:
    mult= contador  % 2  and contador % 3  and contador % 5  and contador % 7 
    if mult == 0:
        print ("")
    else:
        print (contador)
    contador = contador + 1
