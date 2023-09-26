import time
from view import actInterface, actLigar, actEmitirSom

from elevenlabs import generate, play, set_api_key

#configurando a chave de API para interagir com a biblioteca 'elevenlabs'
set_api_key("29444481d5fd068cfa67291345da0e54")

#função para gerar fala e reproduzir um áudio
def falar(str):
    #gerando um áudio com o texto 'str' usando a voz 'Gigi'
    #e um modelo específico ('eleven_multilingual_v2')
    audio = generate(
        text=str, 
        voice="Gigi", 
        model="eleven_multilingual_v2")
    
    #reproduzindo o áudio gerado
    play(audio)

    #esperando por 3 segundos após a reprodução do áudio
    time.sleep(3)

#função para realizar uma ligação 
def ligar():
    actLigar.realizaLigacao()

#função para mostrar uma interface
def mostrarInterface(str):
    actInterface.mostraInterface(str)

#função para emitir um som associado a um animal
def emitirSom(animal):
    actEmitirSom.emitirSom(animal)

