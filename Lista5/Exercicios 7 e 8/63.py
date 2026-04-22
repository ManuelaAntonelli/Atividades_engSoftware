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