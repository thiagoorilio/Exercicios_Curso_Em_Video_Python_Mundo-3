'''''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas
partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,tudo isso será guardado
em um dicionário,incluindo o total de gols feitos durante o campeonato.
'''''
aproveitamento = list()
jogadores = dict()
jogadores['nome'] = str(input('Nome do jogador: '))
jogos = int(input('Quantas partidas disputou o jogador? '))
for i in range(1, jogos + 1):
    aproveitamento.append(int(input(f'Quantos gols o jogador fez na {i}º partida? ')))

jogadores['gols'] = aproveitamento[:]
jogadores['total_gols'] = sum(aproveitamento)
print('--=--' * 15)
print(jogadores)
print('--=--' * 15)
for k, v in jogadores.items():
    print(f'{k} recebe o valor {v}')
print('--=--' * 15)
print(f'O jogador {jogadores["nome"]} jogou {jogos} partidas.')
for k, v in enumerate(aproveitamento):
    print(f'Na partida {k}, fez {v} gols.')
print(f'Foi um total de {sum(aproveitamento)} gols.')
