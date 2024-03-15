from classes.usuario import Usuario
 
class Responsavel(Usuario):
    def __init__(self, nome, email, senha, telefone, endereco, criancas):
        super()._init_ (nome, email, senha, telefone, endereco)   

        self.criancas = []

    def cadastrar_crianca(self, crianca):
        self.criancas.append(crianca)

    def enviar_carta(self, crianca, mensagem):
        carta = CartaCrianca(crianca.nome, crianca.idade, mensagem)
