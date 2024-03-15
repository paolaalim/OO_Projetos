Sistema de Apadrinhamento

    Este é um sistema simples de apadrinhamento implementado em Python, onde os usuários podem se cadastrar como padrinhos ou responsáveis por meio das 
classes `Usuario`, `Padrinho`, `Responsavel`, `Crianca` e `Material`.

Classes:

1. Usuario:
    - `cadastrar_como_responsavel()`: Cadastra o usuário como responsável e envia a carta da criança.
    - `cadastrar_como_padrinho()`: Cadastra o usuário como padrinho, doa dinheiro, gera código PIX, doa materiais e busca uma criança para apadrinhar.

2. Padrinho:
    - `doar_dinheiro()`: Simula a doação de dinheiro para a criança apadrinhada.
    - `gerar_codigo_pix()`: Gera um código PIX para transações financeiras.
    - `doar_materiais(material)`: Simula a doação de materiais para a criança apadrinhada.
    - `buscar_crianca()`: Simula a busca por uma criança disponível.

3. Responsavel:
    - `enviar_carta(crianca, mensagem)`: Envia uma carta à criança com a mensagem especificada.

4. Crianca:
    - Representa uma criança com um nome.

5. Material:
    - `set_descricao(descricao)`: Define a descrição do material a ser doado.

Uso na Main:

    No arquivo `main.py`, um objeto `Usuario` é criado, e o usuário é cadastrado como responsável e padrinho. Cartas são enviadas, dinheiro é doado, 
códigos PIX são gerados, materiais são doados e uma criança é apadrinhada (ou uma mensagem é exibida se nenhuma criança está disponível).
    Para executar o programa, basta rodar o arquivo `main.py` em um ambiente Python. Certifique-se de ter as classes `Usuario`, `Padrinho`, `Responsavel`, 
`Crianca` e `Material` no mesmo diretório ou importe-as corretamente no arquivo `main.py`.
