class base:
    def atributo(self):
        return "atributo base"
    
class decorador(base):
    def __init__(self, base):
        self.base = base
    def atributo(self):
        return self.base.atributo()

class decorador1(decorador):
    def atributo(self):
        return self.base.atributo() + " decorado 1 vez" 

class decorador2(decorador):
    def atributo(self):
        return self.base.atributo() + " decorado 2 vezes"

teste = base()
teste = decorador1(teste)
teste = decorador2(teste)
print(teste.atributo())    
##########################################################################    
class pizzabase:
    def sabor(self):
        return "massa, molho, queijo"
    
class decorador_pizza(pizzabase):
    def __init__(self, pizza):
        self.pizza= pizza
    def sabor(self):
        return self.pizza.sabor()

class calabresa(decorador_pizza):
    def sabor(self):
        return self.pizza.sabor() + " ,calabresa"

class bacon(decorador_pizza):
    def sabor(self):
        return self.pizza.sabor() + " ,bacon"

pizza = pizzabase()
pizza = calabresa(pizza)
pizza = bacon(pizza)
print(pizza.sabor())    
