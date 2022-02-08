import pygame
from WindowLib.triggers.interacts.textBox import TextBox
from WindowLib.window import Window
from WindowLib.colors import Colors
from WindowLib.abstractUserInterface import AbstractUserInterface
from WindowLib.triggers.interacts import Button, TextBox
from WindowLib.commands import TestPrintCommand, EntityMoveCommmand
from WindowLib.positioner import Positioner
from WindowLib.text import Text
from WindowLib.timer import Timer

pygame.init()
w = Window((400, 500))
w.BG_COLOR = Colors.GOLD


class TestInterface(AbstractUserInterface):
    def config(self):
        self.first_button = self.new_interact(
            Button(0, 0, "square", "white", None, self.window),
            Positioner(self.window, center_x=True, center_y=True),
        )
        self.first_button.set_commands([
            EntityMoveCommmand(self.window, self.first_button.entity, 1, 0)
        ])
        self.text_box = self.new_interact(
            TextBox(0, 100, 200, 50, self.window),
            Positioner(self.window, center_x=True, center_y=True),
        )
      
        self.timer1 = Timer()

    
    def update(self):
        super().update()
        
        


w.set_interface(TestInterface)

w.start()
