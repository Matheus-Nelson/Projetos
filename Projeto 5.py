#Calculadora simples em Python

while True:
    num1 = float(input('Digite o primeiro número: '))
    operador = input('Digite o operador (+, -, *, /, **, %, //): ')
    num2 = float(input('Digite o segundo número: '))


    if operador == '+':
        novo_numero = num1 + num2
        print(f'O resultado da soma é igual a {novo_numero}.')
    elif operador == '-':
        novo_numero = num1 - num2
        print(f'O resultado da subtração é igual a {novo_numero}.')
    elif operador == '*':
        novo_numero = num1 * num2
        print(f'O resultado da multiplicação é igual a {novo_numero}.')
    elif operador == '/':
        if num2 == 0:
            print('Não é possível dividir por zero.')
        else:
            novo_numero = num1 / num2
            print(f'O resultado da divisão é igual a {novo_numero}.')
    elif operador == '**':
        novo_numero = num1 ** num2
        print(f'O resultado da exponenciação é igual a {novo_numero}.')
    elif operador == '%':
        if num2 == 0:
            print('Não é possível calcular o resto da divisão por zero.')
        else:
            novo_numero = num1 % num2
            print(f'O resultado do resto da divisão é igual a {novo_numero}.')
    elif operador == '//':
        if num2 == 0:
            print('Não é possível calcular a divisão inteira por zero.')
        else:
            novo_numero = num1 // num2
            print(f'O resultado da divisão inteira é igual a {novo_numero}.')
    else:
        print('Operador inválido.')

    while True:
        resposta = input("Deseja realizar outra operação? (s/n): ")
        if resposta == 's' or resposta == 'n':
            break  # Sai do loop se a resposta for válida
        else:
            print("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")

    if resposta == 'n':
        break  # Sai do loop principal se a resposta for 'n'
        
print("Calculadora encerrada.")