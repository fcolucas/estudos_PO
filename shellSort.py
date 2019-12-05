import matplotlib as mpl
mpl.use('Agg')
from timeit import timeit
from random import randint
import matplotlib.pyplot as plt

def desenhaGrafico(x,y,z,xl = "Tempo", yl = "Elementos"):
	fig = plt.figure(figsize=(10, 10))
	ax = fig.add_subplot(111)
	ax.plot(x,y, label = "Caso Médio")
	plt.plot(x, z, label = "Pior Caso")
	ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
	plt.ylabel(yl)
	plt.xlabel(xl)
	fig.savefig("shellSort.png")

def shellSort(lista):
    inc = len(lista) // 2
    while inc:
        for i, num in enumerate(lista):
            while i >= inc and lista[i - inc] > num:
                lista[i] = lista[i - inc]
                i -= inc
            lista[i] = num
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return lista

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

length = []
tempo1 = []
tempo2 = []

for i in range (3000, 24001, 3000):
	length.append(i)
	lista1 = random_lista(i)
	lista2 = reverso_lista(i)
	tempo1.append(timeit("shellSort({})".format(lista1),setup="from __main__ import shellSort",number=1))
	tempo2.append(timeit("shellSort({})".format(lista2),setup="from __main__ import shellSort",number=1))

desenhaGrafico(length, tempo1, tempo2)