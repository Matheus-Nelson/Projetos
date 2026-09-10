# Programa para gerenciar funcionários e seus turnos

Funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)

lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)

lista3 = set(Funcionarios).difference(tem_carro)
print(lista3)