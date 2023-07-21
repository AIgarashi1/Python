"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

count_tentativa = 0
count_letra = 0
palavra_secreta = 'sol'
palavra_descoberta = len(palavra_secreta) * '*'
palavra_passada = ''
letra_usuario = 'a'
letra_atual = 'a'

while palavra_descoberta != palavra_secreta:
    os.system('cls')
    print(palavra_descoberta)
    letra_usuario = input('Digite uma letra para a tentativa: ')
    count_tentativa += 1
    count_letra = 0
    if len(letra_usuario) > 1:
        print('DIGITE APENAS UMA LETRA POR VEZ')
    elif letra_usuario in palavra_secreta:
        for letra_atual in palavra_secreta:
            if palavra_descoberta[count_letra] == '*' and letra_atual == letra_usuario:
                palavra_passada += letra_atual
                count_letra += 1  
            else:
                palavra_passada += palavra_descoberta[count_letra]
                count_letra += 1
        palavra_descoberta = palavra_passada
        palavra_passada = ''
    
print(f'Parabéns você descobriu que a palavra secreta é {palavra_secreta.upper()} com {count_tentativa} tentativas')