from animal import Animal
from perro import Perro
from gato import Gato
from ave import Ave
from murcielago import Murcielago
from ornitorrinco import Ornitorrinco

def main():
    leon = Animal("leon", 5)
    leon.hacer_sonido()

    perro = Perro("churro",3, "salchicha")
    perro.hacer_sondo()
    print(perro.es_cachorro())

    gato = Gato("michi", 2, 7)
    gato.hacer_sonido()
    print("vidas restantes", gato.vidas)
    print("Atropelladi 🙈" if not gato.sobrevive() else "vive 😎")
    print("vidas restantes", gato.vidas)
    print("Intoxicado 🙈" if not gato.sobrevive() else "vive 😎")
    print("vidas restantes", gato.vidas)
    print("Electrocutado 🙈" if not gato.sobrevive() else "vive 😎")
    print("vidas restantes", gato.vidas)

    ave = Ave("KP", 1)
    ave.hacer_sonido()

    dracula = Murcielago("Dracula",100,"Vampiro")
    dracula.hacer_sonido()
    dracula.soy_un()

    perry = Ornitorrinco("perry", 5)
    perry.hacer_sonido()
    print(f"{perry.nombre} hapuesto {perry.NUMERO_HUEVOS} huevos")
    for i in range (3):
        perry.poner_huevos() 
        print(f"{perry.nombre} hapuesto {perry.NUMERO_HUEVOS} huevos")


if __name__ == "__main__":
    main()