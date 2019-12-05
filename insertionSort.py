import matplotlib.pyplot as plt
from timeit import timeit
from random import randint

def insertionSort(lista):
	for i in range(1,len(lista)):
    	x = lista[i]
    	j = i-1
    	while j>=0 and x<lista[j]:
        	lista[j+1] = lista[j]
        	j=j-1
		
		lista[j+1] = x
	return lista

def random_lista(tam):
	lista = [ ]
	for i in range(tam):
		n = randint(1,1*tam)
		if n not in lista: lista.append(n)
			
	return lista

def desenhaGrafico(x,y,z,xl = "Elementos", yl = "Tempo"):
	fig = plt.figure(figsize=(10, 10))
	ax = fig.add_subplot(111)
	ax.plot(x,y, label = "Caso 1")
	plt.plot(x, z, label="Caso 2")
	ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
	plt.ylabel(yl)
	plt.xlabel(xl)
	fig.savefig('image.png')
  
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
	tempo1.append(timeit("insertionSort({})".format(lista1),setup="from __main__ import insertionSort",number=1))
	tempo2.append(timeit("insertionSort({})".format(lista2),setup="from __main__ import insertionSort",number=1))

desenhaGrafico(length, tempo1, tempo2)