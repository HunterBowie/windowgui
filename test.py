import windowgui, pygame
from os import path
pygame.init()

windowgui.Text.default_style["font_file"] = path.join(windowgui.FOUNTS_DIR, "rounded.ttf")

win = windowgui.Window((800, 800))
win.bg_color = windowgui.Colors.WHITE

my_button = windowgui.Button("my-btn", 10, 10, 100, 100, top_img=windowgui.load_image("audioOn", windowgui.IMAGES_DIR, scale=(50, 50), convert=False, colorkey=None))
my_textbox = windowgui.TextBox("my-textbox", 100, 150, 300, 50)
my_slider = windowgui.Slider("my-slider", 300, 400, 200, 75)
win.managers["ui"].add(my_button)
win.managers["ui"].add(my_textbox)
win.managers["ui"].add(my_slider)

win.managers["flash"].add(
windowgui.Flash(130, 0, (400, 50), windowgui.Text(0, 0, "Please provide valid input!", style={"size": 20}), windowgui.Colors.LIGHT_BLUE)
)
class Manager:
    def __init__(self, window):
        self.window = window
    
    def eventloop(self, event):
        if event.type == windowgui.Event.BUTTON_CLICK:
            if event.ui_element.id == "my-btn":
                self.window.managers["flash"].add(
                windowgui.Flash(100, 0, (400, 50), windowgui.Text(0, 0, "Please provide valid input!", style={"size": 20}), windowgui.Colors.LIGHT_BLUE)
                )

win.managers["main"] = Manager(win)
win.start(auto_cycle=True)


