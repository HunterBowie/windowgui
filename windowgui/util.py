import pygame
from os import path
from .constants import Colors


class Text:
    """
    A class for handling text rendering and format.
    """
    default_format = {
        "font_file": pygame.font.get_default_font(),
        "size": 30,
        "antialias": True,
        "color": Colors.BLACK
    }

    def __init__(self, x, y, string, format=None, newline_width=None):
        self.format = format
        if self.format is None:
            self.format = self.default_format.copy()
        for setting, value in self.default_format.items():
            if setting not in self.format:
                self.format[setting] = value
        self.x = x
        self.y = y
        self.newline_width = newline_width
        self.set(string)

    def set(self, string):
        self.raw_string = string
        self.lines = string.split("\n")
        self.string = string.replace("\n", "")
        if self.newline_width:
            new_lines = []
            for line in self.lines:
                new_line = "" 
                for char in line:
                    new_line = new_line + char
                    if get_text_size(new_line, self.format)[0] >= self.newline_width:
                        new_lines.append(new_line.strip())
                        new_line = ""
                if new_line:
                    new_lines.append(new_line.strip())
            self.lines = new_lines
        self._load_surf()
    
    def add(self, string):
        self.set(self.raw_string + string)
    
    def pop(self):
        char = self.string[len(self.string)-1]
        self.set(self.string[:len(self.string)-1])
        return char
    
    def get_width(self):
        return self.surface.get_width()
    
    def get_height(self):
        return self.surface.get_height()
    
    def get_size(self):
        return self.get_width(), self.get_height()

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.get_width(), self.get_height())
    
    def _load_surf(self):
        font = pygame.font.Font(self.format["font_file"], self.format["size"])

        if len(self.lines) > 1:
            renders = []    
            for string in self.lines:
                renders.append(font.render(string, self.format["antialias"], self.format["color"]))
            
            height = 0
            width = 0
            for line_surf in renders:
                height += line_surf.get_height()
                if line_surf.get_width() > width:
                    width = line_surf.get_width()
            
            self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
            x = y = 0
            for line_surf in renders:
                self.surface.blit(line_surf, (x, y))
                y += line_surf.get_height()
            
        else:
            self.surface = font.render(self.string, self.format["antialias"], self.format["color"])
    
    def render(self, screen):
        screen.blit(self.surface, (self.x, self.y))
    
    def center_y(self, rect):
        self.y = rect.center[1]-self.get_height()/2

    def center_x(self, rect):
        self.x = rect.center[0]-self.get_width()/2
    
    def center(self, rect):
        self.center_x(rect)
        self.center_y(rect)

def render_text_background(surface, text, color, alpha, margin):
    surf = get_surf((text.get_width()+margin, text.get_height()+margin), color, alpha)
    surface.blit(surf, (int(text.x-margin/2), int(text.y-margin/2)))

def get_text_size(string, format=Text.default_format):
    if format != Text.default_format:
        for setting, value in Text.default_format.items():
            if setting not in format:
                format[setting] = value
    font = pygame.font.Font(format["font_file"], format["size"])
    surf = font.render(string, format["antialias"], format["color"])
    return surf.get_width(), surf.get_height()


class RealTimer:
    """
    A class for calculating time in seconds.
    """
    def __init__(self):
        self.start_time = -1
        self.stop_time = -1
    
    def start(self):
        self.reset()
    
    def get(self):
        if self.start_time == -1:
            return 0
        if self.stop_time == -1:
            return time.monotonic()-self.start_time

        return self.stop_time-self.start_time
    
    def reset(self):
        self.start_time = time.monotonic()
        self.stop_time = -1

    def stop(self):
        self.stop_time = time.monotonic()
    
    def passed(self, seconds):
        return self.get() >= seconds
    
    def __repr__(self):
        return f"time: {self.get()}"
    

class GameTimer:
    """
    A class for calculating time in pygame ticks.
    """
    def __init__(self):
        self.reset()
    
    def start(self):
        self.start_time = pygame.time.get_ticks()
    
    def get(self):
        if self.start_time == -1:
            return 0
        now = pygame.time.get_ticks()
        return int(now-self.start_time)
    
    def reset(self):
        self.start_time = -1
    
    def passed(self, seconds):
        return self.get() >= seconds

def get_surf(size, color, alpha):
    surf = pygame.Surface(size, pygame.SRCALPHA)
    surf.fill(color)
    surf.set_alpha(alpha)
    return surf


def render_border(surface, rect, size):
    pygame.draw.line(surface, Colors.BLACK, rect.topleft, rect.topright, size)
    pygame.draw.line(surface, Colors.BLACK, rect.topleft, rect.bottomleft, size)
    pygame.draw.line(surface, Colors.BLACK, rect.bottomleft, rect.bottomright, size)
    pygame.draw.line(surface, Colors.BLACK, rect.topright, rect.bottomright, size)


def root_rect(screen_size, rect, top=False, bottom=False,
    left=False, right=False, center_x=False, center_y=False):
    """
    A function for positioning a rect relative to the screen.
    """
    center_pos = int(screen_size[0]/2), int(screen_size[1]/2)
    
    new_x, new_y = 0, 0
    if center_x:
        new_x = center_pos[0]-int(rect.width/2)
    if center_y:
        new_y = center_pos[1]-int(rect.height/2)
    if left_x:
        new_x = 0
    if right_x:
        new_x = screen_size[0]-rect.width
    if bottom_y:
        new_y = screen_size[1]-rect.height
    if top_y:
        new_y = 0
    rect.x += new_x
    rect.y += new_y
    return rect.x, rect.y

def load_image(img_name, img_path, ext=".png", colorkey=None, convert=False, scale=None):
    full_path = path.join(img_path, img_name) + ext
    try:
        img = pygame.image.load(full_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"no image for path {full_path}")
    if scale is not None:
        img = pygame.transform.scale(img, scale)
    if convert:
        img = img.convert()
    if colorkey:
        img.set_colorkey(Colors.BLACK)
    return img

