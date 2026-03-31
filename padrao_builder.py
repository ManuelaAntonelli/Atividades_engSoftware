from abc import ABC, abstractmethod
from typing import List, Optional

# ============== PRODUCT ==============
class Computador:
    """Produto final que será construído"""
    
    def __init__(self):
        self.processador: Optional[str] = None
        self.memoria: Optional[int] = None
        self.armazenamento: Optional[int] = None
        self.placa_video: Optional[str] = None
        self.perifericos: List[str] = []
        
    def __str__(self) -> str:
        return f"""
        ===== COMPUTADOR =====
        Processador: {self.processador}
        Memória: {self.memoria}GB
        Armazenamento: {self.armazenamento}GB
        Placa de Vídeo: {self.placa_video}
        Periféricos: {', '.join(self.perifericos) if self.perifericos else 'Nenhum'}
        """
    
    def adicionar_periferico(self, periferico: str) -> None:
        self.perifericos.append(periferico)


# ============== BUILDER ABSTRACT ==============
class ComputadorBuilder(ABC):
    """Builder abstrato definindo as etapas de construção"""
    
    @abstractmethod
    def reset(self) -> None:
        pass
    
    @abstractmethod
    def definir_processador(self, processador: str) -> 'ComputadorBuilder':
        pass
    
    @abstractmethod
    def definir_memoria(self, memoria: int) -> 'ComputadorBuilder':
        pass
    
    @abstractmethod
    def definir_armazenamento(self, armazenamento: int) -> 'ComputadorBuilder':
        pass
    
    @abstractmethod
    def definir_placa_video(self, placa: str) -> 'ComputadorBuilder':
        pass
    
    @abstractmethod
    def adicionar_periferico(self, periferico: str) -> 'ComputadorBuilder':
        pass
    
    @abstractmethod
    def get_resultado(self) -> Computador:
        pass


# ============== CONCRETE BUILDER ==============
class ComputadorGamerBuilder(ComputadorBuilder):
    """Builder concreto para computadores gamers"""
    
    def __init__(self):
        self.computador = Computador()
        
    def reset(self) -> None:
        self.computador = Computador()
        
    def definir_processador(self, processador: str) -> ComputadorBuilder:
        # Validação específica para PC Gamer
        if "i9" not in processador and "Ryzen 9" not in processador:
            print("⚠️  Aviso: Processador pode não ser ideal para jogos pesados")
        self.computador.processador = processador
        return self
        
    def definir_memoria(self, memoria: int) -> ComputadorBuilder:
        if memoria < 16:
            print("⚠️  Aviso: Para jogos, recomendamos no mínimo 16GB de RAM")
        self.computador.memoria = memoria
        return self
        
    def definir_armazenamento(self, armazenamento: int) -> ComputadorBuilder:
        self.computador.armazenamento = armazenamento
        return self
        
    def definir_placa_video(self, placa: str) -> ComputadorBuilder:
        self.computador.placa_video = placa
        return self
        
    def adicionar_periferico(self, periferico: str) -> ComputadorBuilder:
        self.computador.adicionar_periferico(periferico)
        return self
        
    def get_resultado(self) -> Computador:
        # Validação final
        if not self.computador.placa_video:
            raise ValueError("PC Gamer deve ter uma placa de vídeo dedicada!")
        return self.computador


class ComputadorEscritorioBuilder(ComputadorBuilder):
    """Builder concreto para computadores de escritório"""
    
    def __init__(self):
        self.computador = Computador()
        
    def reset(self) -> None:
        self.computador = Computador()
        
    def definir_processador(self, processador: str) -> ComputadorBuilder:
        self.computador.processador = processador
        return self
        
    def definir_memoria(self, memoria: int) -> ComputadorBuilder:
        if memoria < 8:
            print("⚠️  Aviso: Para escritório, recomendamos no mínimo 8GB de RAM")
        self.computador.memoria = memoria
        return self
        
    def definir_armazenamento(self, armazenamento: int) -> ComputadorBuilder:
        self.computador.armazenamento = armazenamento
        return self
        
    def definir_placa_video(self, placa: str) -> ComputadorBuilder:
        # PC de escritório geralmente não precisa de placa de vídeo dedicada
        print("ℹ️  PC de escritório geralmente usa vídeo integrado")
        self.computador.placa_video = placa
        return self
        
    def adicionar_periferico(self, periferico: str) -> ComputadorBuilder:
        self.computador.adicionar_periferico(periferico)
        return self
        
    def get_resultado(self) -> Computador:
        # Configuração padrão se alguns campos não foram definidos
        if not self.computador.memoria:
            self.computador.memoria = 8
        if not self.computador.armazenamento:
            self.computador.armazenamento = 256
        return self.computador


def exemplo_1():
    """Exemplo usando Builder diretamente para mais flexibilidade"""
    print("\n" + "="*50)
    print("EXEMPLO 2: USANDO BUILDER DIRETAMENTE")
    print("="*50)
    
    builder = ComputadorGamerBuilder()
    
    pc_personalizado = (builder
                        .definir_processador("AMD Ryzen 9 7950X")
                        .definir_memoria(64)
                        .definir_armazenamento(4000)
                        .definir_placa_video("AMD Radeon RX 7900 XTX")
                        .adicionar_periferico("Mouse Razer")
                        .adicionar_periferico("Teclado Corsair")
                        .adicionar_periferico("Monitor 240Hz")
                        .get_resultado())
    
    print("\n--- PC Gamer Personalizado ---")
    print(pc_personalizado)


if __name__ == "__main__":
    exemplo_1()