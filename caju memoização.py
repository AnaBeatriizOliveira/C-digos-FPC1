def maxCajus(soma, memo, i, j, M, N):
    # Verificar se a área M x N cabe dentro dos limites da matriz soma
    if i + M > len(soma) or j + N > len(soma[0]):
        return 0
    
    # Verificar se já calculamos o resultado para essa posição (i, j)
    if memo[i][j] != -1:
        return memo[i][j]
    
    # Calcular a soma acumulada na área M x N a partir de (i, j)
    total = soma[i + M - 1][j + N - 1]
    if i > 0:
        total -= soma[i - 1][j + N - 1]
    if j > 0:
        total -= soma[i + M - 1][j - 1]
    if i > 0 and j > 0:
        total += soma[i - 1][j - 1]
    
    # Armazenar o resultado na matriz memo e calcular recursivamente
    # as outras possibilidades (mover para próxima linha ou coluna)
    memo[i][j] = max(total, maxCajus(soma, memo, i + 1, j, M, N), maxCajus(soma, memo, i, j + 1, M, N))
    return memo[i][j]

def calcular_colheita():
    # Ler as dimensões da fazenda e da área de interesse
    L, C, M, N = map(int, input().split())
    
    # Ler a matriz da fazenda
    fazenda = [list(map(int, input().split())) for _ in range(L)]
    
    # Criar a matriz de somas acumuladas (programação dinâmica)
    soma = [[0] * C for _ in range(L)]
    for i in range(L):
        for j in range(C):
            soma[i][j] = fazenda[i][j]
            if i > 0:
                soma[i][j] += soma[i - 1][j]
            if j > 0:
                soma[i][j] += soma[i][j - 1]
            if i > 0 and j > 0:
                soma[i][j] -= soma[i - 1][j - 1]
    
    # Criar a matriz de memoização com valores iniciais -1
    memo = [[-1] * C for _ in range(L)]
    
    # Calcular o resultado máximo usando a função maxCajus
    result = maxCajus(soma, memo, 0, 0, M, N)
    
    # Imprimir o resultado máximo de cajus que podem ser colhidos
    print(result)

if __name__ == "__main__":
    calcular_colheita()

