# Considerando duas listas de inteiros ou floats (lista A e lista B)
# Some os valores nas listas retornando uma nova lista com os valores somados:
# Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
# menor.
# Exemplo:
# lista_a     = [1, 2, 3, 4, 5, 6, 7]
# lista_b     = [1, 2, 3, 4]
# =================== resultado
# lista_soma  = [2, 4, 6, 8]

# # def soma_lista(lista1, lista2):
#     max_range = min(len(lista1), len(lista2))
#     return [lista1[i] + lista2[i] for i in range(max_range)]

lista_a = [1, 2, 3.5, 4, 5.8, 6, 7]
lista_b = [1.1, 2, 3.234, 4]
# print(soma_lista(lista_a, lista_b))
try:
    lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
    print(lista_soma)
except TypeError:
    print('A lista contém valores diferente de int ou float')


