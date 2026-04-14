class prova:
    def mostrar_prova(self):
        print("Olhe a prova!")

class professor_proxy:
    def __init__(self, prova_real):
        self.prova_real = prova_real

    def ver_prova(self, nome_aluno):
        print("Essa prova é sua?")

        if nome_aluno == "manuela":
            self.prova_real.mostrar_prova()
        else:
            print(" Essa prova não é sua, você não pode ver!")

prova_real = prova()
proxy = professor_proxy(prova_real)
proxy.ver_prova("manuela")
proxy.ver_prova("jose")


