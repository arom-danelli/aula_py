# Formatação no Python
# Aqui é está o exercício 2 da forma que construi, usando a penas a lógica de vírgulas e quebra de linha.
nome = "Arom Danelli"
altura = 1.85
peso = 96
imc = ...

imc = peso / (altura ** 2) # A única coisa que diferiu do professor é que por costume, coloquei os parenteses na exponenciação. Mas pela ordem de prioridade, o python já ia ler o expoente primeiro.
print(nome, 'tem', altura, 'de altura e pesa', peso,'Kg' )
print('Seu IMC é de', imc)

# Aqui é assim que ficaria usando a formatação f-string

nome = "Arom Danelli"
altura = 1.85
peso = 96
imc = ...
teste= 1051651.6

imc = peso / (altura ** 2) # A única coisa que diferiu do professor é que por costume, coloquei os parenteses na exponenciação. Mas pela ordem de prioridade, o python já ia ler o expoente primeiro.
print(f'{nome} tem altura de {altura} e pesa {peso} Kg' )
print(f'Seu IMC é de {imc:.2f}')
