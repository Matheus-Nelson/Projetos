#Calculadora simples em Python
num1 = float(input('Digite o primeiro número: '))
operador = input('Digite o operador (+, -, *, /, **): ')
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
    novo_numero = num1 / num2
    print(f'O resultado da divisão é igual a {novo_numero}.')
elif operador == '**':
    novo_numero = num1 ** num2
    print(f'O resultado da exponenciação é igual a {novo_numero}.')
else:
    print('Operador inválido.')