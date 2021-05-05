arquivo=open("texto.txt","r")
conteudo = arquivo.read()
arquivo.close() # O que acontece se não fechar?

# Imprime o conteúdo
print(conteudo)
