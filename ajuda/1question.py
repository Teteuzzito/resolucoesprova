numero = int(input('Montar a tabuada de: '))
comeco = int(input('Começar por: '))
termino = int(input('Terminar em: '))

while comeco <= termino:
  print(f'{numero} X {comeco} = {numero * comeco}')
  comeco += 1