from tkinter import *
from random import choice
import matplotlib.pyplot as plt

class Janela(Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.pessoas = []
        self.sorteio = []
        self.qntdd = []
        self.create_widgets()

    def create_widgets(self):
        self.lb1 = Label(self, text="Pessoa")
        self.lb1.place(x=80, y=50)
        self.nome = Entry(self)
        self.nome.place(x=130, y=50)
        self.addar = Button(self, text="Adicionar", bg='green')
        self.addar["command"] = self.adicionar
        self.addar.place(x=260, y=45)
        self.sorteiomaker = Button(self, text="Sortear", bg='blue')
        self.sorteiomaker["command"] = self.sortear
        self.sorteiomaker.place(x=200, y= 300)
        self.resultado = Label(self, text="O resultado será mostrado aqui", fg='red')
        self.resultado.place(x=100, y=330)
        self.apagar = Button(self, text="apagar", bg='red')
        self.apagar["command"] = self.erase
        self.apagar.place(x=150, y=300)
        self.possibilidade = Button(self, text="Chance", bg='yellow')
        self.possibilidade["command"] = self.probabilidade
        self.possibilidade.place(x=200, y=80)
        self.labpos = Label(self, text="Probabilidade:\nNenhuma 100%")
        self.labpos.place(x=130, y= 120)

    def adicionar(self):
        existente = False
        x = str(self.nome.get()).capitalize()
        if x.count("") == 0:
            return
        self.sorteio.append(x)
        for i in range(len(self.pessoas)):
            if self.pessoas[i] == x:
                self.qntdd[i] += 1
                existente = True
                break
        if not(existente):
            self.qntdd.append(1)
            self.pessoas.append(x)

    def sortear(self):
        if len(self.sorteio) == 0:
            return
        self.resultado["text"] = choice(self.sorteio)
        if len(self.qntdd)>6:
            return
        plt.bar(self.pessoas, self.qntdd, color="red")
        plt.show()
        plt.clf()

    def erase(self):
        self.pessoas = []
        self.qntdd = []
        self.sorteio = []

    def probabilidade(self):
        total = sum(self.qntdd)
        if len(self.qntdd) > 6:
            self.labpos["text"] = "Probabilidade (Mostrando as 6 primeiras pessoas) {} bilhetes:\n".format(total)
            for i in range(6):
                self.labpos["text"] += "{} tem {}% de chances\n".format(self.pessoas[i], round((self.qntdd[i]/total) * 100), 2)
        else:
            self.labpos["text"] = "Probabilidade ({} bilhetes):\n".format(total)
            for i in range(len(self.pessoas)):
                self.labpos["text"] += "{} tem {}% de chances\n".format(self.pessoas[i], round((self.qntdd[i]/total) * 100), 2)

root = Janela()
root.geometry("400x400")
root.title("Probabilidade")
root.mainloop()
