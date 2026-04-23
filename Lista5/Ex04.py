'''4) Implementar em Python (ou Java ou C++) o exercício da transparência 16 da aula 16.'''

class RealImage:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.carregar_do_disco()

    def carregar_do_disco(self):
        print(f"Carregando {self.nome_arquivo} do disco...")
    
    def exibir(self):
        print(f"Renderizando {self.nome_arquivo}")

class ProxyImage:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.imagem_real = None

    def exibir(self):
        if self.imagem_real == None:
            self.imagem_real = RealImage(self.nome_arquivo)
        else:
            print("Imagem já estava na memória. não há necessidade de mais um carregamento!")
        
        self.imagem_real.exibir()

#aqui eu vou testar o proxy que fiz
arquivo = "foto_gigante_da_kali_uchis.png"
imagem = ProxyImage(arquivo)

print("1º tentativa")
imagem.exibir()

print("\n2º tentativa")
imagem.exibir()
