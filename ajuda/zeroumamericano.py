def zeroUmAmericano (num1, num2, num3, num4):
    valores = [num1, num2, num3, num4]
    
    total = 0
    valido = True

    for i in valores:
        if i < 0:
            valido = False
            return ('Existe um valor inválido')
            break
        else:
            total += i
            
    resto = 0
    
    if valido:
        resto = total % 4
    
        if resto == 0:
            return ('O jogador ganhador foi o 4°!')
        else:
            return (f'O jogador ganhador foi o {resto}°!')
            
num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))
num4 = int(input('Digite um número: '))

todos = zeroUmAmericano(num1, num2, num3, num4)
print(todos)