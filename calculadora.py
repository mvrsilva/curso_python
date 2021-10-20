#1: Implementar uma função para cada operação
#1.1 Soma
def somar(n1,n2):
return n1+n2
#1.2 Subtração
def diminuir(n1,n2):
return n1-n2
#1.3 Divisao
def dividir(n1,n2):
if(n2 != 0):
return n1/n2
print('Não dividirás por zero')
#1.4 Multiplicação
def multiplicar(n1,n2):
return n1*n2
#2: Função principal
def main():
#2.1: Capturar dois números:
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
#2.2: Apresentar a opções de cálculo
opcao = input('Digite a opção desejada: 1 - Somar\n2 - Subtrair\n3 - Multiplicar\
n4 - Dividir')
#2.3: Realizar a operação matemática de acordo com o cálculo escolhido:
if opcao == '1':
print(somar(n1,n2))
elif opcao == '2':
print(diminuir(n1,n2))
elif opcao == '3':
print(multiplicar(n1,n2))
elif opcao == '4':
print(dividir(n1,n2))
else:
print('Opcao Inválida')
if __name__ == '__main__':
  
