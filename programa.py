pergunta= True
while pergunta:
    print ("Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha. Existem apenas dois movimentos possíveis:" )  
    print ("1. Empilhar uma carta sobre a carta imediatamente anterior;") 
    print ("2. Empilhar uma carta sobre a terceira carta anterior." )
    print ()
    print ("Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida: ")
    print ()
    print ("1. As duas cartas possuem o mesmo valor ou") 
    print ("2. As duas cartas possuem o mesmo naipe." )
    print ('')
    print ("Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada." )
    print ('')
    
    # copiar jogo funcional aqui

    pergunta_1=input("deseja jogar de novo? ")
    if pergunta_1 == "nao" or pergunta_1=="não":
        pergunta=False
    else: 
        pergunta= True