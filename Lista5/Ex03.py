'''3) Implementar em Python (ou Java ou C++) os 3 exemplos apresentados a partir da transparência
64 da aula 15.'''

#prototype -> clonar um objeto já pronto em vez de criar um do zero neah

import copy

class Carro:
    def __init__(self, modelo, cor, motor):  #aqui é tipo o molde do carro
     self.modelo = modelo
     self.cor = cor
     self.motor = motor

    def clone(self):
        return copy.deepcopy(self)
    def mostrar(self):
       print(f"O modelo do carro é: {self.modelo}")
       print(f"A cor do carro é: {self.cor}")
       print(f"O motor do carro é: {self.motor}")

carro_original = Carro("SUV", "Preto", "2.0")
carro_clone = carro_original.clone()  #aqui eu criei uma variável "carro_clone" e guardei uma cópia dentro dela
carro_clone.cor = "Roxão"
carro_clone.motor = "V10"

print("Original: ")
carro_original.mostrar() 
print("\n")
print("Cópia: ")
carro_clone.mostrar()



    





