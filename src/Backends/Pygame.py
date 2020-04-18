from src.Backends.Backend import Backend
from Engine.Peripherals.Pygame_Keyboard import Pygame_Keyboard
from Engine.Peripherals.Pygame_Mouse import Pygame_Mouse
from src.Views.PygameView import PygameView


class Pygame(Backend):

    def __init__(self):
        self.keyboard = Pygame_Keyboard()
        self.mouse = Pygame_Mouse()

    def get_keyboard(self):
        return self.keyboard

    def get_mouse(self):
        return self.mouse

    def get_view(self):
        return PygameView()
