# Exercício - todo_list de tarefas com desfazer e refazer
# todo = [] -> todo_list de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os

def show_list(todo_list):
    if len(todo_list) > 0:
        print('Tarefas:')
        for item in todo_list:
            print(f'\t{item}')
    else:
        print('Não há tarefas')

def include(todo_list, tarefa):
    todo_list.append(tarefa)


def exclude(todo_list):
    if len(todo_list) > 0:
        return todo_list.pop()
    else:
        print('Não há tarefas para serem removidas')

def undo(undo_list, redo_list):
    if len(undo_list) > 0:
        aux = undo_list.pop()
        action = aux.pop()
        info = aux.pop()
        if action == 'include':
            redo_list.append([info,'exclude'])
            return 'excluir'
        else:
            redo_list.append(['','include'])
            return info
    else:  
        print('Não ações para desfazer')
        return 'listar'


def redo(undo_list, redo_list):
    if len(redo_list) > 0:
        aux = redo_list.pop()
        action = aux.pop()
        info = aux.pop()
        if action == 'exclude':
            undo_list.append([info, 'include'])
            return info
        else:
            return 'excluir'
    else:  
        print('Não ações para refazer')
        return 'listar'


comando = ''
lista_tarefa = []
lista_exec = []
lista_redo = []
lista_undo = []
undo_flag = False
while(comando != ' '):
    print('Comandos: listar, desfazer, refazer, excluir')
    comando = input('Digite uma tarefa para incluir ou um comando para ser executado: ')
    os.system('cls')

    
    if comando == 'desfazer':
        comando = undo(lista_undo, lista_redo)
        undo_flag = True

    if comando == 'refazer': 
        undo_flag = False
        comando = redo(lista_undo, lista_redo)

    if comando == 'excluir':
        if undo_flag == False:
            lista_undo.append([exclude(lista_tarefa), 'exclude'])
        else:
            exclude(lista_tarefa)
            undo_flag = False
        show_list(lista_tarefa)

    elif comando == 'listar':
        show_list(lista_tarefa)

    else:
        include(lista_tarefa, comando)
        if undo_flag == False:
            lista_undo.append([comando, 'include']) 

        show_list(lista_tarefa)

    print('\n\n\n')
