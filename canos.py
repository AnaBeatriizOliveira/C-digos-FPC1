def max_valor_corte_cano(numero_canos, tamanho_fabricado, informacoes_canos):
    # Inicializamos uma lista de zeros para armazenar os maiores valores possíveis para cada tamanho
    max_valores = [0] * (tamanho_fabricado + 1)

    # Iteramos pelos tamanhos dos canos desejados
    for i in range(numero_canos):
        # Percorremos a lista dos possíveis tamanhos a serem fabricados e atualizamos os valores máximos
        for j in range(tamanho_fabricado, informacoes_canos[i][0] - 1, -1):
            max_valores[j] = max(max_valores[j], max_valores[j - informacoes_canos[i][0]] + informacoes_canos[i][1])

    # O valor máximo de venda para o tamanho fabricado estará na última posição da lista
    return max_valores[tamanho_fabricado]

# Função para ler as entradas e chamar a função principal
def main():
    # Lê a quantidade de canos e o tamanho fabricado
    numero_canos, tamanho_fabricado = map(int, input().split())

    # Lê os comprimentos e valores dos canos desejados pelos clientes
    canos = []
    for _ in range(numero_canos):
        comprimento, valor_venda = map(int, input().split())
        canos.append((comprimento, valor_venda))

    # Chama a função para encontrar o valor máximo e imprime o resultado
    resultado = max_valor_corte_cano(numero_canos, tamanho_fabricado, canos)
    print(resultado)

if __name__ == "__main__":
    main()

 