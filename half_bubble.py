from random import shuffle

def half_bubble(lista):
    nova_lista = []
    tam = len(lista)
    half_tam = int(len(lista)/2)

    for j in range(half_tam):
        for i in range(tam - 1):
            if lista[tam - 1 - i] < lista[tam - 2 - i]:
                lista[tam - 1 - i], lista[tam - 2 - i] = lista[tam - 2 - i], lista[tam - 1 - i]
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista

def geraLista(tam):
    lista = list(range(0, tam+1))
    shuffle(lista)
    return lista

lista = geraLista(100)
half_bubble(lista)
print(lista)
