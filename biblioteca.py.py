def adicionar_livro(titulo, autor):
    livros.append({"titulo": titulo, "autor": autor, "disponivel": True})
    print(f"Livro '{titulo}' adicionado com sucesso!")

def remover_livro(titulo):
    for livro in livros:
        if livro["titulo"].lower() == titulo.lower():
            livros.remove(livro)
            print(f"Livro '{titulo}' removido com sucesso!")
            return
    print(f"Livro '{titulo}' não encontrado.")

def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado.")
    else:
        print("\n--- Lista de Livros ---")
        for livro in livros:
            status = "Disponível" if livro["disponivel"] else "Emprestado"
            print(f"{livro['titulo']} - {livro['autor']} ({status})")


def registrar_usuario(nome):
    usuarios.append({"nome": nome, "livros_emprestados": []})
    print(f"Usuário '{nome}' registrado com sucesso!")

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário registrado.")
    else:
        print("\n--- Lista de Usuários ---")
        for usuario in usuarios:
            print(f"Nome: {usuario['nome']} | Livros emprestados: {usuario['livros_emprestados']}")


def emprestar_livro(nome_usuario, titulo_livro):
    for usuario in usuarios:
        if usuario["nome"].lower() == nome_usuario.lower():
            for livro in livros:
                if livro["titulo"].lower() == titulo_livro.lower() and livro["disponivel"]:
                    livro["disponivel"] = False
                    usuario["livros_emprestados"].append(titulo_livro)
                    print(f"Livro '{titulo_livro}' emprestado para {nome_usuario}.")
                    return
            print(f"Livro '{titulo_livro}' não está disponível.")
            return
    print(f"Usuário '{nome_usuario}' não encontrado.")

def consultar_livros():
    disponiveis = [livro['titulo'] for livro in livros if livro['disponivel']]
    emprestados = [livro['titulo'] for livro in livros if not livro['disponivel']]

    print("\n--- Consulta de Livros ---")
    print("Disponíveis:", disponiveis if disponiveis else "Nenhum")
    print("Emprestados:", emprestados if emprestados else "Nenhum")


def menu():
    while True:
        print("\n=== Sistema de Biblioteca ===")
        print("1 - Adicionar livro")
        print("2 - Remover livro")
        print("3 - Listar livros")
        print("4 - Registrar usuário")
        print("5 - Listar usuários")
        print("6 - Emprestar livro")
        print("7 - Consultar livros")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            adicionar_livro(titulo, autor)
        elif opcao == "2":
            titulo = input("Título do livro a remover: ")
            remover_livro(titulo)
        elif opcao == "3":
            listar_livros()
        elif opcao == "4":
            nome = input("Nome do usuário: ")
            registrar_usuario(nome)
        elif opcao == "5":
            listar_usuarios()
        elif opcao == "6":
            nome = input("Nome do usuário: ")
            titulo = input("Título do livro: ")
            emprestar_livro(nome, titulo)
        elif opcao == "7":
            consultar_livros()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")