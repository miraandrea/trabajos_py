#Una frutería ofrece las manzanas con descuento según la siguiente tabla
kilo = int(input("ingresa el kilo:"))
if kilo <= 2:
    descuento = (kilo*0)
    print ("no tiene descuento")
else:
    if (kilo >= 2.01) and (kilo <= 5):
        DEScuento = (kilo*10/100)
        print ("su descuento es",DEScuento)
    else:
        if (kilo >= 5.01) and (kilo <= 10):
            descueNto = (kilo*15/100)
            print ("su descuento es", descueNto)
        else:
            desCUENTO = (kilo*20/100)
            print ("su descuento es",desCUENTO)