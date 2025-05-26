#get leer
#set escribir
from multipledispatch import dispatch
class Podometro:
        __pasos = -1

        
        def __init__(self, pasos=0):
            self.__pasos = pasos

        @dispatch()
        def contar(self):
             self.__pasos += 1

        @dispatch(int)
        def contar(self, pasos=1):
             self.__pasos += pasos
        
        @dispatch(int, int)
        def contar(self, pasos, saltos = 0):
             self.__pasos += pasos + (2 * saltos)

        def getPasos(self):
            return self.__pasos

        def __add__(self, cuenta):
             return Podometro(self.getPasos() + cuenta.getPasos())
        
        def __sub__(self, cuenta):
             return Podometro(self.getPasos() - cuenta.getPasos())

        def __str__(self):
             return str(self.getPasos()) + "🤰🏻"

        def calcularDistancia(self, pasos = 0, unidad = "m"):
             if pasos == 0:
               return self.getPasos() * 0.7
             else:
               return pasos * 0.7
          
        def distanciaPasos(self, distancia = 0, unidad = "m"):
          _distancia = self.__convertidorDistancia(distancia, unidad)
          return round(distancia / 0.7)
        
        def saltar(self):
          self.contar(2)

        def __convertidorDistancia(self, distancia = 0, unidad = "m"):
          match unidad:
               case "cm":
                    return distancia / 1000
               case "m":
                    return distancia
               case "km":
                    return distancia * 1000
               case _:
                    return distancia


pod1 = Podometro(5)
print(pod1.getPasos())
pod1.contar()
pod1.contar(3)
#pod1.contar(1, 2)
print(pod1)
print(f"5,000 pasos equivalen {pod1.calcularDistancia[5000]}")
pod1.saltar()
#print(f"distancia actual{pod1.calcularDistancia}:.2f")
print(f"1km equivale a {pod1.distanciaPasos{150,"m"}}")
#pod2 = Podometro(7)
#pod3 = pod1 + pod2
#print(pod3.getPasos())
#pod4 = pod2 - pod1
#print(pod4)


