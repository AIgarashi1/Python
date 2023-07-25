# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opcoes': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opcoes': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opcoes': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
acerto = 0
amount = 0

for key in perguntas: 
    amount += 1
    i = 1
    print(f'Pergunta: ', key['Pergunta'])
    
    for alternativa in key['Opcoes']:
        print(f'{i})', alternativa)
        i += 1
    
    escolha = input('Insira sua alternativa: ')

    if escolha.isdigit() and key['Opcoes'][int(escolha)-1] == key['Resposta']:
        print('Resposta certa!')
        acerto += 1
    else:
        print('Resposta errada!')
    print()

print('Você acertou', acerto, f'respostas de', amount)
    # print(key['Pergunta'])

# print(f'a) {perguntas[0]['Opcoes'][1]}')



# print(f'Pergunta: {perguntas[1]['Pergunta']}')





# print(f'Pergunta: {perguntas[2]['Pergunta']}')

