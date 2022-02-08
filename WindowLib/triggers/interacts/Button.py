from cgitb import text
import pygame
from .Interact import Interact
from ...Entity import Entity
from ...private.Loader import Loader



class Button(Interact):
    RELEASE_DELAY = 50
    def __init__(self, x, y, type, color, interface, text=None, icon=None, positioner=None):
        super().__init__(interface, positioner)
        self.image = Loader.get_button(type, color, False)
        self.clicked_image = Loader.get_button(type, color, True)
        self.current_image = self.image
        self.entity = Entity(x, y, self.image.get_width(), self.image.get_height())
        self.position()
        
        self.text = text
        if self.text:
            self.text.center(self.image.get_rect())
        self.icon = icon
        if self.icon:
            self.icon.center(self.image.get_rect())
        
        self.clicked_timer = pygame.time.get_ticks()-Button.RELEASE_DELAY
        self.mouse_down_on = False


    def update(self):
        pos = pygame.mouse.get_pos()
        if self.entity.rect.collidepoint(pos):
            if pygame.mouse.get_pressed() == (1, 0, 0) and self.mouse_down_on:
                self.clicked_timer = pygame.time.get_ticks()

        now = pygame.time.get_ticks()
        if now - self.clicked_timer < Button.RELEASE_DELAY:
            self.current_image = self.clicked_image
        else:
            self.current_image = self.image

    def eventloop(self, event):
        pos = pygame.mouse.get_pos()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.entity.rect.collidepoint(pos):
                self.trigger()
                self.clicked_timer = pygame.time.get_ticks()
                self.mouse_down_on = True
            else:
                self.mouse_down_on = False
            
    
    def render(self, screen):
        image = self.current_image.copy()
        overlay_surf = pygame.Surface((image.get_width(), image.get_height()), pygame.SRCALPHA)
        if self.text:
            self.text.render(overlay_surf)
        if self.icon:
            self.icon.render(overlay_surf)
        pos = self.entity.get_pos()
        if self.current_image == self.image:
            pos = pos[0], pos[1]-4
        screen.blit(image, pos)
        screen.blit(overlay_surf, pos)
