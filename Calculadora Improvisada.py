"""Calculadora Improvisada"""

#definir uma função para o sucessor
def sucessor (a):
  return a + 1

#a partir da função sucessor conseguimos criar a função soma, executando a operação do sucessor b vezes
def somar(a,b):
  for i in range(b):
    a = sucessor(a)
  return a 

#na multiplicação somamos a, b vezes   
def multiplicar(a,b):
  c = 0 
  for i in range(b):
    c = somar(c,a)
  return c  

# multiplicamos a base a pelo expoente b, b vezes  
def exponecial(a,b):
  c = 1
  for i in range(b):
    c = multiplicar(c,a) 
  return c

# utilizando o == "" para que o usuário tenha liberdade de escrever vários comandos
operação = []
while True:
    comando_usuario = (input())
    if comando_usuario == "":
        break
    operação.append(comando_usuario.split())


# as funções são printadas a partir do primeiro índice da lista de entrada, por exemplo Suc (print função sucessor) e assim por diante
for comando_usuario in operação:
    if comando_usuario[0] == "Suc":
      print(sucessor(int(comando_usuario[1]))); 
    elif comando_usuario[0] == "Soma":
      print(somar(int(comando_usuario[1]), int(comando_usuario[2])))
    elif comando_usuario[0] == "Multi"  or comando_usuario[0] == "Mult":
      print(multiplicar(int(comando_usuario[1]), int(comando_usuario[2])))
    elif comando_usuario[0] == "Exp":
      print(exponecial(int(comando_usuario[1]), int(comando_usuario[2])))
    else:
     break
  
  
  



