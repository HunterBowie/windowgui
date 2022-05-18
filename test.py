<<<<<<< HEAD
import windowgui, pygame, time
pygame.init()


SCREEN_SIZE = 600, 600
win = windowgui.Window(SCREEN_SIZE)
win.bg_color = windowgui.Colors.WHITE

pygame.display.set_caption("hello")


win.start(auto_cycle=False)

text = windowgui.Text(10, 10, "Forever")
win.managers["ui"].ui.append(windowgui.ui.Button("btn", 250, 250, 200, 50, top_img=text.surface))
win.managers["ui"].ui.append(windowgui.ui.TextBox("txtbx", 150, 450, 200, 50))

while win.running:
    for event in pygame.event.get():
        win.eventloop(event)

        if event.type == windowgui.Event.BUTTON_CLICK:
            pass

    win.update(auto_eventloop=False)

win.end()
=======
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
>>>>>>> d41f0815f6cbb58bda6725272bcced867d33bfaf


        


win.managers["main"] = MyUI(win)

win.start(auto_cycle=False)

while win.running:
    for event in pygame.event.get():
        win.eventloop(event)
    win.update()

