# Quando utiliza o AND todas as condições deverão ser verdadeiras.

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')

else:
    print('Sair')   



# Avaliação de curto circuito, é quando o compilador vai checando as condições
# e para no FALSE. Quando para o FALSE ele vai imprimir o valor de false e parar ali.
