# Programa para calcular a quantidade de tinta necessária para pintar uma parede

total_tinta = int(input("qual o rendimento da lata de tinta? "))
altura_parede = int(input("qual a altura da parede? "))
largura_parede = int(input("qual a largura da parede? "))

def calculo_tinta():
    area_parede = altura_parede * largura_parede
    latas_tinta = area_parede / total_tinta
    print(f"Você precisará de {latas_tinta} latas de tinta.")

calculo_tinta()