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
