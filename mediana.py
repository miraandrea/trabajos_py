
import statistics as stats
lista = []

def entero(numero):
    valor = int(input(numero))
    return valor

def cantidadx(numero):
    contador = 1
    while contador <= numero:
        contador = contador + 1
        x = float(input("numero: "))
        lista.append(x)
        lista.sort()

def mediana(lista):
    x =(stats.median(lista))
    print(str(x)+"000")

def fin():
    numero = entero("cantidad de numeros e ingresar: ")
    cantidadx(numero)
    mediana(lista)
fin()
