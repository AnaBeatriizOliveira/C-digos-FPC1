def maior_valor_mochila_rep(comprimentos, valores, capacidade):
    n_itens = len(comprimentos)
    T = [0 for _ in range(capacidade + 1)]

    for j in range(1, capacidade + 1):
        max_valor = T[j - 1]  # Valor máximo possível considerando um item a menos
        for i in range(n_itens):
            if comprimentos[i] <= j:
                max_valor = max(max_valor, T[j - comprimentos[i]] + valores[i])
        T[j] = max_valor

    return T[capacidade]

# Entrada do usuário
n, capacidade = map(int, input().split())
tamanhos = []
valores = []

for _ in range(n):
    tam, val = map(int, input().split())
    tamanhos.append(tam)
    valores.append(val)

print(maior_valor_mochila_rep(tamanhos, valores, capacidade))
