import pygame

class Clock:
    def __init__(self, window, fps):
        self.clock = pygame.time.Clock()
        self.clock.tick(fps)
        self.window = window

    def wait(self, duration):
        self.clock.wait(duration)
