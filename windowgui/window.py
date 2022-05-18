import pygame
from .util import Colors
from .flash import FlashManager
from .ui import UIManager

class Window:
    """
    A class for handling window settings and updating managers.
    """
    def __init__(self, screen_size):
        self.screen = pygame.display.set_mode(screen_size)
        self.clock = pygame.time.Clock()
        self.running = False
        self.max_fps = 60
        self.bg_color = Colors.WHITE
        self.managers = {
        "ui": UIManager(self),
        "flash": FlashManager(self)
        }
    
    def start(self, auto_cycle=False):
        self.running = True
        if auto_cycle:
            while self.running:
                self.update(auto_eventloop=True)
            self.end()

    def end(self):
        for manager in self.managers.values():
            if self._has_callable_attr(manager, "end"):
                manager.end()
        pygame.quit()

    def eventloop(self, event):
        for manager in self.managers.values():
            if self._has_callable_attr(manager, "eventloop"):
                manager.eventloop(event)

        if event.type == pygame.QUIT:
            self.running = False
        
    def update(self, auto_eventloop=False):
        if auto_eventloop:
            for event in pygame.event.get():
                self.eventloop(event)

        for manager in self.managers.values():
            if self._has_callable_attr(manager, "update"):
                manager.update()
        
        pygame.display.flip()
        self.clock.tick(self.max_fps)
        self.screen.fill(self.bg_color)
    
    @staticmethod
    def _has_callable_attr(object, attr):
        value = getattr(object, attr, None)
        if value == None:
            return False
        if callable(value):
            return True
        return False
        


