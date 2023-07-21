import os

cpf = '123'

while cpf != (cpf[0] * len(cpf)):
    
    cpf = input('Digite um CPF: ').replace('.', '').replace('-', '').replace(' ', '')
    caracter = ''
    digito = 0

    contador = 0
    soma = 0


    for caracter in cpf:
        try: 
            int(caracter)
            aceitar = True
        except:
            aceitar = False
            break
    if len(cpf) != 11:
        aceitar = False

    if aceitar:
        while contador < 9:
            soma += int(cpf[contador]) * (10 - contador) 
            contador += 1

        digito = (soma * 10) % 11

        primeiro_digito = digito if digito <=9 else 0


        contador = 0
        soma = 0

        while contador < 10:
            soma += int(cpf[contador]) * (11 - contador) 
            contador += 1

        digito = (soma * 10) % 11

        segundo_digito = digito if digito <=9 else 0

        if primeiro_digito == int(cpf[-2]) and segundo_digito == int(cpf[-1]):
            os.system('cls')
            print(f'O CPF {cpf} é válido')
        else:
            os.system('cls')
            print(f'O CPF {cpf} é inválido')

    else:
        os.system('cls')
        print('Digite um CPF no formato: xxx.xxx.xxx-xx')
os.system('cls')
print('Saindo...')
                