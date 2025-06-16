cont = 0
num = int(input('Diz aí pão: '))

for c in range(1, num+1):
  if num % c == 0:
    cont += 1

if cont == 2:
  print('Primo')
elif cont > 2:
  print('Não primo')