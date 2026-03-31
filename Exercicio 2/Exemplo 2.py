class ConexaoBancoDados:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(ConexaoBancoDados, cls).__new__(cls)
            cls._instancia.status_conexao = "Conectado ao PostgreSQL"
            print(">> Conexão física com o Banco de Dados estabelecida!")
        return cls._instancia

    def consultar_usuario(self, id_usuario):
        return f"Buscando dados do usuário {id_usuario}..."


banco_login = ConexaoBancoDados()
print(banco_login.consultar_usuario(15))

banco_relatorio = ConexaoBancoDados()
print(banco_relatorio.consultar_usuario(99))

print("Os módulos compartilham a mesma conexão?", banco_login is banco_relatorio)