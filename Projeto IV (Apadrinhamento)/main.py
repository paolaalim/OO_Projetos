from classes.Material import Material
from classes.Crianca import Crianca
from classes.CartaCrianca import CartaCrianca
from classes.Responsavel import Responsavel
from classes.Padrinho import Padrinho
from classes.Usuario import Usuario

def main():
    usuario = Usuario()

    # Cadastro como responsável
    print("Cadastro como responsável:")
    usuario.cadastrar_como_responsavel()

    # Cadastro como padrinho
    print("\nCadastro como padrinho:")
    usuario.cadastrar_como_padrinho()

    # Exemplo adicional de funcionalidade (buscar criança)
    print("\nBusca por uma criança para apadrinhar:")
    padrinho = Padrinho()
    crianca_apadrinhada = padrinho.buscar_crianca()
    if crianca_apadrinhada:
        print("Criança apadrinhada:", crianca_apadrinhada.nome)
    else:
        print("Não há crianças disponíveis para adoção.")

if __name__ == "__main__":
    main()
