#Para calcular el factorial de un número se deben multiplicar todos los números previos a él y el
#mismo número, por ejemplo, el factorial de 6 es 1*2*3*4*5*6. Dado un número N calcular su
#factorial

n = int(input("ingrese el valor de n"))
for e in range (n):
    mul = e*e
    print (mul)
    