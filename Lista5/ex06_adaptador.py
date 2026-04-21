class sistema_europa:
    def valor_europeu (self):
        print("Controlado em Fahrenheit.")

class sistema_brasileiro:
    def valor_brasileiro(self):
        print("Controlado em centígrados.")

class adaptador_sistema(sistema_europa):
    def __init__(self,forno_brasileiro):
        self.forno = forno_brasileiro

    def valor_europeu(self):
        return self.forno.valor_brasileiro()
    
meu_forno = sistema_brasileiro()

adaptador = adaptador_sistema(meu_forno)

adaptador.valor_europeu()



