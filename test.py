import windowgui, pygame
from os import path
pygame.init()

windowgui.Text.default_style["font_file"] = path.join(windowgui.FOUNTS_DIR, "rounded.ttf")

win = windowgui.Window((800, 800))
win.bg_color = windowgui.Colors.WHITE

class MyUI:
    def __init__(self, window):
        self.window = window
        self.window.managers["ui"].clear()
        my_button = windowgui.Button("my-btn", 10, 10, 100, 100, color_style=windowgui.UIColorStyle.BLUE, top_img=windowgui.load_image("audioOn", windowgui.IMAGES_DIR, scale=(50, 50), convert=False, colorkey=None))
        my_textbox = windowgui.TextBox("my-textbox", 100, 150, 300, 50, text_style={"color": windowgui.Colors.BLUE})
        my_slider = windowgui.Slider("my-slider", 300, 400, 200, 75, color_style=windowgui.UIColorStyle.BLUE)
        my_checkbox = windowgui.CheckBox("my-checkbox", 10, 600, 35, 35, color_style=windowgui.UIColorStyle().BLUE, checked=True)
        window.managers["ui"].add(my_button)
        window.managers["ui"].add(my_textbox)
        window.managers["ui"].add(my_slider)
        window.managers["ui"].add(my_checkbox)
    
    def eventloop(self, event):
        if event.type == windowgui.UIEvent.CHECKBOX_CLICKED:
            print("buon is good stuff")
        
        if event.type == windowgui.UIEvent.BUTTON_CLICKED:
            self.window.managers["main"] = MyOtherUI(self.window)
    
class MyOtherUI:
    def __init__(self, window):
        self.window = window
        self.window.managers["ui"].clear()
        my_textbox = windowgui.TextBox("my-textbox", 200, 150, 300, 50, text_style={"color": windowgui.Colors.RED})
        self.window.managers["ui"].add(my_textbox)
    
    def eventloop(self, event):
        if event.type == windowgui.UIEvent.TEXTBOX_POSTED:
            print("ho yeah")


        


win.managers["main"] = MyUI(win)

win.start(auto_cycle=False)

while win.running:
    for event in pygame.event.get():
        win.eventloop(event)
    win.update()

