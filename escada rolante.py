# Leitura do número de pessoas
n_pessoas = int(input())

# introdução da lista de instantes
lista_instantes = []

# atribuição das variáveis
tempo_total = 0
ultimo_instante = 0

# leitura dos instantes em que as pessoas passaram pelo sensor
for i in range(n_pessoas):
    instante = int(input())
    lista_instantes.append(instante)
    
    if tempo_total == 0 or instante > ultimo_instante:
        tempo_total = (instante + 10) - lista_instantes[0]
    
    else:
      tempo_total = ultimo_instante + 10
    
    ultimo_instante = instante



print(tempo_total)
