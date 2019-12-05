import matplotlib.pyplot as plt
from timeit import timeit
from random import randint

def random_lista(tam):
  lista = [ ]
  for i in range(tam):
  	n = randint(1,1*tam)
  	if n not in lista: lista.append(n)
  return lista

def reverso_lista(tam):
  lista = []
  n = tam
  for i in range(tam):
    lista.append(n)
    n=n-1
  return lista

def geraLista(tam):
    lista = [ ]
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

def desenhaGrafico(x,y,z,xl = "Elementos", yl = "Tempo"):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Caso Medio")
    plt.plot(x, z, label="Pior Caso")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig('image.png')
 
def selection(lista):
    for j in range(len(lista)-1,0,-1):
        x = 0
        for i in range(1,j+1):
            if lista[i]>lista[x]:
                x = i
        lista[j],lista[x] = lista[x],lista[j]
    return lista

tempo1 = []
tempo2 = []
length = []
for i in range (3000, 24001, 3000):
	length.append(i)
	lista1 = random_lista(i)
	lista2 = reverso_lista(i)
	tempo1.append(timeit("selection({})".format(lista1),setup="from __main__ import selection",number=1))
	tempo2.append(timeit("selection({})".format(lista2),setup="from __main__ import selection",number=1))
 
desenhaGrafico(length, tempo1, tempo2)