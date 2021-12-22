'''''
Faça um programa que tenha uma função chamada escreva(),que receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável.
'''''
def escreva(msg):
    t = len(msg)
    print('~' * t)
    print(msg)
    print('~' * t)

escreva('Olá')
escreva('Python')
escreva('My SQL')
escreva('Feliz em estar aprendendo')
