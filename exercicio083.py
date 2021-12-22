'''''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''''
expressao = input('Digite uma expressao: ')
count1 = expressao.count('(')
count2 = expressao.count(')')
if count1 == count2:
    print('Esta expressão é válida!')
else:
    print('Esta expressão é inválida!')
