cantidadBodega = int(input("ingrese la cantidad de bodega: "))
cantidadMinima = int(input("ingrese la cantidad minima: "))

if cantidadBodega > cantidadMinima:
    resta = cantidadBodega - cantidadMinima
    if resta < 10:
        print("El pedido fue realizado exitosamente")
        print("¡Alerta! el lote es menor de 10.")
    else:
        print("No es necesario realizar el pedido, unidades hacen falta para vender: ", resta)
if cantidadBodega < cantidadMinima:
    print("Es necesario realizar el pedido")
    cantidadDeseada = int(input("Ingrese la cantidad deseada: "))
    valorCompra = int(input("valor de compra unidad: "))
    multiplicacion = valorCompra * cantidadDeseada
    caja = int(input("Presupuesto de la caja: "))

    if multiplicacion > caja:
        print("El presupuesto no alcanza para las unidades extras.")
    else:
        print("Si es posible realizar el pedido")

