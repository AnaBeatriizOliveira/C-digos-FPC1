"""DECIFRA"""

#entradas
alfabeto_permutado = input()
frase_criptografada = input()


alfabeto_original = "abcdefghijklmnopqrstuvwxyz"
#zip(alfabeto_permutado, alfabeto) combina os elementos das duas sequências: `alfabeto_permutado` e `alfabeto_original`
#a letra permutada é mapeada para sua respectiva letra original do alfabeto, usando a sequência `alfabeto_permutado` e `alfabeto`.
# o dicionário `alfabeto_permutado` substitui as letras permutadas por suas letras originais na frase criptografada durante o processo de decifração
alfabeto_permutado = {letra_permutada: letra for letra_permutada, letra in zip(alfabeto_permutado, alfabeto_original)}

#função para decifrar a frase criptografada
def decifrar_frase_criptografada(alfabeto_permutado, frase_criptografada):
    
#a variável frase_decifrada começa como uma string vazia, onde a partir dela iremos construir a frase decifrada completa    
    frase_decifrada = ""
    for letra in frase_criptografada:
        if letra in alfabeto_permutado:
            frase_decifrada += alfabeto_permutado[letra]
        else:
            frase_decifrada += letra
    
    return frase_decifrada

#utiliza-se a função a baixo para encontrarmos o resultado dentro da frase criptografada
frase_decifrada = decifrar_frase_criptografada(alfabeto_permutado, frase_criptografada)

print(frase_decifrada)


