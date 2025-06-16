def ParEImpar(numeros):
  par = 0
  impar = 0

  for num in numeros:
    if num % 2 == 0:
      par += 1
    else:
      impar += 1

  return (par, impar)

valores = []

quantNumeros = int(input('Deseja digitar quantos números: '))

for i in range(quantNumeros):
  num = int(input('Digite um número: '))
  valores.append(num)

resultado = ParEImpar(valores)

print(valores)
print(resultado)