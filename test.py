import windowgui, pygame

win = windowgui.Window((400, 400))
win.bg_color = windowgui.Colors.BLACK

my_button = windowgui.ui.Button("my-btn", 10, 10, 100, 50)
win.managers["ui"].ui.append(my_button)

win.start(auto_cycle=True)


