import os
from tkinter import *
from PIL import Image, ImageTk

def mostraInterface(funcAtualizarInterface):
    #obtém o diretório do projeto atual
    diretorio_projeto = os.path.dirname(os.path.abspath(__file__)) + "/imagens/"

    janela = Tk()
    janela.title("Rosto do Robozinho")
    #maximiza a janela
    janela.state('zoomed')
    #defina um tamanho mínimo para a janela para evitar redimensionamento
    janela.minsize(800, 600)

    #obtém o tamanho da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    #função para atualizar a imagem com base na função de atualização fornecida
    def atualizar_imagem():
        caminho_imagem = os.path.join(diretorio_projeto, funcAtualizarInterface())
        imagem_robo = Image.open(caminho_imagem)
        imagem_robo = imagem_robo.resize((largura_tela, altura_tela))
        imagem_robo = ImageTk.PhotoImage(imagem_robo)
        label_imagem.configure(image=imagem_robo)
        label_imagem.image = imagem_robo  # Atualize a referência para a nova imagem
        janela.after(1000, atualizar_imagem)  # Chama a função a cada 1000 milissegundos (1 segundo)

    #constrói o caminho relativo para a imagem usando a função fornecida
    caminho_imagem = os.path.join(diretorio_projeto, funcAtualizarInterface())

    #carrega a imagem do robô
    imagem_robo = Image.open(caminho_imagem)

    #redimensiona a imagem para o tamanho da tela
    imagem_robo = imagem_robo.resize((largura_tela, altura_tela))

    #converte a imagem para um formato compatível com o tkinter
    imagem_robo = ImageTk.PhotoImage(imagem_robo)

    #exibir a imagem em um Label
    label_imagem = Label(janela, image=imagem_robo)
    label_imagem.grid(column=0, row=0)

    #inicializa a atualização automática da imagem
    atualizar_imagem()

    janela.mainloop()
