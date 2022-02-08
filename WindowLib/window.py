import pygame
<<<<<<< HEAD:WindowLib/Window.py
from .Clock import Clock
from .Scheduler import Scheduler
from .Colors import Colors
=======
from .clock import Clock
from .scheduler import Scheduler
from .colors import Colors
>>>>>>> b27ee00ae734cc14552f5c80c4def47bfca70d74:WindowLib/window.py

class Window:
    def __init__(self, screen_size):
        self.screen = pygame.display.set_mode(screen_size)
        self.clock = Clock(self)
        self.scheduler = Scheduler(self)
        self.interface = None

        self.running = False
        
        self.bg_color = Colors.RED
    
    def set_display_color(self, color):
        self.bg_color = color
        
    def set_interface(self, interface):
        self.interface = interface(self)
    
    def set_caption(self, caption):
        self.caption = caption
        pygame.display.set_caption(self.caption)
    
    def set_icon(self, icon):
        self.icon = icon
        pygame.display.set_icon(self.icon)
    
    def start(self):
        self.running = True
        while self.running:
            self.update()
        pygame.quit()
    
    def stop(self):
        self.running = False
    
    def update(self):
        self.scheduler.run()
        
        if self.interface:
            self.interface.update()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()

        pygame.display.update()
<<<<<<< HEAD:WindowLib/Window.py
        self.screen.fill(self.bg_color)
=======
        self.screen.fill(self.BG_COLOR)
>>>>>>> b27ee00ae734cc14552f5c80c4def47bfca70d74:WindowLib/window.py
        self.clock.update()

