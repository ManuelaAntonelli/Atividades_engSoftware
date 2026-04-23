'''3) Apresentar 2 exemplos práticos da utilização do design pattern Facade na linguagem Python (ou
Java ou C++).'''

'''Exemplo 1

class Luzes:
    def ligar(self):
        print("Luzes ligadas!")
    def desligar(self):
        print("Luzes apagadas para assistir na televisão!")

class Som:
    def configurar_volume(self, nivel):
        print(f"Volume ajustado para: {nivel}") #MEU DEUS EU TÔ ENTENDENDO. MEU DEUSSSSSS


#Aqui que eu vou inicializar
class FachadaHomeTheater:
    def __init__(self):
        self.luz = Luzes()
        self.som = Som()

    def assistir_filme(self):
        print("Preparando ambiente...")
        self.luz.desligar()
        self.som.configurar_volume(45)

        print("Tudo pronto para iniciar o filme!")

home_cinema = FachadaHomeTheater()
home_cinema.assistir_filme()
'''


'''Exemplo 2'''

class Estoque:
    def baixar_item(self):
        print("Item baixado no estoque.")

class Pagamento:
    def realizar_pagamento(self):
        print("Pagamento processado.")

class Logistica:
    def gerar_frete(self):
        print("Frete calculado para o endereço informado.")

#Aqui eu começo a inicialização
class FachadaCompra:
    def __init__(self):
        self.produto = Estoque()
        self.valor = Pagamento()
        self.endereco = Logistica()

    def finalizar_compra(self,item): 
        print(f"Iniciando check-out para: {item}")

        #aqui eu chamo os métodos lá de cima. ÊEEEEEEEEEEEE
        self.produto.baixar_item()
        self.valor.realizar_pagamento()
        self.endereco.gerar_frete()
        print("Compra realizada com sucesso!")

#Essa parte aqui é do cliente, como eu não fiz interativo, já vou deixar uma opção pronta neah
comprar = FachadaCompra()
comprar.finalizar_compra("Notbook mágico para programar que não seja o meu")


