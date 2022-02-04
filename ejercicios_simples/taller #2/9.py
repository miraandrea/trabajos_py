# Un comerciante compra un artículo a un costo dado. Determine el precio al cual debe venderlo si 
# desea ganar el 15% para valores inferiores a 100000 y 10% para valores superiores.
compra = int(input("en cuanto lo quiere vender"))
if compra > 100000:
    descuento = (compra*15/100)
    print("gana ",descuento)
else:
    print("no gana ")
