from timeit import timeit
from random import randint
import matplotlib.pyplot as plt

def desenhaGrafico(x,y,z,xl = "Elementos", yl = "Tempo"):
  fig = plt.figure(figsize=(10, 10))
  ax = fig.add_subplot(111)
  ax.plot(x,y, label = "Caso 1")
  plt.plot(x, z, label="Caso 2")
  ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
  plt.ylabel(yl)
  plt.xlabel(xl)
  fig.savefig('mergesort.png')

def mergeSort(x):
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x)/2)
    y = mergeSort(x[:mid])
    z = mergeSort(x[mid:])
    while (len(y) > 0) or (len(z) > 0):
        if len(y) > 0 and len(z) > 0:
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
        elif len(z) > 0:
            for i in z:
                result.append(i)
                z.pop(0)
        else:
            for i in y:
                result.append(i)
                y.pop(0)
    return result

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


tempo1 = []
tempo2 = []
length = []

for i in range (3000, 24001, 3000):
	length.append(i)
	lista1 = random_lista(i)
	lista2 = reverso_lista(i)
	tempo1.append(timeit("mergeSort({})".format(lista1),setup="from __main__ import mergeSort",number=1))
	tempo2.append(timeit("mergeSort({})".format(lista2),setup="from __main__ import mergeSort",number=1))

desenhaGrafico(length, tempo1, tempo2)