import tkinter
from tkinter import messagebox, Entry, Label, PhotoImage, Button
from PIL import Image, ImageTk
import modules
from modules import calcula_imc, classificacao_imc

def acao():
    print('botao confirmado')
    indice = modules.calcula_imc(peso=entrada_peso.get().strip().replace(',','.'), altura=entrada_altura.get().strip().replace(',','.'))
    classificacao = modules.classificacao_imc(indice)
    msg = messagebox.showinfo('Classificação de IMC', classificacao)


janela = tkinter.Tk()
janela.title('Calcula IMC - rjz')

# Carrega a imagem e redimensiona
imagem_original = Image.open("png_hamburguer.png")
imagem_redimensionada = imagem_original.resize((56, 45))
imagem_tk = ImageTk.PhotoImage(imagem_redimensionada)

# Logo
logo = Label(master=janela, image=imagem_tk)
logo.grid(row=0, column=0, rowspan=2)

# Etiqueta de altura e entrada de altura
etiqueta_altura = Label(master=janela, text='Digite sua altura: ')
etiqueta_altura.grid(row=0, column=1)

entrada_altura = Entry(master=janela)
entrada_altura.grid(row=0, column=2)

# Etiqueta de entrada de peso e entrada de altura
etiqueta_peso = Label(master=janela, text='Digite seu peso: ')
etiqueta_peso.grid(row=1, column=1)

entrada_peso = Entry(master=janela)
entrada_peso.grid(row=1, column=2)

# Botão de ação
botao_acao = Button(master=janela, text='Calcular', command=acao)
botao_acao.grid(row=2, column=2, rowspan=2)

janela.mainloop()
