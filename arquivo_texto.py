arquivo=open("texto.txt","r",encoding="utf-8")
conteudo = arquivo.read()
arquivo.close() # O que acontece se não fechar?

# Imprime o conteúdo
print(conteudo)
