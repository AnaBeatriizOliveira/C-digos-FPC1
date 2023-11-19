class No:

    def __init__(self, dado):
        self.dado = dado
        self.prox = None

class Pilha:

    def __init__(self):
        self.inicio = None

    def is_vazia(self):
        return self.inicio is None

    def push(self, dado):
        novo_no = No(dado)
        if self.is_vazia():
            self.inicio = novo_no
        else:
            novo_no.prox = self.inicio
            self.inicio = novo_no

    def pop(self):
        if self.is_vazia():
            return None
        r = self.inicio
        self.inicio = self.inicio.prox
        return r.dado


# entrada é lista de strings
while True:
    entrada = input()
    if not entrada:
        break
    tokens = entrada.split()
    pilha = Pilha()  #Camelcase snakecase
    for token in reversed(tokens):
        if token.isnumeric():
            pilha.push(int(token))
        else:
            operando_1 = pilha.pop()
            operando_2 = pilha.pop()
            if token == "*":
                r = operando_1 * operando_2
            elif token == "/":
                r = int(operando_1 / operando_2)
            elif token == "+":
                r = operando_1 + operando_2
            elif token == "-":
                r = operando_1 - operando_2
            pilha.push(r)
    print(pilha.pop())