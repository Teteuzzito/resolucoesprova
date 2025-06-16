quant_linhas = int(input('Digite a quantidade de linhas da matriz: '))
quant_colunas = int(input('Digite a quantidade de colunas da matriz: '))

matriz = []

for i in range(quant_linhas):
  linhas = []
  for j in range(quant_colunas):
    valor = int(input('Digite um dos valores da matriz: '))
    linhas.append(valor)  
  matriz.append(linhas)

lista_soma = [0] * quant_colunas

for j in range(quant_colunas):
  for i in range(quant_linhas):
    lista_soma[j] += matriz[i][j]

for linha in matriz:
  print(linha)
  
print('A soma de todos os números de cada coluna: ')
print(lista_soma)