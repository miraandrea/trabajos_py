#elabore un algoritmo para leer 3 numeros enteros diferentes entre si y determinar el numero mayor de los 
# tres
print("ingrese tres numero")
n1 = int(input("numero 1:"))
n2 = int(input("numero 2:"))
n3 = int(input("numero 3:"))
diferentes = n1!=n2 and n2!=n3 and n3!=n1
if  n1>n2 and n1>n3 and diferentes:
    print (n1, "es mayor y diferentes",diferentes)
elif n2>n3 and n2>n1 and diferentes:
    print(n2,"es mayor y diferentes",diferentes)
else:
    print(n3,"es mayor y diferesntes",diferentes)
          
