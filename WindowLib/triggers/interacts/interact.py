import pygame
from ..triggerable import Triggerable

class Interact(Triggerable):
    def __init__(self, interface):
      super().__init__(interface)
      self.entity = None
    
    def set_pos(self, x, y):
      self.entity.set_pos(x, y)
    
