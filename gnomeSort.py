import matplotlib.pyplot as plt
from timeit import timeit
from random import randint

def gnomeSort(items):
    i = 0
    n = len(items)
    while i < n:
        if i and items[i] < items[i-1]:
            items[i], items[i-1] = items[i-1], items[i]
            i -= 1
        else:
            i += 1
    return items

def reverse_list(tam):
    lista = []
    i = 0
    while i < tam:
        lista.append(tam - i)
        i = i + 1
    return lista
      
def random_list(tam):
    lista = [ ]
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
        
    return lista

def desenhaGrafico(x, y, z, xl = "Tamanho", yl = "Tempo(s)"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Caso Médio")
    plt.plot(x, z, label= "Pior Caso")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig("gnome.png")

length = []
time1 = []
time2 = []

for tams in range(3000, 24001, 3000):
    length.append(tams)
    time1.append(timeit("gnomeSort({})".format(random_list(tams)),setup="from __main__ import gnomeSort",number=1))
    time2.append(timeit("gnomeSort({})".format(reverse_list(tams)),setup= "from __main__ import gnomeSort",number=1))
 
print(length)
print(time1)
print(time2)

desenhaGrafico(length, time1, time2)