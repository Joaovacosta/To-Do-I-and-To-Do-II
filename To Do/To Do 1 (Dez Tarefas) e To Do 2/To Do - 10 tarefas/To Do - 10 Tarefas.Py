import os
editar = 0
out = 1
trf1 = None
trf2 = None
trf3 = None
trf4 = None
trf5 = None
trf6 = None
trf7 = None
trf8 = None
trf9 = None
trf10 = None 
os.system("cls")

while out == 1: #Menu de início
    
    print("Seja bem vindo(a) ao seu To do!")
    print("Veja suas opções:\n1º Opção: Add tarefas\n2º Opção: Listar\n3º Opção: Exlcuir tarefas\n4º Opção: Sair do To Do")
    escolha = int(input("Escolha uma das opções:"))
    
    if escolha == 1: 
        os.system("cls")
        Fim = print("Digite sua lista de tarefas abaixo (São 10 tarefas para adicionar).\n\n")
        trf1 = input("Primeira Tarefa: ")
        trf2 = input("Segunda Tarefa: ")
        trf3 = input("Terceira Tarefa: ")
        trf4 = input("Quarta Tarefa: ")
        trf5 = input("Quinta Tarefa: ")
        trf6 = input("Sexta Tarefa: ")
        trf7 = input("Sétima Tarefa: ")
        trf8 = input("Oitava Tarefa: ")
        trf9 = input("Nona Tarefa: ")
        trf10 = input("Décima Tarefa: ")
        
        print("Tarefas adicionadas!")
        os.system ("pause")
        os.system ("cls")
    
    elif escolha == 2: #Listar tarefas atribuídas para o To Do
        if (trf1 == None and trf2 == None and trf3 == None and trf4 == None and trf5 == None and trf6 == None and trf7 == None and trf8 == None and trf9 == None and trf10 == None):
            print("Nenhuma tarefa foi adicionada. Volte ao início para adicioná-las")
            os.system ("pause")
            os.system ("cls")
        else:
            print(f"Lista de suas tarefas está aqui! Veja como ficou:\nPrimeira tarefa: {trf1}\nSegunda Tarefa: {trf2}\nTerceira Tarefa: {trf3}\n Quarta Tarefa: {trf4}\n Quinta Tarefa: {trf5}\n Sexta Tarefa: {trf6}\nSétima Tarefa: {trf7}\n Oitava tarefa: {trf8}\n Nona Tarefa: {trf9}\n Décima tarefa: {trf10}")
            os.system ("pause")
            os.system ("cls")

        
    elif escolha == 3: #Exluir tarefa do To Do
        if (trf1 == None and trf2 == None and trf3 == None and trf4 == None and trf5 == None and trf6 == None and trf7 == None and trf8 == None and trf9 == None and trf10 == None):
            print("Nenhuma tarefa foi adicionada. Volte ao início para adicionar.")
            os.system("pause")
            os.system("cls")
        else:
            os.system("cls")
            remover = int(input("Digite o número da tarefa para remove-la: "))
            if remover == 1:    
                    trf1=None
                    print (f"Tarefa 1 ({trf1}) removida")
            elif remover == 2:    
                    trf2=None
                    print (f"Tarefa 2 ({trf2}) removida")
            elif remover == 3:    
                    trf3=None
                    print (f"Tarefa 3 ({trf3}) removida")
            elif remover == 4:    
                    trf4=None
                    print (f"Tarefa 4 ({trf4}) removida")
            elif remover == 5:    
                    trf5=None
                    print (f"Tarefa 5 ({trf5}) removida")
            elif remover == 6:    
                    trf6=None
                    print (f"Tarefa 6 ({trf6}) removida")
            elif remover == 7:    
                    trf7=None
                    print (f"Tarefa 7 ({trf7}) removida")
            elif remover == 8:    
                    trf8=None
                    print (f"Tarefa 8 ({trf8}) removida")
            elif remover == 9:    
                    trf9=None
                    print (f"Tarefa 9 ({trf9}) removida")
            elif remover == 10:    
                    trf10=None
                    print (f"Tarefa 10 ({trf10}) removida")
            elif remover == 0:
                    print ("Remoção cancelada")
            else:
                    print ("Número de Tarefa ERRADA")
                    int(input("Insira a tarefa correta: "))
            print ("\n\nRetornando ao MENU")
            os.system ("pause")
            os.system ("cls")
    elif escolha == 4: #Sair do To Do
        os.system("cls")
        print("Saindo do To Do...")
        out = 4
        os.system("pause")
        os.system ("cls")

