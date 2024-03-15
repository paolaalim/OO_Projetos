class Responsavel:
    def __init__(self):
        self.criancas = []

    def cadastrar_crianca(self, crianca):
        self.criancas.append(crianca)

    def enviar_carta(self, crianca, mensagem):
        carta = CartaCrianca(crianca.nome, crianca.idade, mensagem)
