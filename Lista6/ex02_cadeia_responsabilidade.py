from abc import ABC, abstractmethod

class aprovador(ABC):
    def __init__(self, proximo_aprovador = None):
        self.proximo_aprovador = proximo_aprovador

    @abstractmethod
    def processar_pedido(self, valor):
        pass #só ignora e passa pra frente

class atendente(aprovador):
    def processar_pedido(self, valor):
        if valor <= 100:
            print("Atendente aprovou a compra.")
        elif self.proximo_aprovador:
            self.proximo_aprovador.processar_pedido(valor)

class gerente(aprovador):
    def processar_pedido(self, valor):
        if valor <= 500:
            print("Gerente aprovou a compra.")
        elif self.proximo_aprovador:
            self.proximo_aprovador.processar_pedido(valor)

class diretor(aprovador):
    def processar_pedido(self, valor):
        print("Diretor aprovou a compra.")

diretor = diretor()
gerente = gerente(diretor)
atendente = atendente(gerente)

atendente.processar_pedido(80)   
atendente.processar_pedido(300)  
atendente.processar_pedido(1500)




    