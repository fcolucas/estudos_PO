from random import shuffle

def verfica(lista):
    return lista.count(lista[0]) == len(lista)


def binsort(output, bin_lista, index):
    if len(bin_lista) == 0:
        return None
    elif len(bin_lista) == 1:
        return bin_lista[0]
    elif verfica(bin_lista):
        return bin_lista

    lista1 = []
    lista2 = []
    for num in bin_lista:
        if not (num & (1 << (bit_len - index))):
            lista1.append(num)
        else:
            lista2.append(num)

    out = binsort(output, lista1, index + 1)
    if out is not None:
        if isinstance(out, list):
            for z in out:
                output.append(z)
        else:
            output.append(out)
    out2 = binsort(output, lista2, index + 1)

    if out2 is not None:
        if isinstance(out2, list):
            for z in out2:
                output.append(z)
        else:
            output.append(out2)


def geraLista(tam):
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista


if __name__ == '__main__':
    output = []
    bin_lista = []
    lista = (geraLista(1000000))
    bit_len = (max(lista)).bit_length()

    binsort(output, lista, 0)
    print(output)
