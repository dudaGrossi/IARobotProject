import os
from tkinter import *
from PIL import Image, ImageTk

def mostraInterface(str):
    # Obtém o diretório do projeto atual
    diretorio_projeto = os.path.dirname(os.path.abspath(__file__)) + "/imagens/"

    janela = Tk()
    janela.title("Rosto do Robozinho")
    janela.attributes('-fullscreen', True)

    # Obtém o tamanho da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Constrói o caminho relativo para a imagem usando o diretório do projeto
    caminho_imagem = os.path.join(diretorio_projeto, str)

    # Carrega a imagem do robô
    imagem_robo = Image.open(caminho_imagem)

    # Redimensiona a imagem para o tamanho da tela
    imagem_robo = imagem_robo.resize((largura_tela, altura_tela))

    # Converte a imagem para um formato compatível com o tkinter
    imagem_robo = ImageTk.PhotoImage(imagem_robo)

    # Exibir a imagem em um Label
    label_imagem = Label(janela, image=imagem_robo)
    label_imagem.grid(column=0, row=0)

    janela.mainloop()
