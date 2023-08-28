# Estudos de if

#Posso usar o IF sozinho

# condicao = 10

# if condicao >= 10:
#     print('Condição 1') # Dentro do bloco de condições

# print('nenhuma condição') # Fora do bloco de condições. Então ele vai imprimir a primeira condição que é verdadeira e vai imprimir o que está fora do bloco, dando sequência na lógica.


# nota1 = int(input('Digite um número: '))
# nota2 = int(input('Digite outro número: '))
# nota = nota1 + nota2

# if nota >= 15:                                   # Neste bloco, vale ressaltar que todos os dados de entrada no INPUT, como padrão, é entendido como STR, então é necessário fazer a conversão para números.
#      print('Passou de ano')                       # A lógica é simples, pediu 2 dados para o usuário, fazemos a soma na própria variável que vai ser guardado o resultado da soma e partindo desta variável, criamos as condições.

# else:
#     print('Não passou de ano')    

# Basicamente a regra é: Abre com IF e fecha com Else. No meio do caminho, caso por ter várias condições, usa o ELIF (famoso else if). Obs.: Pode ter o IF sozinho, sem fechar com else.
# Abaixo tem a lógica de usada a cima com o ELIF no meio.

nota1 = int(input('Digite um número: '))
nota2 = int(input('Digite outro número: '))
nota = nota1 + nota2

if nota >= 15:                                  
     print('Passou de ano')    

elif 10 <= nota < 15:
    print('Elif')                        

else:
    print('Não passou')