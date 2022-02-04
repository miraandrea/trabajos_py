#Programa que lee 3 números enteros diferentes y los despliega de mayor a menor
n1 = int(input("ingrese un numero entero"))
n2 = int(input("ingrese otro numero entero"))
n3 = int(input("y otro numero entero"))
if n1>n2>n3:
    numeros = sorted ([n1,n2,n3],reverse=True)
    print("mayor a menor",numeros)
else:
    if n2>n3>n1:
        NUmeros= sorted ([n2,n3,n1],reverse=True)
        print("mayor a menor",NUmeros)
    else:
        nuMEROS= sorted ([n3,n1,n2],reverse= True)
        print("mayor a menor",nuMEROS)