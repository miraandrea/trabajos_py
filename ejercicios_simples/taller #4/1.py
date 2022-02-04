class nota:
    def __init__(self,nombreap):
        self.nombre = nombreap
        self.notap = ""
        self.notaa = ""
        self.notam = ""
    def notas(self,nota1,nota2,nota3):
        self.notap = nota1
        self.notaa = nota2
        self.notam = nota3
    def calcular(self):
        self.ñ= (self.notap + self.notaa + self.notam)/3
    def notafinal(self):
        print("el aprendiz",self.nombre , "su nota final es",self.ñ)

ae = nota("andrea")
ae.notas(3, 4, 1)
ae.calcular()
ae.notafinal()

pal = input("su nombre es:")
aep = nota(pal)
n= int(input("nota1: "))
n2= int(input("nota2: "))
n3= int(input("nota3: "))
aep.notas(n, n2, n3)
aep.calcular()
aep.notafinal()