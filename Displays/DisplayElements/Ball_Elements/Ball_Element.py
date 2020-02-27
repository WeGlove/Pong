from abc import abstractmethod

class Ball_Element:

    @abstractmethod
    def draw(self, screen, ball, width, height, width_game, height_game, scale_width, scale_height):
        pass
