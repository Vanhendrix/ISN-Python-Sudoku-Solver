from tkinter import *
import os
class Sudoku:
    def __init__(self, jeu):#jeu eh uma matrix 9x9:
        try:
            for i in range(9):
                for j in range(9):
                    if int(jeu[i][j]) >= 0 or int(jeu[i][j]) <=9:
                        jeu[i][j] = int(jeu[i][j])
                    else:
                        raise ValueError("DADOS INCORRETOS")
        except:
            print('ERRO DE INICIALIZAÃ‡ÃƒO')
        self.__jeu = jeu
        self.__solution = []

    def getjeu(self):
        return self.__jeu
        print(self.__jeu)
    def setsolution(self, jeu):
        self.__solution = jeu
    def getNum(self, i,j):
        return self.__jeu[i][j]
    def setNum(self,i,j,n):
        self.__jeu[i][j] = n
    def getsolution(self):
        return self.__solution
    def verifica(self,lin,col, n):
        #n varia de um a nove
        #a funcao verifica se eh possivel acrescentar um numero no jeu sem contrariar as regras

        lin = int(lin)
        col = int(col)
        if self.getNum(lin,col) == n:
            return True

        if self.getNum(lin,col) != 0:
            return False

        for c in range(0,9):#verifica se o numero ja existe na linha
            if self.__jeu[lin][c] == n:
                return False

        for l in range(0,9):#verifica se o numero ja existe na coluna
            if self.__jeu[l][col] == n:
                return False
        lr = int(lin/3)
        cr = int(col/3)
        for l in range(lr*3, (lr + 1)*3):
            for c in range(cr*3, (cr + 1)*3):
                #if l >= 9 or c >= 9:
                #    continue
                if self.__jeu[l][c] == n:
                    #print('l = ', l, 'c = ', c, 'num = ', self.getNum(l,c), 'n = ', n)
                    return False
        return True

    def resolve(self, i, j):
        if i == 9:
            self.setsolution(self.__jeu)
            self.ecritsolution(self.getsolution())
            return 0

        else:
            for n in range(1,10):
                if self.verifica(i,j,n):
                    t = self.getNum(i,j)
                    self.setNum(i,j,n)
                    if j == 8:
                        self.resolve(i+1, 0)
                    else:
                        self.resolve(i, j+1)
                    self.setNum(i,j,t)

    def ecritsolution(self, solution):
        f = open("SudokuTEMP.txt", "w")
        try:
            for i in range (0,9):
                for j in range (0,9):
                    f.write(str(solution[i][j]))
                    f.write(' ')
                f.write('\n')
            f.write('\n\n')
            f.close()
        except:
            print("ERRO AO SALVAR O ARQUIVO")
        finally:
            f.close()



class Janela:
    def __init__(self, toplevel):

        toplevel.resizable(width = False, height = False)
        toplevel.title('sOLVEUR DE SUDOKU')

        fonte = ('Arial', 18)

        self.fr = Frame(toplevel)
        self.fr.bind('<Motion>', self.corrige)
        self.fr.pack(ipady = 0, padx = 0)
        self.fr1 = Frame(toplevel)
        self.fr1.bind('<Motion>', self.corrige)
        self.fr1.pack(ipady = 0, padx = 0)
        self.fr2 = Frame(toplevel)
        self.fr2.bind('<Motion>', self.corrige)
        self.fr2.pack(ipady = 0, padx = 0)
        self.fr3 = Frame(toplevel)
        self.fr3.bind('<Motion>', self.corrige)
        self.fr3.pack(ipady = 0, padx = 0)
        self.fr4 = Frame(toplevel)
        self.fr4.bind('<Motion>', self.corrige)
        self.fr4.pack(ipady = 0, padx = 0)
        self.fr5 = Frame(toplevel)
        self.fr5.bind('<Motion>', self.corrige)
        self.fr5.pack(ipady = 0, padx = 0)
        self.fr6 = Frame(toplevel)
        self.fr6.bind('<Motion>', self.corrige)
        self.fr6.pack(ipady = 0, padx = 0)
        self.fr7 = Frame(toplevel)
        self.fr7.bind('<Motion>', self.corrige)
        self.fr7.pack(ipady = 0, padx = 0)
        self.fr8 = Frame(toplevel)
        self.fr8.bind('<Motion>', self.corrige)
        self.fr8.pack(ipady = 0, padx = 0)
        self.fr9 = Frame(toplevel)
        self.fr9.bind('<Motion>', self.corrige)
        self.fr9.pack(ipady = 1, padx = 1)

        self.__jeu = []
        for i in range(1,10):
            self.__jeu += [[0,0,0,0,0,0,0,0,0]]

        variavel = self.fr
        px = 0
        py = 0
        cor = 'white'
        espessura = 0
        for i in range(0,9):
            for j in range(0,9):

                if i == 0:
                    variavel = self.fr
                if i == 1:
                    variavel = self.fr1
                if i == 2:
                    variavel = self.fr2
                if i == 3:
                    variavel = self.fr3
                if i == 4:
                    variavel = self.fr4
                if i == 5:
                    variavel = self.fr5
                if i == 6:
                    variavel = self.fr6
                if i == 7:
                    variavel = self.fr7
                if i == 8:
                    variavel = self.fr8


                if j%2 == 0 and i%2 == 0:
                    espessura = 1
                if j%2 != 0 and i%2 != 0:
                    espessura = 1

                if j in [3,4,5] and i in [0,1,2,6,7,8]:
                    cor = 'gray'
                elif j not in [3,4,5] and i not in [0,1,2,6,7,8]:
                    cor = 'gray'
                else:
                    cor = 'white'
                self.__jeu[i][j] = Entry(variavel, width = 2, font = fonte, bg = cor, cursor = 'arrow', borderwidth = 0,
                                          highlightcolor = 'yellow', highlightthickness = 1, highlightbackground = 'black',
                                          textvar = jg[i][j])
                self.__jeu[i][j].bind('<Button-1>', self.corrige)
                self.__jeu[i][j].bind('<FocusIn>', self.corrige)
                self.__jeu[i][j].bind('<Motion>', self.corrige)
                self.__jeu[i][j].pack(side = LEFT, padx = px, pady = py)

                espessura = 0

        self.btn1 = Button(self.fr9, text = 'Save', fg = 'purple', font = ('Arial', 13), command = self.salvar)
        self.btn1.pack(side = RIGHT)

        self.btn2 = Button(self.fr9, text = 'Solve', fg = 'green', font = ('Arial', 13), command = self.regra)
        self.btn2.pack(side = LEFT)

        self.btn3 = Button(self.fr9, text = 'Open', fg = 'blue', font = ('Arial', 13), command = self.abre)
        self.btn3.pack(side = LEFT)

        self.btn3 = Button(self.fr9, text = 'Reset', fg = 'red', font = ('Arial', 13), command = self.reset)
        self.btn3.pack(side = RIGHT)

        self.__nomedoarquivo = "Entrada.txt"
    def regra(self):
        try:
            solution = Sudoku(self.getjeu())
            solution.resolve(0,0)
            self.__nomedoarquivo = "SudokuTEMP.txt"
            self.abre()
            self.__nomedoarquivo = "Entrada.txt"
            os.remove("SudokuTEMP.txt")
        except:
            print("ERRO DE LEITURA")
        finally:
            self.__nomedoarquivo = "Entrada.txt"


    def getjeu(self):
        jeu = []
        for i in range(9):
            jeu += [[0,0,0,0,0,0,0,0,0]]
        for i in range(9):
            for j in range(9):
                #self.__jeu[i][j]
                jeu[i][j] = jg[i][j].get()
                if jeu[i][j] == '':
                    jeu[i][j] = 0
        return jeu

    def reset(self):
        for i in range(9):
            for j in range(9):
                jg[i][j].set('')
    def salvar(self):
        f = open("Sudoku.txt", "a")
        try:
            for i in range (9):
                for j in range (9):
                    if self.__jeu[i][j].get() == "":
                        f.write('0')
                    else:
                        f.write(self.__jeu[i][j].get())
                    f.write(' ')
                f.write('\n')
            f.write('\n\n')
            f.close()
        except:
            print("ERRO AO SALVAR O ARQUIVO")
        finally:
            f.close()

    def corrige(self, event):
        for i in range(9):
            for j in range(9):
                if jg[i][j].get() == '':
                    continue
                if len(jg[i][j].get()) > 1 or jg[i][j].get() not in ['1','2','3','4','5','6','7','8','9']:
                    jg[i][j].set('')
    def completa(self):
        for i in range(0,9):
            for j in range(0,9):
                jg[i][j].set(self.__jeu[i][j])
    def abre(self):
        try:
            f = open(self.__nomedoarquivo, 'r')

            texto = f.readline()
            texto = texto.split(' ')
            for i in range(0,9):
                for j in range(0,9):
                    if texto[0] == '0':
                        jg[i][j].set('')
                    else:
                        jg[i][j].set(texto[0])
                    texto.pop(0)
                texto = f.readline()
                texto = texto.split(' ')
            f.close()

        except:
            print ("ERRO FATAL")
        finally:
            f.close()




solution = []
raiz = Tk()
txt = StringVar(raiz)
jg = []
for i in range(1,10):
    jg += [[0,0,0,0,0,0,0,0,0]]
for i in range(0,9):
    for j in range(0,9):
        jg[i][j] = StringVar(raiz)

a = Janela(raiz)
raiz.mainloop()
