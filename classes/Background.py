import os
import sys
import string
import random
import cv2 as cv
import numpy as np
try:
    import cv2 as cv
    import numpy as np
except ImportError:
    print('Background  bindings requires "cv2" package.')
    print('Install it via command:')
    print('    pip install opencv-python')
    raise


class Background:
    '''
    Background(background,format)

    ...

    Paramètres
    -----

    background : list
        est de type liste de taille 3 ou chaque élément représente une couleur de type RGB
        c'est la couleur de l'image qui sera formé .

    format : str 
        est le format de l'image qui sera généré avec ce background 
        (9:16 , 16:9 , 4:5 , 1:1 )

    ex: Background([239, 215,178 ],"16:9")'''

    def __init__(self, bg, format="16:9"):
        
        self.set_bg(bg)
        if format == "16:9":
            self.set_size([1920, 1080])
        elif format == "9:16":
            self.set_size([1080, 1920])
        elif format == "4:5":
            self.set_size([1080, 1350])
        elif format == "1:1":
            self.set_size([1920, 1920])
        else:

            raise ValueError(
                'aucun format correspondant\n exemple de format  9:16 , 16:9 , 4:5 , 1:1\n ex format = "16:9"')

    def generate_background(self):
        img = np.zeros((self.__size[1], self.__size[0], 3), np.uint8)
        img[:, :] = (self.__bg[2], self.__bg[1], self.__bg[0])
        name = self.generate_name()+".png"
        cv.imwrite("Backgrounds/"+name, img)
        return name

        # accessor and getter functions
    def get_bg(self):
        return self.__bg

    def set_bg(self, bg):
        self.__bg = bg

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size

    def generate_name(self):
        length_of_string = 8
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))


# a = Background([207, 44, 31], format="16:9")
# a.generate_background()
