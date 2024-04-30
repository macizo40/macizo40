class Vehiculo:
    def __init__(self,modelo,marca) -> None: #si quiero retornar int para enteros, str para strings, lista es list, dict es para diccionario, float para numeros reales
        self.modelo = modelo
        self.marca = marca
    def mover(self) -> None:
        self._encender()
        print('Moviendose')
    def _encender(self)-> None:
        print('Encendiendose')
#Auto hereda de vehiculo, dentro del parentesis toda clase de la quiere heredar
class Auto(Vehiculo):
    def __init__(self, modelo, marca) -> None:
        super().__init__(modelo, marca)
        self.num_llantas = 4
    def mover(self) -> None:
        super()._encender()       
        print('Arrancando')

class Avion(Vehiculo):
    def __init__(self, modelo, marca) -> None:
        super().__init__(modelo, marca)
        self.num_llantas = 2
    def mover(self) -> None:
        super()._encender()       
        print('Despegando')

vehiculo = Vehiculo('Modelo1','Marca1')
carro = Auto('Nissan','Versa')
avion = Avion('Concor','F200') 

vehiculo.mover()
carro.mover()
avion.mover()

print(carro.num_llantas)
print(avion.num_llantas)