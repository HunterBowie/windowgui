from windowgui.window import Window
from windowgui.ui import Button
from windowgui.util import Colors
import pygame

win = Window((300, 300))
win.bg_color = Colors.WHITE
win.ui = {
"mybutton": Button(10, 10, 100, 100, "blue"),
"yourbutton": Button(15, 150, 140, 75, "red")
}

pygame.display.set_caption("Window GUI")
win.start()
