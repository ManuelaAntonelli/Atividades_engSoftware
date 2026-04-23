'''7) Implementar em Python (ou Java ou C++) o exercício da transparência 86 da aula 19.'''

class SensorTemperatura:
    def __init__(self):
        self._observadores = [] #lista de quem quer receber avisos
        self._temperatura = 0

    def adicionar_observador(self, observador):
        self._observadores.append(observador)

    def remover_observador(self, observador):
        self._observadores.remove(observador)

    def set_temperatura(self, nova_temp):
        print(f"\n[Sensor] Nova temperatura detectada: {nova_temp}°C")
        self._temperatura = nova_temp
        self.notificar_todos()

    def notificar_todos(self):
        #"para cada display na lista, mande um aviso"
        for obs in self._observadores:
            obs.atualizar(self._temperatura)

class DisplayCelular:
    def atualizar(self, temperatura):
        print(f"-> [Celular] Notificação: A temperatura agora é {temperatura}°C")

class DisplayPrevisaoTempo:
    def atualizar(self, temperatura):
        print(f"-> [Painel de Rua] Atualizando painel para: {temperatura}°C")

sensor = SensorTemperatura()

celular_da_ranny = DisplayCelular()
painel_centro = DisplayPrevisaoTempo()

sensor.adicionar_observador(celular_da_ranny)
sensor.adicionar_observador(painel_centro)

sensor.set_temperatura(25)
sensor.set_temperatura(32)

