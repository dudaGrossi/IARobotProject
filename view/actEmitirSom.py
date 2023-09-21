import os
import pygame

def emitirSom(animal):
    # Inicialize o pygame
    pygame.init()

    diretorio_sons = os.path.dirname(os.path.abspath(__file__)) + "/sons/"

    arquivoAudio = ""  # Inicialize arquivoAudio como uma string vazia

    # Crie um objeto de som para o som do animal correspondente:
    if animal == "urso":
        arquivoAudio = "bear.wav"
    elif animal == "touro":
        arquivoAudio = "bull.wav"
    elif animal == "coelho":
        arquivoAudio = "bunny.wav"
    elif animal == "gato":
        arquivoAudio = "cat.wav"
    elif animal == "vaca":
        arquivoAudio = "cow.wav"
    elif animal == "cachorro":
        arquivoAudio = "dog.wav"
    elif animal == "macaco":
        arquivoAudio = "monkey.wav"
    elif animal == "panda":
        arquivoAudio = "panda.wav"

    caminho_completo = os.path.join(diretorio_sons, arquivoAudio)  # Combine o diretório com o nome do arquivo

    som = pygame.mixer.Sound(caminho_completo)

    # Reproduza o som do animal
    som.play()

    # Aguarde a reprodução do som terminar
    pygame.time.delay(int(som.get_length() * 1000))  # Espera até que o som termine (em milissegundos)

    # Encerre o pygame
    pygame.quit()

#emitirSom("gato")
