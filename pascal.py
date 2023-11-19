# Função para calcular a combinação binomial C(n, k) usando a relação de Stifel
def calcular_combinacao(n, k):
    if k == 0 or k == n:
        return 1  # Caso base: C(n, 0) = 1 e C(n, n) = 1
    else:
        # Chamadas recursivas para calcular C(n, k) com base em C(n-1, k-1) e C(n-1, k)
        return calcular_combinacao(n - 1, k - 1) + calcular_combinacao(n - 1, k)
        # A relação de Stifel é aplicada aqui, onde usamos a soma dos resultados
        # das chamadas recursivas para calcular C(n, k).

# Função para gerar a linha n do Triângulo de Pascal
def linha_pascal(n):
    if n == 0:
        return [1]  # Caso base: A primeira linha é [1]
    else:
        # Chamada recursiva para obter a linha n-1
        linha_anterior = linha_pascal(n - 1)
        # Calcula os valores da linha n usando a função calcular_combinacao
        nova_linha = [calcular_combinacao(n, k) for k in range(n + 1)]
        return nova_linha

# Solicita ao usuário o valor de n
n = int(input("Digite o valor de n: "))
# Obtém a linha n do Triângulo de Pascal e a imprime
resultado = linha_pascal(n)
print(resultado)

