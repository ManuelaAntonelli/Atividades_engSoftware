class CPU:
    def process_data(self):
        print("CPU processando...")


class Memory:
    def load(self):
        print("Carregando Memoria...")


class HardDrive:
    def read_data(self):
        print("Lendo HD...")

class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hd = HardDrive()

    def run(self):
        print("Iniciando computador\n")
        self.hd.read_data()
        self.memory.load()
        self.cpu.process_data()
        print("Bem vindo(a)!\n")


pc = Computer()
pc.run()