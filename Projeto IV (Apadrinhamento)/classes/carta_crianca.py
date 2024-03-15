from classes.crianca import Crianca

class CartaCrianca(Crianca):
    def __init__(self, nome, idade, mensagem):
        super()._init_ (nome, idade)        
        self.mensagem = mensagem


