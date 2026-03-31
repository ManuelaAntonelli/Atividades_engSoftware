import copy

class mascote:
    def __init__(self, cor, acessorio):
        self.cor = cor
        self.acessorio = acessorio
        self.dados_pesados = "Banco de dados carregados..." 

    def clonar(self):
        """Retorna uma cópia exata deste objeto."""
        return copy.deepcopy(self)

    def __str__(self):
        return f"mascote{self.cor} com {self.acessorio}"

mascote_original = mascote("Verde", "Nenhum")
print("Original criado:", mascote_original )

mascote_pirata = mascote_original.clonar()

mascote_pirata.acessorio = "Chapéu de Pirata e Tapa-olho"
print("Clone modificado:", mascote_pirata)