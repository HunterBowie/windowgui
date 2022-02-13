import pygame
from windowgui.util import Textures

class UIElement:
    def __init__(self):
        pass

class Button(UIElement):
    def __init__(self, x, y, width, height, color_name):
        self.rect = pygame.Rect(x, y, width, height)
        self.clicked = False
        self._img_up = Textures.get(Textures.BUTTON_UP, (width, height), color_name)
        self._img_down = Textures.get(Textures.BUTTON_DOWN, (width, height-4), color_name)
        
        
    
    def eventloop(self, event):
        pos = pygame.mouse.get_pos()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pos):
                self.clicked = True


    def render(self, surface):
        pos = pygame.mouse.get_pos()
    
        if not pygame.mouse.get_pressed() == (1, 0, 0):
            self.clicked = False
                

        if self.clicked:
            surface.blit(self._img_down, self.rect.topleft)
        else:   
            surface.blit(self._img_up, (self.rect.left, self.rect.top-4))


class Slider(UIElement):
    pass

class TextBox(UIElement):
    pass

