from re import M
from tkinter import *
from datetime import  datetime
from tkinter.filedialog import Open
            #Importando uma fonte baixada
import pyglet
f = pyglet.font.add_file('Digital-7.ttf')


###### Cores usadas #######
cor1 = "#3d3d3d"  # preta
cor2 = "#fafcff"  # branca
cor3 = "#21c25c"  # verde
cor4 = "#eb463b"  # vermelha
cor5 = "#dedcdc"  # cinza
cor6 = "#3080f0"  # azul    
        ##Definindo quais as cores que irei usar
fundo = cor1
cor = cor6
        ##Criando e definindo como variavel janela 
janela = Tk()
        ##titulo da janela/programa
janela.title('')
        ##Definindo o tamanho da janela do relógio
janela.geometry('430x180')
        ##Desabilitando o modo de alterar o tamanho da janela direto do aplicativo
janela.resizable(width=FALSE, height=FALSE)
        ##Definindo a cor de fundo do relógio
janela.configure(bg=cor1)

        ##Criando as funções
def relogio ():
        ##Criando a variavel tempo e atribuindo a biblioteca datetime(now de Agora)
    tempo = datetime.now()
        ##Criando as variaveis e 
    horas = tempo.strftime('%H:%M:%S')
    dia_semana = tempo.strftime('%A')
    dia = tempo.day
    mes = tempo.strftime('%m')
    ano = tempo.strftime('%Y')
    outro = tempo.strftime('%p')
    l1.config(text=horas)
    l1.after(200, relogio)
    l2.config(text=dia_semana + ' '*5 + str(dia) + '/' + str(mes) + '/' + str(ano) + ' '*28 + str(outro))
    
    return dia, mes, ano, outro

        #Sem Fonte
##l1=Label(janela, text='', font=('Arial 80'), bg=fundo, fg=cor)
        #Com fonte
l1=Label(janela, text='', font=('Digital-7 100'), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)
        #Com fonte
l2=Label(janela, text='', font=('Digital-7 17'), bg=fundo, fg=cor)
         #Sem Fonte
##l2=Label(janela, text='', font=('Arial 15'), bg=fundo, fg=cor)
l2.grid(row=2, column=0, sticky=W, padx=5)

relogio()
janela.mainloop()