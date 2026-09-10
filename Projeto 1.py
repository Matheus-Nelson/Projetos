# Programa para verificar o estado da carne com base na temperatura

tem_cel = int(input("Qual a temperatura da carne? "))

if tem_cel < 48:
    print("A carne está crua.")
elif tem_cel < 54:
    print("A carne está selada.")
elif tem_cel < 60:
    print("A carne está ao ponto.")
elif tem_cel < 65:
    print("A carne está bem passada.")
else:
    print("A carne está muito passada.")