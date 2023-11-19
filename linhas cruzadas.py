n_pregos_vertical = int(input())
ordem_horizontal = list(map(int, input().split()))

# Primeiro loop (i) itera sobre os pregos verticais, "i" representa o prego atual
# Segundo loop(j) itera sobre os pregos verticais restantes a patir do índice seguinte ao índice atual "i"
def contar_cruzamentos(n, ordem_horizontal):
    cruzamentos = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if ordem_horizontal[i] > ordem_horizontal[j]:
                cruzamentos += 1
    return cruzamentos


# Chamada da função 'contar cruzamentos', o resultado retornado é atribuído a variável "cruzamentos"
cruzamentos = contar_cruzamentos(n_pregos_vertical, ordem_horizontal)
print(cruzamentos)
