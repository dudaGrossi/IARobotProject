import time
from view import actInterface, actLigar, actEmitirSom

from elevenlabs import generate, play, set_api_key

set_api_key("29444481d5fd068cfa67291345da0e54")

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

