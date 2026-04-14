class morador:
    def abrir_porta(self):
        print("Porta aberta!")

class porteiro_proxy:
    def __init__(self, morador):
        self.morador = morador

    def pedir_entrada(self,nome_visitante):
        print("Quem é o visitante?")

        if nome_visitante == "manuela":
            self.morador.abrir_porta()
        else:
            print("Desculpe, você não pode entrar!")

manuela = morador()
porteiro = porteiro_proxy(manuela)
porteiro.pedir_entrada("manuela")
print()
porteiro.pedir_entrada("jose")
