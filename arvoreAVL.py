from tkinter import *
import math
import random
 
class Arvore(object):
    def __init__(self, data):
        self.data = data
        self.setaFilhos(None, None)

    def setaFilhos(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita
    
    def balanco(self):
        prof_esq = 0
        if self.esquerda:
            prof_esq = self.esquerda.profundidade()
        prof_dir = 0
        if self.direita:
            prof_dir = self.direita.profundidade()
        return prof_esq - prof_dir

    def profundidade(self):
        prof_esq = 0
        if self.esquerda:
            prof_esq = self.esquerda.profundidade()
        prof_dir = 0
        if self.direita:
            prof_dir = self.direita.profundidade()
        return 1 + max(prof_esq, prof_dir)

    def rotacaoEsquerda(self):
        self.data, self.direita.data = self.direita.data, self.data
        old_esquerda = self.esquerda
        self.setaFilhos(self.direita, self.direita.direita)
        self.esquerda.setaFilhos(old_esquerda, self.esquerda.esquerda)

    def rotacaoDireita(self):
        self.data, self.esquerda.data = self.esquerda.data, self.data
        old_direita = self.direita
        self.setaFilhos(self.esquerda.esquerda, self.esquerda)
        self.direita.setaFilhos(self.direita.direita, old_direita)

    def rotacaoEsquerdaDireita(self):
        self.esquerda.rotacaoEsquerda()
        self.rotacaoDireita()

    def rotacaoDireitaEsquerda(self):
        self.direita.rotacaoDireita()
        self.rotacaoEsquerda()

    def executaBalanco(self):
        bal = self.balanco()
        if bal > 1:
            if self.esquerda.balanco() > 0:
                self.rotacaoDireita()
            else:
                self.rotacaoEsquerdaDireita()
        elif bal < -1:
            if self.direita.balanco() < 0:
                self.rotacaoEsquerda()
            else:
                self.rotacaoDireitaEsquerda()

    def insere(self, data):
        if data <= self.data:
            if not self.esquerda:
                self.esquerda = Arvore(data)
            else:
                self.esquerda.insere(data)
        else:
            if not self.direita:
                self.direita = Arvore(data)
            else:
                self.direita.insere(data)
                 
class Aplicacao:
    def __init__(self, pai):
        self.Arvore = None
        self.t1 = Entry(pai)
        self.t1.bind("<Return>", self.constroiArvore)
        self.t1.pack()
        self.b1 = Button(pai)
        self.b1.bind("<Button-1>", self.constroiArvore)
        self.b1["text"] = "ENTRE COM VALOR"
        self.b1.pack()
        self.c1 = Canvas(pai, width=1024, height=650)
        self.c1.pack()
 
    def constroiArvore(self, *args):
        try:
            valor = int(self.t1.get())
        except Exception:
            return
        print(valor)
        if self.Arvore == None:
            print("Criando")
            self.Arvore = Arvore(valor)
        else:
            print("Inserindo")
            self.Arvore.insere(valor)
        self.desenhaArvore()
 
    def desenhaArvore(self):
        self.HORIZONTAL = 1024
        self.VERTICAL = 750
        self.tamanho = 30
        self.c1.delete(ALL)
        self.c1.create_rectangle(
            0, 0, self.HORIZONTAL, self.VERTICAL, fill="white")
        self.xmax = self.c1.winfo_width() - 40  # margem de 40
        self.ymax = self.c1.winfo_height()
        self.numero_linhas = self.Arvore.profundidade()
        x1 = int(self.xmax / 2 + 20)
        y1 = int(self.ymax / (self.numero_linhas + 1))
        self.Arvore.executaBalanco()
        self.desenhaNoh(self.Arvore, x1, y1, x1, y1, 1)
 
    def desenhaNoh(self, noh, posAX, posAY, posX, posY, linha):
        if noh == None:
            return
        numero_colunas = 2**(linha + 1)
        x1 = int(posX - self.tamanho / 2)
        y1 = int(posY - self.tamanho / 2)
        x2 = int(posX + self.tamanho / 2)
        y2 = int(posY + self.tamanho / 2)
        self.c1.create_line(posAX, posAY, posX, posY, fill="white")
        self.c1.create_oval(x1, y1, x2, y2, fill="white")
        self.c1.create_text(posX, posY, text=str(noh.data))
        posAX, posAY = posX, posY
        dx = self.xmax / numero_colunas
        dy = self.ymax / (self.numero_linhas + 1)
        posX = posAX + dx
        posY = posAY + dy
        self.desenhaNoh(noh.direita, posAX, posAY, posX, posY, linha + 1)
        posX = posAX - dx
        self.desenhaNoh(noh.esquerda, posAX, posAY, posX, posY, linha + 1)
     
 
if __name__ == "__main__":
    root = Tk(None, None, "Árvore AVL")
    root.geometry("1024x750")
    ap = Aplicacao(root)
    root.mainloop()
