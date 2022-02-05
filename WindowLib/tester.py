from window import Window
from colors import Colors
from abstractInterface import AbstractInterface
from interacts import Button
from triggers import TestPrintTrigger

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
