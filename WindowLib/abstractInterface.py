import pygame

class AbstractInterface:
    def __init__(self, window):
        self.window = window
        self.screen = window.screen
        self.interacts = []
        self.visuals = []
        self.run_eventloop = True
        self.sub_interfaces = []
        self.config()
        
    def set_sub_interfaces(self, sub_interfaces):
        self.sub_interfaces = [sub_interface(self) for sub_interface in self.sub_interfaces]

    def config(self):
        pass

    def create_interact(self, interact, triggers, positioner):
        for trigger in triggers:
            interact.add_trigger(trigger)
        if positioner:
            interact.set_positioner(positioner)
        self.interacts.append(interact)
    
    def create_visual(self, visual, animation, positioner):
        pass

    
    def eventloop(self, event):
        for interact in self.interacts:
            interact.eventloop(event)
        
        for sub_interface in self.sub_interfaces:
            sub_interface.eventloop(event)

        if event.type == pygame.QUIT:
            self.window.stop()
    
    def update(self):
        if self.run_eventloop:
            for event in pygame.event.get():
                self.eventloop(event)

        for interact in self.interacts:
            interact.update()
    
        for visual in self.visuals:
            visual.render(self.screen)

        for interact in self.interacts:
            interact.render(self.screen)
        
        for sub_interface in self.sub_interfaces:
            sub_interface.update()
    
        
            