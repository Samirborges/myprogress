expression = input('Digite uma expressão: ')
expressionlist = list(expression)
pilha = []

for símb in expressionlist:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break       

if len(pilha) == 0:
    print('A expressão está correta')
else:
    print('A expressão não está correta.')
print(len(pilha))
print(pilha)