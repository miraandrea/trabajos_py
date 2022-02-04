#s=2+4-6+8+10-9+11+13-15+17+19-18...N
#S= 1+2-3+6+7-8+11+12-13
contador = 2
n = int(input("valor de N: "))

textoSuma = "S = "
positivo = 1
esnegativo = 3
while(contador <= 11):
    
    if esnegativo > positivo :
        textoSuma = textoSuma + " + " + str(contador)
        positivo = positivo + 1
    else:
        textoSuma = textoSuma + " - " + str (contador)
        positivo = 0
        esnegativo = esnegativo + 1
    if contador == 10:
        resta = contador - 1
        textoSuma = textoSuma + " - " + str (resta)
    contador = contador + 2
contador = 11
while (contador <=19):
    if esnegativo > positivo :
        textoSuma = textoSuma + " + " + str(contador)
        positivo = positivo + 1
    else:
        textoSuma = textoSuma + " - " + str (contador)
        positivo = 0
        esnegativo = esnegativo + 1
    if contador == 19:
        resta = contador - 1
        textoSuma = textoSuma + " - " + str (resta)
    contador = contador + 2
print(textoSuma)

