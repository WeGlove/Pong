from abc import abstractmethod
from Displays.DisplayElements.Info_Elements.Info_Element import Info_Element
import pygame

class Info_Mono(Info_Element):

    def __init__(self, font):
        Info_Element.__init__(self)
        self.font = font

    @abstractmethod
    def draw(self, screen, info, width, height, width_game, height_game, scale_width, scale_height):
        text = self.font.render(info, True, (0, 128, 0))
        screen.blit(text,(0,0))

