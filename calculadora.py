#1: Implementar uma função para cada operação
2
3 #1.1 Soma
4 def somar(n1,n2):
5 return n1+n2
6
7 #1.2 Subtração
8 def diminuir(n1,n2):
9 return n1-n2
10
11 #1.3 Divisao
12 def dividir(n1,n2):
13 if(n2 != 0):
14 return n1/n2
15 print('Não dividirás por zero')
16
17 #1.4 Multiplicação
18 def multiplicar(n1,n2):
19 return n1*n2
20
21 #2: Função principal
22 def main():
23
24 #2.1: Capturar dois números:
25 n1 = float(input("Digite o primeiro número: "))
26 n2 = float(input("Digite o segundo número: "))
27
28 #2.2: Apresentar a opções de cálculo
29 opcao = input('Digite a opção desejada: 1 - Somar\n2 - Subtrair\n3 - Multiplicar\
n4 - Dividir')
30
31 #2.3: Realizar a operação matemática de acordo com o cálculo escolhido:
32 if opcao == '1':
33 print(somar(n1,n2))
34 elif opcao == '2':
35 print(diminuir(n1,n2))
36 elif opcao == '3':
37 print(multiplicar(n1,n2))
38 elif opcao == '4':
39 print(dividir(n1,n2))
40 else:
41 print('Opcao Inválida')
