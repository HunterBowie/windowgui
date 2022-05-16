"""
A package that provides a simplified and organized struture for designing UIs in pygame
"""

from .util import Colors, RealTimer, GameTimer, Text, root_rect, load_image
from .constants import UIColorStyle, Event, Colors
from .assets import IMAGES_DIR, SOUNDS_DIR, FOUNTS_DIR

from .window import Window

from .flash import Flash
from .ui import Button, Slider, TextBox


