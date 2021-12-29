'''''
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
um dicionário com as seguintes informações: Quantidade de notas, A maior nota, A menor nota, A média da turma 
e a Situação (opcional).
Adicione também as docstrings da função.
'''''


def notas(*num, sit=False):
    dicionario = dict()
    dicionario['total'] = len(num)
    dicionario['maior'] = max(num)
    dicionario['menor'] = min(num)
    dicionario['media'] = sum(num) / len(num)
    if sit:
        if dicionario['media'] >= 7:
            dicionario['situacao'] = 'APROVADO!'
        elif dicionario['media'] >= 5:
            dicionario['situacao'] = 'RECUPERAÇÃO!'
        else:
            dicionario['situacao'] = 'REPROVADO!'

    return dicionario


print(notas(5.5, 2.5, 6, 9, sit=True))
print(notas(8, 9, 10, 7, sit=True))
print(notas(4, 5, 3, 2))
