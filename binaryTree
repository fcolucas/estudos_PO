from random import shuffle, sample
import random


class No:
    def __init__(self, chaves=None, folhas=True, filhos=None):
        if chaves is None:
            chaves = []
        if filhos is None:
            filhos = []
        self.chaves = chaves
        self.folhas = folhas
        self.filhos = []

    def __getitem__(self, i):
        return self.chaves[i]

    def __delitem__(self, i):
        del self.chaves[i]

    def __setitem__(self, i, k):
        self.chaves[i] = k

    def __len__(self):
        return len(self.chaves)

    def __repr__(self):
        return str(self.chaves)

    def __str__(self):
        filhos = ','.join([str(no.chaves) for no in self.filhos])
        return f'chaves:     {self.chaves}\nfilhos: {filhos}\nfolhas:   {self.folhas}'

    def obterfilho(self, i):
        return self.filhos[i]

    def apagarfilho(self, i):
        del self.filhos[i]

    def definirfilho(self, i, filho):
        self.filhos[i] = filho

    def obterfilhos(self, begin=0, end=None):
        if end is None:
            return self.filhos[begin:]
        return self.filhos[begin:end]

    def procurarchave(self, chave):
        for i, k in enumerate(self.chaves):
            if k >= chave:
                return i
        return len(self)

    def atual(self, chaves=None, folhas=None, filhos=None):
        if chaves is not None:
            self.chaves = chaves
        if filhos is not None:
            self.filhos = filhos
        if folhas is not None:
            self.folhas = folhas

    def insert(self, i, chave=None, no=None):
        if chave is not None:
            self.chaves.insert(i, chave)
        if not self.folhas and no is not None:
            self.filhos.insert(i, no)

    def folhasNo(self):
        return self.folhas

    def dividir(self, prt, t):
        # form new two Nos
        k = self[t - 1]
        no1 = No()
        no2 = No()
        no1.chaves, no2.chaves = self[:t - 1], self[
                                               t:]  # note that t is 1 bigger than  chave index
        no1.folhas = no2.folhas = self.folhas
        if not self.folhas:
            # note that  filhos index is one bigger than chave index, and all filhos included
            no1.filhos, no2.filhos = self.filhos[0:t], self.filhos[t:]
        # connect them to parent
        posicao = prt.procurarchave(k)
        if prt.filhos != []:
            prt.filhos.remove(self)  # remove the original No
        prt.insert(posicao, k, no2)
        prt.insert(posicao, no=no1)
        return prt


class binaryTree:
    def __init__(self, baixo=2):
        self.raiz = No()
        self.baixo = baixo
        self.NoNum = 1
        self.chaveNum = 0

    def procurar(self, chave, withpath=False):
        no = self.raiz
        pai = []
        while True:
            i = no.procurarchave(chave)
            if i == len(no):
                pai.append((no, i - 1, i))
            else:
                pai.append((no, i, i))
            if i < len(no) and no[i] == chave:
                if withpath:
                    return no, i, pai
                else:
                    return no, i
            if no.folhasNo():
                if withpath:
                    return None, None, None
                else:
                    return None, None
            no = no.obterfilho(i)

    def insert(self, chave):
        if len(self.raiz) == self.baixo * 2 - 1:
            self.raiz = self.raiz.dividir(No(folhas=False), self.baixo)
            self.NoNum += 2
        no = self.raiz
        while True:
            posicao = no.procurarchave(chave)
            if posicao < len(no) and no[posicao] == chave:
                return
            if no.folhasNo():
                no.insert(posicao, chave)
                self.chaveNum += 1
                return
            else:
                filho = no.obterfilho(posicao)
                if len(
                    filho
                ) == self.baixo * 2 - 1:  # ensure its chaves won't excess when its filho dividir ano u
                    no = filho.dividir(no, self.baixo)
                    self.NoNum += 1
                else:
                    no = filho

    def apagar(self, chave):
        no, posicao, pai = self.procurar(chave, withpath=True)
        if no is None:
            return
        del no[posicao]
        self.chaveNum -= 1
        if not no.folhasNo():
            filho = no.obterfilho(posicao)  # find the predecessor chave
            while not filho.folhasNo():
                pai.append((filho, len(filho) - 1, len(filho)))
                filho = filho.obterfilho(-1)
            pai.append((filho, len(filho) - 1, len(filho)))
            no.insert(posicao, filho[-1])
            del filho[-1]
        if len(pai) > 1:
            self.balanceamento(pai)

    def balanceamento(self, pai):
        no, chaveposicao, filhoposicao = pai.pop()
        while len(no) < self.baixo - 1:  # balanceamento tree from down to up
            prt, chaveposicao, filhoposicao = pai[-1]
            no_esquerdo = [] if filhoposicao == 0 else prt.obterfilho(filhoposicao - 1)
            no_direito = [] if filhoposicao == len(prt) else prt.obterfilho(filhoposicao + 1)
            if len(no_esquerdo) < self.baixo and len(
                no_direito) < self.baixo:  # merge two deficient Nos
                beforeNo, afterNo = None, None
                if no_esquerdo == []:
                    chaveposicao = filhoposicao
                    beforeNo, afterNo = no, no_direito
                else:
                    beforeNo, afterNo = no_esquerdo, no
                    chaveposicao = filhoposicao - 1  # important, when choosing
                chaves = beforeNo[:] + [prt[chaveposicao]] + afterNo[:]
                filhos = beforeNo.obterfilhos() + afterNo.obterfilhos()
                folhas = beforeNo.folhasNo()
                prt.apagarfilho(chaveposicao + 1)
                del prt[chaveposicao]
                no.atual(chaves, folhas, filhos)
                prt.filhos[chaveposicao] = no
                self.NoNum -= 1
            elif len(
                no_esquerdo
            ) >= self.baixo:  # rotate  when only one sibling is deficient
                chaveposicao = filhoposicao - 1
                no.insert(0, prt[chaveposicao])  # rotate chaves
                prt[chaveposicao] = no_esquerdo[-1]
                del no_esquerdo[-1]
                if not no.folhasNo():  # if not leaf, move filhos
                    no.insert(0, no=no_esquerdo.obterfilho(-1))
                    no_esquerdo.apagarfilho(-1)
            else:
                chaveposicao = filhoposicao
                no.insert(len(no), prt[chaveposicao])  # rotate chaves
                prt[chaveposicao] = no_direito[0]
                del no_direito[0]
                if not no.folhasNo():  # if not leaf, move filhos
                    # note that insert(-1,ele) will make the ele be the last secono one
                    no.insert(len(no), no=no_direito.obterfilho(0))
                    no_direito.apagarfilho(0)
            if len(pai) == 1:
                if len(self.raiz) == 0:
                    self.raiz = no
                    self.NoNum -= 1
                break
            no, i, j = pai.pop()

    def __str__(self):
        cabeca = '\n' + '-' * 30 + 'B  Tree' + '-' * 30
        cauda = '-' * 30 + 'the end' + '-' * 30 + '\n'
        lista = [[cabeca], [f'No num: {self.NoNum},  chave num: {self.chaveNum}']]
        cur = []
        noNum = 0
        noTotal = 1
        que = [self.raiz]
        while que != []:
            no = que.pop(0)
            cur.append(repr(no))
            noNum += 1
            que += no.obterfilhos()
            if noNum == noTotal:
                lista.append(cur)
                cur = []
                noNum = 0
                noTotal = len(que)
        lista.append([cauda])
        lista = [','.join(li) for li in lista]
        return '\n'.join(lista)

    def __iter__(self, no=None):
        if no is None:
            no = self.raiz
        que = [no]
        while que != []:
            no = que.pop(0)
            yield no
            if no.folhasNo():
                continue
            for i in range(len(no) + 1):
                que.append(no.obterfilho(i))


if __name__ == '__main__':
    btree = binaryTree()

    print("Programa Btree")
    opcao = 0
    while opcao != 4:
        print("***********************************")
        print("Entre com a opcao:")
        print(" --- 1: Inserir")
        print(" --- 2: Excluir")
        print(" --- 3: Pesquisar")
        print(" --- 4: Sair do programa")
        print("***********************************")
        opcao = int(input("-> "))
        if opcao == 1:
            # Alterar a quantidade de elementos
            valor = [100]
            for x in valor:
                lista = list(range(0, x + 1))
                random.shuffle(lista)
            # teste = sample(lista, len(lista) // 4)
            print("Btree: ")
            for i in lista:
                btree.insert(i)
                print("Elemento inserido", i)
                print(btree)
            print(btree)
        elif opcao == 2:
            for i in lista:
                print("Elemento para deletar", i)
                btree.apagar(i)
                print(btree)
        elif opcao == 3:
            print("Procura ", i)
            for i in lista:
                no, posicao = btree.procurar(i)
                print(f'No: {repr(no)}[{posicao}]== {i}')

        elif opcao == 4:
            break
