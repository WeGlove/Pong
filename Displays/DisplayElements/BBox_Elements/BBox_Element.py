from abc import abstractmethod

class BBox_Element:

    @abstractmethod
    def draw(self, screen, brick, width, height, width_game, height_game, scale_width, scale_height):
        pass
