import time
from view import actInterface, actLigar

from elevenlabs import generate, play, set_api_key

set_api_key("9077d79c1d6b8fffd8e385ad062f8605")

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
