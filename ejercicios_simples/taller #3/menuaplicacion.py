#menu
usuario = []
contraseña = []
y = 7
while y == 7:
    print("1. Agregar un usuario (Usuario y contraseña")
    print("2. Iniciar sesión")
    print("3. Eliminar un Usuario")
    print("4. Mostrar todos los usuarios registrados(Sin contraseña)")
    print("5. Buscar un usuario ")
    print("6. salir")
    print()
    opciones = int(input("que opcion quieres escoger: "))
    if opciones == 1:
        print()
        n = input("nombre de usuario: ") 
        m = input("contraseña: ")
        usuario.append(n)
        contraseña.append(m)
        print("se agrego corectamente")
        print()
    elif opciones == 2:
        p = input("usuario: ")
        q = input("contraseña")
        usuario.index(p)
        contraseña.index(q)
        print("inision correcta")
    elif opciones == 3:
        l = input("contraseña: ")
        i = input("usuario: ")
        contraseña.index(l)
        usuario.index(i)
        eliminar= input("nombre del usuario que quieres eliminar: ")
        if eliminar in usuario:
            el = usuario.index(eliminar)
            contraseña[el] 
            usuario.pop(el)
            contraseña.pop(el)
            print ("se elimio correctamente")
            print(usuario)
            print(contraseña)
    elif opciones == 4:
        print (usuario)
    elif opciones == 5:
        bus = input("nombre del usuario aquien quieres buscar: ")
        print()
        index =0 
        lista = len(usuario)
        while index < lista:
            if usuario[index]== bus:
                print("usuario: ",usuario[index])
                print("contraseña: ",contraseña[index])
            index = index +1
    elif opciones == 6:
        print("bye")
    y = int(input("quieres volver al menu 7: "))
        



    

        

