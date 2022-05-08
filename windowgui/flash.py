import pygame
from .util import RealTimer

class Flash:
    """
    A class for temperarily rendering messages on the screen.
    """
    def __init__(self, x, y, text, size, color, duration=3):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.size = size
        self.alpha = 0
        self._surf_init()

        self.timer = RealTimer()
        self.duration = duration
    
    def start(self):
        self.timer.start()
    
    def _surf_init(self):
        self.surface = pygame.Surface(self.size, pygame.SRCALPHA)
        self.surface.fill(self.color)
        self.text.center(self.surface.get_rect())
        self.text.render(self.surface)
        self.surface.set_alpha(self.alpha)
    
    def _surf_fade_in(self):
        if self.alpha < 255:
            self.alpha += Constants.FLASH_FADE_SPEED
            self.surface.set_alpha(self.alpha)
    
    def _surf_fade_out(self):
        if self.alpha > 0:
            self.alpha -= Constants.FLASH_FADE_SPEED
            self.surface.set_alpha(self.alpha)
    
    def is_finished(self):
        return self.timer.passed(self.duration)
    
    def render(self, surface):
        if self.timer.get() < Constants.FLASH_FADE_TIME:
            self._surf_fade_in()
        elif self.duration-self.timer.get() < Constants.FLASH_FADE_TIME:
            self._surf_fade_out()
        surface.blit(self.surface, (self.x, self.y))

class FlashManager:
    """
    A built in Manager class that handles updating and provides an interface for flashing.
    """
    def __init__(self, window):
        self.window = window
        self.flashes = []

    def flash(self, flash):
        flash.start()
        self.flashes.append(flash)

    def update(self):
        finished_flahes = []
        for flash in self.flashes:
            if flash.is_finished():
                finished_flahes.append(flash)
                continue
            flash.render(self.screen)
        
        for flash in finished_flahes:
            self.flashes.remove(flash)
