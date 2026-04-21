from abc import ABC, abstractmethod

class bebida_quente(ABC):
    def preparar_bebida(self):
        self.ferver_agua()
        self.adicionar_ingredientes()
        self.servir()

    def ferver_agua(self):
        print("Fervendo a agua.")

    def servir(self):
        print("Servindo a bebida.")

    @abstractmethod #para uma etapa que tem que ser diferente nas duas bebidas
    def adicionar_ingredientes(self):
        pass

class cafe(bebida_quente):
    def adicionar_ingredientes(self):
        print("Adicionando café e açucar.")
    
class cha(bebida_quente):
    def adicionar_ingredientes(self):
        print("Adicionando chá")

meu_cafe = cafe()
meu_cafe.preparar_bebida()

print()

meu_cha = cha()
meu_cha.preparar_bebida()



