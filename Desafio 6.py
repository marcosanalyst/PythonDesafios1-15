# Desafio!

frutas = ['maça', 'banana', 'manga', 'uva'] # conchetes quer dizer que iniciarei uma lista

#método, quando eu coloco '.' estou acessando os métodos do objeto
#append: envia o item para o final da lista

# frutas[1] = 'morango'
# frutas.append('abacaxi')

# alterando mais de um index de uma vez

frutas[1:3] = ['acabaxi', 'abacate'] # altera o index 1 e 2, o último index é INDICATIVO de onde para!!!!

# insirindo no meio! MÉTODO

frutas.insert(2, 'Abacate') # (posição do INDEX, qual o OBJETO)

print(frutas)