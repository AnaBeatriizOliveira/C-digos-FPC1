"""Problema da Peça Perdida"""


def somar_lista(lista):
    """"Função para a somar os elementos de uma lista de números inteiros"""
    # Vamos usar a função para somar os elementos da lista incompleta
    soma = 0
    for i in lista:
        soma += i
    return soma

    
def encontrar_peca_perdida(n_pecas,lista_incompleta):
    """"Função para encontrarmos a peça perdida"""
   
    soma_lista_incompleta = somar_lista(lista_incompleta)

    # Para calcularmos a soma dos elementos da lista completa, usamos a soma de uma PA
    soma_lista_completa = int((n_pecas * (n_pecas + 1)) / 2)
    peca_perdida = soma_lista_completa - soma_lista_incompleta
    print(peca_perdida)


def main():
    """"Função principal"""
    # Leitura do número de peças
    n_pecas = int(input())
    # Lista com uma peça faltando, leitura na entrada
    lista_incompleta = [int(i) for i in input().split()]
    encontrar_peca_perdida(n_pecas,lista_incompleta)

main()


