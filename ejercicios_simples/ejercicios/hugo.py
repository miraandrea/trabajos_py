from math import sqrt
def desviacion_estandar(valores, media):
    suma = 0
    for valor in valores:
        suma += (valor - media)**2

    radicando = suma / (len(valores)-1)
    return sqrt(radicando)

def calcular_media(valores):
    suma = 0
    for valor in valores:
        suma += valor
    return suma / len(valores)

if __name__ == "__main__":
    numeros = [3.15,5,6]
    mediap = calcular_media(numeros)
    resultado = desviacion_estandar(numeros, mediap)
    print("la desviacion estandar es: ", format(resultado))