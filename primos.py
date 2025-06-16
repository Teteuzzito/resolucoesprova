numero = int(input('Digite o número para ver se ele é par ou não: '))
cont = 2

while cont < numero:
  if numero % cont == 0:
    print('Não é primo!!')
    break

  else:
    cont += 1

if numero / cont == 1:
  print('É primo!!')