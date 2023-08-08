# Exercício - todo_list de tarefas com desfazer e refazer
# todo = [] -> todo_list de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

def show_list(todo_list):
    print('Lista de tarefas:')
    for item in todo_list:
        print(item)

def undo(todo_list, undo_list):
    if len(todo_list) > 0:
        undo_list.append(todo_list.pop())
    else:
        print('Não há o que ser desfeito')
        print()

def redo(todo_list, undo_list):
    if len(undo_list) > 0:
        todo_list.append(undo_list.pop())
    else:
        print('Não há o que ser refeito')
        print()

def include(todo_list, tarefa):
    todo_list.append(tarefa)

comando = ''
lista_tarefa = []
lista_removidos = []
while(comando != ' '):
    print('Comandos: listar, desfazer, refazer')
    comando = input('Digite uma tarefa para incluir ou um comando para ser executado: ')
    print()

    if comando == 'listar':
        show_list(lista_tarefa)
    elif comando == 'desfazer':
        undo(lista_tarefa, lista_removidos)
        show_list(lista_tarefa)
    elif comando == 'refazer': 
        redo(lista_tarefa, lista_removidos)
        show_list(lista_tarefa)
    else:
        include(lista_tarefa, comando)
        show_list(lista_tarefa)
        lista_removidos.clear()

    print('\n\n\n')
