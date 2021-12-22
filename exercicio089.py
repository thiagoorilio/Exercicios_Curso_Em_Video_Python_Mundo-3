'''''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final,mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada
aluno individualmente.
'''''
lista = []
temp = []
media = numero = aluno = 0
nome = str
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    lista.append(temp[:])
    temp.clear()
    resposta = input('Voce deseja continuar? [S/N] ').upper()
    while resposta not in 'SN':
        resposta = input('Código errado. Voce deseja continuar? [S/N] ').upper()
        if resposta == 'N':
            break
    if resposta == 'N':
        break
print('-=' * 30)
print(f'{"No.":<4} {"NOME":^10} {"MÉDIA":>8}')
print('-' * 35)
for i in range(len(lista)):
    numero = i
    print(numero)
for i in range(len(lista)):
    nome = lista[i][0]
    print(nome.title())
for i in lista:
    media = (i[1] + i[2]) / 2
    print(media)
print('-' * 35)
while aluno != 999:
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    while aluno > len(lista):
        aluno = int(input('Número invalido. Mostrar notas de qual aluno? (999 interrompe): '))
    print(f'As notas de {lista[aluno][0]} são {lista[aluno][1]} e {lista[aluno][2]}')
    if aluno == 999:
        break
