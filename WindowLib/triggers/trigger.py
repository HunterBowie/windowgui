import pygame

class Trigger:
    def __init__(self, window):
        self.window = window
    
    def execute(self):
        pass

    def end(self):
        pass

    def is_finished(self):
        return True

        