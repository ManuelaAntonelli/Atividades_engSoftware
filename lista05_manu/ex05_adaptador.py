class tomada_tres_pinos:
    def ligar_tomada_tres_pinos(self):
        print("Tomada de três pinos ligada")

class tomada_dois_pinos:
    def ligar_tomada_dois_pinos(self):
        print("Tomada de dois pinos ligada")

class adaptador_tomada(tomada_tres_pinos):
    def __init__(self, dispositivo_dois_pinos):
        self.dispositivo = dispositivo_dois_pinos

    def ligar_tomada_de_tres_pinos(self):
        return self.dispositivo.ligar_tomada_dois_pinos()
    
meu_celular = tomada_dois_pinos()

adaptador = adaptador_tomada(meu_celular)

adaptador.ligar_tomada_tres_pinos()
        

    