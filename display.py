from cria_baralho import cria_baralho
from extrai_naipe import extrai_naipe

baralho = cria_baralho()

def display(baralho):
    n=1
    for cartas in baralho:
        naipe = extrai_naipe(cartas)
        if naipe == '♠':
            print('\033[37m{0}. \033[96m{1}' .format(n, cartas))
        elif naipe == '♥':
            print('\033[37m{0}. \033[91m{1}' .format(n, cartas))
        elif naipe == '♦':
            print('\033[37m{0}. \033[92m{1}' .format(n, cartas))
        else:
            print('\033[37m{0}. \033[95m{1}' .format(n, cartas))
        
        n+=1
    return

print(display(baralho))