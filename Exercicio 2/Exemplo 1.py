class ConfiguracoesPapuguinho:
    _instancia = None

    def __new__(cls):
        
        if cls._instancia is None:
           
            cls._instancia = super(ConfiguracoesPapuguinho, cls).__new__(cls)
            
            cls._instancia.volume_som = 100
            cls._instancia.idioma = "PT-BR"
            print(">> Criando o gerenciador de configurações pela primeira vez!")
            
        return cls._instancia

config_tela_inicial = ConfiguracoesPapuguinho()
print(f"Volume na Tela Inicial: {config_tela_inicial.volume_som}")

config_tela_inicial.volume_som = 30

config_tela_jogo = ConfiguracoesPapuguinho()
print(f"Volume na Tela de Jogo: {config_tela_jogo.volume_som}")

print("As duas variáveis apontam para o mesmo lugar na memória?", config_tela_inicial is config_tela_jogo)