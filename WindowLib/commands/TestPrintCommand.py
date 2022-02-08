import pygame
from .Command import Command

class TestPrintCommand(Command):
    def __init__(self, interface, msg):
        super().__init__(interface)
        self.msg = msg
    
    def execute(self):
        print(f"--- {self.msg} ---")