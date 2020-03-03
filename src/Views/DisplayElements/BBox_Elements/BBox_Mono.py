from abc import abstractmethod
from Views.DisplayElements.BBox_Elements.BBox_Element import BBox_Element
import pygame

class BBox_Mono(BBox_Element):

    def __init__(self, color):
        BBox_Element.__init__(self)
        self.color = color
        self.border_width = 0.5

    @abstractmethod
    def draw(self, screen, bbox, width, height, width_game, height_game, scale_width, scale_height):
        surface_border = pygame.Surface((bbox.width*scale_width, bbox.height*scale_height))
        surface_border.fill(self.color)
        surface_inner = pygame.Surface(((bbox.width-self.border_width)*scale_width, (bbox.height-self.border_width)*scale_height))

        surface_inner.fill(0x000000)
        surface_border.blit(surface_inner, (self.border_width*scale_width/2,self.border_width*scale_height/2))
        surface_border.set_colorkey(0x000000)
        screen.blit(surface_border, ((bbox.position[0]-bbox.width/2)*scale_width, (bbox.position[1]-bbox.height/2)*scale_height))

