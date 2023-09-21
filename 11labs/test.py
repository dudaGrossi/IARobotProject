from elevenlabs import clone, generate, play, set_api_key
from elevenlabs.api import History

set_api_key("9077d79c1d6b8fffd8e385ad062f8605")

from elevenlabs import generate, play

audio = generate(
  text="Voltei",
  voice="Rachel",
  model="eleven_multilingual_v2"
)

play(audio)