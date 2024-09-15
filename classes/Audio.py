from TTS.api import TTS
from moviepy.editor import AudioFileClip
from playsound import playsound
from abc import ABC


class Audio(ABC):
    '''
    Audio est classe qui génère un audio à partir du texte avec l'intéligence artificiel

    ...

    Paramètres
    ---------
    none

    '''

    def __init__(self):
        pass

    def generate_audio(self, text="Bonjour",  speed=1, file_path="audio.wav"):
        '''
        generate_audio génère un audio à partir du texte avec l'intéligence artificiel

        ...

        Paramètres
        ---------
        text : str 
            le texte à générer

        speaker : str
            la voie de génération 
            ex: charlotte
                pour plus de voix executez:
                    $ tts --model_name tts_models/multilingual/multi-dataset/xtts_v2 \ --list_speaker_idx

        language : str
            la langue de la voie
            ex: fr, en, de etc ...

        speed: float
            la vitesse de la voie

        file_path : str
            le chemin ou sera savegarder le fichier audio
            ex: audio.wav
        '''
        print("getting voice ...")
        self.tts.tts_to_file(text=text,
                             file_path="../temp/"+file_path,
                             speed=speed,
                             split_sentences=True
                             )

        audio = AudioFileClip(filename="../temp/"+file_path)

        print("voice genered ...")
        self.play(audio="../temp/"+file_path)
        return audio

    def play(self, audio=""):
        playsound(audio)
        print("playing audio ...")


class Audio_fr(Audio):
    def __init__(self):
        self.tts = TTS("tts_models/fr/css10/vits",
                       progress_bar=True, gpu=False)


class Audio_de(Audio):
    def __init__(self):
        self.tts = TTS("tts_models/de/css10/vits-neon",
                       progress_bar=True, gpu=False)
