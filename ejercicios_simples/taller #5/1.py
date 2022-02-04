class veterinario: 
    def __init__(self,nom,e,raz):
        self.nombreMascota = nom
        self.edad = e
        self.raza = raz
        self.vacuna1 = ""
        self.vacuna2 = ""
        self.vacuna3 = ""
    def vacunas(self,vacuna11):
        self.vacuna1 = vacuna11
    def va(self,vacuna22):
        self.vacuna2 = vacuna22
    def vacu(self,vacuna33):
        self.vacuna3 = vacuna33
    def resul(self):
        print(self.vacuna1)
        print(self.vacuna2)
        print(self.vacuna3)

nombre =input("nombre de la mascota: ")
ed =int(input("edad de la mascota: "))
ra = input("cual es la raza de tu mascota: ")
variable = veterinario(nombre, ed, ra)
variable.vacunas("vacuna1: rabia")
variable.va("vacuna2: moquillo")
variable.vacu("vacuna3: parvovirosis")
variable.resul()
