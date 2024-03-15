from classes.usuario import Usuario

class Padrinho (Usuario):
    def __init__(self, nome, email, senha, telefone, endereco, materiais, codigo_pix, cartas_disponiveis):
        super()._init_ (nome, email, senha, telefone, endereco)        
        self.materiais = []
        self.codigo_pix = codigo_pix
        self.cartas_disponiveis = cartas_disponiveis

    def doar_materiais(self, descricao):
        material1 = Material()
        material1.descricao = descricao
        self.materiais.append(material1)
        print("Doação realizada com sucesso!")

    def doar_dinheiro(self, valor):
        print(f"Realizando doação de R$ {valor:.2f} para o código PIX {self.codigo_pix}.")

    def gerar_codigo_pix(self):
        print("Código PIX gerado com sucesso!")

    def buscar_crianca(self):
        if len(self.cartas_disponiveis) == 0:
            print("Não há cartas disponíveis para adoção.")
            return None
        index = random.randint(0, len(self.cartas_disponiveis) - 1)
        carta_selecionada = self.cartas_disponiveis.pop(index)
        return carta_selecionada
