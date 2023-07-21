import os
import random

cpf = ''

for i in range(0, 9):
    cpf += str(random.randint(0, 9))    

caracter = ''
digito = 0

contador = 0
soma = 0

while contador < 9:
    soma += int(cpf[contador]) * (10 - contador) 
    contador += 1

digito = (soma * 10) % 11

primeiro_digito = digito if digito <=9 else 0

cpf += str(primeiro_digito)

contador = 0
soma = 0

while contador < 10:
    soma += int(cpf[contador]) * (11 - contador) 
    contador += 1

digito = (soma * 10) % 11

segundo_digito = digito if digito <=9 else 0

cpf += str(segundo_digito)

print(cpf)

                