from abc import ABC
try:
    from moviepy.editor import *

except ImportError:
    print('Clip  bindings requires "moviepy" package.')
    print('Install it via command:')
    print('pip install moviepy')
    raise


class Clip(ABC):

    def save(self, filename, fps=1):
        pass

    def add_clip(clip):
        pass

    def remove_clip(clip):
        pass

    def is_composition():
        return False


class Leaf_clip(Clip):
    '''

    '''

    def __init__(self, bg=[0, 0, 0], format="16:9", text="Hello!", traduction="Bonjour", font='FreeSans-Gras', audio1="", audio2=""):
        self.bg: list = bg
        self.text: str = text
        self.traductions: str = traduction
        self.audio1 = AudioFileClip(filename=audio1)
        self.audio2 = AudioFileClip(filename=audio2)
        self.duration = 1+self.audio1.duration+1+self.audio2.duration+1

        print("définition du format...")
        if format == "16:9":
            self.resolution = (1920, 1080)
            self.font_size = 120
        elif format == "9:16":
            self.resolution = (1080, 1920)
            self.font_size = 70
        elif format == "4:5":
            self.resolution = (1080, 1350)
        elif format == "1:1":
            self.resolution(1920, 1920)
            self.font_size = 120

        # construction de clip
        print("création du background ...")
        self.clip = ColorClip(
            size=self.resolution, color=self.bg, duration=self.duration+1)

        print("insertion du texte ...")
        self.text_clip = TextClip(
            txt=text, fontsize=self.font_size-20 if self.font_size > 30 else self.font_size, font=font, color='white')
        self.text_clip = self.text_clip.set_position(
            ("center", 0.8), relative=True).set_duration(self.duration+1)

        self.traduction_clip = TextClip(
            txt=traduction, fontsize=self.font_size, font=font,  color='white')
        self.traduction_clip = self.traduction_clip.set_position(
            'center').set_duration(self.duration+1)

        # print("composite video")
        print("Composition de la vidéo ...")
        self.video = CompositeVideoClip(
            [self.clip, self.text_clip, self.traduction_clip])

        print("Composition de l'audio ...")
        audio_compo = CompositeAudioClip([self.audio1.set_start(1),
                                          self.audio2.set_start(2+self.audio1.duration)])

        self.video = self.video.set_audio(audio_compo)
        self.video = CompositeVideoClip(
            [self.video, self.video.set_start(self.video.duration)])

    def save(self, filename="leaf_clip.mp4", fps=1):
        print("Enregistrement de la vidéo ...")
        self.video.write_videofile("../videos/"+filename, fps=fps)


class Title_clip(Clip):
    '''

    '''

    def __init__(self, bg=[0, 0, 0], format="16:9", title="Hello!", font='FreeSans-Gras', audio=""):
        self.bg: list = bg
        self.title: str = title
        self.audio = AudioFileClip(filename=audio)
        self.duration = 1+self.audio.duration

        print("définition du format...")
        if format == "16:9":
            self.resolution = (1920, 1080)
            self.font_size = 120
        elif format == "9:16":
            self.resolution = (1080, 1920)
            self.font_size = 70
        elif format == "4:5":
            self.resolution = (1080, 1350)
        elif format == "1:1":
            self.resolution(1920, 1920)
            self.font_size = 120

        # construction de clip
        print("création du background ...")
        self.clip = ColorClip(
            size=self.resolution, color=self.bg, duration=self.duration)

        print("insertion du texte ...")

        self.title_clip = TextClip(
            txt=self.title, fontsize=self.font_size, font=font,  color='white')
        self.title_clip = self.title_clip.set_position(
            'center').set_duration(self.duration)

        # print("composite video")
        print("Composition de la vidéo ...")
        self.video = CompositeVideoClip(
            [self.clip, self.title_clip])

        print("Composition de l'audio ...")

        self.video = self.video.set_audio(self.audio)

    def save(self, filename="title_clip.mp4", fps=1):
        print("Enregistrement de la vidéo ...")
        self.video.write_videofile("../videos/"+filename, fps=fps)


class Composition_clip(Clip):
    '''

    '''
    composition = None

    def __init__(self):
        self.clips: list = []

    def add_clip(self, clip):
        self.clips.append(clip)
        if self.composition == None:
            self.composition = clip
        else:
            self.composition = concatenate_videoclips(
                [self.composition.copy(), clip.copy()])

    def get_number_clip(self):
        return len(self.clips)

    def is_composition():
        return True

    def save(self, filename="composition_clip.mp4", fps=1):
        print("Enregistrement de la vidéo ...")
        # final_video = concatenate_videoclips(self.clips)
        # final_video.write_videofile("../videos/"+filename, fps=fps)
        self.composition.write_videofile("../videos/"+filename, fps=fps)
