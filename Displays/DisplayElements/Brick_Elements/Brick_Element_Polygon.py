from abc import abstractmethod
from Displays.DisplayElements.Brick_Elements.Brick_Element import Brick_Element
import pygame
import numpy
import random

class Brick_Element_Polygon(Brick_Element):

    def __init__(self, color, points):
        Brick_Element.__init__(self)
        self.color = color
        self.points = points

    def draw(self, screen, brick, width, height, width_game, height_game, scale_width, scale_height):
        surface = pygame.Surface((brick.width*scale_width, brick.height*scale_height))
        surface.set_colorkey(0x000000)
        pygame.draw.polygon(surface,self.color,[(point[0]*brick.width*scale_width,point[1]*brick.height*scale_height) for point in self.points])
        screen.blit(surface, ((brick.position[0]-brick.width/2)*scale_width, (brick.position[1]-brick.height/2)*scale_height))

    @staticmethod
    def sample_square_point(t, offset=0):
        t = (t + offset) % 1
        if t < 0.25:
            return numpy.array([t * 4, 0])
        elif t < 0.5:
            return numpy.array([1, (t - 0.25) * 4])
        elif t < 0.75:
            return numpy.array([1 - (t - 0.5) * 4, 1])
        else:
            return numpy.array([0, 1 - (t - 0.75) * 4])

    @staticmethod
    def sample_square(amount, offset=0):
        return [Brick_Element_Polygon.sample_square_point(index/amount, offset) for index in range(amount)]

    @staticmethod
    def noisy_rect(amount, offset):
        points = Brick_Element_Polygon.sample_square(amount, offset)
        for i in range(amount):
            rand = random.random() * 0.5
            points[i] = points[i] + ([0.5,0.5] - points[i]) * rand
        return points
