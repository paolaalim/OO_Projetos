import random

class Material:
    def __init__(self):
        self.descricao = ""

    def set_descricao(self, descricao):
        self.descricao = descricao

class Crianca:
    def __init__(self, nome):
        self.nome = nome

class CartaCrianca:
    def __init__(self, nome):
        self.nome = nome

class Responsavel:
    def enviar_carta(self, crianca, mensagem):
        carta = CartaCrianca(crianca.nome)
        print(f"Carta enviada para {carta.nome}: {mensagem}")

class Padrinho:
    def doar_dinheiro(self):
        print("Dinheiro doado com sucesso!")

    def gerar_codigo_pix(self):
        print("Código PIX gerado com sucesso!")

    def doar_materiais(self, material):
        material.set_descricao("Materiais doados")
        print(f"Materiais doados: {material.descricao}")

    def buscar_crianca(self):
        # Lógica para buscar e retornar uma criança
        crianca = Crianca("Criança Apadrinhada")
        return crianca

class Usuario:
    def cadastrar_como_responsavel(self):
        responsavel = Responsavel()
        crianca = Crianca("Nome da Criança")
        mensagem = "Mensagem da Carta"
        responsavel.enviar_carta(crianca, mensagem)

    def cadastrar_como_padrinho(self):
        padrinho = Padrinho()
        material = Material()
        padrinho.doar_dinheiro()
        padrinho.gerar_codigo_pix()
        padrinho.doar_materiais(material)
        crianca_apadrinhada = padrinho.buscar_crianca()
        if crianca_apadrinhada:
            print("Criança apadrinhada:", crianca_apadrinhada.nome)
        else:
            print("Não há crianças disponíveis para adoção.")
