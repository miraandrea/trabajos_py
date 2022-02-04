#menu
print ()
print ("aplicacion de listas.")
print ()
y = 7
while y == 7:
    print ("0. explicacion sobre que son las listas")
    print ("1. Agregar un elemento a la lista")
    print ("2. Eliminar un elemento por su posición")
    print ("3. Buscar un dato que se encuentre en la lista y eliminarlo")
    print ("4. Editar o actualizar la información que contenga la lista en una posición especifica.")
    print ("5. Mostrar todos los valores que contiene la lista")
    print ("6. Mostrar una posición de la lista")
    print ("8. salir")
    print () 
    opciones = int(input("escoge una opcion que quieras: "))
    print()
    if opciones == 1:
        print("SOLO NUMEROS")
        print()
        lista = []
        otro = 0
        while otro < 2:
            n = int(input("que elemento quieres agregar a la lista: "))
            lista.append(n)  
            print(lista) 
            print()
            print ("quieres agregar otro elemento ")   
            otro= int(input("1 si ,7 volver al menu: "))
            print()
    elif opciones == 2:
        eliminar = lista
        otro2= 0
        while otro2 <2:
            print (eliminar)
            m= int(input("que elemento quieres eliminar: "))
            eliminar.pop(m)
            print (eliminar)
            print()
            print("quieres eliminar otro elemento")
            otro2 = int(input("1 si, 7 volver al menu: "))
            print ()
    elif opciones == 3:
        buscar = lista
        otro3= 0
        while otro3 <2:
            print(buscar)
            l= int(input("buscar un dato y eliminarlo: "))
            buscar.remove(l)
            print(buscar)
            print()
            print("quieres Buscar otro dato y eliminarlo")
            otro3 = int(input("1 si, 7 volver al menu: "))
            print()
    elif opciones == 4:
        print ()
        otro4= 0
        while otro4 <2:
            print(lista)
            ñ = int(input("donde quieres que valla coloque el indices: "))
            s = int(input("que quieres agregar a la lista: "))
            lista.insert(ñ,s)
            print(lista)
            print()
            print("quieres agregar otro elemento ")
            otro4 = int(input("1 si, 7 volver al menu: "))
            print()
    elif opciones == 5:
        valores=lista 
        print("contiene", len(valores),"valores que son",valores)
        otro5= int(input("7 volver al mnenu: "))
        print()
    elif opciones == 6:
        index = 0
        otro5= 0
        while otro5 <2:
            mostrar = []
            print(lista)
            p = int(input("Mostrar una posición de la lista: "))
            print()
            for q in lista:
                if q == p:
                    mostrar.append(index)
                index = index + 1
            index =0
            print("el elemento", p,"esta en la posicion", mostrar)
            print()
            print("quieres ver otra posición de la lista: ")
            otro5 = int(input("1 si, 7 volver al menu: "))
            print()
    elif opciones == 0:
        print ("Una lista en Python es una estructura de datos formada por una secuencia ordenada de objetos.") 
        print ("Los elementos de una lista pueden accederse mediante su índice, siendo 0 el índice del primer")
        print ("elemento.")
        print()
        fin = int(input("7 para volver al menu: "))
        print()
    elif opciones == 8:
        print("GRACIAS POR USAR LA APLICACION ^_^")
        print()
        vol= int(input("7 volver al menu: "))
        print()
    
    