# Importando todas as funções
from lista_movimentos import lista_movimentos_possiveis
from cria_baralho import cria_baralho
from extrai_naipe import extrai_naipe
from extrai_valor import extrai_valor
from possui_movimentos import possui_movimentos_possiveis
from empilha import empilha
from display import display


# Imprimindo o início do jogo
arquivo=open("texto.txt","r",encoding="utf-8")
conteudo = arquivo.read()
arquivo.close() 

print(conteudo)
#

# Criando um loop para recomeçar o jogo no final
pergunta= True
while pergunta:
    baralho = cria_baralho()
    movimentos = True

# Criando um loop para o jogador continuar jogando enquanto houver movimentos possíveis
    while movimentos:
        print(display(baralho))
        movimentos = possui_movimentos_possiveis(baralho)
        posicao = int(input('Escolha uma numero de 1 a {0}: '.format(len(baralho))))
        if posicao > len(baralho):
            print('Ops, não temos tudo isso de cartas! Vamos considerar que vc queria pegar a ultima carta ok?')
            posicao = len(baralho)
        posicao -= 1
        possivel = lista_movimentos_possiveis(baralho, posicao)

# Criando um loop até o jogador escolher uma carta com movimentos possíveis
        while len(possivel) == 0:
            print('Essa carta não possui movimentos')
            posicao = int(input('Escolha uma numero de 1 a {0}: '.format(len(baralho))))
            if posicao > len(baralho):
                print('Ops, não temos tudo isso de cartas! Vamos considerar que vc queria pegar a ultima carta ok?')
                posicao = len(baralho)
            posicao -= 1
            possivel = lista_movimentos_possiveis(baralho, posicao)

# Mostrando os movimentos possíveis
        if len(possivel) == 2:
            print('Esses são os movimentos possíveis: ')

# Colorindo a carta do primeiro movimento
            naipe = extrai_naipe(baralho[posicao-1])
            if naipe == '♠':
                print('\033[37m{0}. \033[96m{1}\033[0m' .format(1, baralho[posicao-1]))
            elif naipe == '♥':
                print('\033[37m{0}. \033[91m{1}\033[0m' .format(1, baralho[posicao-1]))
            elif naipe == '♦':
                print('\033[37m{0}. \033[92m{1}\033[0m' .format(1, baralho[posicao-1]))
            else:
                print('\033[37m{0}. \033[95m{1}\033[0m' .format(1, baralho[posicao-1]))

# Colorindo a carta do segundo movimento
            naipe = extrai_naipe(baralho[posicao-3])
            if naipe == '♠':
                print('\033[37m{0}. \033[96m{1}\033[0m' .format(2, baralho[posicao-3]))
            elif naipe == '♥':
                print('\033[37m{0}. \033[91m{1}\033[0m' .format(2, baralho[posicao-3]))
            elif naipe == '♦':
                print('\033[37m{0}. \033[92m{1}\033[0m' .format(2, baralho[posicao-3]))
            else:
                print('\033[37m{0}. \033[95m{1}\033[0m' .format(2, baralho[posicao-3]))

# Pede para o jogador escolher um movimento            
            soma = int(input('Escolha uma posição para mover (1-2): '))
            if soma !=2 and soma !=1:
                soma = int(input('Numero invalido escolha (1-2) para mover: '))
            if soma == 2:
                soma = 3

# Caso a carta tenha apenas um movimento possível o programa já faz essa movimentação automática
        else:
            soma = possivel[0]
        destino = posicao - soma
        baralho = empilha(baralho, posicao, destino)

# Descobrino se o jogador ganhou ou perdeu
    if len(baralho) > 1:
        jogar = input('Infelizmente você perdeu... deseja começar um novo jogo? digite sim ou nao: ')
        if jogar == 'sim':
            pergunta = True
        else:
            print('Muito obrigado por jogar nosso jogo, volte smp freguês')
            pergunta = False
    else:
        jogar = input('Parabéns! Você ganhou o jogo! Deseja começar um novo jogo? digite sim ou nao: ')
        if jogar == 'sim':
            pergunta = True
        else:
            print('Muito obrigado por jogar nosso jogo, volte smp!')
            pergunta = False