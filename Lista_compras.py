import os

inserir = False
remover = False
listar = False
num_item = 0
lista_compra = []
escolha = ''
while escolha != 'sair':
    escolha = input('Escolha uma das opções: \n[i]nserir\t[r]emover\t[l]istar\n')

    if escolha =='i':
        os.system('cls')
        lista_compra.append(input('Digite o item que deseja inserir: '))
        os.system('cls')

    elif escolha == 'r':
        if len(lista_compra) > 0:
            os.system('cls')
            item = input('Escolha qual item deseja remover: ')
            os.system('cls')
            for num_item, nome_item in enumerate(lista_compra):
                if nome_item == item:
                    del lista_compra[int(num_item)]
                    break
            else:
                os.system('cls') 
                print('Esse item não existe na lista')
        else:
            os.system('cls') 
            print('Sua lista está vazia')

    elif escolha == 'l':
        if len(lista_compra) > 0:
            os.system('cls')
            for indice, nome in enumerate(lista_compra):
                print(indice, nome)
        else:
            os.system('cls') 
            print('Sua lista está vazia')

    elif escolha == 'sair':
       os.system('cls')
        
    else:
        os.system('cls')
        print('opção inválida')