from shutil import move
from .Command import Command

class EntityMoveCommmand(Command):
    def __init__(self, interface, entity, move_x, move_y):
        super().__init__(interface)
        self.entity = entity
        self.move_x = move_x
        self.move_y = move_y
    
    def execute(self):
        self.entity.move(self.move_x, self.move_y)
    
    def is_finished(self):
        return True