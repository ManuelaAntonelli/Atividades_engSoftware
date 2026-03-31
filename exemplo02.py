class pizza1:
    def sabor(self):
        return "calabresa"

class pizza2:
    def sabor(self):
        return "marguerita"
    
class pizza3:
    def sabor(self):
        return "frango"
    
class pizzaria:
    def fazer_pizza(sabor_pizza):
        if sabor_pizza == "pizza1":
            return pizza1()
        elif sabor_pizza == "pizza2":
            return pizza2()
        elif sabor_pizza == "pizza3":
            return pizza3()
        else:
            return None
        
minha_pizza = pizzaria.fazer_pizza("pizza2")

if minha_pizza:
    print(minha_pizza.sabor())
else:
    print("Sabor não encontrado")



    