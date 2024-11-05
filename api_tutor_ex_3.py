import os
import pandas as pd
from elevenlabs import ElevenLabs, VoiceSettings

ELEVENLABS_API_KEY = os.getenv("ELEVEN_API_KEY")
client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)

def text_to_speech_file(text: str, save_file_path: str) -> None:
    # Calling the text_to_speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcFmaJgB", # Adam pre-made voice
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_turbo_v2_5", # use the turbo model for low latency
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )

    # Writing the audio to a file
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

def process_spreadsheet(file_path: str) -> None:
    # Read the spreadsheet
    df = pd.read_excel(file_path, header=None)

    # Iterate through each row in the spreadsheet
    for index, row in df.iterrows():
        text = row.iloc[0]
        save_file_path = row.iloc[1]
        text_to_speech_file(text, save_file_path)

# Example usage
process_spreadsheet("LinesofText.xlsx")
