from abc import abstractmethod
from Displays.DisplayElements.Background_Elements.Background_Element import Background_Element

class Background_Mono(Background_Element):

    def __init__(self, color):
        Background_Element.__init__(self)
        self.color = color

    def draw(self, screen, width, height, width_game, height_game, scale_width, scale_height):
        screen.fill(self.color)
