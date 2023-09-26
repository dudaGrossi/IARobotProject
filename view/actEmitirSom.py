import os
import pygame

def emitirSom(animal):
    #inicializa o pygame
    pygame.init()

    diretorio_sons = os.path.dirname(os.path.abspath(__file__)) + "/sons/"

    arquivoAudio = ""  #inicializa arquivoAudio como uma string vazia

    #cria um objeto de som para o som do animal correspondente:
    if animal == "robo":
        arquivoAudio = "robot.wav"
    elif animal == "urso":
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

    caminho_completo = os.path.join(diretorio_sons, arquivoAudio)  #combina o diretório com o nome do arquivo

    som = pygame.mixer.Sound(caminho_completo)

    #reproduz o som do animal
    som.play()

    #aguarda a reprodução do som terminar
    pygame.time.delay(int(som.get_length() * 1000))  #espera até que o som termine (em milissegundos)

    #encerra o pygame
    pygame.quit()


