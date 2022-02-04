#elaborar un algoritmo, que permita ingresar el nombre y el apellido de un aprendiz, luego solicitar la edad del papa y la mama, si la mama es mayor, decir -- Matriarcado al poder, de lo contrario, Patriarcado al poder, seguido del nombre del aprendiz.
aprendiz = input("nombre y apellido del aprendiz")
edad1 = int(input("edad del papa"))
edad2 = int(input("edad de la mama"))

if edad2 > 18:
    print("matricado al poder")
else:
    print("patricado al poder", aprendiz)
