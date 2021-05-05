from lista_movimentos import lista_movimentos_possiveis
from cria_baralho import cria_baralho
from extrai_naipe import extrai_naipe
from extrai_valor import extrai_valor
from possui_movimentos import possui_movimentos_possiveis
from empilha import empilha
from display import display


baralho = cria_baralho()
movimentos = True
while movimentos:
    print(display(baralho))
    movimentos = possui_movimentos_possiveis(baralho)
    posicao = int(input('Escolha uma numero de 1 a {0}: '.format(len(baralho))))
    posicao -= 1
    possivel = lista_movimentos_possiveis(baralho, posicao)
    while len(possivel) == 0:
        print('Essa carta não possui movimentos')
        posicao = int(input('Escolha uma numero de 1 a {0}: '.format(len(baralho))))
        posicao -= 1
        possivel = lista_movimentos_possiveis(baralho, posicao)

    if len(possivel) == 2:
        print('Esses são os movimentos possíveis: ')
        print('1. {0}'.format(baralho[posicao - 1]))
        print('2. {0}'.format(baralho[posicao - 3]))
        soma = int(input('Escolha uma posição para mover (1-2): '))
        if soma !=2 and soma !=1:
            soma = int(input('Numero invalido escolha (1-2) para mover: '))
        if soma == 2:
            soma = 3
    else:
        soma = possivel[0]
    destino = posicao - soma
    baralho = empilha(baralho, posicao, destino)

if len(baralho) > 1:
    jogar = input('Infelizmente você perdeu... deseja começar um novo jogo? digite sim ou nao: ')
    if jogar == 'sim':
        pergunta = True
    else:
        print('Muito obrigado por jogar nosso jogo, volte smp freguês')
else:
    jogar = input('Parabéns! Você ganhou o jogo! Deseja começar um novo jogo? digite sim ou nao: ')
    if jogar == 'sim':
        pergunta = True
    else:
        print('Muito obrigado por jogar nosso jogo, volte smp!')    
        