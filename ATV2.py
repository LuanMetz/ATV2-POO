# Classe base
class Transporte:
    def mover(self):
        return "O transporte está se movendo..."


# Classe filha Carro
class Carro(Transporte):
    def mover(self):
        return "O carro está rodando pela estrada."


# Classe filha Moto
class Moto(Transporte):
    def mover(self):
        return "A moto está acelerando."


# Classe filha Bicicleta
class Bicicleta(Transporte):
    def mover(self):
        return "A bicicleta está pedalando."


# Lista com os objetos das classes
transportes = [Carro(), Moto(), Bicicleta()]

# Percorrendo a lista e chamando mover()
for t in transportes:
    print(t.mover())
