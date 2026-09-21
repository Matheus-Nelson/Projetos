frase = "Eu estou estudando Python"

caracteres = len(frase)
palavras = frase.split()
elementos_lista = len(palavras)

vogais = 0
for letra in frase.lower():
    if letra in 'aeiou':
        vogais += 1

maior_palavra = palavras[0]

for palavra in palavras:
    if palavras in len(palavras):
        maior_palavra = palavras

print(f'O numero de caracteres é: {caracteres}')
print(f'A quantidade de palavras é: {elementos_lista}')
print('A primeira palavra é: ', palavras[0])
print('A ultima palavra é: ', palavras[-1])
print(f'o numero de vogais é: {vogais}')
print(f'A palavra mais longa é: {maior_palavra}')