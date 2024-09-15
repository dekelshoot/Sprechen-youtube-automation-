from Clip import Leaf_clip, Title_clip, Composition_clip
from Audio import Audio_fr, Audio_de
from random import choice
import sys


class Sprechen():
    '''
    '''

    def __init__(self, data_path="../data/data.csv", format="16:9", filename="final.mp4"):
        self.format = format
        # intialisation des variables que nous allons utilisées
        print("\t >> load model...")
        self.audio_fr = Audio_fr()
        self.audio_de = Audio_de()
        self.composition = Composition_clip()

        print("\n\t >> load data...\n")
        self.data = self.load_data(data_path)

        print("\n\t >> generate composition with data\n")
        self.generate_composition_with_data(self.data)

        print("\n\t >> saving composition...\n")
        self.save(filename=filename)

    def load_data(self, filename):

        with open(filename, 'r', encoding="utf8") as file:
            print("création du dictionnaire...")
            lecteur_csv = file.readlines()
            data = {"data": {}}
            # create_graph(data)
            i = 1
            for ligne in lecteur_csv:
                ligne = ligne.strip().split(',')
                data["data"][i] = {
                    "text": ligne[0],
                    "traduction": ligne[1]
                }
                i += 1

            return data

    def generate_composition_with_data(self, data):
        length = len(data["data"])
        a = 0
        b = length+1
        percentage = 0
        c = ("\033[93m"+str(percentage)+"% ["+a*"#"+b*"-"+"]"+"\033[0m")
        sys.stdout.write('\r'+c)
        print("")
        a += 1
        b -= 1
        i = 1
        for key in data["data"].keys():

            self.audio_fr.generate_audio(
                text=data["data"][key]["text"]+".", file_path="../temp/audio1.wav")
            sys.stdout.write('\r'+c)
            self.audio_de.generate_audio(
                text=data["data"][key]["traduction"]+".", file_path="../temp/audio2.wav")
            sys.stdout.write('\r'+c)
            cl = Leaf_clip(bg=choice(self.get_bg()), format=self.format,
                           text=data["data"][key]["text"], traduction=data["data"][key]["traduction"], audio1="../temp/audio1.wav", audio2="../temp/audio2.wav")
            sys.stdout.write('\r'+c)
            self.composition.add_clip(cl.video)

            a += 1
            b -= 1
            percentage = int((i*100)/length)
            c = ("\033[93m"+str(percentage)+"% ["+a*"#"+b*"-"+"]"+"\033[0m")
            sys.stdout.write('\r'+c)
            i += 1
        return self.composition

    def save(self, filename="final.mp4", fps=1):
        self.composition.save(filename, fps=fps)

    def get_bg(self):
        return [[0, 100, 80], [30, 50, 100], [232, 17, 91], [216, 64, 0], [0, 100, 80], [20, 138, 8], [80, 55, 80], [140, 25, 50], [0, 100, 80], [141, 103, 171], [225, 17, 140], [233, 20, 41], [119, 119, 119], [216, 64, 0], [0, 100, 80], [230, 30, 50], [67, 130, 112], [140, 25, 50], [92, 10, 1], [1, 68, 92], [47, 92, 1], [165, 2, 78], [39, 1, 92], [5, 177, 120], [138, 68, 43], [23, 5, 187], [92, 78, 1], [162, 19, 155]]
