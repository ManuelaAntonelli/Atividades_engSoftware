class Carro:
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo

    def clone(self):
        return Carro(self.cor, self.modelo)


c1 = Carro("vermelho", "Sandero")
c2 = c1.clone()

c2.cor = "azul"
c2.modelo = "Onix"

print(c1.modelo, c1.cor)  
print(c2.modelo, c2.cor)  

#Matheus, Jose, Victor, Manuela