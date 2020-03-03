from abc import abstractmethod
from Views.DisplayElements.Brick_Elements.Brick_Element import Brick_Element
import pygame

class Brick_Mono(Brick_Element):

    def __init__(self, color):
        Brick_Element.__init__(self)
        self.color = color

    @abstractmethod
    def draw(self, screen, brick, width, height, width_game, height_game, scale_width, scale_height):
        surface = pygame.Surface((brick.width*scale_width, brick.height*scale_height))
        surface.fill(self.color)
        screen.blit(surface, ((brick.position[0]-brick.width/2)*scale_width, (brick.position[1]-brick.height/2)*scale_height))

