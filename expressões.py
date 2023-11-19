def esta_bem_definida(expressao):
    pilha = []

    for char in expressao:
        if char in "{[(":
            pilha.append(char)
        elif char in "}])":
            if not pilha:
                return False
            ultimo_abertura = pilha.pop()
            if (char == "}" and ultimo_abertura != "{") or \
               (char == "]" and ultimo_abertura != "[") or \
               (char == ")" and ultimo_abertura != "("):
                return False
    
    return len(pilha) == 0

# Lê o número de instâncias
T = int(input())

# Lê todas as linhas de entrada de uma vez
entradas = []
for _ in range(T):
    entrada = input()
    entradas.append(entrada)

# Processa cada instância
for expressao in entradas:
    if esta_bem_definida(expressao):
        print("S")
    else:
        print("N")
