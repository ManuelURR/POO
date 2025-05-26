from animal import Animal
from gato import Animal
from perro import Animal
from zoo import Zoo
from ave import Ave
from murcielago import Murcielago
from ornitorrinco import Ornitorrinco

def main():
    pass
    mascota = Animal("pelu", 5)
    mascota.comer()
    #print(type(mascota), mascota)
    mascota = Perro("pelu", 5,"chihuahua")
    #print(type(mascota), mascota)
    mascota.comer()
    mascota = Gato("Pelu", 5, 9)
    #print(type(mascota), mascota)
    mascota.comer()
    
    zoo = Zoo()

    leon = Animal("simba", 3)
    tigre = Animal("Tigger", 4)
    gato = Gato("Miau", 2, 9)
    perro = Perro("Rex", 1, "Canaria")
    ave = Ave("pajaro", 1, "Canario")
    murcielago = Murcielago("Murci", 2, "Murcielago")
    ornitorrinco = Ornitorrinco("Orni", 3, "Ornitorrinco") 

    zoo.agregar_animal(leon)
    zoo.agregar_animal(tigre)
    zoo.agregar_animal(gato)
    zoo.agregar_animal(perro)
    zoo.agregar_animal(ave)
    zoo.agregar_animal(murcielago)
    zoo.agregar_animal(ornitorrinco)

    zoo.alimentar_animales()

if __name__ == "__main__":
    main()