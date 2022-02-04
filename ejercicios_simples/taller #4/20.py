#Genere e imprima los números y la sumatoria de la serie fibbonaci: S = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, …, N.
n = int(input("ingrese un numero fibbonaci"))
a = 0
b = 1 

while (a <= n):
    print(a, end =' ')
    a, b = b, a+b
    print()



