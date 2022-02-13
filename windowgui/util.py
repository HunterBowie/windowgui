import pygame
from os import path

class Colors:
	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)
	RED = (255, 0, 0)
	GREEN = (0, 255, 0)
	BLUE = (0, 0, 255)
	YELLOW = (255, 255, 0)
	ORANGE = (255, 100, 0)
	PURPLE = (150, 50, 250)
	GOLD = (200, 200, 30)
	GREY = (128, 128, 128)

class Timer:
    def __init__(self):
        self.ticks = 0
        self.stopped = False
        self.stop_time = 0
        self.passed_timer = pygame.time.get_ticks()
    
    def start(self):
        self.stopped = False
        self.stop_time = 0
        self.ticks = pygame.time.get_ticks()
    
    def stop(self):
        self.stopped = True
        self.stop_time = pygame.time.get_ticks()
    
    def time_passed_reset(self):
        self.passed_timer = pygame.time.get_ticks()
    
    def ticks_passed(self, ticks):
        now = pygame.time.get_ticks()
        if now - self.passed_timer >= ticks:
            return True
        return False
    
    def get(self):
        if self.stopped:
            return self.stop_time-self.ticks
        return pygame.time.get_ticks()-self.ticks


CURRENT_DIR = path.dirname(__file__)
IMAGES_DIR = path.join(CURRENT_DIR, "assets/images")
SOUNDS_DIR = path.join(CURRENT_DIR, "assets/sounds")

def load_img(img_path, ext=".png", colorkey=Colors.BLACK):
    full_path = path.join(IMAGES_DIR, img_path) + ext
    img = pygame.image.load(full_path).convert()
    img.set_colorkey(Colors.BLACK)
    return img




class Textures:
    # colors: blue green white red yellow

    # types
    BUTTON_UP = 0
    BUTTON_DOWN = 1

    @staticmethod
    def get(type, scale, color_name):
        shape = "_square"
        if scale[0] > scale[1] * 1.50:
            shape = "_long"
        img = None
        if type == Textures.BUTTON_DOWN:
            img = load_img(color_name + "_button_down" + shape)
        elif type == Textures.BUTTON_UP:
            img = load_img(color_name + "_button_up" + shape)

        return pygame.transform.scale(img, scale)




class Sounds:
    pass

class Fonts:
    pass