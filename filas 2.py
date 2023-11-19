# Leitura da entrada
N = int(input())
fila_inicial = list(map(int, input().split()))
M = int(input())
pessoas_que_deixaram = list(map(int, input().split()))

# Função para obter o estado final da fila
def estado_final_fila(N, fila_inicial, M, pessoas_que_deixaram):
    nova_fila = []
    for pessoa in fila_inicial:
        if pessoa not in pessoas_que_deixaram:
            nova_fila.append(pessoa)
    
    return nova_fila

# Chamar a função e obter o estado final da fila
estado_final = estado_final_fila(N, fila_inicial, M, pessoas_que_deixaram)

# Imprimir o resultado
print(" ".join(map(str, estado_final)))
