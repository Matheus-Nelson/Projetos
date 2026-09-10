# Programa para calcular o IMC (Índice de Massa Corporal) e classificar o estado de saúde com base no resultado

altura = float(input('Qual a sua altura em cm: '))
peso = float(input('Qual o seu peso em kg: '))

imc = peso / (altura/100) ** 2
if imc < 18.5:
    print(f"Você está abaixo do peso.")
elif imc < 24.9:
    print(f"Você está com o peso normal.")
elif imc < 29.9:
    print(f"Você está com sobrepeso.")
elif imc < 39.9:
    print(f"Você está com obesidade")
else:
    print(f"Você está com obesidade grave.")