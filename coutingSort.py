import matplotlib.pyplot as plt
from timeit import timeit
from random import randint

def countingSort(lista, tam):
    indice = [0] * (tam + 1)
    for i in lista:
        indice[i] += 1
    ndx = 0;
    for i in range(len(indice)):
        while 0 < indice[i]:
            lista[ndx] = i
            ndx += 1
            indice[i] -= 1   
    return lista

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
    ax.plot(x,y, label = "Pior Caso")
    plt.plot(x, z, label= "Caso Medio")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig("counting.png")

length = []
time1 = []
time2 = []

for tams in range(3000, 24001, 3000):
    length.append(tams)
    time1.append(timeit("countingSort({}, {})".format(random_list(tams), tams),setup="from __main__ import countingSort",number=1))
    time2.append(timeit("countingSort({}, {})".format(reverse_list(tams), tams),setup="from __main__ import countingSort",number=1))
  
print(length)
print(time1)
print(time2)

desenhaGrafico(length, time1, time2)