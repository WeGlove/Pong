from abc import abstractmethod
from Displays.DisplayElements.Ball_Elements.Ball_Element import Ball_Element
import pygame

class Ball_Mono(Ball_Element):

    def __init__(self, color, background, thickness=1):
        Ball_Element.__init__(self)
        self.color = color
        self.background = background
        self.thickness = thickness

    @abstractmethod
    def draw(self, screen, ball, width, height, width_game, height_game, scale_width, scale_height):
        surface = pygame.Surface((ball.error*2*scale_width,ball.error*2*scale_height))
        surface.fill(self.background.color)
        surface.set_colorkey(self.background.color)
        pygame.draw.circle(surface, self.color,
                           (int(ball.error*scale_width),int(ball.error*scale_height)),
                           int(ball.error*scale_width),
                            self.thickness)
        screen.blit(surface, ((ball.position[0]-ball.error)*scale_width, (ball.position[1]-ball.error)*scale_height))

