import matplotlib as mpl
mpl.use('Agg')
from timeit import timeit
from random import randint
import matplotlib.pyplot as plt

def random_list(tam):
    lista = []
    i = 0
    while(i < tam):
        n = randint(1,1*tam)
        if n not in lista: 
            lista.append(n)
            i += 1
    return lista

def desenhaGrafico(x, y, z, w, xl = "Quantidades", yl = "Tempo"):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label = "Busca Linear")
    plt.plot(x, z, label = "Busca Binária")
    plt.plot(x, w, label = "Diferença")
    ax.legend(bbox_to_anchor = (1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.title("Busca Linear X Busca Binária", fontsize = 18)
    fig.savefig("pesquisas.png")

def busca_linear(lista, item):
    for i in range(len(lista)):
        if lista[i] == item:
            return True
    return False

def busca_binaria(lista, item):
    first = 0
    last = len(lista)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if lista[midpoint] == item:
            found = True
        else:
            if item < lista[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
	
        return found

def media (lista):
    x = 0
    for i in lista:
        x += i
    return x / len(lista)

qntes = []
mediasLinear = []
mediasBinario = []
mediasDiferenca = []

for i in range (6000, 24001, 3000):
    temposLinear = []
    temposBinario = []
    temposDiferenca = []
    qntes.append(i)
    lista = random_list(i)
    lista.sort()
    for j in range(10):
        num = lista[randint(0, i)]
        tlinear = timeit("busca_linear({}, {})".format(lista, num), setup="from __main__ import busca_linear", number=1)
        tbinario = (timeit("busca_binaria({}, {})".format(lista, num), setup="from __main__ import busca_binaria", number=1))
        temposLinear.append(tlinear)
        temposBinario.append(tbinario)
        temposDiferenca.append(abs(tlinear - tbinario))
    mediasLinear.append(media(temposLinear))
    mediasBinario.append(media(temposBinario))
    mediasDiferenca.append(media(temposDiferenca))

desenhaGrafico(qntes, mediasLinear, mediasBinario, mediasDiferenca)
