import pygame

class Scheduler:
    def __init__(self, window):
        self.window = window
        self.triggers = []
    
    def add_trigger(self, trigger):
        self.triggers.append(trigger)
    
    def run(self):
        ended_triggers = []
        for trigger in self.triggers:
            trigger.execute()
        
            if trigger.is_finished():
                trigger.end()
                ended_triggers.append(trigger)
        
        for trigger in ended_triggers:
            self.triggers.remove(trigger)
