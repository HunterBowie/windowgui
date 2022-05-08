import pygame


TEXTBOX_SHIFT_CHARS = {"1":"!","2":"@","3":"#",
    "4":"$","5":"%","6":"^","7":"&","8":"*",
    "9":"(","0":")","-":"_","=":"+","`":"~",
    "/": "?", ";": ":", "\\": "\|"}
TEXTBOX_MARGIN = 5
TEXTBOX_CURSOR_BLINK_TIME = .45
TEXTBOX_BACKSPACE_DELAY = .1
TEXTBOX_BORDER_WIDTH = 4

FLASH_FADE_TIME = .5
FLASH_FADE_SPEED = 10

M_FLASH_KEY = "flash"
M_UI_KEY = "ui"
M_SOUND_KEY = "sound"

class Event:
    BUTTON_CLICK = pygame.USEREVENT 
    TEXTBOX_POST = pygame.USEREVENT + 1

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
    LIGHT_YELLOW = (200, 200, 0)
    LIGHT_RED = (255, 50, 50)
    LIGHT_GREEN = (50, 200, 50)



    

    
