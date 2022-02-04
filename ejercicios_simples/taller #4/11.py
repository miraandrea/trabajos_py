#Para calcular el factorial de un número se deben multiplicar todos los números previos a él y el
#mismo número, por ejemplo, el factorial de 6 es 1*2*3*4*5*6. Dado un número N calcular su
#factorial

numero = int(input("ingrese un numero:"))
factorial = 1
fa= 2
contador = 1
while (contador <= numero):
    factorial = factorial * fa
    fa=fa+1
    contador = contador + 1
    print ("factorial",contador,"es",factorial)

