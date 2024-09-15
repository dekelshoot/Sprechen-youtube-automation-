from TTS.api import TTS
from moviepy.editor import AudioFileClip
from playsound import playsound
from abc import ABC
import torch
import os
import locale
os.environ["PYTHONIOENCODING"] = "utf-8"

device = "cuda" if torch.cuda.is_available() else "cpu"
speaker_wav = "../speaker/Daniel_fr.mp3"
speaker_wav2 = "../speaker/charlotte_de.mp3"
file_path = "../temp/audio1.wav"
file_path2 = "../temp/audio2.wav"

# tts = TTS(model_name="tts_models/fr/mai/tacotron2-DDC",
#           progress_bar=True).to(device)

tts2 = TTS(model_name="tts_models/de/css10/vits-neon",
           progress_bar=True).to(device)

# tts.tts_to_file("C'est le clonage de la voix.",
#                 speaker_wav=speaker_wav,
#                 file_path=file_path)

# print("voice genered ...")
# playsound(file_path)

tts2.tts_to_file("Am FlughafenFamilie Müller plant ihren Urlaub. Sie geht in ein Reisebüro und lässt sich von einem Angestellten beraten. Als Reiseziel wählt sie Mallorca aus. Familie Müller bucht einen Flug auf die Mittelmeerinsel. ",
                 file_path=file_path2,
                 split_sentences=False)

print("voice genered ...")
playsound(file_path2)
