import pygame

class Interact:
    def __init__(self, interface):
        self.interface = interface
        self.triggers = []
    
    def add_trigger(self, trigger):
        self.triggers.append(trigger)
            
    def update(self):
        pass
    
    def set_positioner(self, positioner):
        positioner.position_interact(self)

    def eventloop(self, event):
        pass

    def render(self, screen):
        pass

    def trigger(self):
        for trigger in self.triggers:
            self.interface.window.scheduler.add_trigger(trigger)
