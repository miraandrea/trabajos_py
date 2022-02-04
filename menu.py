
#Estos dos algoritmos deben estar en un MENU, es decir, elegir una de las opciones que quiero 
# verificar y posteriormente ejecutar el algoritmo
print ("buenas tardes instructor carlos")
menu = int(input("quieres ver el menu escruiba el numero 3:"))
if (menu == 3):
    print("1) cuanto pago la empresa")
    print("2) los numeros primos")
opciones = int(input("opcion elegida:"))
if (opciones == 1):
    nempleados = int(input("cuantos empleados hay en la empresa:"))
    contador = 1
    suma = 0
    while (contador <=nempleados):
        sueldo =int(input("ingrese el sueldo:"))
        dias = int(input("dias que trabajaron en la semna :"))
        horas = int(input("horas que trabajaron cada dia:"))
        pago = sueldo*dias*horas
        print ("el sueldo semanal del empleado es",pago)
        contador = contador + 1
        suma = suma + pago 
    print("la empresa paga por los empleados", suma)
        
        
elif (opciones == 2):
    n= int(input("ingrese el numero que quieres ver de numeros primos:"))
    contador = 1
    while (contador <= n):
        if (n % contador == 0):
            print(contador)
            contador = contador + 1
        else: 
            print ("")
    contador = contador + 1

print ("gracias por usar nuestro servico ")
