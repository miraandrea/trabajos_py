#El promedio de prácticas de un curso se calcula con base en cuatro prácticas calificadas de las cuales se elimina la nota menor y se promedian las tres notas más altas. Diseñe un algoritmo que determine la nota eliminada y el promedio de prácticas de un estudiante.
print ("promedio")
n1 = int(input("nota 1"))
n2 = int(input("nota 2"))
n3 = int(input("nota 3"))
n4 = int(input("nota 4"))
if n1 < n2 and n1 < n3 and n1 < n4:
    suma = n2+n3+n4
    PROMEDIO = suma/4
    print ("se elimina",n1,PROMEDIO)
else:
    if n2 < n1 and n2 < n3 and n2 < n4:
        suMA = n1+n3+n4
        promedio = suMA/4
        print (n2,"se elimina", promedio)
    else:
        if n3 < n1 and n3 < n2 and n3 < n4:
            SUMa = n2+n1+n4
            promEDIO = SUMa/4
            print ("el",n3, " se elimina",promEDIO)
        else:
            SuMA = n1+n2+n3
            PROmedio = SuMA/4
            print ("se elmina el",n4,PROmedio)
