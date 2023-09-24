import time
from view import actInterface, actLigar, actEmitirSom

from elevenlabs import generate, play, set_api_key

set_api_key("030fbc23763c00a37e26d23eeb44eeac")

def falar(str):
    audio = generate(
        text=str, 
        voice="Gigi", 
        model="eleven_multilingual_v2")
    play(audio)
    time.sleep(3)

def ligar():
    actLigar.realizaLigacao()

def mostrarInterface(str):
    actInterface.mostraInterface(str)

def emitirSom(animal):
    actEmitirSom.emitirSom(animal)

