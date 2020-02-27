from abc import abstractmethod
from Displays.DisplayElements.Paddle_Elements.Paddle_Element import Paddle_Element
import pygame

class Paddle_Mono(Paddle_Element):

    def __init__(self, color):
        Paddle_Element.__init__(self)
        self.color = color

    @abstractmethod
    def draw(self, screen, paddle, width, height, width_game, height_game, scale_width, scale_height):
        surface = pygame.Surface((paddle.width*scale_width, paddle.height*scale_height))
        surface.fill(self.color)
        screen.blit(surface, ((paddle.position[0]-paddle.width/2)*scale_width, (paddle.position[1]-paddle.height/2)*scale_height))

