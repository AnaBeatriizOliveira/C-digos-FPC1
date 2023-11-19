def encontrar_navio(T, i, j, n, m):
    if i < 0 or i >= n or j < 0 or j >= m:
        return
    if T[i][j] != '#':
        return
    T[i][j] = '.'
    encontrar_navio(T, i, j + 1, n, m)
    encontrar_navio(T, i, j - 1, n, m)
    encontrar_navio(T, i + 1, j, n, m)
    encontrar_navio(T, i - 1, j, n, m)

def destruir_navios(T, disparos):
    n, m = len(T), len(T[0])
    navios_destruidos = 0

    for disparo in disparos:
        l, c = disparo
        if T[l-1][c-1] == '#':
            navios_destruidos += 1
            encontrar_navio(T, l-1, c-1, n, m)
        T[l-1][c-1] = '.'

    return navios_destruidos

# Lendo a entrada
N, M = map(int, input().split())
T = []
for _ in range(N):
    linha = list(input())
    T.append(linha)

K = int(input())
disparos = []
for _ in range(K):
    l, c = map(int, input().split())
    disparos.append((l, c))

# Chamando a função para destruir os navios e obter o resultado
resultado = destruir_navios(T, disparos)

# Imprimindo o número de navios destruídos
print(resultado)



