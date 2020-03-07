from src.Backends.Backend import Backend


class Pygame(Backend):

    def __init__(self, keyboard, mouse, view):
        self.keyboard = keyboard
        self.mouse = mouse
        self.view = view

    def get_keyboard(self):
        return self.keyboard

    def get_mouse(self):
        return self.mouse

    def get_view(self):
        return self.view