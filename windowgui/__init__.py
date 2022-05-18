"""
A package that provides a simplified and organized struture for designing UIs in pygame
"""

<<<<<<< HEAD


from .util import Colors, RealTimer, GameTimer, Text, root_rect
from .constants import *
from .assets import load_asset

from .window import Window

import windowgui.flash
import windowgui.ui
=======
from .util import Colors, RealTimer, GameTimer, Text, root_rect, load_image
from .constants import UIColorStyle, UIEvent, Colors
from .assets import IMAGES_DIR, SOUNDS_DIR, FOUNTS_DIR

from .window import Window

from .flash import Flash
from .ui import Button, Slider, TextBox, CheckBox

>>>>>>> d41f0815f6cbb58bda6725272bcced867d33bfaf


