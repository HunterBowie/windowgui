

class Triggerable:
    def __init__(self, window):
        self.window = window
        self.commands = []

    def set_commands(self, cmds):
        self.commands = cmds
    
    def trigger(self):
        for cmd in self.commands:
            self.window.scheduler.new_command(cmd)

