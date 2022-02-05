from WindowLib.window import Window
from WindowLib.colors import Colors
from WindowLib.abstractInterface import AbstractInterface
from WindowLib.interacts import Button
from WindowLib.triggers import TestPrintTrigger

w = Window((400, 500))
w.BG_COLOR = Colors.GOLD


class TestInterface(AbstractInterface):
    def config(self):
        self.create_interact(
            Button(20, 20, "long", "white", None, self),
            None,
            [TestPrintTrigger("hello world")]
        )


w.set_interface(TestInterface)

w.start()
