def contar_pares_corretos(lista_botas):
    pares_corretos = 0
    pilha_botas = {}

    for tamanho, pe in lista_botas:
        if tamanho not in pilha_botas:
            pilha_botas[tamanho] = [pe]
        else:
            outro_pe = 'D' if pe == 'E' else 'E'
            if outro_pe in pilha_botas[tamanho]:
                pilha_botas[tamanho].remove(outro_pe)
                pares_corretos += 1
            else:
                pilha_botas[tamanho].append(pe)
    
    return pares_corretos

# Lê o número de botas
N = int(input())

# Lê a descrição de cada bota e armazena em uma lista de tuplas
lista_botas = []
for _ in range(N):
    tamanho, pe = input().split()
    lista_botas.append((int(tamanho), pe))

# Chama a função para contar os pares corretos de botas
resultado = contar_pares_corretos(lista_botas)

# Imprime o resultado
print(resultado)
