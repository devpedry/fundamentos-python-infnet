from datetime import datetime

tarefas = []


def adicionar_tarefa(descricao, urgencia="Média"):
    """
    Adiciona uma nova tarefa na lista

    Parametros:
        descricao: descrição da tarefa
        urgencia: nível de urgencia da tarefa
    """

    nova_tarefa = {
        "id": len(tarefas) + 1,
        "descricao": descricao,
        "data_criacao": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "status": "Pendente",
        "urgencia": urgencia
    }

    tarefas.append(nova_tarefa)

    return nova_tarefa


def listar_tarefas():
    """Mostra todas as tarefas cadastradas"""

    if len(tarefas) == 0:
        print("\nNenhuma tarefa cadastrada\n")
        return

    print("\n===== LISTA DE TAREFAS =====")

    for tarefa in tarefas:
        print(f"""
ID: {tarefa["id"]}
Descrição: {tarefa["descricao"]}
Data: {tarefa["data_criacao"]}
Status: {tarefa["status"]}
Urgencia: {tarefa["urgencia"]}
-----------------------------
""")


def buscar_tarefa(id_tarefa):
    """Busca uma tarefa pelo ID"""

    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            return tarefa

    return None


def concluir_tarefa(id_tarefa):
    """Marca uma tarefa como concluida"""

    tarefa = buscar_tarefa(id_tarefa)

    if tarefa is not None:
        tarefa["status"] = "Concluída"
        return True

    return False


def remover_tarefa(id_tarefa):
    """Remove uma tarefa da lista"""

    tarefa = buscar_tarefa(id_tarefa)

    if tarefa:
        tarefas.remove(tarefa)
        return True

    return False


def menu():
    """Menu principal do sistema"""

    while True:

        print("""
===== GERENCIADOR DE TAREFAS =====

1 - Adicionar tarefa
2 - Listar tarefas
3 - Concluir tarefa
4 - Remover tarefa
0 - Sair
""")

        opcao = input("Escolha uma opção: ")

        match opcao:

            case "1":

                descricao = input("Digite a descrição da tarefa: ")
                urgencia = input("Urgencia (Baixa/Média/Alta): ")

                tarefa = adicionar_tarefa(
                    descricao=descricao,
                    urgencia=urgencia
                )

                print(f"\nTarefa '{tarefa['descricao']}' adicionada\n")

            case "2":
                listar_tarefas()

            case "3":

                try:
                    id_tarefa = int(input("Digite o ID da tarefa: "))

                    if concluir_tarefa(id_tarefa):
                        print("\nTarefa concluida\n")
                    else:
                        print("\nNão encontrei essa tarefa\n")

                except ValueError:
                    print("\nDigite um número válido\n")

            case "4":

                try:
                    id_tarefa = int(input("Digite o ID da tarefa: "))

                    if remover_tarefa(id_tarefa):
                        print("\nTarefa removida\n")
                    else:
                        print("\nNão encontrei essa tarefa\n")

                except ValueError:
                    print("\nDigite um número válido\n")

            case "0":
                print("\nEncerrando sistema...")
                break

            case _:
                print("\nOpção inválida\n")


menu()
