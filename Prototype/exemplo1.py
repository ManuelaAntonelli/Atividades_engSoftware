class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def clone(self):
        return Personagem(self.nome, self.vida)


p1 = Personagem("Herói", 100)
p2 = p1.clone()

p2.nome = "Vilão"

print(p1.nome)  
print(p2.nome)  

#Matheus, Jose, Victor, Manuela