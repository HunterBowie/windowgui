import pygame
from ..Triggerable import Triggerable

class Interact(Triggerable):
    def __init__(self, interface, positioner=None):
      super().__init__(interface)
      self.positioner = positioner
      self.entity = None
    
    def position(self):
      if self.positioner:
        self.positioner.position(self)
    
    def get_positioning_data(self):
      return self.entity.unpack()
    
    def set_positioning_data(self, x, y):
      self.entity.set_pos(x, y)
