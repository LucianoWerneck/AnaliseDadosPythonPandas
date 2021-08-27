'''print('Olá Mundo')

divisão = 10 / 2
print(divisão)

#criando uma string
frase = 'Luciano esta estudando Analise de Dados com Python e Pandas'
print(frase[0])
print(frase[0:22])

frase = frase.upper()

print(frase.count('dados'))

print(frase.replace('Luciano', 'Snow'))

#criando uma lista chamada animais
animais = [1, 2, 3]
print(animais)

animais = ['cachorro', 'gato', 12345, 6.5]
print(animais)

#imprimindo o primeiro elemento da lista
print(animais[0])
print(animais[3])

#substiruindo o primeiro elemento da lista
animais[0] = 'galinha'
print(animais[0])

#removendo gato da lista
animais.remove('gato')
print(animais)
print(len(animais))

lista = [500, 30, 200, 10, 50]
print(max(lista))
print(min(lista))

animais.append('leão')
print(animais)
animais.extend(['cobra', 8])
print(animais)

lista.sort()
print(lista)

#as tuplas usam parênteses como sintaxe
tp = ('Banana', 'Maçã', 10, 50)

#diferente das listas as tuplas são imutáveis, o que quer dizer que não podemos alterar os seus elementos
#tp[0] = 'Laranja'

tp.count('Maçã')
print(tp[0:2])'''

#para criar um dicionario utilizamos as {}
dc = {'Maçã':20, 'Banana':10, 'Laranja':15, 'Uva':5}
print(dc)

#acessando o valor de um dicionário através da chave
print(dc['Maçã'])

#atualizando o valor de Maçã
dc['Maçã'] = 25

#retornando todas as chaves do dicionários
print(dc.keys())

#retornando valores do dicionário
print(dc.values())

#verificando se ja exite um chave no dicionário e caso não exita é inserida
dc.setdefault('Banana',10)
dc.setdefault('Amora', 30)
print(dc)

