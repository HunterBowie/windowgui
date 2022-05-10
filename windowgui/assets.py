import pygame
from os import path
from .util import load_image


CURRENT_DIR = path.dirname(__file__)
IMAGES_DIR = path.join(CURRENT_DIR, "assets/images")
SOUNDS_DIR = path.join(CURRENT_DIR, "assets/sounds")
FOUNTS_DIR = path.join(CURRENT_DIR, "assets/fonts")

FONTS = {
    "regular": pygame.font.get_default_font(),
    "rounded": path.join(FOUNTS_DIR, "rounded.ttf"),
    "future": path.join(FOUNTS_DIR, "future.ttf")
}

def get_button_img(pressed, scale, color_style):
    shape = "_square"
    if scale[0] > scale[1] * 1.50:
        shape = "_long"
    img_name = ""
    if pressed:
        img_name = color_style + "_button_down" + shape
    else:
        img_name = color_style + "_button_up" + shape
    img = load_image(img_name, IMAGES_DIR)
    return pygame.transform.scale(img, scale)

def get_slider_image(direction, color_style):
    img_name = color_style + "_slider"
    direction = direction[0].upper() + direction[1:]
    img_name = img_name + direction
    img = load_image(img_name, IMAGES_DIR)
    return img

def get_checkbox_img():
    pass


def load_asset(type, name):
    """
    A function for getting windowgui images, fonts, and sounds.
    """
    if type == "images":
        return load_image(name, IMAGES_DIR, colorkey=None)
    if type == "fonts":
        return FONTS[name]
    if type == "sounds":
        pass

    raise ValueError(f"type: {type} is not a valid asset type")
