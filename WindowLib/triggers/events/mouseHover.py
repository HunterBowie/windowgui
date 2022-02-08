import pygame
<<<<<<< HEAD:WindowLib/triggers/events/MouseHover.py
from .Event import Event
=======
from ..interacts.interact import Interact
>>>>>>> b27ee00ae734cc14552f5c80c4def47bfca70d74:WindowLib/triggers/events/mouseHover.py

class MouseHover(Event):
    def __init__(self, rect, interface):
        super().__init__(interface)
        self.rect = rect
    
    def update(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.trigger()
