import pygame

class Positioner:
    def __init__(self, interface, center_x=False, center_y=False,
     left_x=False, right_x=False, bottom_y=False, top_y=False):
        self.interface = interface
        self.left_x = left_x
        self.right_x = right_x
        self.center_y = center_y
        self.center_x = center_x
        self.bottom_y = bottom_y
        self.top_y = top_y
        self.center_pos = int(interface.window.screen.get_width()/2), int(interface.window.screen.get_height()/2)
    
    def position(self, positionable):
        x, y, width, height = positionable.get_positioning_data()
        new_x, new_y = 0, 0
        if self.center_x:
            new_x = self.center_pos[0]-int(width/2)
        if self.center_y:
            new_y = self.center_pos[1]-int(height/2)
        if self.left_x:
            new_x = 0
        if self.right_x:
            new_x = self.interface.window.screen.get_width()-width
        if self.bottom_y:
            new_y = self.interface.window.screen.get_height()-height
        if self.top_y:
            new_y = 0
        positionable.set_positioning_data(x+new_x, y+new_y)
    
        


