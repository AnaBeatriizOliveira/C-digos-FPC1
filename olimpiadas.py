
N, M = map(int, input().split())

def organizar_classificacao(paises, modalidades):
    # Inicializar o dicionário de contagem de medalhas por país
    medalhas = {i: [0, 0, 0] for i in range(1, paises + 1)}

    # Contar as medalhas de ouro, prata e bronze de cada país
    for i in range(modalidades):
        ouro, prata, bronze = map(int, input().split())
        medalhas[ouro][0] += 1
        medalhas[prata][1] += 1
        medalhas[bronze][2] += 1

    # Função auxiliar para determinar a pontuação de cada país
    def pontuacao(pais):
        ouro, prata, bronze = medalhas[pais]
        return (-ouro, -prata, -bronze, pais)

    # Implementação do algoritmo Quicksort
    def quicksort(array):
        if len(array) <= 1:
            return array
        else:
            pivo = array[0]
            menores = [item for item in array[1:] if pontuacao(item) < pontuacao(pivo)]
            maiores = [item for item in array[1:] if pontuacao(item) >= pontuacao(pivo)]
            return quicksort(menores) + [pivo] + quicksort(maiores)

    
    classificacao = quicksort(list(medalhas.keys()))

    return classificacao


# Obter a classificação dos países
classificacao_final = organizar_classificacao(N, M)


print(*classificacao_final)



