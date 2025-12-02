# Classe base
class Transporte:
    def mover(self):
        return "O transporte está se movendo..."


# Classes filhas com polimorfismo
class Carro(Transporte):
    def mover(self):
        return "O carro está rodando pela estrada."


class Moto(Transporte):
    def mover(self):
        return "A moto está acelerando."


class Bicicleta(Transporte):
    def mover(self):
        return "A bicicleta está pedalando."



# Criando os objetos
transportes = [
    Carro(),
    Moto(),
    Bicicleta()
]

# Demonstrando polimorfismo
for t in transportes:
    print(t.mover())
