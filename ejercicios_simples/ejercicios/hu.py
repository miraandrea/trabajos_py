numero= int(input("ingrese un numero: "))
for e in range(1,numero+1):
    divisible = e % 3
    divi = e% 5
    if divisible == 0:
        print(e,"divisible",3) 
    elif divi == 0: 
        print(e,"divisible",5)
    else:
        print(e)



