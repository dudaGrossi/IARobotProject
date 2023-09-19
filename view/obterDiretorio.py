import os

def caminho():
    # Obtém o diretório do projeto atual
    diretorio_projeto = os.path.dirname(os.path.abspath(__file__))
    # Constrói o caminho relativo para a imagem usando o diretório do projeto
    caminho_imagem = os.path.join(diretorio_projeto, "dog.png")

    return diretorio_projeto