#menu
mascota = []
propetario = []
telefono = []
y=6
while y == 6:
    print("1. Agregar una mascota ")
    print("2. Consultar el teléfono del propietario ")
    print("3. Eliminar una mascota")
    print("4. Mostrar los datos ")
    print("5. salir")
    opciones = int(input("que opcion quieres eligir: "))
    print()
    if opciones == 1:
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
    elif opciones == 2:
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
    elif opciones == 3:
        l = input("nombre del propetario: ")
        i = int(input("telefono: "))
        propetario.index(l)
        telefono.index(i)
        contador = 0
        listados = len(propetario)
        listados = len(telefono)
        while contador < listados:
            if propetario[contador]== l:
                print()
                if telefono[contador] == i:
                    print()
                    if l in propetario:
                        el = propetario.index(l)
                        mascota[el] 
                        mascota.pop(el)
                        propetario.pop(el)
                        telefono.pop(el)
                        print ("se elimio correctamente")
                else:
                    print("ingreso un dato mal")
            contador= contador+1

    elif opciones == 4:
        print("nombre de las mascotas: ",mascota)
        print("nombre de los propetarios: ",propetario)
        print("numero de telefono: ",telefono)
    elif opciones == 5:
        print("bye")
    y = int(input("volver al menu el numero 6: "))