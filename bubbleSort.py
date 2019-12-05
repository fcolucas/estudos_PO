import matplotlib.pyplot as plt
from timeit import timeit
from random import randint

def geraLista(tam):
    lista = [ ]
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

def desenhaGrafico(x,y,xl = "Tempo de Ordenação", yl = "Quantidade de elementos na lista"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label ="gráfico")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig('graph.png')
 
def bubbleSort(lista):
    for j in range(0,len(lista)):
        for i in range(0,len(lista)-1):
            if lista[i]>lista[i+1]:
                aux = lista[i+1]
                lista[i+1] = lista[i]
                lista[i] = aux
    return lista

qntes = [1000,3000,6000,9000,12000,15000,18000,21000,24000]
tempos = []

for tam in qntes:
	lista = geraLista(tam)
	#print(lista)
	tempos.append(timeit("bubbleSort({})".format(lista),setup="from __main__ import bubbleSort",number=1))
	#print(bubbleSort(lista))
 
desenhaGrafico(tempos, qntes)