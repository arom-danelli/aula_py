# Calcular o IMC

nome = "Arom Danelli"
altura = 1.85
peso = 96
imc = ...

imc = peso / (altura ** 2) # A única coisa que diferiu do professor é que por costume, coloquei os parenteses na exponenciação. Mas pela ordem de prioridade, o python já ia ler o expoente primeiro.
print(nome, 'tem', altura, 'de altura e pesa', peso,'Kg' )
print('Seu IMC é de', imc)