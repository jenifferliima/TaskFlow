from gerenciador import Gerenciador

gerenciador = Gerenciador()

while True:
    print("\n===== TASKFLOW =====")
    print("1 - Cadastrar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Título: ")
        descricao = input("Descrição: ")
        prioridade = input("Prioridade (Baixa, Média ou Alta): ")

        gerenciador.cadastrar(titulo, descricao, prioridade)
        print("\n✅ Tarefa cadastrada com sucesso!")

    elif opcao == "2":
        tarefas = gerenciador.listar()

        if not tarefas:
            print("\nNenhuma tarefa cadastrada.")
        else:
            print("\n===== LISTA DE TAREFAS =====")
            for tarefa in tarefas:
                print(tarefa)

    elif opcao == "3":
        codigo = int(input("Digite o ID da tarefa: "))

        if gerenciador.concluir(codigo):
            print("\n✅ Tarefa concluída!")
        else:
            print("\n❌ Tarefa não encontrada.")

    elif opcao == "4":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")