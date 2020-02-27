from abc import abstractmethod

class Brick_Element:

    @abstractmethod
    def draw(self, screen, brick, width, height, width_game, height_game, scale_width, scale_height):
        pass
