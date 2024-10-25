import os
from elevenlabs import play
from elevenlabs.client import ElevenLabs

api_key = os.getenv("ELEVEN_API_KEY")
if not api_key:
    raise ValueError("ELEVEN_API_KEY environment variable not set")

client = ElevenLabs(api_key=api_key)

audio = client.generate(
  text="Hello! 你好! Hola! नमस्ते! Bonjour! こんにちは! مرحبا! 안녕하세요! Ciao! Cześć! Привіт! வணக்கம்!",
  voice="Brian",
  model="eleven_multilingual_v2"
)
play(audio)