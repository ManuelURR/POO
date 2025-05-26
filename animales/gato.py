class Gato(Animal):
    def __init__(self, nombre,edad,vidas):
        super().__init__(nombre.edad)
        self.vida = vidas

    def hacer_sonido(self):
        print("Miau!🐈")

    def sobrevive(self):
        if self.edad > 15 or self.vidas > 1:
            self.vidas -= 1
            self.edad = 1

        return self.vida > 0