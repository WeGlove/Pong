from abc import abstractmethod

class Background_Element:

    @abstractmethod
    def draw(self, screen, width, height, width_game, height_game, scale_width, scale_height):
        pass
