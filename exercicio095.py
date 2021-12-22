'''''
*Aprimore o exercicio 093 para que ele funcione com vários jogadores,incluindo um sistema de visualização de detalhes
de aproveitamento de cada jogador.
'''''
time = list()
aproveitamento = list()
jogadores = dict()

while True:
    jogadores.clear()
    jogadores['nome'] = str(input('Nome do jogador: '))
    jogos = int(input('Quantas partidas disputou o jogador? '))
    for i in range(1, jogos + 1):
        aproveitamento.append(int(input(f'Quantos gols o jogador fez na {i}º partida? ')))
    jogadores['gols'] = aproveitamento[:]
    jogadores['total_gols'] = sum(aproveitamento)
    time.append(jogadores.copy())
    while True:
        resposta = input('Quer continuar? [S/N] ').upper()
        if resposta in 'SN':
            break
        print('ERRO. Responda [S/N]: ')
    if resposta == 'N':
        break
print('Cod ', end='')
for i in jogadores.keys():
    print(f'{i:<15}', end='')
print()
print('--=--' * 15)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for n in v.values():
        print(f'{str(n):<15}', end='')
    print()
print('--=--' * 15)
while True:
    busca = int(input('Mostrar os dados de qual jogador? [999 para parar]: '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro, Não existe jogador com o código {busca}. ')
    else:
        print(f' Dados do jogador {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('=' * 30)
print('PROGRAMA FINALIZADO.')