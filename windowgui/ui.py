"""
A collection of UI elements to use with the UI manager.
"""

import pygame, pyperclip
from numpy import interp
from .assets import get_button_img, get_checkbox_img, get_slider_image
from .util import render_border, Text, get_text_size, RealTimer
from .constants import Colors, TEXTBOX_BACKSPACE_DELAY, TEXTBOX_BORDER_WIDTH, TEXTBOX_CURSOR_BLINK_TIME,\
TEXTBOX_MARGIN, TEXTBOX_SHIFT_CHARS, Event, UIColorStyle

class UIElement:
    def __init__(self, id, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.id = id

    def post_event(self, event_type):
        event_data = {
            "ui_element": self,
            "ui_id": self.id,
        }
        pygame.event.post(pygame.event.Event(event_type, event_data))
                

class Button(UIElement):
    """
    A UI element for togglable or non-togglable buttons.
    """
    def __init__(self, id, x, y, width, height, color_style=UIColorStyle.WHITE, top_img=None, hide_button=False):
        super().__init__(id, x, y, width, height)
        self.clicked = False
        self.top_img = top_img
        self.hide_button = hide_button
        self.top_img_x = self.top_img_y = 0
        if self.top_img:
            self.top_img_x = int(self.rect.width/2-self.top_img.get_width()/2)
            self.top_img_y = int(self.rect.height/2-self.top_img.get_height()/2)
            
        self._img_up = get_button_img(False, (width, height), color_style)
        self._img_down = get_button_img(True, (width, height-4), color_style)
    
    def eventloop(self, event):
        pos = pygame.mouse.get_pos()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pos):
                self.clicked = True
                self.post_event(Event.BUTTON_CLICK) 
    
    def update(self):
        pos = pygame.mouse.get_pos()
        if not pygame.mouse.get_pressed() == (1, 0, 0):
            self.clicked = False

    def render(self, surface):
        if not self.hide_button:
            if self.clicked:
                surface.blit(self._img_down, self.rect.topleft)
            else:   
                surface.blit(self._img_up, (self.rect.left, self.rect.top-4))
        
        if self.top_img:
            if self.clicked:
                surface.blit(self.top_img, (self.top_img_x+self.rect.x, self.top_img_y+self.rect.y))
            else:
                surface.blit(self.top_img, (self.top_img_x+self.rect.x, self.top_img_y+self.rect.y-4))


class Slider(UIElement):
    """
    A UI element that allows that user to slide an arrow to ajust a value from 0-100.
    """
    def __init__(self, id, x, y, width, height, color_style=UIColorStyle.WHITE):
        super().__init__(id, x, y, width, height)
        self.value = 0
        self._slider_img = get_slider_image("up", color_style)
        self.mouse_held = False
        self.release_timer = RealTimer()
    
    def calc_slider_pos(self):
        return self.rect.x+self.get_mapped_value()-int(self._slider_img.get_width()/2), self.rect.centery-int(self._slider_img.get_height()/2)
    
    def get_slider_rect(self):
        x, y = self.calc_slider_pos()
        return pygame.Rect(x, y, self._slider_img.get_width(), self._slider_img.get_height())

    def get_mapped_value(self):
        return int(interp(self.value, [0, 100], [0, self.rect.width]))
    
    def set_range_value(self, mapped_value):
        self.value = int(interp(mapped_value, [0, self.rect.width], [0, 100]))
    
    def change_value(self, change):
        self.value += change
        if self.value < 0:
            self.value = 0
        elif self.value > 100:
            self.value = 100
    
    def eventloop(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.get_slider_rect().collidepoint(mouse_pos):
                self.mouse_held = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.mouse_held = False
    
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if not self.get_slider_rect().collidepoint(mouse_pos):
            self.mouse_held = False
        
        if self.mouse_held:
            mouse_value = mouse_pos[0]-self.rect.x
            if mouse_value > -1 and mouse_value <= self.rect.width:
                self.set_range_value(mouse_value)

    def render(self, screen):
        pygame.draw.line(screen, Colors.BLACK, (self.rect.left, self.rect.centery), (self.rect.right, self.rect.centery), 4)
        screen.blit(self._slider_img, self.calc_slider_pos())

class TextBox(UIElement):
    """
    A UI element for getting text from the user.
    """
    def __init__(self, id, x, y, width, height, style=None, border=True):
        super().__init__(id, x, y, width, height)
        if style is None:
            self.text = Text(0, 0, "", {"size": 20})
        
        else:
            self.text = Text(0, 0, "", style)
        
        self.border = border
        self.selected = False
        self.cursor_blink = True
        self.cursor_timer = RealTimer()
        self.cursor_timer.start()
        self.backspace_timer = RealTimer()
        self.held_backspace_timer = RealTimer()


    def is_appendable(self, string):
        text_size = get_text_size(self.text.string + string, self.text.style)
        if text_size[0] >= (self.rect.width-TEXTBOX_MARGIN*2):
            return False
        return True
    

    def eventloop(self, event):
        keys = pygame.key.get_pressed()
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pos):
                self.selected = True
            else:
                self.selected = False

        if self.selected:
            if event.type == pygame.KEYDOWN:
                hit_key = True
                key_name = pygame.key.name(event.key)
                if key_name == "space":
                    if self.is_appendable(" "):
                        self.text.add(" ")
                elif key_name == "backspace":
                    self.backspace_timer.reset()
                    self.held_backspace_timer.reset()
                    if self.text.string:
                        self.text.pop()
                elif key_name == "return":
                    self.post_event(Event.TEXTBOX_POST)

                elif len(key_name) == 1:
                    string_data = key_name
                    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                        string_data = key_name.upper()
                        if key_name in TEXTBOX_SHIFT_CHARS.keys():
                            string_data = TEXTBOX_SHIFT_CHARS[key_name]
                        elif key_name == "v" and event.mod and pygame.KMOD_CTRL:
                            if self.is_appendable(pyperclip.paste()):
                                string_data = pyperclip.paste()
                    if self.is_appendable(string_data):
                        self.text.add(string_data)
                else:
                    hit_key = False
                
                if hit_key:
                    self.cursor_timer.reset()
                    self.cursor_blink = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_BACKSPACE:
                    self.backspace_timer.reset()
                    self.backspace_timer.stop()
    
    def update(self):
        self.text.center_y(pygame.Rect(0, 0, self.rect.width, self.rect.height))
        keys = pygame.key.get_pressed()
        if self.selected:
            if keys[pygame.K_BACKSPACE]:
                if self.backspace_timer.passed(TEXTBOX_BACKSPACE_DELAY*2):
                    if self.held_backspace_timer.passed(TEXTBOX_BACKSPACE_DELAY):
                        self.held_backspace_timer.reset()
                        if self.text.string:
                            self.text.pop()
                
        
    def render(self, surface):
        render_border(surface, self.rect, 3)
        surf = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        self.text.render(surf)
        surface.blit(surf, (self.rect.x + TEXTBOX_MARGIN, self.rect.y))
        
        # render cursor
        if self.selected:
            x = self.rect.x+TEXTBOX_MARGIN+self.text.get_width()
            string = ""
            if self.cursor_blink:
                string = "|"
            
            if self.cursor_timer.passed(TEXTBOX_CURSOR_BLINK_TIME):
                self.cursor_timer.reset()
                self.cursor_blink = not self.cursor_blink
            

            text = Text(x, 0, string)
            text.center_y(self.rect)
            text.render(surface)


class UIManager:
    """
    A built in Manager class that handles updating and provides an interface for UI.
    """
    def __init__(self, window):
        self.window = window
        self.ui = []
    
    def add(self, element):
        self.ui.append(element)
    
    def get_element(self, id):
        for element in self.ui:
            if element.id == id:
                return element
        raise ValueError(f"No element with id: {id}")

    def eventloop(self, event):
        for element in self.ui:
            element.eventloop(event)
    
    def update(self):
        for element in self.ui:
            element.update()
            element.render(self.window.screen)


