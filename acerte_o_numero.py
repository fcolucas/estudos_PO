import random


def usuario(numero_gerado):
    contador_usuario = 0
    chute_usuario = 0
    while chute_usuario != numero_gerado:
        chute_usuario = int(input("Tente adivinhar o número: "))
        contador_usuario += 1
        if chute_usuario > numero_gerado:
            print("O número gerado é menor que o chute: ", chute_usuario)
        elif chute_usuario < numero_gerado:
            print("O número gerado é maior que o chute: ", chute_usuario)

    print("NA MOSCA! O número gerado foi: ", numero_gerado)
    print("Você precisou de ", contador_usuario,
          " rodadas para acertar o número gerado.")
    return contador_usuario


def maquina(numero_gerado):
    menor_numero = 1
    maior_numero = 1000000
    chute = 500000
    contador = 0

    while chute != numero_gerado:
        chute = (menor_numero+maior_numero)//2
        contador += 1
        print(contador, "° Tentativa da máquina foi: ", chute)
        if chute > numero_gerado:
            maior_numero = chute
        elif chute < numero_gerado:
            menor_numero = chute + 1

    print("A máquina precisou de ", contador,
          " rodadas para acertar o número gerado!!")
    return contador


def main():
    numero_gerado = random.randrange(1, 1000000)
    print("A máquina gerou o número ", numero_gerado)
    if numero_gerado < 1 or numero_gerado > 1000000:
        print("O número precisa estar entre [1, 1000000]")
    else:
        contador_usuario = usuario(numero_gerado)
        contador_maquina = maquina(numero_gerado)
        if contador_usuario < contador_maquina:
            print("PARABÉNS! Você ganhou da máquina.")
        else:
            print("Não foi dessa vez que você venceu a máquina!")


main()
