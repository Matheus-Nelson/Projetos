import random
tentativas = 0
numero_secreto = random.randint(1, 100)
#print(numero_secreto)  # Exibe o número secreto para fins de teste

print("Bem-vindo ao jogo de adivinhação!")

while True:
    try:
        palpite = int(input("Tente adivinhar o número secreto (entre 1 e 100): "))
    except ValueError:
        print('ERRO! Você precisa digitar um número inteiro.')
        continue
        
    if palpite < 1 or palpite > 100:
        print('ERRO!, Digite apenas números entre 1 e 100.')
        continue
    tentativas += 1
    #print (f'O numero de tentativas foi de: {tentativas})

    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número secreto.")
        print(f'O numero de tentativas foi de: {tentativas}')
        break
    elif palpite < numero_secreto:
        print("O número secreto é maior que o seu palpite.")
    else:
        print("O número secreto é menor que o seu palpite.")