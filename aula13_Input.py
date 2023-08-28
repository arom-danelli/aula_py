# Nessa aula estamos vendo sobre input

# nome = input('Qual o seu nome? ') # O input sempre vai ser string. Por isso é interessante fazer a coerção de dados.
# print(f'O seu nome é {nome}')

# numero_1 = input('Digite um número: ')
# numero_2 = input('Digite outro número: ')

# print(f'A soma dos número é: {int(numero_1) + int(numero_2)}')

# O código acima foi eu que fiz. Mas o professor indicou para fazer da seguinte forma.

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1) # Como o input vai sempre pegar o valor como uma string. Não é interessante fazer a coerção dentro da própria variavel. É importante criar uma nova variável e nela fazer a coerção.
int_numero_2 = int(numero_2)

print(f'A soma dos número é: {int(int_numero_1) + int(int_numero_2)}')