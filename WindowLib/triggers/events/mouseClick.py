import pygame
<<<<<<< HEAD:WindowLib/triggers/events/MouseClick.py
from .Event import Event
=======
from ..interacts.interact import Interact
>>>>>>> b27ee00ae734cc14552f5c80c4def47bfca70d74:WindowLib/triggers/events/mouseClick.py

class MouseClick(Event):
    def __init__(self, interface, rect=None, mode="down", hold_data=(1, 0, 0)):
        super().__init__(interface)
        self.rect = rect
        self.mode = mode
        self.hold_data = hold_data

    def eventloop(self, event):
        pos = pygame.mouse.get_pos()
        mouse_focused = False

        if self.rect is None:
            mouse_focused = pygame.mouse.get_focused()

        elif self.rect.collidepoint(pos):
            mouse_focused = True
        
        if mouse_focused:
            if self.mode == "down":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.trigger()
            elif self.mode == "up":
                if event.type == pygame.MOUSEBUTTONUP:
                    self.trigger()
            elif self.mode == "hold":
                if pygame.mouse.get_pressed() == self.hold_data:
                    self.trigger()
            else:
                raise ValueError("mouseclick gived invalid mode arg")
