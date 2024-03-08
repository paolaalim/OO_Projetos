class CartaCrianca:
    def __init__(self, nome, idade, mensagem):
        self.nome = nome
        self.idade = idade
        self.mensagem = mensagem

class Crianca:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Responsavel:
    def __init__(self):
        self.criancas = []

    def cadastrar_crianca(self, crianca):
        self.criancas.append(crianca)

    def enviar_carta(self, crianca, mensagem):
        carta = CartaCrianca(crianca.nome, crianca.idade, mensagem)
