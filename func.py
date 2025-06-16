#def ehImpar(num):
#  if num % 2 != 0:
#    return print("É impar!!")
#  else:
#    return print("É par!!")
  
#valor = int(input("Digite um número: "))
#ehImpar(valor)

def fact (valor):
  result = 1
  while valor > 1:
    result *= valor
    valor -= 1
  return result

num = fact(4)
print(num)