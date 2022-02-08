import pygame
from os import path
from ..Colors import Colors


class Loader:
    CURRENT_DIR = path.dirname(__file__)
    IMAGES_DIR = path.join(CURRENT_DIR, "assets/images")
    SOUNDS_DIR = path.join(CURRENT_DIR, "assets/sounds")
   
    @staticmethod
    def load_img(img_path, ext=".png", convertable=True):
        full_path = path.join(Loader.IMAGES_DIR, img_path) + ext
        img = None
        if convertable:
            img = pygame.image.load(full_path).convert()
            img.set_colorkey(Colors.BLACK)
        else:
            img = pygame.image.load(full_path)
        return img
    
    @staticmethod
    def get_button(type, color, pressed):
        button_path = ""
        if color == "white":
            color = "grey"
        button_path = button_path + color + "_button"

        button_nums = None # up / down

        if color == "grey":
            if type == "long":
                button_nums = ("03", "04")
            elif type == "square":
                button_nums = ("12", "13")

        elif color == "green":
            if type == "long":
                button_nums = ("04", "03")
            elif type == "square":
                button_nums = ("11", "12")

        elif color == "blue":
            if type == "long":
                button_nums = ("04", "05")
            elif type == "square":
                button_nums = ("11", "12")

        elif color == "red":
            if type == "long":
                button_nums = ("01", "02")
            elif type == "square":
                button_nums = ("8", "9")


        button_num = None

        if pressed:
            button_num = button_nums[1]
        else:
            button_num = button_nums[0]
        
        button_path = button_path + button_num

        return Loader.load_img(button_path)





    @staticmethod
    def get_slider():
        pass
    
    @staticmethod
    def get_tickbox():
        pass




