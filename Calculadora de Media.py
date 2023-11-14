from tkinter import *

class janela:
  def __init__(self, master):
    self.widget2=master
    self.widget2.title("Média Anual")

    self.fontePadrao = ("Arial", "10")

    self.zeroContainer = Frame(master)
    self.zeroContainer["padx"] = 10
    self.zeroContainer["pady"] = 5
    self.zeroContainer.pack()
    
    self.primeiroContainer = Frame(master)
    self.primeiroContainer["padx"] = 10
    self.primeiroContainer.pack()

    self.segundoContainer = Frame(master)
    self.segundoContainer["padx"] = 20
    self.segundoContainer.pack()

    self.terceiroContainer = Frame(master)
    self.terceiroContainer["padx"] = 20
    self.terceiroContainer["pady"] = 5
    self.terceiroContainer.pack()

    self.quartoContainer = Frame(master)
    self.quartoContainer["padx"] = 20
    self.quartoContainer.pack()

    #elementos da interface
  
    self.labelMed1 = Label(self.primeiroContainer, text="Média 1º Tri:   ")
    self.labelMed1["font"] = ("Arial", "10", "bold")
    self.labelMed1.pack(side=LEFT)

    self.entryMed1 = Entry(self.segundoContainer)
    self.entryMed1["width"] = 15
    self.entryMed1["font"] = self.fontePadrao
    self.entryMed1.pack(side=LEFT)
    self.entryMed1.insert(10, 0.0) 

    self.labelMed2 = Label(self.primeiroContainer, text="Média 2º Tri:   ")
    self.labelMed2["font"] = ("Arial", "10", "bold")
    self.labelMed2.pack(side=LEFT)

    self.entryMed2 = Entry(self.segundoContainer)
    self.entryMed2["width"] = 15
    self.entryMed2["font"] = self.fontePadrao
    self.entryMed2.pack(side=LEFT)
    self.entryMed2.insert(10, 0.0)

    self.labelMed3 = Label(self.primeiroContainer, text="Média 3º Tri:   ")
    self.labelMed3["font"] = ("Arial", "10", "bold")
    self.labelMed3.pack(side=LEFT)

    self.entryMed3 = Entry(self.segundoContainer)
    self.entryMed3["width"] = 15
    self.entryMed3["font"] = self.fontePadrao
    self.entryMed3.pack(side=LEFT)
    self.entryMed3.insert(10, 0.0)

    self.labelMedia1 = Label(self.quartoContainer,
                             text=" Média Anual: ")
    self.labelMedia1["font"] = ("Arial", "10", "bold")
    self.labelMedia1.pack(side=LEFT)

    self.entryMedia1 = Entry(self.quartoContainer)
    self.entryMedia1["width"] = 15
    self.entryMedia1["font"] = self.fontePadrao
    self.entryMedia1.pack(side=LEFT)

    self.calcular = Button(self.terceiroContainer)
    self.calcular["text"] = "Calcular"
    self.calcular["width"] = 13
    self.calcular["font"] = self.fontePadrao
    self.calcular["bg"] = "white"
    self.calcular["fg"] = "black"
    self.calcular["command"] = self.calculando
    self.calcular.pack(side=LEFT)

  def calculando(self):
    self.entryMedia1.delete(0, END)

    self.Med1 = float(self.entryMed1.get())
    self.Med2 = float(self.entryMed2.get())
    self.Med3 = float(self.entryMed3.get())

    self.Medt = (self.Med1 + self.Med2 + self.Med3)/3
    self.entryMedia1.insert(10, self.Medt)
      

      
    


class janelac:
  def __init__(self, master):
    self.widget2=master
    self.widget2.title("Créditos")

    self.primeiroContainer = Frame(master)
    self.primeiroContainer["padx"] = 10
    self.primeiroContainer.pack()

    self.segundoContainer = Frame(master)
    self.segundoContainer["padx"] = 10
    self.segundoContainer.pack()

    self.terceiroContainer = Frame(master)
    self.terceiroContainer["padx"] = 10
    self.terceiroContainer.pack()

    self.labelt1 = Label(self.primeiroContainer, text=" Programadores")
    self.labelt1["font"] = ("Arial", "11", "bold")
    self.labelt1.pack()

    self.labelRaf = Label(self.primeiroContainer, text=" Rafael Parise Rego")
    self.labelRaf["font"] = ("Arial", "10", "italic")
    self.labelRaf.pack()

    self.labelGab = Label(self.primeiroContainer, text=" Gabriel Lopes Prodossimo")
    self.labelGab["font"] = ("Arial", "10", "italic")
    self.labelGab.pack()

    self.labelPe = Label(self.primeiroContainer, text=" Participações Especiais")
    self.labelPe["font"] = ("Arial", "11", "bold")
    self.labelPe.pack()

    self.labelRod = Label(self.primeiroContainer, text=" Rodolfo Cruz da Silva")
    self.labelRod["font"] = ("Arial", "10", "italic")
    self.labelRod.pack()

    self.labelLuca = Label(self.primeiroContainer, text=" Luca Morelatto Mattedi")
    self.labelLuca["font"] = ("Arial", "10", "italic")
    self.labelLuca.pack()


class Application:
  def __init__(self, master):
    #menu
    self.widget1 = master
    self.widget1.title("Quanto falta para não pegar rec? 11.8.3")

    self.barra_menu = Menu(self.widget1)
    self.widget1.config(menu=self.barra_menu)

    self.arquivo = Menu(self.barra_menu, tearoff = 0)
    
    #self.barra_menu.add_command(label = "1T", command = self.neojanela1t)
    #self.barra_menu.add_command(label="2T", command = self.neojanela2t)
    #self.barra_menu.add_command(label="3T", command = self.neojanela3t)
    self.barra_menu.add_command(label = "Media Anual", command = self.neojanela)
    self.barra_menu.add_command(label = "Créditos", command = self.neojanelac)
    
    self.abrir = Menu(self.arquivo,tearoff = 0)
    self.abrir.add_command
    
    self.barra_menu = Menu()

    
    #Containers
    self.fontePadrao = ("Arial", "10")

    self.zeroContainer = Frame(master)
    self.zeroContainer["padx"] = 10
    self.zeroContainer.pack()
    
    self.primeiroContainer = Frame(master)
    self.primeiroContainer["pady"] = 10
    self.primeiroContainer.pack()

    self.segundoContainer = Frame(master)
    self.segundoContainer["padx"] = 20
    self.segundoContainer.pack()

    self.terceiroContainer = Frame(master)
    self.terceiroContainer["padx"] = 20
    self.terceiroContainer.pack()

    self.quartoContainer = Frame(master)
    self.quartoContainer["padx"] = 20
    self.quartoContainer["pady"] = 5
    self.quartoContainer.pack()

    self.quintoContainer = Frame(master)
    self.quintoContainer["padx"] = 20
    self.quintoContainer["pady"] = 5
    self.quintoContainer.pack()

    self.sextoContainer = Frame(master)
    self.sextoContainer["padx"] = 20
    self.sextoContainer["pady"] = 5
    self.sextoContainer.pack()

    #elementos da interface
    self.labelMedia1 = Label(self.quintoContainer,
                             text=" Média do Trimestre: ")
    self.labelMedia1["font"] = ("Arial", "10", "bold")
    self.labelMedia1.pack(side=LEFT)

    self.entryMedia1 = Entry(self.quintoContainer)
    self.entryMedia1["width"] = 15
    self.entryMedia1["font"] = self.fontePadrao
    self.entryMedia1.pack(side=LEFT)
    self.entryMedia1.insert(10, "???")

    self.labelAv11 = Label(self.segundoContainer, text="Nota Av1:     ")
    self.labelAv11["font"] = ("Arial", "10", "bold")
    self.labelAv11.pack(side=LEFT)

    self.entryAv11 = Entry(self.terceiroContainer)
    self.entryAv11["width"] = 15
    self.entryAv11["font"] = self.fontePadrao
    self.entryAv11.pack(side=LEFT)
    self.entryAv11.insert(10, 0.0)

    self.labelProc1 = Label(self.segundoContainer, text="Nota Processual:     ")
    self.labelProc1["font"] = ("Arial", "10", "bold")
    self.labelProc1.pack(side=LEFT)

    self.entryProc1 = Entry(self.terceiroContainer)
    self.entryProc1["width"] = 15
    self.entryProc1["font"] = self.fontePadrao
    self.entryProc1.pack(side=LEFT)
    self.entryProc1.insert(10, 0.0)

    self.labelAv21 = Label(self.segundoContainer, text="Nota Av2/REC:     ")
    self.labelAv21["font"] = ("Arial", "10", "bold")
    self.labelAv21.pack(side=LEFT)

    self.entryAv21 = Entry(self.terceiroContainer)
    self.entryAv21["width"] = 15
    self.entryAv21["font"] = self.fontePadrao
    self.entryAv21.pack(side=LEFT)
    self.entryAv21.insert(10, 0.0)

    self.labelBonus1 = Label(self.segundoContainer, text="Bonificação:")
    self.labelBonus1["font"] = ("Arial", "10", "bold")
    self.labelBonus1.pack(side=LEFT)

    self.entryBonus1 = Entry(self.terceiroContainer)
    self.entryBonus1["width"] = 15
    self.entryBonus1["font"] = self.fontePadrao
    self.entryBonus1.pack(side=LEFT)
    self.entryBonus1.insert(10, 0.0)

    #radiobutton
    self.var = IntVar()
    self.queroCalcularAMedia1 = Radiobutton(self.zeroContainer, text="<-Quero Calcular a Média", variable=self.var, value=1)
    self.queroCalcularAMedia1["font"] = ("Arial", "11", "bold")
    self.queroCalcularAMedia1["bg"] = "lightgrey"
    self.queroCalcularAMedia1.pack()
    self.queroCalcularAAv21 = Radiobutton(self.primeiroContainer, text="<-Quero Calcular quanto tenho que tirar na Av2", variable=self.var, value=2)
    self.queroCalcularAAv21["font"] = ("Arial", "11", "bold")
    self.queroCalcularAAv21["bg"] = "lightgrey"
    self.queroCalcularAAv21.pack()
    
    
    
    #elementos da interface
    self.tirar = "?"
    
    self.labelQuanto1 = Label(self.sextoContainer,
                              text="Baseado na sua nota, tem que tirar ")
    self.labelQuanto1["font"] = ("Arial", "10", "bold")
    self.labelQuanto1.pack(side=LEFT)
    
    self.entryQuanto1 = Entry(self.sextoContainer)
    self.entryQuanto1["width"] = 6
    self.entryQuanto1["font"] = self.fontePadrao
    self.entryQuanto1.pack(side=LEFT)
    self.entryQuanto1.insert(10, "???")
    

    self.labelQuantoLinha1 = Label(self.sextoContainer,
                              text= " para não pegar rec.")
    self.labelQuantoLinha1["font"] = ("Arial", "10", "bold")
    self.labelQuantoLinha1.pack(side=LEFT)
    #depois tenta em vez de LEFT padx ou pady

    self.calcular = Button(self.quartoContainer,
                           text="Calcular",
                           bg="white",
                           fg="black", width = "13",
                           command=self.calculo)
    self.calcular["bg"] = "lightgrey"
    self.calcular["font"] = ("Arial", "11", "bold")
    self.calcular.pack(side=LEFT)

  def neojanela(self):
    self.neojanela = Toplevel(self.widget1)
    janela(self.neojanela)

  def neojanelac(self):
    self.neojanelac = Toplevel(self.widget1)
    janelac(self.neojanelac)

  def calculo(self):
    self.entryMedia1.delete(0, END)

    self.Av11 = float(self.entryAv11.get())
    self.Proc1 = float(self.entryProc1.get())
    self.Av21 = float(self.entryAv21.get())
    self.Bonus1 = float(self.entryBonus1.get())
    self.VariavelRadio = int(self.var.get())

    self.Media1 = ((self.Av11 + self.Proc1 + self.Av21) / 3 + self.Bonus1)
    if self.Media1 > 10:
      self.Media1 = 10

    self.entryMedia1.insert(10, self.Media1)

    QuantoTirar = 18 - (self.Av11 + self.Proc1 + (self.Bonus1*3))
    if self.VariavelRadio == 1:
      self.entryQuanto1.delete(0, END)
      self.entryQuanto1.insert(10, " X")
    if self.VariavelRadio ==2:
      self.entryQuanto1.delete(0, END)
      if self.Media1 <= 6:
        self.entryQuanto1.delete(0, END)
        self.entryQuanto1.insert(10, QuantoTirar)
      else:
        self.entryQuanto1.delete(0, END)
        self.entryQuanto1.insert(10, 0)
    

import tkinter as tk
from tkinter import ttk

root = Tk()
root.title("Calculador de média v0.0.7")
Application(root)
root.mainloop()
