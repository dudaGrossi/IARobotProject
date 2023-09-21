from elevenlabs import clone, generate, play, set_api_key
from elevenlabs.api import History

set_api_key("9858874ac087f38c73b03412b998bcb9")

from elevenlabs import generate, play

audio = generate(
  text="Voltei",
  voice="Daniel",
  model="eleven_multilingual_v2"
)

play(audio)