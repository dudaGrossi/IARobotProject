import time
from view import actLigar

from elevenlabs import generate, play

def act(str):
    audio = generate(
        text=str, 
        voice="Daniel", 
        model="eleven_multilingual_v2")
    play(audio)
    time.sleep(3)

def ligar():
    actLigar.realizaLigacao()
