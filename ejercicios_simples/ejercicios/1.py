#s=2+4-6+8+10-9+11+13-15+17+19-18...N
contador = 2
n = int(input("valor de N: "))
textoSuma = "S = "
positivo = 0
esnegativo = 1
while(contador  <= n ):
    if positivo < 2:
        textoSuma = textoSuma + " + " + str(contador)
        positivo = positivo + 1
    else:
        textoSuma = textoSuma + " - " + str (contador)
        positivo = 0
    
    if esnegativo == 5:
        contador = contador - 1
        esnegativo = 0
    
    else :
        esnegativo = esnegativo +1
        contador = contador + 2
print (textoSuma)