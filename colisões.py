# leitura das entradas
X0A, Y0A, X1A, Y1A = [int(i) for i in input().split()]
X0B, Y0B, X1B, Y1B = [int(i) for i in input().split()]
# Análise da não colisão dos eixos
if X0B > X1A or X1B < X0A or Y0B > Y1A or Y1B < Y0A:
    print("0")
else:
    print("1")

