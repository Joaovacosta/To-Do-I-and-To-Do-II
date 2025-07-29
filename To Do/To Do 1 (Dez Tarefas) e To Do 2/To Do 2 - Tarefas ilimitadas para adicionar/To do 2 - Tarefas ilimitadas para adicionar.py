import os
menu = 1
lista_tarefas = []
os.system("cls")
while menu == 1:
    print("Seja bem vindo(a) ao seu To do!")
    print("Veja suas opções:\n1º Opção: Add tarefas\n2º Opção: Listar\n3º Opção: Excluir tarefas\n4º Opção: Modificar uma tarefa\n5º Opção: Sair do To Do")
    escolha = int(input("Escolha uma das opções:"))
    
    if escolha == 1: #Adicionar uma tarefa
        adicionar_tarefa_nova = "sim"  
        while adicionar_tarefa_nova != "não": 
            tarefa = input("Informe a sua tarefa: ")
            lista_tarefas.append(tarefa)
            adicionar_tarefa_nova = input("Deseja adicionar mais tarefas? (sim/não): ")
            while adicionar_tarefa_nova != "sim" and adicionar_tarefa_nova != "não":
                print("Resposta inválida. Digite sim ou não.")
                adicionar_tarefa_nova = input("Deseja adicionar mais tarefas? (sim/não): ")
                
        print("Tarefas adicionadas.")
        os.system("pause")
        os.system("cls")

    elif escolha == 2: #2: Listar as tarefas
        if lista_tarefas == []:
            print("Nenhuma tarefa foi adicionada. Adicione primeiro para listá-las.")

        else:
            print("Suas tarefas estão abaixo: ")
            print(lista_tarefas)
        os.system("pause")
        os.system("cls")

     #3: Exluir uma tarefa já selecionada
    elif escolha == 3:
        if lista_tarefas == []:
            print("\nNão existem tarefas para excluir. Adicione primeiro para exclui-las depois.")
            os.system("pause")
            os.system("cls")
        
        else:
            print("\nTarefas disponíveis para remoção:")
            indice = 1
            for tarefa in lista_tarefas:
                print(f"{indice} - {tarefa}")
                indice += 1
            escolha = int(input("\nDigite o número da tarefa que deseja apagar: "))
            tarefa_removida = lista_tarefas.pop(escolha - 1)
            print(f"\nTarefa '{tarefa_removida}' removida com sucesso!")

    elif escolha == 4: #Modificar uma tarefa
        if lista_tarefas == []:
            print("\nNão existem tarefas para editar")
        else:
            os.system("cls")
            print("\nTarefas disponíveis para edição:")
            indice = 1
            for tarefa in lista_tarefas:
                print(f"{indice} - {tarefa}")
                indice += 1
            escolha = int(input("\nDigite o número da tarefa que deseja editar: "))
            tarefa_atual = lista_tarefas[escolha - 1]
            nova_tarefa = input("Digite a nova descrição da tarefa: ")
            lista_tarefas[escolha - 1] = nova_tarefa
            print("\nTarefa atualizada com sucesso!")

    elif escolha == 5:  # Sair do To Do
        os.system("cls")
        print("Saindo do To Do. Obrigado por usar.")
        os.system("pause")
        os.system("cls")
        menu = 0 

    else:
        print("Opção inválida. Digite a opção correta.")
        os.system("pause")
        os.system("cls")