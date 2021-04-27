from cria_baralho import cria_baralho

baralho = cria_baralho()

def display(baralho):
    n=1
    for cartas in baralho:
        print('{0}. {1}' .format(n, cartas))
        n+=1
    return

print(display(baralho))