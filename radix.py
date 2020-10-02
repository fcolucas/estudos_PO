from random import randint, shuffle
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt

def geraLista(tam):
    lista = list(range(0, tam+1))
    shuffle(lista)
    return lista

def plot_grafico(x, y, file_name, label1, xl = "Entradas", yl = "Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label= label1)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)

    fig.savefig(file_name)

def radix_sort(lista):
    base = 1
    maior = max(lista)

    while maior/base > 0:
        indice = len(lista) + 1
        ocorrencias = [0] * indice

        for i in lista:
            ocorrencias[i] += 1

        j = 0

        for i in range(indice):
            for j in range(ocorrencias[i]):
                lista[j] = i
                j += 1
        base *= 10

if __name__ == '__main__':
    x = [100000, 200000, 400000, 500000, 1000000, 2000000]
    y_des = []
    tempo_des = []

    for i in range(len(x)):
        y_des.append(geraLista(x[i]))

    for i in range(len(x)):
        tempo_des.append(timeit.timeit("radix_sort({})".format(y_des[i]), setup="from __main__ import radix_sort", number=1))
        print(i)

    plot_grafico(x, tempo_des, "Tempo do vetor aleatório", "Tempo")
