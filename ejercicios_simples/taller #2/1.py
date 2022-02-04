#determinar si un alumno aprueba o reprueba un curso, si su promedio de 4 calificaciones es mayor 
# o igual a 3,5; encaso contrario reprueba 
n1 = int(input("ingrese la 1 calificaciones:"))
n2 = int(input("ingrese la 2 calificaciones:"))
n3 = int(input("ingrese la 3 calificaciones:"))
n4 = int(input("ingrese la 4 calificaciones:"))
promedio = (n1 + n2 + n3 + n4)/4

if promedio >= 3.5 :
    print("aprobo",promedio)
else:          
    print("reprobo",promedio)
 