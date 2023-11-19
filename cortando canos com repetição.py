
n_comprimentos, tamanho_original = map(int, input().split())  # Lê o número de comprimentos e o tamanho original
comprimentos = []
valores = []

def maior_valor_corte_canos(n_comprimentos, tamanho_original, comprimentos, valores):
    n_itens = n_comprimentos
    max_valores = [0 for _ in range(tamanho_original + 1)]  # Inicializa a lista para armazenar os valores máximos

    for j in range(1, tamanho_original + 1):  # Loop para calcular os valores máximos para cada tamanho
        max_valor = max_valores[j - 1]  # Valor máximo possível considerando um cano de tamanho menor
        for i in range(n_itens):
            if comprimentos[i] <= j:  # Verifica se o comprimento do cano cabe na capacidade atual
                # Calcula o valor máximo entre não adicionar o cano ou adicionar o cano e somar o valor correspondente
                max_valor = max(max_valor, max_valores[j - comprimentos[i]] + valores[i])
        max_valores[j] = max_valor  # Armazena o valor máximo obtido para o tamanho j

    return max_valores[tamanho_original]  # Retorna o valor máximo obtido com o tamanho original

# Loop para ler os comprimentos e valores dos canos
for _ in range(n_comprimentos):
    comprimento, valor = map(int, input().split())
    comprimentos.append(comprimento)
    valores.append(valor)

# Calcula e imprime o maior valor obtido 
print(maior_valor_corte_canos(n_comprimentos, tamanho_original, comprimentos, valores))

