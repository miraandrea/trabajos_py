#elabore un algoritmo que sirva para identificar el tipo de triangulo conociendo sus tres lados
l1= int(input("ingrese el lado 1 del triangulo"))
l2= int(input("ingrese el lado 2 del triangulo"))
l3= int(input("ingrese el lado 3 del triangulo"))
if l1==l2:
    print("es un triangulo equilatero")
else:
    if l1==l3:
        print("es un triangulo isoceles")
    else:
        if l2==l3:
            print("es un triangulo isoceles")
        else:
            print("es un triangulo escaleno")
            