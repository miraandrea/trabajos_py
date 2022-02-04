#Si se suman los números impares, se obtienen los cuadrados así:
contador = 1
n = int(input("valor de N: "))
textoSuma = "S = "
suma = 0
suMA = 0

while(contador <= n):
    print(contador)
    suma = suma + contador
    suMA = contador*2
    textoSuma = textoSuma + " + " + str(contador)
    textoSuma = textoSuma + " *2= " + str(contador)
    suma = suma + contador
    suMA = suMA**2
    contador = contador + 1

print(textoSuma)

