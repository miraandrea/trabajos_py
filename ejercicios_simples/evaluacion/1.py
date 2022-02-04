mascota = []
propetario = []
telefono = []
def opcion1 ():
    n = input("nombre de la mascota: ") 
    m = input("nombre del propetadrio: ")
    if m in propetario:
        print("no se puede permitir dos mascotas con el mismo propetario")
    else:
        ñ = int(input("numero de telefono: "))
        mascota.append(n)
        propetario.append(m)
        telefono.append(ñ)
        print("se agrego corectamente")
    print()
def opcion2():
    mas = input("nombre de la mascota: ") 
    pro = input("nombre del propetadrio: ")
    mascota.index(mas)
    propetario.index(pro)
    print()
    index =0 
    lista = len(mascota)
    lista = len(propetario)
    while index < lista:
        if mascota[index]== mas:
            if propetario[index]==pro:
                print("el numero de telefono es: ",telefono[index])
                print()
            else:
                print("ingreso un dato mal")
        index = index +1
def opcion3 ():
    dueño = input("nombre del propetario: ")
    tel = int(input("telefono: "))
    propetario.index(dueño)
    telefono.index(tel)
    contador = 0
    listados = len(propetario and telefono)
    while contador < listados:
        if propetario[contador]== dueño:
            if telefono[contador] == tel:
                if dueño in propetario:
                    el = propetario.index(dueño)
                    mascota[el] 
                    mascota.pop(el)
                    propetario.pop(el)
                    telefono.pop(el)
                    print ("se elimio correctamente")
            else:
                print("ingreso un dato mal")
        contador= contador+1
def opcion4 ():
    print("nombre de las mascotas: ",mascota)
    print("nombre de los propetarios: ",propetario)
    print("numero de telefono: ",telefono)
def opcion5 ():
    print("bye")
y=6
while y == 6:
    print()
    print("1. Agregar una mascota ")
    print("2. Consultar el teléfono del propietario ")
    print("3. Eliminar una mascota")
    print("4. Mostrar los datos ")
    print("5. salir")
    opciones = int(input("que opcion quieres eligir: "))
    print()
    if opciones == 1:
        opcion1()
        y = int(input("volver al menu el numero 6: "))
    elif opciones == 2:
        opcion2()
        y = int(input("volver al menu el numero 6: "))
    elif opciones == 3:
        opcion3()
        y = int(input("volver al menu el numero 6: "))
    elif opciones == 4:
        opcion4()
        y = int(input("volver al menu el numero 6: "))
    elif opciones == 5:
        opcion5()
        y = int(input("volver al menu el numero 6: "))
