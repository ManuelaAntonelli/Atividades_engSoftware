from abc import ABC, abstractmethod

class Caractere(ABC):
    @abstractmethod
    def desenhar(self, linha, coluna):
        pass

class CaractereConcreto(Caractere):
    def __init__(self, simbolo):
        self.simbolo = simbolo 

    def desenhar(self, linha, coluna):
        print(f"Caractere '{self.simbolo}' na posição ({linha}, {coluna})")

class FabricaDeCaracteres:
    def __init__(self):
        self.caracteres = {}

    def get_caractere(self, simbolo):
        if simbolo not in self.caracteres:
            self.caracteres[simbolo] = CaractereConcreto(simbolo)
        return self.caracteres[simbolo]

class EditorTexto:
    def __init__(self):
        self.fabrica = FabricaDeCaracteres()
        self.texto = []

    def adicionar_caractere(self, simbolo, linha, coluna):
        caractere = self.fabrica.get_caractere(simbolo)
        self.texto.append((caractere, linha, coluna))

    def renderizar(self):
        for caractere, linha, coluna in self.texto:
            caractere.desenhar(linha, coluna)

editor = EditorTexto()

editor.adicionar_caractere('A', 1, 1)
editor.adicionar_caractere('A', 1, 2)
editor.adicionar_caractere('B', 2, 1)

editor.renderizar()