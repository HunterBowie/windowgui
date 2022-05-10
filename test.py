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


