# Precedência entre operadores

# Em ordem de execução é
# 1. (n + n) tudo o que está em parenteses. Isso significa que se tiver parenteses dentro de parenteses, é o parentes mais interno que vai ser executado primeiro.
# 2. ** exponenciação
# 3. * / // % (multiplicação, divisão, divisão inteira e módulo)
# 4. + - 

conta_1 = 1 + 1 ** 5 + 5
print(conta_1) # Verifica-se que o resultado é 7, pois ele vai resolver primeiro a exponenciação e depois vai somar.

conta_2 = (1 + 1) ** (5 + 5)
print(conta_2) # Verifica=se que primeiro vai resolver o que está em parenteses e depois a exponenciação.