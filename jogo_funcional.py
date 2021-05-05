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
    possivel = lista_movimentos_possiveis(baralho, posicao)
    if len(possivel) < 1:
        print('Essa carta não possui movimentos')
    else:
        if len(possivel) == 2:
            soma = int(input('Escolha uma posição para mover (1-2): '))
            if soma == 2:
                soma = 3
        else:
            soma = possivel[0]
        destino = posicao - soma
        baralho = empilha(baralho, posicao, destino)

        #baralho está mudando para cartas acima