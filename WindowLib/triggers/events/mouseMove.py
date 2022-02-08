import pygame
<<<<<<< HEAD:WindowLib/triggers/events/MouseMove.py
from .Event import Event
=======
from ..interacts.interact import Interact
>>>>>>> b27ee00ae734cc14552f5c80c4def47bfca70d74:WindowLib/triggers/events/mouseMove.py

class MouseMove(Event):
    def __init__(self, interface):
        super().__init__(interface)
        self.init = True
        self.mouse_pos = (0, 0)
    
    def update(self):
        pos = pygame.mouse.get_pos()
        if self.init:
            self.mouse_pos = pos
            self.init = False
        
        else:
            if pos != self.mouse_pos:
                self.mouse_pos = pos
                self.trigger()
    
    def get(self):
        return self.mouse_pos