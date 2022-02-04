# en un almacen se hace un 20% de descuento cuya compra supere $1000, cual sera la cantidad que 
# pagara una persona por su compra 
compra = int(input("cuanto compro"))
if compra > 1000:
    descuento = (compra*0.2)
    print("tiene descuento",descuento)
else:
    print("no tiene descuento")
 