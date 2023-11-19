"""quadrado mágico"""

def somar_lista(lista):
    """Função para somar os elementos de uma lista de números inteiros"""
    soma = 0
    for i in lista:
        soma += i
    return soma

n_linhas = int(input())
quadrado = [None] * n_linhas

for linha in range(n_linhas):
    nova_linha = [int(i) for i in input().split()]
    quadrado[linha] = nova_linha

# Imprimir as linhas e calcular as somas
print("Linhas:")
soma_linhas = []
for linha in quadrado:
    soma_linha = somar_lista(linha)
    soma_linhas.append(soma_linha)

# Imprimir as colunas e calcular as somas
print("Colunas:")
soma_colunas = []
for coluna in range(n_linhas):
    coluna_atual = [quadrado[linha][coluna] for linha in range(n_linhas)]
    soma_coluna = somar_lista(coluna_atual)
    soma_colunas.append(soma_coluna)

# Verificar se há uma linha com soma diferente das outras linhas
for i in range(n_linhas):
    if soma_linhas.count(soma_linhas[i]) == 1:
        linha_diferente = i
        break

# Verificar se há uma coluna com soma diferente das outras colunas
for j in range(n_linhas):
    if soma_colunas.count(soma_colunas[j]) == 1:
        coluna_diferente = j
        break

soma_linha_diferente = soma_linhas[linha_diferente]
soma_linha_normal = soma_linhas[0] if linha_diferente != 0 else soma_linhas[1]
diferenca_linhas = soma_linha_diferente - soma_linha_normal


# Achar numero trocado
numero_trocado = quadrado[linha_diferente][coluna_diferente]
# Achar numero original
numero_original = numero_trocado - diferenca_linhas

print(numero_original,numero_trocado)




