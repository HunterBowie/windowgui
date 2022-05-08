import pygame
from os import path
from .util import load_image


def get_asset(type, name):
    """
    A function for getting windowgui images, fonts, and sounds.
    """
    if type == "images":
        print(load_img(name, Assets.IMAGES_DIR, colorkey=None))
        return load_img(name, Assets.IMAGES_DIR, colorkey=None)
    if type == "fonts":
        return Assets.FONTS[name]
    if type == "sounds":
        pass


class Assets:
    CURRENT_DIR = path.dirname(__file__)
    IMAGES_DIR = path.join(CURRENT_DIR, "assets/images")
    SOUNDS_DIR = path.join(CURRENT_DIR, "assets/sounds")
    FOUNTS_DIR = path.join(CURRENT_DIR, "assets/fonts")

    FONTS = {
        "regular": pygame.font.get_default_font(),
        "rounded": path.join(FOUNTS_DIR, "rounded.ttf")
    }

    @classmethod
    def get_button_img(cls, pressed, scale, color_style):
        shape = "_square"
        if scale[0] > scale[1] * 1.50:
            shape = "_long"
        img_name = ""
        if pressed:
            img_name = color_style + "_button_down" + shape
        else:
            img_name = color_style + "_button_up" + shape
        img = load_image(img_name, cls.IMAGES_DIR)
        return pygame.transform.scale(img, scale)
    
    @classmethod
    def get_slider_image(cls, direction, color_style):
        img_name = color_style + "_slider"
        direction = direction[0].upper() + direction[1:]
        img_name = img_name + direction
        img = load_image(img_name, cls.IMAGES_DIR)
        return img

    @classmethod
    def get_checkbox_img(cls):
        pass