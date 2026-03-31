class cachorro:
    def som(self):
        return "Au au"
    
class gato:
    def som(self):
        return "miau"
    
class fabrica_pet:
    def criar_pet(tipo_pet):
        if tipo_pet == "cachorro":
            return cachorro()
        elif tipo_pet == "gato":
            return gato()
        else:
            return None
        
meu_pet = fabrica_pet.criar_pet("cachorro")
print(meu_pet.som())