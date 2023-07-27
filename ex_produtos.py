import copy
from dados_ex_import import produtos

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos em 10%
# Gere novos_produtos por deep copy (cópia profunda)

novos_produtos = [ {**new_product, 'preco': round(new_product['preco'] * 1.1, 2)} for new_product in copy.deepcopy(produtos) ]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = sorted(copy.deepcopy(produtos), key=lambda new_product: new_product['nome'], reverse = True )


# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = sorted(copy.deepcopy(produtos), key=lambda new_product: new_product['preco'] )


print('Produtos originais:')
print(*produtos, sep='\n')
print('\n Produtos com aumento de preço:')
print(*novos_produtos, sep='\n')
print('\n Produtos ordenados por nome:')
print(*produtos_ordenados_por_nome, sep='\n')
print('\n Produtos ordenados por preço:')
print(*produtos_ordenados_por_preco, sep='\n')
