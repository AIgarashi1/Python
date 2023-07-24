# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def cria_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = cria_multiplicador(2)
triplicar = cria_multiplicador(3)
quadriplicar = cria_multiplicador(4)

print(duplicar(2))
print(duplicar(3))
print(duplicar(4))
print(duplicar(5))
print('\n')
print(triplicar(2))
print(triplicar(3))
print(triplicar(4))
print(triplicar(5))
print('\n')
print(quadriplicar(2))
print(quadriplicar(3))
print(quadriplicar(4))
print(quadriplicar(5))