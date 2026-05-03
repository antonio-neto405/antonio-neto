# Sistema simples de cadastro de tarefas

tarefas = []

while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada!")

    elif opcao == "2":
        print("\nLista de tarefas:")
        for i, t in enumerate(tarefas):
            print(f"{i} - {t}")

    elif opcao == "3":
        indice = int(input("Digite o número da tarefa: "))
        if 0 <= indice < len(tarefas):
            tarefas.pop(indice)
            print("Tarefa removida!")
        else:
            print("Índice inválido!")

    elif opcao == "4":
        print("Saindo...")
        break
    
    else:
    print("Opção inválida!")
