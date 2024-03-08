class Padrinho:
    def __init__(self, usuario):
        self.usuario = usuario

    def cadastrar_como_padrinho(self):
        print("Cadastro como padrinho realizado com sucesso!")

class Responsavel:
    def __init__(self, usuario):
        self.usuario = usuario

    def cadastrar_como_responsavel(self):
        print("Cadastro como responsável realizado com sucesso!")

class Usuario:
    def __init__(self, nome, email, senha, telefone, endereco):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.endereco = endereco

    def cadastrar_como_padrinho(self):
        novo_padrinho = Padrinho(self)
        print("Cadastro como padrinho realizado com sucesso!")

    def cadastrar_como_responsavel(self):
        novo_responsavel = Responsavel(self)
        print("Cadastro como responsável realizado com sucesso!")
      
