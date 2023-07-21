"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (74682489070)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

#cpf = '74682489070'
cpf = input('Digite um CPF: ').replace('.', '').replace('-', '').replace(' ', '')
caracter = ''
digito = 0

contador = 0
soma = 0


for caracter in cpf:
    try: 
        int(caracter)
        aceitar = True
    except :
        aceitar = False
        break
    print(aceitar)

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

    print(primeiro_digito)
    print(cpf[-2])
    print(segundo_digito)
    print(cpf[-1])


    if primeiro_digito == int(cpf[-2]) and segundo_digito == int(cpf[-1]):
        print('CPF válido')
    else:
        print('CPF inválido')
else:
    print('CPF inválido')


            