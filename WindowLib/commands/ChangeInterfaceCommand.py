import pygame
from .Command import Command

class ChangeInterfaceCommand(Command):
    def __init__(self, interface, new_interface):
        super().__init__(interface)
        self.new_interface = new_interface
    
    def execute(self):
        window = self.interface.window
        window.set_interface(self.new_interface(window))