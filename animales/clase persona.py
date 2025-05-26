
class Persona:
    nombre = ""
    edad = 0

    def saludar(self):
        print(f"hola, soy {self.nombre}")

    def setEdad(self, year):
        self.edad = 2025 - year

Persona1 = Persona()
Persona1.nombre = "Jaime"
Persona1.saludar()
Persona1.setEdad(1987)
print(Persona1.edad)
#print(Persona1)

Persona2 = Persona()
Persona2.nombre = "Santiago"
Persona2.saludar()
Persona2.setEdad(2006)
print(Persona2.edad)
