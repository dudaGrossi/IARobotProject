import time
from view import actInterface, actLigar

from elevenlabs import generate, play

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
