import pygame
from .trigger import Trigger

class TestPrintTrigger(Trigger):
    def __init__(self, window, msg):
        super().__init__(window)
        self.msg = msg
    
    def execute(self):
        print(f"--- {self.msg} ---")