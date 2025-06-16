numero = int(input("Digite um número para verificar se é primo: "))
if numero < 2:
    print(f"{numero} não é primo.")
else:
    eh_primo = True
    divisor = 2

    while divisor <= numero // 2:
        if numero % divisor == 0:
            eh_primo = False
            break
        divisor += 1

    if eh_primo:
        print(f"{numero} é primo.")
    else:
        print(f"{numero} não é primo.")