from your_module_name import Material, Crianca, CartaCrianca, Responsavel, Padrinho, Usuario

def main():
    usuario = Usuario()

    # Cadastro como responsável
    print("Cadastro como responsável:")
    usuario.cadastrar_como_responsavel()

    # Cadastro como padrinho
    print("\nCadastro como padrinho:")
    usuario.cadastrar_como_padrinho()

if __name__ == "__main__":
    main()

