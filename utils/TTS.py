import os
import torch
import requests
import urllib.parse
import unicodedata
import re
import subprocess
import sys
from dimits import Dimits

def silero_tts(tts, language, model, speaker):
    device = torch.device('cpu')
    torch.set_num_threads(4)
    local_file = 'model.pt'

    if not os.path.isfile(local_file):
        torch.hub.download_url_to_file(f'https://models.silero.ai/models/tts/{language}/{model}.pt',
                                    local_file)  

    model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
    model.to(device)

    example_text = "i'm fine thank you and you?"
    sample_rate = 48000

    audio_paths = model.save_wav(text=tts,
                                speaker=speaker,
                                sample_rate=sample_rate)

def mbrola_tts(tts, langs, speaker):
    voice = Voice(lang=langs, voice_id=speaker)
    wav = voice.to_audio(tts)
    with open("test.wav", "wb") as wavfile:
        wavfile.write(wav)

def text_sanitizing(text):
    # Normalize unicode to NFKD
    text = unicodedata.normalize("NFKD", text)
    # Remove non-ASCII, encode to ASCII, ignore bad characters
    text = text.encode("ascii", "ignore").decode("ascii")
    # Remove emojis and control characters
    text = re.sub(r'[\U00010000-\U0010ffff]', '', text)
    # Strip weird characters and allow safe characters including useful punctuation
    text = re.sub(r"[^a-zA-Z0-9.,!?'\-\"()\[\] \n]", '', text)
    # Replace multiple spaces with one
    text = re.sub(r'\s+', ' ', text)

    return text.strip()

def piper_tts(tts):
    clean = text_sanitizing(tts)
    script = f"""
from dimits import Dimits
dt = Dimits("en_US-bryce-medium")
dt.text_2_audio_file(
    '''{clean}''',
    "test",
    r"C:\\Users\\Vayne\\Documents\\Fully-Adaptive-Liaison-and-Companion-Oracle",
    format="wav"
)
"""

    try:
        result = subprocess.run(
            [sys.executable, "-c", script],
            capture_output=True,
            text=True,
            timeout=60
        )
        if result.returncode != 0:
            print("[PIPER TTS ERROR]", result.stderr.strip())
        else:
            print("[PIPER TTS SUCCESS]")
    except subprocess.TimeoutExpired:
        print("[PIPER TTS ERROR] Piper timed out.")
    except Exception as e:
        print("[PIPER TTS ERROR]", e)

if __name__ == "__main__":
    silero_tts()
