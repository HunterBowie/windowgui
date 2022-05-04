

class Manager:
    def __init__(self, window):
        self.window = window
        self.ui = []
    
    def get_element(self, id):
        for element in self.ui:
            if element.id == id:
                return element
        raise ValueError(f"no element with id: {id}")

    def _end(self):
        self.end()
    
    def _eventloop(self, event):
        for element in self.ui:
            element.eventloop(event)
        self.eventloop(event)
    
    def _update(self):
        self.update()
        for element in self.ui:
            element.update()
            element.render(self.window.screen)
    
    def end(self):
        pass
    
    def eventloop(self, event):
        pass

    def update(self):
        pass


